import json
import glob
import os
import csv

# ==========================================
# 設定：你的檔案路徑
# ==========================================
source_folder = r'C:\Users\User\Desktop\C.ai_project\n8n node json\n8n_AI_Agent\node_schemas'
output_csv = 'n8n_nodes_structured_data_v2.csv'

# 新增了 auth_type, param_load_method, param_type_options
csv_headers = [
    "node_filename",
    "node_display_name", 
    "node_description",
    "auth_type",            # [新增] 憑證類型
    "param_name",
    "param_label",
    "param_type",
    "param_default",
    "param_required",
    "param_description",
    "param_load_method",    # [新增] 動態選單來源 (例如 getTags)
    "param_type_options",   # [新增] 額外設定 (例如 minValue, password)
    "display_condition",
    "options_list"
]

def format_condition(display_options):
    if not display_options or 'show' not in display_options:
        return ""
    conditions = []
    for key, val in display_options['show'].items():
        conditions.append(f"{key}={val}")
    return " AND ".join(conditions)

def extract_parameters(properties_list, node_info, writer):
    for prop in properties_list:
        # 提取 typeOptions 裡的詳細資訊
        type_opts = prop.get('typeOptions', {})
        load_method = type_opts.get('loadOptionsMethod', '')
        
        # 將 typeOptions 轉成字串，方便 AI 參考 (排除 loadOptionsMethod 以免重複)
        other_type_opts = {k:v for k,v in type_opts.items() if k != 'loadOptionsMethod'}
        type_opts_str = str(other_type_opts) if other_type_opts else ""

        row_data = {
            "node_filename": node_info['filename'],
            "node_display_name": node_info['displayName'],
            "node_description": node_info['description'],
            "auth_type": node_info['auth'],  # 填入憑證資訊
            
            "param_name": prop.get('name', ''),
            "param_label": prop.get('displayName', ''),
            "param_type": prop.get('type', ''),
            "param_default": str(prop.get('default', '')),
            "param_required": prop.get('required', False),
            "param_description": prop.get('description', ''),
            
            "param_load_method": load_method, # [新增]
            "param_type_options": type_opts_str, # [新增]
            
            "display_condition": format_condition(prop.get('displayOptions')),
            "options_list": ""
        }

        # 處理靜態 Options
        if 'options' in prop and isinstance(prop['options'], list):
            try:
                options = [str(opt.get('name', '')) for opt in prop['options'] if isinstance(opt, dict)]
                row_data["options_list"] = ", ".join(options)
            except:
                row_data["options_list"] = "Complex List"

        writer.writerow(row_data)

        # 遞迴處理巢狀結構
        if 'options' in prop and isinstance(prop['options'], list):
             for opt in prop['options']:
                 if isinstance(opt, dict) and 'values' in opt:
                     extract_parameters(opt['values'], node_info, writer)

# ==========================================
# 主程式
# ==========================================
files = glob.glob(os.path.join(source_folder, '*.json'))
print(f"找到 {len(files)} 個檔案，開始 V2 轉換...")

with open(output_csv, 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_headers)
    writer.writeheader()

    for file_path in files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                # [新增] 抓取 Credentials
                auth_info = ""
                if 'credentials' in data and isinstance(data['credentials'], list):
                    auths = [c.get('name', '') for c in data['credentials']]
                    auth_info = ", ".join(auths)

                node_info = {
                    "filename": os.path.basename(file_path),
                    "displayName": data.get('displayName', ''),
                    "description": data.get('description', ''),
                    "auth": auth_info
                }

                if 'properties' in data:
                    extract_parameters(data['properties'], node_info, writer)

        except Exception as e:
            print(f"Error {file_path}: {e}")

print("-" * 30)
print(f"V2 轉換完成！新檔案: {output_csv}")