import json
import os
import re

INPUT_FILE = r"c:\Users\User\Desktop\C.ai_project\2026_4_7\n8n_predicted_workflows_v2.jsonl"
CLEAN_FILE = r"c:\Users\User\Desktop\C.ai_project\2026_4_7\n8n_predicted_workflows_v2_clean.jsonl"

def extract_json(text_content):
    if not text_content:
        return None
    
    text_content = text_content.strip()
    
    # Try direct parse
    try:
        return json.loads(text_content)
    except json.JSONDecodeError:
        pass
        
    # Remove markdown formatting
    if text_content.startswith('```'):
        lines = text_content.split('\n')
        text_content_no_md = '\n'.join([
            line for line in lines
            if not line.strip().startswith('```')
        ])
        try:
            return json.loads(text_content_no_md)
        except json.JSONDecodeError:
            pass

    # Try heuristic 1: Regex
    json_match = re.search(r'\{.*\}', text_content, re.DOTALL)
    if json_match:
        try:
            return json.loads(json_match.group())
        except json.JSONDecodeError:
            pass
            
    # 我們不在此處使用「退回式修補」 (Heuristic 2: Truncated JSON)
    # 因為我們要找出「真的被截斷」的，如果我們幫他修補了，反而就以為它沒斷！
    return None

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: 找不到 {INPUT_FILE}")
        return

    good_count = 0
    bad_count = 0
    bad_ids = []

    with open(INPUT_FILE, "r", encoding="utf-8") as in_f, \
         open(CLEAN_FILE, "w", encoding="utf-8") as out_f:
        
        for line in in_f:
            if not line.strip(): continue
            
            data = json.loads(line)
            predicted = data.get("predicted", "")
            
            parsed_json = extract_json(predicted)
            
            if parsed_json is not None:
                # 完整的 JSON，寫入乾淨檔案
                out_f.write(line)
                good_count += 1
            else:
                # 截斷的 JSON (或者完全爛掉的)，不寫入
                bad_count += 1
                bad_ids.append(str(data.get("id")))

    print("="*50)
    print("📊 截斷資料清理報告 (修正版)")
    print("="*50)
    print(f"✅ 完整生成的模板數量: {good_count}")
    print(f"❌ 被截斷/損毀的模板數量: {bad_count}")
    if bad_count > 0:
        print(f"📌 被截斷的 ID: {', '.join(bad_ids)}")
        print(f"\n💡 處理方式：我們已經把這 {bad_count} 筆截斷的資料從紀錄中移除，並存成 {CLEAN_FILE}。")

if __name__ == "__main__":
    main()
