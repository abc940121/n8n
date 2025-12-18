import json
import csv
import glob
import os

# --- 1. 定義 Ontology 欄位順序 ---
ONTOLOGY_COLUMNS = [
    # 核心識別
    "node_internal_name", "node_display_name", "node_description", "node_version", "node_category",
    # 連接架構
    "input_types", "output_types", "credential_types", "icon_name",
    # 互動模式
    "interaction_model", "trigger_type", "trigger_interval",
    # 功能分類
    "resources", "operations", "events", "generic_methods",
    # 資料處理
    "binary_handling", "supported_file_formats", "data_transformation",
    # 參數特徵
    "standard_parameters", "pagination_mode", "dynamic_parameters", "complex_ui_elements",
    # AI 與 Meta
    "ai_features", "ai_model_parameters", "documentation_url", "special_notices"
]

def extract_options(parameter):
    """從參數中提取 options 列表"""
    if not parameter or 'options' not in parameter:
        return []
    return [opt.get('name', opt.get('value')) for opt in parameter['options']]

def map_node_to_ontology(node):
    """將單一 n8n 節點 JSON 映射到 Ontology 欄位"""
    
    # 初始化空資料
    data = {col: "" for col in ONTOLOGY_COLUMNS}
    
    # 1. 核心識別
    data['node_internal_name'] = node.get('name', '')
    data['node_display_name'] = node.get('displayName', '')
    data['node_description'] = node.get('description', '')
    data['node_version'] = node.get('version', 1)
    # Icon 通常在原始碼中，這裡嘗試讀取 defaults
    data['icon_name'] = node.get('icon', '') 
    
    # 2. 推斷 Input/Output (簡易邏輯)
    # n8n JSON 通常不直接寫 inputs/outputs，需依賴 inputs 屬性或預設值
    data['input_types'] = str(node.get('inputs', []))
    data['output_types'] = str(node.get('outputs', []))
    
    # 3. 屬性遍歷 (Properties Loop)
    properties = node.get('properties', [])
    
    resources = set()
    operations = set()
    events = set()
    std_params = set()
    complex_ui = set()
    
    has_binary = False
    
    for prop in properties:
        p_name = prop.get('name', '')
        p_type = prop.get('type', '')
        
        # 歸類 Resource/Operation/Event
        if p_name == 'resource':
            resources.update(extract_options(prop))
        elif p_name == 'operation':
            operations.update(extract_options(prop))
        elif p_name == 'event' or p_name == 'events':
            events.update(extract_options(prop))
            
        # 偵測標準參數
        if p_name in ['limit', 'returnAll', 'simple']:
            std_params.add(p_name)
            
        # 偵測二進位處理
        if p_name == 'binaryPropertyName' or p_type == 'binary':
            has_binary = True
            
        # 偵測複雜 UI
        if p_type in ['collection', 'fixedCollection', 'json']:
            complex_ui.add(p_name)

    # 4. 填入集合資料 (轉換為字串以存入 CSV)
    data['resources'] = str(list(resources)) if resources else ""
    data['operations'] = str(list(operations)) if operations else ""
    data['events'] = str(list(events)) if events else ""
    data['standard_parameters'] = str(list(std_params))
    data['complex_ui_elements'] = str(list(complex_ui))
    data['binary_handling'] = str(has_binary)
    
    # 5. 推斷 Interaction Model (規則引擎)
    display_name = data['node_display_name'].lower()
    if 'trigger' in display_name:
        data['interaction_model'] = 'Trigger'
        data['trigger_type'] = 'Webhook' if 'webhook' in data['node_description'].lower() else 'Polling'
    elif 'agent' in display_name or 'chain' in display_name:
        data['interaction_model'] = 'Logic'
        data['ai_features'] = str(['AI Integration'])
    elif resources:
        data['interaction_model'] = 'Resource-Based'
    else:
        data['interaction_model'] = 'Generic-API'

    return data

def main():
    # 1. 搜尋所有 batch JSON 檔案
    files = glob.glob('batch_*.json')
    files.sort()
    
    if not files:
        print("❌ 找不到 batch_*.json 檔案，請確認路徑。")
        return

    all_rows = []
    print(f"🔍 發現 {len(files)} 個檔案，開始處理...")

    # 2. 讀取並處理每個檔案
    for file_path in files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = json.load(f)
                
                # 處理 content 是 List 還是 Dict 的情況
                nodes = []
                if isinstance(content, list):
                    nodes = content
                elif isinstance(content, dict) and 'nodes' in content:
                    nodes = content['nodes']
                else:
                    # 如果是單一節點結構
                    nodes = [content]

                for node in nodes:
                    # 部分檔案可能包了一層 fullContent
                    target_node = node.get('fullContent', node)
                    row = map_node_to_ontology(target_node)
                    all_rows.append(row)
                    
        except Exception as e:
            print(f"⚠️ 處理檔案 {file_path} 時發生錯誤: {e}")

    # 3. 輸出 CSV
    output_file = 'n8n_ontology_full_list.csv'
    with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=ONTOLOGY_COLUMNS)
        writer.writeheader()
        writer.writerows(all_rows)

    print(f"\n✅ 成功！已將 {len(all_rows)} 個節點轉換為 '{output_file}'")
    print("👉 CSV 格式已自動處理引號與逗號問題，可直接用 Excel 開啟。")

if __name__ == "__main__":
    main()