"""
Qwen 3.5 27B QLoRA Fine-tuning Script (Updated for 'messages' format)
直接使用 transformers + peft + bitsandbytes
"""
import json
import torch
import os
from datasets import Dataset
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    TrainingArguments,
    Trainer,
    DataCollatorForSeq2Seq,
    BitsAndBytesConfig,
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training

# ==================== 設定區 (Model 3) ====================
MODEL_PATH = "/work/u4439705/models/Qwen3.5-27B"
DATA_FILE = "/work/u4439705/data/create_highfreq_no_sticky_prefixed_train_messages.jsonl"
OUTPUT_DIR = "/work/u4439705/n8n_qwen35_lora_model3"

# 訓練參數
NUM_EPOCHS = 3
LEARNING_RATE = 1e-4
BATCH_SIZE = 1
GRAD_ACCUM_STEPS = 8
CUTOFF_LEN = 4096
LORA_RANK = 16
LORA_ALPHA = 32

# 測試模式：設定 None 處理全部，或設定數字只處理前 N 筆
MAX_SAMPLES = None 

# ==================== 載入資料 ====================
print("📂 載入訓練資料 (Model 3)...")
raw_data = []
with open(DATA_FILE, "r", encoding="utf-8") as f:
    for line in f:
        item = json.loads(line.strip())
        raw_data.append(item)

if MAX_SAMPLES:
    raw_data = raw_data[:MAX_SAMPLES]
    print(f"⚡ 測試模式：只使用前 {MAX_SAMPLES} 筆資料")

print(f"✅ 載入 {len(raw_data)} 筆訓練資料")

# ==================== 載入 Tokenizer ====================
print("🔤 載入 Tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH,
    trust_remote_code=True,
    padding_side="right",
)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# ==================== 資料預處理 ====================
print("🔧 預處理資料 (處理 messages 格式)...")

def format_and_tokenize(examples):
    """將 messages 轉成 chat format 並 tokenize"""
    input_ids_list = []
    labels_list = []

    for messages in examples["messages"]:
        # 假設每個 messages 最後一個是 assistant 的回答
        # 找出最後一個 assistant message 之前的訊息作為 prompt
        user_messages = []
        assistant_content = ""
        
        for msg in messages:
            if msg["role"] == "assistant":
                assistant_content = msg["content"]
                break
            user_messages.append(msg)

        # Tokenize prompt 部分
        prompt_text = tokenizer.apply_chat_template(
            user_messages, tokenize=False, add_generation_prompt=True
        )
        prompt_ids = tokenizer(prompt_text, add_special_tokens=False)["input_ids"]

        # Tokenize 完整對話
        full_text = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=False
        )
        full_ids = tokenizer(full_text, add_special_tokens=False)["input_ids"]

        # 截斷
        if len(full_ids) > CUTOFF_LEN:
            full_ids = full_ids[:CUTOFF_LEN]

        # 建立 labels
        prompt_len = min(len(prompt_ids), len(full_ids))
        labels = [-100] * prompt_len + full_ids[prompt_len:]

        input_ids_list.append(full_ids)
        labels_list.append(labels)

    return {"input_ids": input_ids_list, "labels": labels_list}

# 建立 Dataset
dataset = Dataset.from_list(raw_data)
tokenized_dataset = dataset.map(
    format_and_tokenize,
    batched=True,
    batch_size=100,
    remove_columns=dataset.column_names,
    desc="Tokenizing",
)

print(f"✅ Tokenize 完成，共 {len(tokenized_dataset)} 筆")

# ==================== 載入模型 (4-bit QLoRA) ====================
print("🚀 載入 Qwen 3.5 27B (4-bit 量化)...")

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True,
)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    quantization_config=bnb_config,
    device_map="auto",
    trust_remote_code=True,
    torch_dtype=torch.bfloat16,
)

model = prepare_model_for_kbit_training(model)

lora_config = LoraConfig(
    r=LORA_RANK,
    lora_alpha=LORA_ALPHA,
    lora_dropout=0.05,
    target_modules="all-linear",
    task_type="CAUSAL_LM",
)

model = get_peft_model(model, lora_config)
model.print_trainable_parameters()

# ==================== 訓練設定 ====================
print("⚙️ 設定訓練參數...")

training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    num_train_epochs=NUM_EPOCHS,
    per_device_train_batch_size=BATCH_SIZE,
    gradient_accumulation_steps=GRAD_ACCUM_STEPS,
    learning_rate=LEARNING_RATE,
    lr_scheduler_type="cosine",
    warmup_ratio=0.1,
    bf16=True,
    logging_steps=10,
    save_steps=200,
    save_total_limit=3,
    gradient_checkpointing=True,
    gradient_checkpointing_kwargs={"use_reentrant": False},
    report_to="none",
    remove_unused_columns=False,
)

data_collator = DataCollatorForSeq2Seq(
    tokenizer=tokenizer,
    padding=True,
    return_tensors="pt",
)

# ==================== 開始訓練 ====================
print("🏋️ 開始訓練 Model 3！")

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    data_collator=data_collator,
)

trainer.train()

# ==================== 儲存模型 ====================
print("💾 儲存 LoRA adapter...")
model.save_pretrained(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)

print(f"✅ Model 3 訓練完成！模型儲存在 {OUTPUT_DIR}")
