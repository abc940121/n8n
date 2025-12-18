import json
import csv
import glob
import re

# --- 1. 定義 Ontology v2.0 欄位 ---
ONTOLOGY_COLUMNS_V2 = [
    # 核心識別與變體
    "node_internal_name", "node_display_name", "node_description", 
    "node_category", "is_ai_tool_variant",
    
    # 連接與認證
    "input_connection_type", "authentication_methods", "icon_brand",
    
    # 互動邏輯
    "interaction_model", "trigger_mechanism", "polling_defaults",
    
    # 資源操作架構
    "available_resources", "available_operations", "supports_custom_api", "trigger_events",
    
    # 數據處理特徵
    "binary_support", "file_processing_features", "output_structure",
    
    # 參數與 UI 結構
    "required_parameters", "standard_options", "ui_field_groups", "dynamic_loading_fields",
    
    # AI 整合能力
    "ai_features", "llm_hyperparameters",
    
    # 系統資訊
    "documentation_url", "api_version_notices"
]

# --- 2. 輔助邏輯 ---

def infer_category_v2(name, display_name):
    """更精準的分類推斷 (v2 標準)"""
    text = (name + " " + display_name).lower()
    
    if 'trigger' in text: return 'Trigger'
    if any(k in text for k in ['ai', 'langchain', 'llm', 'chat', 'model', 'agent']): return 'AI'
    if any(k in text for k in ['sql', 'mongo', 'db', 'firebase', 'postgres', 'sheet', 'table']): return 'Database'
    if any(k in text for k in ['aws', 'google', 'azure', 'cloud', 'ftp', 'http']): return 'Cloud'
    if any(k in text for k in ['mail', 'slack', 'telegram', 'discord', 'message', 'sms']): return 'Communication'
    if any(k in text for k in ['customer', 'crm', 'sales', 'hubspot', 'pipedrive', 'marketing']): return 'Marketing'
    if any(k in text for k in ['json', 'xml', 'csv', 'html', 'transform', 'compression', 'convert']): return 'Utility'
    
    return 'Utility' # Default

def extract_options(prop):
    """提取屬性選項 (過濾掉 Custom API Call)"""
    if 'options' in prop and isinstance(prop['options'], list):
        return [opt.get('name', opt.get('value')) for opt in prop['options']]
    return []

def map_node_v2(node):
    """v2.0 映射邏輯"""
    data = {col: "" for col in ONTOLOGY_COLUMNS_V2}
    
    # --- 1. 核心識別 ---
    internal_name = node.get('name', '')
    display_name = node.get('displayName', '')
    data['node_internal_name'] = internal_name
    data['node_display_name'] = display_name
    data['node_description'] = node.get('description', '')
    data['node_category'] = infer_category_v2(internal_name, display_name)
    
    # 判斷是否為 AI Tool 變體
    data['is_ai_tool_variant'] = 'Tool' in display_name or 'tool' in internal_name or data['node_category'] == 'AI'
    data['icon_brand'] = node.get('icon', '')

    # --- 2. 屬性深度掃描 ---
    properties = node.get('properties', [])
    
    resources = set()
    operations = set()
    events = set()
    auth_methods = set()
    required_params = set()
    std_opts = set()
    ui_groups = set()
    dynamic_fields = set()
    ai_feats = set()
    llm_params = set()
    
    has_custom_api = False
    has_binary = False
    poll_defaults = ""
    
    for p in properties:
        p_name = p.get('name', '')
        p_type = p.get('type', '')
        p_options = extract_options(p)
        
        # 偵測必填
        if p.get('required') is True:
            required_params.add(p_name)
            
        # 偵測動態載入
        if 'loadOptionsMethod' in p.get('typeOptions', {}):
            dynamic_fields.add(p_name)

        # 1. 資源與操作 (過濾 Custom API)
        if p_name == 'resource':
            # 檢查是否有 Custom API
            if any('custom' in opt.lower() or '__CUSTOM' in opt for opt in p_options):
                has_custom_api = True
            # 過濾掉 Custom API 選項
            clean_opts = [o for o in p_options if 'custom' not in o.lower() and '__' not in o]
            resources.update(clean_opts)
            
        elif p_name == 'operation':
            if any('custom' in opt.lower() for opt in p_options):
                has_custom_api = True
            clean_opts = [o for o in p_options if 'custom' not in o.lower()]
            operations.update(clean_opts)
            
        elif p_name in ['event', 'events', 'triggerOn']:
            events.update(p_options)
            
        # 2. 認證
        if p_name in ['authentication', 'credentials']:
            auth_methods.update(p_options)
            
        # 3. 參數特徵
        if p_name in ['limit', 'returnAll', 'simple']:
            std_opts.add(p_name)
        if 'binary' in p_name.lower() or p_type == 'binary':
            has_binary = True
        
        # 4. UI 群組
        if p_type in ['collection', 'fixedCollection', 'json'] or 'Fields' in p_name:
            ui_groups.add(p_name)
            
        # 5. AI 與 LLM
        if p_name in ['temperature', 'topP', 'frequencyPenalty', 'presencePenalty']:
            llm_params.add(p_name)
        if 'prompt' in p_name.lower() or 'model' in p_name.lower():
            ai_feats.add(p_name)
            
        # 6. Polling Defaults
        if p_name == 'pollTimes' and 'default' in p:
            poll_defaults = str(p['default'])

    # --- 3. 填入與後處理 ---
    data['available_resources'] = list(resources)
    data['available_operations'] = list(operations)
    data['supports_custom_api'] = has_custom_api
    data['trigger_events'] = list(events)
    data['authentication_methods'] = list(auth_methods)
    data['required_parameters'] = list(required_params)
    data['standard_options'] = list(std_opts)
    data['binary_support'] = has_binary
    data['ui_field_groups'] = list(ui_groups)
    data['dynamic_loading_fields'] = list(dynamic_fields)
    data['ai_features'] = list(ai_feats)
    data['llm_hyperparameters'] = list(llm_params)
    data['polling_defaults'] = poll_defaults

    # 推斷 Interaction Model & Trigger Mechanism
    is_trigger = 'trigger' in internal_name.lower() or 'trigger' in display_name.lower()
    
    if is_trigger:
        data['interaction_model'] = 'Trigger'
        data['input_connection_type'] = 'None'
        # 判斷 Polling vs Webhook
        if 'poll' in str(properties).lower() or poll_defaults:
            data['trigger_mechanism'] = 'Polling'
        else:
            data['trigger_mechanism'] = 'Webhook'
    else:
        # 非 Trigger
        if 'agent' in internal_name.lower() or 'chain' in internal_name.lower():
            data['interaction_model'] = 'Logic'
            data['input_connection_type'] = 'AI_Chain'
        elif resources:
            data['interaction_model'] = 'Resource-Based'
            data['input_connection_type'] = 'Main'
        else:
            data['interaction_model'] = 'Generic-API'
            data['input_connection_type'] = 'Main'

    return data

def main():
    # 支援讀取原始大檔或 batch 檔案
    source_files = glob.glob('batch_*.json')
    if not source_files:
        source_files = ['All_n8n_nodes.json']
        
    output_file = 'n8n_ontology_v2_mapped.csv'
    all_rows = []
    
    print(f"🚀 開始使用 v2.0 邏輯處理檔案...")
    
    for file_path in source_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                raw_data = json.load(f)
                
            # 標準化結構 (Handle {nodes: []} vs [])
            nodes = raw_data.get('nodes', []) if isinstance(raw_data, dict) else raw_data
            
            for n in nodes:
                # 提取 fullContent
                target_node = n.get('fullContent', n)
                mapped_row = map_node_v2(target_node)
                all_rows.append(mapped_row)
                
        except Exception as e:
            print(f"⚠️ 跳過檔案 {file_path}: {e}")

    # 寫入 CSV
    if all_rows:
        with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=ONTOLOGY_COLUMNS_V2)
            writer.writeheader()
            writer.writerows(all_rows)
        print(f"✅ 成功！已輸出 {len(all_rows)} 筆資料至: {output_file}")
    else:
        print("❌ 未能提取任何節點資料，請檢查 JSON 來源。")

if __name__ == "__main__":
    main()