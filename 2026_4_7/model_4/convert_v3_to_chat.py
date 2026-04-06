"""
convert_v3_to_chat.py
將 qwen27b_v3_train.jsonl / qwen27b_v3_test.jsonl
從 instruction/input/output 格式
轉換為 Qwen Chat Messages 格式 (messages list)
"""

import json
import os

# ── 路徑設定 ──────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR  = os.path.join(BASE_DIR, "..", "my_qwen_test")
OUT_DIR  = os.path.join(BASE_DIR)

SPLITS = {
    "train": "qwen27b_v3_train.jsonl",
    "valid": "qwen27b_v3_test.jsonl",   # 用 test 當 validation
}

# ── System Prompt（保持中文，讓模型學會中文指令→英文JSON的映射）──
SYSTEM_PROMPT = (
    "你是一個專業的 n8n 工作流程生成助手。"
    "請根據使用者的需求描述，生成一個節點與連線皆正確且能成功執行的 n8n workflow JSON。"
    "輸出必須是純 JSON 格式，包含 nodes 和 connections 兩個頂層欄位，不需要任何額外說明文字。"
)

def convert_record(rec: dict) -> dict | None:
    """將單筆 instruction/input/output 記錄轉為 messages 格式"""
    instruction = (rec.get("instruction") or "").strip()
    input_text  = (rec.get("input")       or "").strip()
    output_text = (rec.get("output")      or "").strip()

    if not output_text:
        return None  # 跳過沒有輸出的記錄

    # User message: instruction 作為背景說明，input 作為實際需求
    if input_text:
        user_content = f"{instruction}\n\n{input_text}" if instruction else input_text
    else:
        user_content = instruction

    return {
        "messages": [
            {"role": "system",    "content": SYSTEM_PROMPT},
            {"role": "user",      "content": user_content},
            {"role": "assistant", "content": output_text},
        ]
    }

def convert_file(src_path: str, dst_path: str) -> tuple[int, int]:
    """轉換整個檔案，回傳 (成功數, 跳過數)"""
    ok = skip = 0
    with open(src_path, "r", encoding="utf-8") as fin, \
         open(dst_path, "w", encoding="utf-8") as fout:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
                converted = convert_record(rec)
                if converted:
                    fout.write(json.dumps(converted, ensure_ascii=False) + "\n")
                    ok += 1
                else:
                    skip += 1
            except json.JSONDecodeError as e:
                print(f"  [WARN] JSON 解析失敗: {e}")
                skip += 1
    return ok, skip

def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    for split, src_name in SPLITS.items():
        src_path = os.path.join(SRC_DIR, src_name)
        dst_name = f"v3_{split}_chat.jsonl"
        dst_path = os.path.join(OUT_DIR, dst_name)

        if not os.path.exists(src_path):
            print(f"[SKIP] 找不到來源檔案: {src_path}")
            continue

        print(f"[{split.upper()}] 轉換 {src_name} → {dst_name}")
        ok, skip = convert_file(src_path, dst_path)
        print(f"  ✅ 成功: {ok} 筆   ⚠️  跳過: {skip} 筆")
        print(f"  儲存到: {dst_path}\n")

    # 快速驗證：印出第 1 筆轉換後的資料
    sample_path = os.path.join(OUT_DIR, "v3_train_chat.jsonl")
    if os.path.exists(sample_path):
        print("=" * 60)
        print("📋 驗證：第 1 筆轉換後的資料結構")
        print("=" * 60)
        with open(sample_path, "r", encoding="utf-8") as f:
            sample = json.loads(f.readline())
        for msg in sample["messages"]:
            role = msg["role"]
            content_preview = msg["content"][:120].replace("\n", "\\n")
            print(f"  [{role}] {content_preview}{'...' if len(msg['content']) > 120 else ''}")
        print()
        print("格式驗證完成！可以開始用於 Qwen fine-tuning。")

if __name__ == "__main__":
    main()
