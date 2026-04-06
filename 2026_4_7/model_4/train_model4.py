#!/usr/bin/env python3
"""
train_model4.py  —  Model 4: v3 資料 + Chat Messages 格式
在 NCHC H200 叢集上進行 Qwen3.5 27B LoRA 微調

使用方式（在 NCHC 上）:
  python train_model4.py
"""

import os, json, torch
from datasets import Dataset
from transformers import (
    AutoTokenizer, AutoModelForCausalLM,
    TrainingArguments, DataCollatorForSeq2Seq,
    Trainer, BitsAndBytesConfig,
)
from peft import LoraConfig, get_peft_model, TaskType, prepare_model_for_kbit_training

# ── 路徑設定（依 NCHC 環境調整）─────────────────────────────
BASE_MODEL   = "/work/u4439705/models/Qwen3.5-27B"
TRAIN_FILE   = "/work/u4439705/model_4/v3_train_chat.jsonl"
VALID_FILE   = "/work/u4439705/model_4/v3_valid_chat.jsonl"
OUTPUT_DIR   = "/work/u4439705/n8n_qwen35_lora_model4"
MAX_LENGTH   = 8192   # v3 資料有 93 節點的超大工作流，給足夠 token

# ── LoRA 設定（與 Model 2 相同，穩定策略）──────────────────
LORA_CONFIG = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                    "gate_proj", "up_proj", "down_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type=TaskType.CAUSAL_LM,
)

# ── 訓練超參數 ──────────────────────────────────────────────
TRAIN_ARGS = TrainingArguments(
    output_dir=OUTPUT_DIR,
    num_train_epochs=3,
    per_device_train_batch_size=1,
    per_device_eval_batch_size=1,
    gradient_accumulation_steps=8,   # 等效 batch size = 8
    learning_rate=2e-4,
    lr_scheduler_type="cosine",
    warmup_ratio=0.05,
    fp16=False,
    bf16=True,                        # H200 支援 BF16
    logging_steps=10,
    eval_strategy="steps",
    eval_steps=100,
    save_steps=200,
    save_total_limit=3,
    gradient_checkpointing=True,
    gradient_checkpointing_kwargs={"use_reentrant": False},
    load_best_model_at_end=False,   # 避免載入多份 weights 導致 OOM
    metric_for_best_model="eval_loss",
    greater_is_better=False,
    report_to="none",
    dataloader_num_workers=4,
    remove_unused_columns=False,
)


def load_jsonl(path: str) -> list[dict]:
    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                data.append(json.loads(line))
    print(f"  讀取 {len(data)} 筆: {path}")
    return data


def tokenize_messages(examples, tokenizer):
    """將 messages 格式序列化為 input_ids + labels"""
    all_input_ids, all_attention_masks, all_labels = [], [], []

    for messages in examples["messages"]:
        # 使用 Qwen 的 chat template
        text = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=False,
        )
        enc = tokenizer(
            text,
            truncation=True,
            max_length=MAX_LENGTH,
            padding=False,
        )
        input_ids = enc["input_ids"]

        # labels: 只對 assistant 部分計算 loss（其餘設為 -100）
        labels = [-100] * len(input_ids)
        # 找出 assistant token 的位置
        assistant_token = tokenizer.encode("<|im_start|>assistant", add_special_tokens=False)
        end_token       = tokenizer.encode("<|im_end|>", add_special_tokens=False)

        # 逐段標記 assistant 回應
        i = 0
        while i < len(input_ids):
            # 找 <|im_start|>assistant
            if (i + len(assistant_token) <= len(input_ids) and
                    input_ids[i:i+len(assistant_token)] == assistant_token):
                i += len(assistant_token)
                # 跳過換行
                while i < len(input_ids) and input_ids[i] in (tokenizer.encode("\n", add_special_tokens=False)):
                    i += 1
                # 標記到 <|im_end|>
                while i < len(input_ids):
                    if (i + len(end_token) <= len(input_ids) and
                            input_ids[i:i+len(end_token)] == end_token):
                        break
                    labels[i] = input_ids[i]
                    i += 1
            else:
                i += 1

        all_input_ids.append(input_ids)
        all_attention_masks.append(enc["attention_mask"])
        all_labels.append(labels)

    return {
        "input_ids":      all_input_ids,
        "attention_mask": all_attention_masks,
        "labels":         all_labels,
    }


def main():
    print("=" * 60)
    print("Model 4 訓練開始")
    print(f"  基礎模型: {BASE_MODEL}")
    print(f"  訓練資料: {TRAIN_FILE}")
    print(f"  輸出目錄: {OUTPUT_DIR}")
    print("=" * 60)

    # ── 載入 Tokenizer ──
    print("\n[1/4] 載入 Tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL, trust_remote_code=True)
    tokenizer.padding_side = "right"

    # ── 載入模型 (4-bit QLoRA + Flash Attention) ──
    print("[2/4] 載入模型 (4-bit QLoRA)...")
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True,
    )
    model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL,
        quantization_config=bnb_config,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
    )
    model = prepare_model_for_kbit_training(model)
    model.enable_input_require_grads()
    model = get_peft_model(model, LORA_CONFIG)
    model.print_trainable_parameters()

    # ── 準備資料集 ──
    print("[3/4] 處理資料集...")
    train_raw = load_jsonl(TRAIN_FILE)
    valid_raw = load_jsonl(VALID_FILE)

    train_ds = Dataset.from_list(train_raw)
    valid_ds = Dataset.from_list(valid_raw)

    tok_fn = lambda ex: tokenize_messages(ex, tokenizer)
    train_ds = train_ds.map(tok_fn, batched=True, batch_size=8,
                            remove_columns=train_ds.column_names)
    valid_ds = valid_ds.map(tok_fn, batched=True, batch_size=8,
                            remove_columns=valid_ds.column_names)

    print(f"  訓練集: {len(train_ds)} 筆 | 驗證集: {len(valid_ds)} 筆")

    # ── 開始訓練 ──
    print("[4/4] 開始訓練...")
    collator = DataCollatorForSeq2Seq(tokenizer, model=model, padding=True)
    trainer = Trainer(
        model=model,
        args=TRAIN_ARGS,
        train_dataset=train_ds,
        eval_dataset=valid_ds,
        data_collator=collator,
    )
    trainer.train(resume_from_checkpoint="/work/u4439705/n8n_qwen35_lora_model4/checkpoint-600")

    # ── 儲存 ──
    print("\n儲存 LoRA adapter...")
    model.save_pretrained(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)
    print(f"完成！模型儲存於: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
