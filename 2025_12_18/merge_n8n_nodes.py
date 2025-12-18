import os
import json

# 設定您的檔案資料夾路徑 (如果是當前目錄則用 '.')
source_folder = r'C:\Users\User\Desktop\C.ai_project\n8n node json\n8n_AI_Agent\node_schemas'
output_file = 'All_n8n_nodes.json'

merged_data = []

# 遍歷資料夾
for filename in os.listdir(source_folder):
    if filename.endswith('.json'):
        file_path = os.path.join(source_folder, filename)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = json.load(f)
                
                # 將檔名與內容封裝在一起，確保資訊不流失
                file_entry = {
                    "fileName": filename,
                    "fullContent": content
                }
                merged_data.append(file_entry)
        except Exception as e:
            print(f"Skipping {filename}: {str(e)}")

# 輸出合併後的檔案
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(merged_data, f, ensure_ascii=False, indent=2)

print(f"成功合併 {len(merged_data)} 個檔案至 {output_file}")