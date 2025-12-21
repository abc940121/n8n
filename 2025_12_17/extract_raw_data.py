import json
import glob
import os
import re

# ================= 配置區域 =================
# 請修改為你的 n8n JSON 檔案路徑
SOURCE_FOLDER = r'C:\Users\User\Desktop\C.ai_project\n8n node json\n8n_AI_Agent\node_schemas'
OUTPUT_FILE = 'raw_mapped_data.json'
# ===========================================

def generate_path_id(parent_path, current_name, index=None):
    """生成結構化的唯一 Path ID (Structural Path)"""
    # 清理名稱中的特殊字符，只保留 alphanumeric 和底線
    safe_name = re.sub(r'[^a-zA-Z0-9_]', '', current_name)
    segment = f"{safe_name}"
    if index is not None:
        segment += f"[{index}]"
    
    if parent_path:
        return f"{parent_path}.{segment}"
    return segment

def extract_raw_options(prop):
    """提取靜態選項 (Static Options)"""
    options = []
    if 'options' in prop and isinstance(prop['options'], list):
        for opt in prop['options']:
            if isinstance(opt, dict):
                options.append({
                    "label": opt.get('displayName', opt.get('name', '')),
                    "value_raw": opt.get('value', None),
                    "description": opt.get('description', '')
                })
    return options

def extract_dynamic_loader(prop):
    """提取動態載入設定 (Dynamic Loader)"""
    loader = {}
    if 'typeOptions' in prop:
        t_opts = prop['typeOptions']
        if 'loadOptionsMethod' in t_opts:
            loader['method'] = t_opts['loadOptionsMethod']
        if 'loadOptionsDependsOn' in t_opts:
            loader['depends_on'] = t_opts['loadOptionsDependsOn']
    return loader

def process_properties(properties, parent_path_id, flattened_list):
    """遞迴處理參數列表，將其扁平化"""
    for idx, prop in enumerate(properties):
        # 1. 基礎識別
        prop_name = prop.get('name', f'unnamed_{idx}')
        # 為了保證唯一性，對於 list 中的元素，我們加上 index 作為 path 的一部分
        # 這裡使用結構化路徑：parent.name
        # 如果是 fixedCollection，name 通常是 collection 名稱
        current_path_id = generate_path_id(parent_path_id, prop_name)

        # 2. 建立參數物件 (Parameter Entity)
        param_entry = {
            "identity": {
                "name": prop_name,
                "label": prop.get('displayName', prop_name),
                "path_id": current_path_id,
                "parent_path_id": parent_path_id,
                "role": "parameter" # 預設，待 LLM 修正
            },
            "data_type": {
                "ui_type": prop.get('type', 'unknown'),
                "value_type": "unknown", # 待推斷
                "is_secret": prop.get('typeOptions', {}).get('password', False)
            },
            "constraints": {
                "required": prop.get('required', False),
                "default_value": prop.get('default', None),
                "validation": {
                    "regex": prop.get('typeOptions', {}).get('regex', None),
                    "min": prop.get('typeOptions', {}).get('minValue', None),
                    "max": prop.get('typeOptions', {}).get('maxValue', None)
                }
            },
            "display_logic": {
                # 這裡只存 RAW data，留給 LLM 解析結構
                "raw_display_options": prop.get('displayOptions', None)
            },
            "options_config": {
                "mode": "static" if 'options' in prop and isinstance(prop['options'], list) else "dynamic" if 'loadOptionsMethod' in prop.get('typeOptions', {}) else "none",
                "static_options": extract_raw_options(prop),
                "dynamic_loader": extract_dynamic_loader(prop)
            }
        }
        
        flattened_list.append(param_entry)

        # 3. 遞迴處理子層級 (Nested Properties)
        # Case A: options (常見於 fixedCollection 或簡單 options)
        if 'options' in prop and isinstance(prop['options'], list):
            for opt_idx, opt in enumerate(prop['options']):
                # 如果 option 裡面有 'values'，代表它是 fixedCollection 的一組欄位
                if 'values' in opt and isinstance(opt['values'], list):
                    # 建立中間層級的路徑，例如 collection.optionName
                    opt_name = opt.get('name', f'opt_{opt_idx}')
                    nested_parent_path = generate_path_id(current_path_id, opt_name)
                    process_properties(opt['values'], nested_parent_path, flattened_list)

def main():
    files = glob.glob(os.path.join(SOURCE_FOLDER, '*.json'))
    print(f"偵測到 {len(files)} 個檔案，開始執行 [Transformer V1 - Raw Extraction]...")

    all_nodes = []
    
    for i, file_path in enumerate(files):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                # 1. 處理 Node Identity
                system_name = data.get('name', os.path.basename(file_path).replace('.json', ''))
                
                node_obj = {
                    "node_identity": {
                        "system_name": system_name,
                        "display_name": data.get('displayName', system_name),
                        "description": data.get('description', ''),
                        "icon": data.get('icon', ''),
                        "codex_category": os.path.basename(os.path.dirname(file_path)),
                        "version": 1 # 預設，若檔名有 version 可解析
                    },
                    "node_context": {
                        "auth_types": [], # 待 LLM 或後續規則補齊
                        "search_text": f"{data.get('displayName', '')} {data.get('description', '')}"
                    },
                    "parameters_flat": [] # 暫存扁平化參數列表
                }
                
                # 2. 處理 Parameters (遞迴扁平化)
                if 'properties' in data and isinstance(data['properties'], list):
                    # Root path id 就是 node system name
                    process_properties(data['properties'], system_name, node_obj['parameters_flat'])
                
                all_nodes.append(node_obj)
                
        except Exception as e:
            print(f"[ERROR] 處理檔案 {file_path} 失敗: {e}")

        if (i + 1) % 100 == 0:
            print(f"已處理 {i + 1}/{len(files)}...")

    # 3. 輸出結果
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump({"ontology_meta": {"version": "v1.0-raw", "type": "flat-parameters"}, "nodes": all_nodes}, f, indent=2, ensure_ascii=False)

    print("-" * 30)
    print(f"處理完成！結果已存為: {OUTPUT_FILE}")
    print(f"總共處理了 {len(all_nodes)} 個節點。")
    print("下一步：請將此檔案分批餵給 LLM 進行 [Step 2: Semantic Enrichment]。")

if __name__ == "__main__":
    main()