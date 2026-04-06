#!/usr/bin/env python3
"""
train_model5.py  —  Model 5: v3 OpenAI FT 格式資料（max 16k token）
在 NCHC H200 叢集上進行 Qwen3.5 27B QLoRA 微調

使用方式（在 NCHC 上）:
  python train_model5.py
"""

import os, json, torch
from datasets import Dataset
from transformers import (
    AutoTokenizer, AutoModelForCausalLM,
    TrainingArguments, DataCollatorForSeq2Seq,
    Trainer, BitsAndBytesConfig,
)
from peft import LoraConfig, get_peft_model, TaskType, prepare_model_for_kbit_training

# ── 路徑設定 ─────────────────────────────────────────────
BASE_MODEL   = "/work/u4439705/models/Qwen3.5-27B"
TRAIN_FILE   = "/work/u4439705/model_5/qwen27b_v3_openai_ft_train_max16000.jsonl"
VALID_FILE   = "/work/u4439705/model_5/qwen27b_v3_test_openai.jsonl"
OUTPUT_DIR   = "/work/u4439705/n8n_qwen35_lora_model5"
MAX_LENGTH   = 8192   # 資料雖含 16k 樣本，但以 8192 截斷確保顯存穩定

# ── QLoRA 設定（與 Model 4 相同） ──────────────────────
LORA_CONFIG = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                    "gate_proj", "up_proj", "down_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type=TaskType.CAUSAL_LM,
)

# ── 訓練超參數 ──────────────────────────────────────────
TRAIN_ARGS = TrainingArguments(
    output_dir=OUTPUT_DIR,
    num_train_epochs=3,
    per_device_train_batch_size=1,
    per_device_eval_batch_size=1,
    gradient_accumulation_steps=8,
    learning_rate=2e-4,
    lr_scheduler_type="cosine",
    warmup_ratio=0.05,
    fp16=False,
    bf16=True,
    logging_steps=10,
    eval_strategy="steps",
    eval_steps=50,
    save_steps=100,
    save_total_limit=3,
    load_best_model_at_end=False,
    gradient_checkpointing=True,
    gradient_checkpointing_kwargs={"use_reentrant": False},
    report_to="none",
    dataloader_num_workers=4,
    remove_unused_columns=False,
)


def load_jsonl(path: str) -> list:
    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                data.append(json.loads(line))
    print(f"  讀取 {len(data)} 筆: {path}")
    return data


def tokenize_messages(examples, tokenizer):
    """將 messages 格式序列化為 input_ids + labels（只計算 assistant 的 loss）"""
    all_input_ids, all_attention_masks, all_labels = [], [], []

    for messages in examples["messages"]:
        # 分離 prompt（system + user）與 assistant 回應
        user_messages = []
        assistant_content = ""
        for msg in messages:
            if msg["role"] == "assistant":
                assistant_content = msg["content"]
                break
            user_messages.append(msg)

        # Tokenize prompt（不含 assistant）
        prompt_text = tokenizer.apply_chat_template(
            user_messages, tokenize=False, add_generation_prompt=True
        )
        prompt_ids = tokenizer(prompt_text, add_special_tokens=False)["input_ids"]

        # Tokenize 完整對話
        full_text = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=False
        )
        full_ids = tokenizer(
            full_text,
            truncation=True,
            max_length=MAX_LENGTH,
            padding=False,
            add_special_tokens=False,
        )["input_ids"]

        # Labels：prompt 部分設為 -100，只計算 assistant 回應的 loss
        prompt_len = min(len(prompt_ids), len(full_ids))
        labels = [-100] * prompt_len + full_ids[prompt_len:]

        all_input_ids.append(full_ids)
        all_attention_masks.append([1] * len(full_ids))
        all_labels.append(labels)

    return {
        "input_ids":      all_input_ids,
        "attention_mask": all_attention_masks,
        "labels":         all_labels,
    }


def main():
    print("=" * 60)
    print("Model 5 訓練開始")
    print(f"  基礎模型: {BASE_MODEL}")
    print(f"  訓練資料: {TRAIN_FILE}")
    print(f"  輸出目錄: {OUTPUT_DIR}")
    print("=" * 60)

    # ── 載入 Tokenizer ──
    print("\n[1/4] 載入 Tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL, trust_remote_code=True)
    tokenizer.padding_side = "right"
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # ── 載入模型（4-bit QLoRA）──
    print("[2/4] 載入模型（4-bit QLoRA）...")
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
    trainer.train()

    # ── 儲存 ──
    print("\n儲存 LoRA adapter...")
    model.save_pretrained(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)
    print(f"完成！模型儲存於: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
