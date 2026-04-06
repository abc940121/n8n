#!/usr/bin/env python3
"""
predict_model4.py  —  Model 4 推論腳本
讀取 v3_valid_chat.jsonl，對每筆 user 訊息進行推論，輸出 JSONL

使用方式（在 NCHC 上）:
  python predict_model4.py
"""

import os, json, torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

# ── 路徑設定 ──────────────────────────────────────────────
BASE_MODEL  = "/work/u4439705/models/Qwen3.5-27B"
LORA_DIR    = "/work/u4439705/n8n_qwen35_lora_model4"
INPUT_FILE  = "/work/u4439705/model_4/v3_valid_chat.jsonl"
OUTPUT_FILE = "/work/u4439705/model_4/n8n_predicted_model4.jsonl"

MAX_NEW_TOKENS  = 8192
MAX_RETRIES     = 2      # 截斷時自動接續次數

SYSTEM_PROMPT = (
    "你是一個專業的 n8n 工作流程生成助手。"
    "請根據使用者的需求描述，生成一個節點與連線皆正確且能成功執行的 n8n workflow JSON。"
    "輸出必須是純 JSON 格式，包含 nodes 和 connections 兩個頂層欄位，不需要任何額外說明文字。"
)


def load_model(base_model: str, lora_dir: str):
    print("載入 Tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(base_model, trust_remote_code=True)
    tokenizer.padding_side = "left"

    print("載入基礎模型（BF16）...")
    model = AutoModelForCausalLM.from_pretrained(
        base_model,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
    )
    print("掛載 LoRA adapter...")
    model = PeftModel.from_pretrained(model, lora_dir)
    model = model.merge_and_unload()
    model.eval()
    print("模型載入完成！")
    return tokenizer, model


def generate_with_continuation(tokenizer, model, messages: list[dict]) -> str:
    """支援自動接續生成，處理超長輸出"""
    current_messages = messages.copy()
    full_output = ""

    for attempt in range(MAX_RETRIES + 1):
        prompt = tokenizer.apply_chat_template(
            current_messages,
            tokenize=False,
            add_generation_prompt=True,
            enable_thinking=False,  # 關閉 Qwen3.5 思考模式，直接輸出 JSON
        )
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

        with torch.no_grad():
            output_ids = model.generate(
                **inputs,
                max_new_tokens=MAX_NEW_TOKENS,
                do_sample=False,
                temperature=1.0,
                repetition_penalty=1.05,
                pad_token_id=tokenizer.eos_token_id,
            )

        new_ids = output_ids[0][inputs["input_ids"].shape[1]:]
        new_text = tokenizer.decode(new_ids, skip_special_tokens=True).strip()
        full_output += new_text

        # 判斷是否完整（包含完整的 JSON 結尾）
        stripped = full_output.strip()
        if stripped.endswith("}") or stripped.endswith("}}}"):
            break

        # 不完整，嘗試接續
        if attempt < MAX_RETRIES:
            print(f"    輸出可能截斷，嘗試接續 (第 {attempt+1} 次)...")
            current_messages = current_messages + [
                {"role": "assistant", "content": full_output},
                {"role": "user",      "content": "請繼續完成未完成的 JSON，從中斷處開始，不要重複已輸出的內容。"},
            ]

    # 後處理：若輸出包含思考文字，嘗試提取 JSON 部分
    output = full_output.strip()
    # 尋找第一個 { 開始的位置
    json_start = output.find('{')
    if json_start > 0:
        output = output[json_start:]
    return output


def main():
    print("=" * 60)
    print("Model 4 推論開始")
    print(f"  輸入: {INPUT_FILE}")
    print(f"  輸出: {OUTPUT_FILE}")
    print("=" * 60)

    tokenizer, model = load_model(BASE_MODEL, LORA_DIR)

    # 讀取驗證集
    records = []
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    print(f"共 {len(records)} 筆待推論\n")

    # 輸出檔案（續寫模式，支援中斷恢復）
    done_ids = set()
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    try:
                        done_ids.add(json.loads(line)["id"])
                    except Exception:
                        pass
        print(f"偵測到已有 {len(done_ids)} 筆結果，將跳過重複推論")

    with open(OUTPUT_FILE, "a", encoding="utf-8") as fout:
        for idx, rec in enumerate(records):
            rid = idx
            if rid in done_ids:
                continue

            messages = rec.get("messages", [])
            # 取出 user 訊息，重建為推論用 messages
            user_content = next(
                (m["content"] for m in messages if m["role"] == "user"), ""
            )
            ground_truth = next(
                (m["content"] for m in messages if m["role"] == "assistant"), ""
            )

            infer_messages = [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": user_content},
            ]

            print(f"[{idx+1}/{len(records)}] 推論中...")
            try:
                predicted = generate_with_continuation(tokenizer, model, infer_messages)
            except Exception as e:
                predicted = f"ERROR: {e}"
                print(f"  錯誤: {e}")

            result = {
                "id":           rid,
                "prompt":       user_content[:200],
                "predicted":    predicted,
                "ground_truth": ground_truth,
            }
            fout.write(json.dumps(result, ensure_ascii=False) + "\n")
            fout.flush()

            # 速覽輸出
            preview = predicted[:80].replace("\n", "\\n")
            print(f"  輸出預覽: {preview}...")

    print(f"\n推論完成！結果儲存於: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
