import json
import csv
import re

# --- 1. 定義 Ontology 欄位 ---
ONTOLOGY_COLUMNS = [
    "node_internal_name", "node_display_name", "node_description", "node_category",
    "input_types", "output_types", "credential_types",
    "interaction_model", "trigger_type",
    "resources", "operations", "events", 
    "standard_parameters", "binary_handling", "ai_features",
    "complex_ui_elements", "dynamic_parameters", "special_notices"
]

# --- 2. 輔助推斷邏輯 ---

def infer_category(name, display_name):
    """從名稱推斷分類"""
    name_lower = name.lower()
    if 'aws' in name_lower or 'cloud' in name_lower or 'google' in name_lower:
        return 'Cloud & IT'
    if 'sql' in name_lower or 'mongo' in name_lower or 'db' in name_lower:
        return 'Database'
    if 'mail' in name_lower or 'slack' in name_lower or 'telegram' in name_lower:
        return 'Communication'
    if 'trigger' in name_lower:
        return 'Trigger'
    if 'transform' in name_lower or 'compression' in name_lower:
        return 'Data Transformation'
    if 'langchain' in name_lower or 'ai' in name_lower or 'gpt' in name_lower:
        return 'AI & Logic'
    return 'Utility' # Default

def extract_options(prop):
    """提取屬性中的選項值"""
    if 'options' in prop and isinstance(prop['options'], list):
        return [opt.get('name', opt.get('value')) for opt in prop['options']]
    return []

def map_node_smart(node):
    """智慧映射函數"""
    data = {col: "" for col in ONTOLOGY_COLUMNS}
    
    # 基本資訊
    data['node_internal_name'] = node.get('name', '')
    data['node_display_name'] = node.get('displayName', '')
    data['node_description'] = node.get('description', '')
    data['node_category'] = infer_category(data['node_internal_name'], data['node_display_name'])
    
    # 屬性深度分析
    properties = node.get('properties', [])
    
    resources = set()
    operations = set()
    events = set()
    creds = set()
    std_params = set()
    complex_ui = set()
    dynamic_params = set()
    ai_feats = set()
    has_binary = False
    
    for p in properties:
        p_name = p.get('name', '')
        p_type = p.get('type', '')
        p_display = p.get('displayName', '')
        
        # 1. 資源與操作
        if p_name == 'resource':
            resources.update(extract_options(p))
        elif p_name == 'operation':
            operations.update(extract_options(p))
        elif p_name in ['event', 'events', 'triggerOn']:
            events.update(extract_options(p))
            
        # 2. 憑證 (從屬性中找)
        if p_name in ['authentication', 'credentials']:
            creds.update(extract_options(p))
            
        # 3. 標準參數與二進位
        if p_name in ['limit', 'returnAll', 'simple']:
            std_params.add(p_name)
        if 'binary' in p_name.lower() or p_type == 'binary':
            has_binary = True
            
        # 4. 特殊 UI 與動態參數
        if p_type in ['collection', 'fixedCollection', 'json']:
            complex_ui.add(p_name)
        if 'loadOptionsMethod' in p.get('typeOptions', {}):
            dynamic_params.add(p_name)
            
        # 5. AI 特徵
        if 'prompt' in p_name.lower() or 'model' in p_name.lower():
            ai_feats.add(p_name)

    # 填入提取結果
    data['resources'] = list(resources) if resources else ""
    data['operations'] = list(operations) if operations else ""
    data['events'] = list(events) if events else ""
    data['credential_types'] = list(creds) if creds else ""
    data['standard_parameters'] = list(std_params)
    data['binary_handling'] = has_binary
    data['complex_ui_elements'] = list(complex_ui)
    data['dynamic_parameters'] = list(dynamic_params)
    data['ai_features'] = list(ai_feats)

    # 智慧推斷 Interaction Model
    is_trigger = 'trigger' in data['node_internal_name'].lower() or 'trigger' in data['node_display_name'].lower()
    
    if is_trigger:
        data['interaction_model'] = 'Trigger'
        data['input_types'] = []
        data['output_types'] = ['main']
        # 簡單判斷 Polling vs Webhook
        if 'poll' in str(properties).lower():
            data['trigger_type'] = 'Polling'
        else:
            data['trigger_type'] = 'Webhook'
    else:
        # 非 Trigger 節點
        data['input_types'] = ['main']
        data['output_types'] = ['main']
        
        if resources:
            data['interaction_model'] = 'Resource-Based'
        elif 'agent' in data['node_internal_name'].lower():
            data['interaction_model'] = 'Logic'
        else:
            data['interaction_model'] = 'Generic-API'

    return data

def main():
    source_file = 'All_n8n_nodes.json'
    output_file = 'n8n_ontology_full_list2.csv'
    
    try:
        with open(source_file, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)
            
        # 處理檔案結構差異 (有些是 {nodes: [...]}, 有些直接是 [...])
        if isinstance(raw_data, dict) and 'nodes' in raw_data:
            nodes = raw_data['nodes']
        else:
            nodes = raw_data
            
        # 提取 fullContent (如果有的話)
        processed_nodes = []
        for n in nodes:
            if 'fullContent' in n:
                processed_nodes.append(n['fullContent'])
            else:
                processed_nodes.append(n)
                
        print(f"🚀 開始處理 {len(processed_nodes)} 個節點...")
        
        with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=ONTOLOGY_COLUMNS)
            writer.writeheader()
            
            for node in processed_nodes:
                row = map_node_smart(node)
                writer.writerow(row)
                
        print(f"✅ 完成！結果已儲存為: {output_file}")
        
    except FileNotFoundError:
        print(f"❌ 找不到檔案: {source_file}，請確認檔名是否正確。")
    except Exception as e:
        print(f"⚠️ 發生錯誤: {e}")

if __name__ == "__main__":
    main()