import json
import torch
import os
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
from tqdm import tqdm
import functools

print = functools.partial(print, flush=True)

# ==================== 設定區 (Model 3) ====================
BASE_MODEL = "/work/u4439705/models/Qwen3.5-27B"
LORA_ADAPTER = "/work/u4439705/n8n_qwen35_lora_model3"

INPUT_FILE = "/work/u4439705/data/test_100_prompts.jsonl"
OUTPUT_FILE = "/work/u4439705/n8n_predicted_workflows_model3.jsonl"

CHUNK_TOKENS = 8192   # 既然我們知道大約 8K 內能解完，我們直接將 Chunk 設大一點
MAX_CHUNKS = 1        # 只給一次接續機會，如果跑到 8192 還沒生成完，直接判定失敗截斷，避免 32K 迴圈

def main():
    print("\n" + "="*50)
    print("🚀 啟動 H200 Turbo 高速推論模式 - Model 3 (BF16 + 自動接續生成)")
    print("="*50 + "\n")

    processed_ids = set()
    if os.path.exists(OUTPUT_FILE):
        print(f"📄 發現現有的輸出檔：{OUTPUT_FILE}")
        with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if not line.strip(): continue
                try:
                    data = json.loads(line)
                    if "id" in data:
                        processed_ids.add(str(data["id"]))
                except json.JSONDecodeError:
                    continue
        print(f"🔄 已經完成 {len(processed_ids)} 筆資料，將自動跳過。")

    print("\n⏳ 載入 Tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(LORA_ADAPTER, trust_remote_code=True)
    
    print("⏳ 載入 Base Model (純 BF16)...")
    base_model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL,
        device_map="auto",
        trust_remote_code=True,
        torch_dtype=torch.bfloat16
    )

    print(f"🧬 載入並融合 LoRA Adapter ({LORA_ADAPTER})...")
    model = PeftModel.from_pretrained(base_model, LORA_ADAPTER)
    
    print("🔄 融合 LoRA 權重至主模型中...")
    model = model.merge_and_unload()
    model.eval()

    print(f"\n📖 讀取測試資料: {INPUT_FILE}")
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        test_data = [json.loads(line) for line in f]
    
    pending_tasks = [item for item in test_data if str(item["id"]) not in processed_ids]
    
    if not pending_tasks:
        print("🎉 所有資料都已經處理完畢，無須執行！")
        return

    print(f"🔥 開始超速推理 (Model 3)，剩餘 {len(pending_tasks)} 筆資料...")
    
    with open(OUTPUT_FILE, "a", encoding="utf-8") as out_f:
        for i, item in enumerate(tqdm(pending_tasks)):
            prompt = item["prompt"]
            messages = [
                {"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ]
            
            text = tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True
            )
            
            input_ids = tokenizer([text], return_tensors="pt").input_ids.to(model.device)
            original_input_len = input_ids.shape[1]
            current_ids = input_ids
            
            for chunk_idx in range(MAX_CHUNKS):
                with torch.no_grad():
                    outputs = model.generate(
                        input_ids=current_ids,
                        max_new_tokens=CHUNK_TOKENS,
                        do_sample=False,
                        repetition_penalty=1.05,
                        use_cache=True,
                        pad_token_id=tokenizer.eos_token_id,
                        eos_token_id=tokenizer.eos_token_id
                    )
                
                # 檢查這 Chunk 新產生的數量
                generated_tokens = outputs[0][current_ids.shape[1]:]
                current_ids = outputs # 更新為下回合的輸入
                
                # 判斷是否自然結束 (遇到 eos_token)
                if outputs[0][-1].item() == tokenizer.eos_token_id or len(generated_tokens) < CHUNK_TOKENS:
                    break
                
                print(f"\n🔄 模板 {item['id']} 已達 {CHUNK_TOKENS * (chunk_idx+1)} Tokens，自動從截斷處接續生成 (第 {chunk_idx+1}/{MAX_CHUNKS} 次接續)...")

            # 只擷取模型輸出的回覆部分 (扣掉最初的 Prompt)
            final_generated_ids = current_ids[0][original_input_len:]
            response = tokenizer.decode(final_generated_ids, skip_special_tokens=True)

            out_f.write(json.dumps({
                "id": item["id"],
                "prompt": prompt,
                "predicted": response
            }, ensure_ascii=False) + "\n")
            out_f.flush()

            del current_ids
            del input_ids
            del outputs

    print(f"✅ Model 3 推論全部完成！結果儲存在 {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
