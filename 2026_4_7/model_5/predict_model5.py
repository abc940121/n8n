#!/usr/bin/env python3
"""
predict_model5.py  —  Model 5 推論腳本
讀取 qwen27b_v3_test_openai.jsonl，對每筆 user 訊息進行推論，輸出 JSONL

使用方式（在 NCHC 上）:
  python predict_model5.py
"""

import os, json, torch, re
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

# ── 路徑設定 ──────────────────────────────────────────────
BASE_MODEL  = "/work/u4439705/models/Qwen3.5-27B"
LORA_DIR    = "/work/u4439705/n8n_qwen35_lora_model5"
INPUT_FILE  = "/work/u4439705/model_5/qwen27b_v3_test_openai.jsonl"
OUTPUT_FILE = "/work/u4439705/model_5/n8n_predicted_model5.jsonl"

MAX_NEW_TOKENS = 8192
MAX_RETRIES    = 2


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


def extract_json(text: str) -> str:
    """若輸出包含思考文字，提取 { 開始的 JSON 部分"""
    text = text.strip()
    json_start = text.find('{')
    if json_start > 0:
        text = text[json_start:]
    return text


def generate_with_continuation(tokenizer, model, messages: list) -> str:
    """支援自動接續生成，處理超長輸出"""
    current_messages = messages.copy()
    full_output = ""

    for attempt in range(MAX_RETRIES + 1):
        prompt = tokenizer.apply_chat_template(
            current_messages,
            tokenize=False,
            add_generation_prompt=True,
            enable_thinking=False,  # 關閉思考模式，直接輸出 JSON
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

        stripped = full_output.strip()
        if stripped.endswith("}") or stripped.endswith("}}}"):
            break

        if attempt < MAX_RETRIES:
            print(f"    輸出可能截斷，嘗試接續 (第 {attempt+1} 次)...")
            current_messages = current_messages + [
                {"role": "assistant", "content": full_output},
                {"role": "user",      "content": "請繼續完成未完成的 JSON，從中斷處開始，不要重複已輸出的內容。"},
            ]

    return extract_json(full_output)


def main():
    print("=" * 60)
    print("Model 5 推論開始")
    print(f"  輸入: {INPUT_FILE}")
    print(f"  輸出: {OUTPUT_FILE}")
    print("=" * 60)

    tokenizer, model = load_model(BASE_MODEL, LORA_DIR)

    records = []
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    print(f"共 {len(records)} 筆待推論\n")

    # 斷點續傳
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

            # 取出 prompt（system + user），遮住 assistant 答案
            infer_messages = [m for m in messages if m["role"] != "assistant"]
            ground_truth = next(
                (m["content"] for m in messages if m["role"] == "assistant"), ""
            )

            print(f"[{idx+1}/{len(records)}] 推論中...")
            try:
                predicted = generate_with_continuation(tokenizer, model, infer_messages)
            except Exception as e:
                predicted = f"ERROR: {e}"
                print(f"  錯誤: {e}")

            result = {
                "id":           rid,
                "prompt":       next((m["content"] for m in messages if m["role"] == "user"), "")[:200],
                "predicted":    predicted,
                "ground_truth": ground_truth,
            }
            fout.write(json.dumps(result, ensure_ascii=False) + "\n")
            fout.flush()

            preview = predicted[:80].replace("\n", "\\n")
            print(f"  輸出預覽: {preview}...")

    print(f"\n推論完成！結果儲存於: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
