import json
import csv
import glob
import re

# --- 1. 定義 Ontology v2.0 欄位 ---
ONTOLOGY_COLUMNS_V3 = [
    # 核心識別
    "node_internal_name", "node_display_name", "node_description", 
    "node_category", "is_ai_tool_variant",
    
    # 連接與認證
    "input_connection_type", "output_connection_type", # 分開輸入輸出更清楚
    "authentication_methods", "icon_brand",
    
    # 互動邏輯
    "interaction_model", "trigger_mechanism", "polling_defaults",
    
    # 資源與操作
    "available_resources", "available_operations", "supports_custom_api", "trigger_events",
    
    # 資料處理
    "binary_support", "file_processing_features", "output_structure",
    
    # 參數
    "required_parameters", "standard_options", "ui_field_groups", "dynamic_loading_fields",
    
    # AI 與 Meta
    "ai_features", "llm_hyperparameters", "documentation_url", "api_version_notices"
]

# --- 2. 輔助工具 ---

def extract_brand_from_name(internal_name):
    """從內部名稱提取品牌 (e.g. n8n-nodes-base.zoom -> zoom)"""
    parts = internal_name.split('.')
    if len(parts) > 1:
        # 去除 Tool 後綴
        brand = parts[-1].replace('Tool', '').replace('Trigger', '')
        # CamelCase to snake_case (e.g. GoogleSheets -> Google Sheets)
        brand = re.sub(r'(?<!^)(?=[A-Z])', ' ', brand)
        return brand
    return ""

def extract_urls(text):
    """從文字中提取 URL"""
    if not text: return ""
    urls = re.findall(r'href=[\'"]?([^\'" >]+)', text)
    return list(set(urls))

def infer_category_v3(name, display_name, description):
    """更強大的分類推斷"""
    text = (name + " " + display_name + " " + description).lower()
    
    if 'trigger' in text: return 'Trigger'
    if any(k in text for k in ['ai', 'langchain', 'llm', 'chat', 'model', 'agent', 'embedding', 'vector']): return 'AI & Logic'
    if any(k in text for k in ['sql', 'mongo', 'db', 'firebase', 'postgres', 'sheet', 'table', 'record']): return 'Database'
    if any(k in text for k in ['aws', 'google', 'azure', 'cloud', 'ftp', 'http', 'api', 'request']): return 'Cloud & IT'
    if any(k in text for k in ['mail', 'slack', 'telegram', 'discord', 'message', 'sms', 'notification']): return 'Communication'
    if any(k in text for k in ['customer', 'crm', 'sales', 'hubspot', 'pipedrive', 'marketing', 'lead']): return 'Marketing'
    if any(k in text for k in ['convert', 'transform', 'compress', 'extract', 'html', 'json', 'xml', 'date']): return 'Data Transformation'
    if any(k in text for k in ['schedule', 'timer', 'wait', 'interval']): return 'Flow Control'
    
    return 'Utility'

def map_node_v3(node):
    """v3.0 深度映射邏輯"""
    data = {col: "" for col in ONTOLOGY_COLUMNS_V3}
    
    # 1. 基礎資訊
    internal_name = node.get('name', '')
    display_name = node.get('displayName', '')
    description = node.get('description', '')
    
    data['node_internal_name'] = internal_name
    data['node_display_name'] = display_name
    data['node_description'] = description
    data['node_category'] = infer_category_v3(internal_name, display_name, description)
    
    # 2. 推斷 Icon & AI Variant
    data['icon_brand'] = extract_brand_from_name(internal_name)
    data['is_ai_tool_variant'] = 'Tool' in display_name or 'tool' in internal_name or 'Agent' in display_name
    
    # 3. 屬性掃描
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
    file_features = set()
    docs_urls = set()
    
    has_custom_api = False
    has_binary = False
    poll_defaults = ""
    
    # 從 description 找 URL
    docs_urls.update(extract_urls(description))
    
    for p in properties:
        p_name = p.get('name', '')
        p_display = p.get('displayName', '')
        p_desc = p.get('description', '')
        p_type = p.get('type', '')
        
        # 提取選項
        options = []
        if 'options' in p and isinstance(p['options'], list):
            options = [opt.get('name', opt.get('value')) for opt in p['options']]
            
        # 收集 URL
        docs_urls.update(extract_urls(p_desc))
        docs_urls.update(extract_urls(p_display))
        
        # 資源與操作
        if p_name == 'resource':
            if any('custom' in str(o).lower() for o in options): has_custom_api = True
            resources.update([o for o in options if 'custom' not in str(o).lower()])
        elif p_name == 'operation':
            if any('custom' in str(o).lower() for o in options): has_custom_api = True
            operations.update([o for o in options if 'custom' not in str(o).lower()])
        elif p_name in ['event', 'events', 'triggerOn']:
            events.update(options)
            
        # 認證 (更寬鬆的匹配)
        if 'auth' in p_name.lower() or 'credential' in p_name.lower() or p_type == 'credentials':
            auth_methods.update(options)
            
        # 參數特徵
        if p.get('required'): required_params.add(p_name)
        if 'loadOptionsMethod' in p.get('typeOptions', {}): dynamic_fields.add(p_name)
        if p_name in ['limit', 'returnAll', 'simple']: std_opts.add(p_name)
        
        # Binary & File Features
        if 'binary' in p_name.lower() or p_type == 'binary':
            has_binary = True
        if p_name in ['fileFormat', 'format', 'mode'] and options:
            file_features.update(options)
            
        # UI Groups
        if p_type in ['collection', 'fixedCollection', 'json'] or 'Fields' in p_name:
            ui_groups.add(p_name)
            
        # AI/LLM
        if p_name in ['temperature', 'topP', 'frequencyPenalty']: llm_params.add(p_name)
        if 'prompt' in p_name.lower() or 'model' in p_name.lower(): ai_feats.add(p_name)
        
        # Polling
        if p_name == 'pollTimes' and 'default' in p:
            poll_defaults = str(p['default'])

    # 4. 填入資料
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
    data['documentation_url'] = list(docs_urls)
    data['file_processing_features'] = list(file_features)

    # 5. 強制推斷 Input/Output (解決 JSON 缺失問題)
    is_trigger = 'trigger' in internal_name.lower() or 'trigger' in display_name.lower()
    
    if is_trigger:
        data['interaction_model'] = 'Trigger'
        data['input_connection_type'] = 'None' # Trigger 沒有輸入
        data['output_connection_type'] = 'Main'
        data['trigger_mechanism'] = 'Polling' if poll_defaults or 'poll' in str(properties).lower() else 'Webhook'
    else:
        # 非 Trigger
        data['output_connection_type'] = 'Main'
        if 'agent' in internal_name.lower() or 'chain' in internal_name.lower() or data['node_category'] == 'AI & Logic':
            data['interaction_model'] = 'Logic'
            data['input_connection_type'] = 'AI_Chain' # AI 類通常接 Chain
            data['output_structure'] = 'String/JSON'
        elif resources:
            data['interaction_model'] = 'Resource-Based'
            data['input_connection_type'] = 'Main'
            data['output_structure'] = 'JSON Array'
        else:
            data['interaction_model'] = 'Generic-API'
            data['input_connection_type'] = 'Main'
            data['output_structure'] = 'JSON'

    return data

def main():
    source_files = glob.glob('batch_*.json')
    if not source_files: source_files = ['All_n8n_nodes.json']
    
    output_file = 'n8n_ontology_full_list3.csv'
    all_rows = []
    
    print("🚀 開始執行 v3.0 Mapping (含深度推斷)...")
    
    for file_path in source_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                raw_data = json.load(f)
            nodes = raw_data.get('nodes', []) if isinstance(raw_data, dict) else raw_data
            
            for n in nodes:
                target_node = n.get('fullContent', n)
                all_rows.append(map_node_v3(target_node))
                
        except Exception as e:
            print(f"⚠️ 跳過 {file_path}: {e}")

    if all_rows:
        with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=ONTOLOGY_COLUMNS_V3)
            writer.writeheader()
            writer.writerows(all_rows)
        print(f"✅ 完成！已生成 {len(all_rows)} 筆資料至: {output_file}")
    else:
        print("❌ 錯誤：未找到任何節點資料")

if __name__ == "__main__":
    main()