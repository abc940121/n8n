import json
import glob
import os
from collections import Counter

# ==========================================
# 設定：你的檔案路徑
# 使用 r'' (raw string) 避免 Windows 反斜線路徑錯誤
# ==========================================
target_folder = r'C:\Users\User\Desktop\C.ai_project\n8n node json\n8n_AI_Agent\node_schemas'
file_pattern = os.path.join(target_folder, '*.json')

# 用來儲存所有欄位結構的 Counter (統計頻率) 和字典 (儲存範例)
all_keys = Counter()
key_examples = {}

def extract_keys(data, parent_key=''):
    """遞迴提取 JSON 中的所有 Key，保留層級結構"""
    if isinstance(data, dict):
        for k, v in data.items():
            # 組合層級名稱，例如: properties.displayName
            current_key = f"{parent_key}.{k}" if parent_key else k
            all_keys[current_key] += 1
            
            # 存入範例值 (排除 dict/list，只存字串或數字，方便 AI 理解)
            if current_key not in key_examples and v is not None and not isinstance(v, (dict, list)):
                key_examples[current_key] = v
                
            extract_keys(v, current_key)
    elif isinstance(data, list):
        for item in data:
            extract_keys(item, parent_key)

# 1. 開始讀取檔案
files = glob.glob(file_pattern)
print(f"路徑: {target_folder}")
print(f"偵測到 {len(files)} 個 JSON 檔案，正在分析結構...")

if len(files) == 0:
    print("錯誤：找不到檔案，請確認路徑是否正確。")
else:
    for i, file in enumerate(files):
        try:
            with open(file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                extract_keys(data)
        except Exception as e:
            print(f"讀取錯誤 {file}: {e}")
            
        # 每處理 100 個檔案顯示一下進度
        if (i + 1) % 100 == 0:
            print(f"已處理 {i + 1} / {len(files)}...")

    # 2. 整理輸出格式
    output_summary = []
    # 依照出現頻率排序，最常見的欄位排前面
    for key, count in all_keys.most_common():
        output_summary.append({
            "field": key,           # 欄位名稱 (含層級)
            "count": count,         # 出現次數 (重要性指標)
            "example": key_examples.get(key, "N/A") # 範例值
        })

    # 3. 輸出結果檔案 (存在跟腳本同一個位置)
    output_filename = 'n8n_ontology_summary.json'
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(output_summary, f, indent=2, ensure_ascii=False)

    print("-" * 30)
    print(f"處理完成！")
    print(f"總共分析了 {len(all_keys)} 種不同的欄位結構。")
    print(f"結果已存為: {os.path.abspath(output_filename)}")
    print("請將此檔案上傳給 AI 進行 Ontology 建立。")