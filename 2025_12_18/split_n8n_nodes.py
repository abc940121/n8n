import json
import os
import math
import re

# 設定參數
SOURCE_FILE = 'All_n8n_nodes.json'  # 你的原始檔名
OUTPUT_DIR = 'n8n_batches'          # 輸出資料夾名稱
BATCH_SIZE = 40                     # 每個檔案包含的節點數量 (建議 40-50)

def sanitize_filename(name):
    """移除非法字元以作為檔名"""
    return re.sub(r'[\\/*?:"<>|]', "", name)

def main():
    # 1. 建立輸出資料夾
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"建立資料夾: {OUTPUT_DIR}")

    # 2. 讀取原始 JSON
    try:
        with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"成功讀取 {len(data)} 個節點資料。")
    except FileNotFoundError:
        print(f"錯誤: 找不到檔案 {SOURCE_FILE}，請確認檔名與路徑。")
        return

    # 3. 資料前處理與排序
    # 我們需要從結構中提取 fullContent 並依照 displayName 排序
    # 原始結構看起來是 List[Dict]，包含 fileName 和 fullContent
    
    nodes_list = []
    for item in data:
        if 'fullContent' in item:
            nodes_list.append(item['fullContent'])
        else:
            # 防呆：如果結構不同，直接視為節點本身
            nodes_list.append(item)

    # 依照 displayName 排序 (如果沒有 displayName 則用 name)
    # 這樣可以確保相似的服務 (如 AWS, Google) 會被分在同一組
    nodes_list.sort(key=lambda x: x.get('displayName', x.get('name', 'UNKNOWN')))

    # 4. 進行分批切檔
    total_batches = math.ceil(len(nodes_list) / BATCH_SIZE)
    print(f"預計分為 {total_batches} 個批次檔案...\n")

    for i in range(total_batches):
        start_idx = i * BATCH_SIZE
        end_idx = start_idx + BATCH_SIZE
        batch_nodes = nodes_list[start_idx:end_idx]
        
        # 取得該批次第一個和最後一個節點名稱，標記在檔名上方便識別
        first_name = sanitize_filename(batch_nodes[0].get('displayName', 'Node'))
        last_name = sanitize_filename(batch_nodes[-1].get('displayName', 'Node'))
        
        # 簡化檔名，避免過長
        filename = f"batch_{i+1:02d}_{first_name}_to_{last_name}.json"
        # 如果檔名太長，截斷一下
        if len(filename) > 50:
             filename = f"batch_{i+1:02d}_{first_name}.json"

        output_path = os.path.join(OUTPUT_DIR, filename)
        
        # 寫入檔案
        with open(output_path, 'w', encoding='utf-8') as out_f:
            json.dump(batch_nodes, out_f, ensure_ascii=False, indent=2)
            
        print(f"[{i+1}/{total_batches}] 已輸出: {filename} (含 {len(batch_nodes)} 個節點)")

    print(f"\n✅ 完成！所有檔案已存於 '{OUTPUT_DIR}' 資料夾中。")

if __name__ == "__main__":
    main()