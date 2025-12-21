import json
import glob
import os
import re
from collections import defaultdict

# ==========================================
# 1. 設定檔案路徑 (與你之前的設定相同)
# ==========================================
source_folder = r'C:\Users\User\Desktop\C.ai_project\n8n node json\n8n_AI_Agent\node_schemas'
output_json = 'n8n_node_index.json'

# ==========================================
# 2. 定義停用詞 (Stopwords)
# 這些詞彙太常見，不適合作為搜尋關鍵字
# ==========================================
STOPWORDS = {
    'the', 'a', 'an', 'to', 'of', 'in', 'for', 'with', 'on', 'by', 'and', 'or', 'is', 'it', 
    'n8n', 'node', 'nodes', 'base', 'api', 'service', 'use', 'integration', 'via'
}

def clean_and_tokenize(text):
    """
    將文字清理乾淨，拆解成關鍵字列表
    例如: "Consume the Action Network API" -> ['consume', 'action', 'network']
    """
    if not text:
        return []
    
    # 轉小寫，移除非英文字元
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    
    # 切割並過濾停用詞
    tokens = text.split()
    keywords = [t for t in tokens if t not in STOPWORDS and len(t) > 2]
    return list(set(keywords)) # 去除重複

# ==========================================
# 3. 主程式邏輯
# ==========================================
files = glob.glob(os.path.join(source_folder, '*.json'))
print(f"正在建立索引，共 {len(files)} 個檔案...")

# 資料結構
node_metadata = {}      # 儲存節點的基本資訊 (ID -> Info)
keyword_index = defaultdict(list) # 倒排索引 (Keyword -> List of Node IDs)
category_index = defaultdict(list) # 分類索引 (Group -> List of Node IDs)

for file_path in files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            # 1. 取得節點核心 ID (通常是 name)
            node_id = data.get('name')
            if not node_id:
                continue

            display_name = data.get('displayName', '')
            description = data.get('description', '')
            
            # 2. 儲存 Metadata (給 AI 最後確認用)
            node_metadata[node_id] = {
                "name": display_name,
                "description": description,
                "filename": os.path.basename(file_path)
            }
            
            # 3. 處理關鍵字 (從名稱和描述中提取)
            # 權重策略：名稱的關鍵字比較重要，描述的次之
            keywords = clean_and_tokenize(display_name + " " + description)
            
            for kw in keywords:
                keyword_index[kw].append(node_id)
                
            # 4. 處理內建分類 (如果有的話，n8n 有時會有 group 欄位)
            # 這能對應到學長架構中的 Taxonomy
            if 'group' in data and isinstance(data['group'], list):
                for grp in data['group']:
                    category_index[grp].append(node_id)

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# ==========================================
# 4. 輸出最終 JSON
# ==========================================
final_output = {
    "total_nodes": len(node_metadata),
    "generated_at": "auto-generated",
    "taxonomy": {
        "by_category": category_index,  # 依功能分類 (e.g., transform, trigger)
        "by_keyword": keyword_index     # 依關鍵字搜尋 (e.g., email, database)
    },
    "nodes": node_metadata              # 節點詳細對照表
}

with open(output_json, 'w', encoding='utf-8') as f:
    json.dump(final_output, f, indent=2, ensure_ascii=False)

print("-" * 30)
print(f"索引建立完成！")
print(f"檔案已儲存為: {output_json}")
print(f"共索引了 {len(keyword_index)} 個關鍵字。")