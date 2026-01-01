import json
import glob
import os

def extract_node_info(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

    # 1. 提取基本識別資訊
    node_summary = {
        "filename": os.path.basename(file_path),
        "name": data.get("name", ""),
        "displayName": data.get("displayName", ""),
        "description": data.get("description", ""),
        "category_tags": [], # 用來存放提取出的關鍵字
        "capabilities": []   # 用來存放具體功能 (Resource + Operation)
    }

    properties = data.get("properties", [])
    
    # 用來暫存找到的 Resource 選項，方便稍後組合顯示
    found_resources = []
    
    # 2. 遍歷 Properties 尋找關鍵特徵
    for prop in properties:
        prop_name = prop.get("name", "")
        prop_options = prop.get("options", [])
        
        # A. 提取 Resource (例如: Spreadsheet, Sheet, File, Folder)
        if prop_name == "resource" and prop_options:
            for opt in prop_options:
                name = opt.get("name", "")
                node_summary["category_tags"].append(name)
                found_resources.append(name)
        
        # B. 提取 Operations (例如: Create, Append, Delete)
        # 這是建立 Taxonomy 最重要的部分，因為它定義了節點的「動作」
        elif prop_name == "operation" and prop_options:
            for opt in prop_options:
                action_name = opt.get("name", "")
                action_desc = opt.get("description", "")
                
                # 組合出更有意義的描述，例如 "Sheet: Append data to a sheet"
                # 如果我們前面有找到 Resource，雖然這裡無法精確對應哪個 Operation 屬於哪個 Resource (因為那是 displayOptions 控制的)
                # 但為了 Taxonomy，我們只需要知道這個節點「總共」能做什麼
                capability = f"{action_name}"
                if action_desc:
                    capability += f" ({action_desc})"
                
                node_summary["capabilities"].append(capability)

        # C. 針對 Trigger 類型 (如 Webhook) 提取方法
        elif prop_name == "httpMethod" and prop_options:
             for opt in prop_options:
                node_summary["capabilities"].append(f"Method: {opt.get('name', '')}")

        # D. 針對 Logic 類型 (如 If) 提取條件類別
        elif prop_name == "conditions":
             node_summary["category_tags"].append("Logic Control")
             # Logic 節點通常比較單純，標記為 Logic Control 即可

    # 3. 清理與去重
    node_summary["category_tags"] = list(set(node_summary["category_tags"]))
    
    # 如果沒有找到特殊的 Operations (可能是簡單的 Logic 節點或 Helper)，
    # 我們嘗試提取前幾個屬性的名稱作為補充，避免資訊過少
    if not node_summary["capabilities"] and not node_summary["category_tags"]:
        top_props = [p.get("displayName", p.get("name")) for p in properties[:3]]
        node_summary["capabilities"] = [f"Config: {p}" for p in top_props]

    return node_summary

def main():
    # 設定你的 JSON 檔案路徑
    # 假設腳本與 json 檔案在同一層目錄
    json_files = glob.glob("*.json")
    
    all_nodes_summary = []
    
    print(f"Found {len(json_files)} files. Processing...")
    
    for file in json_files:
        # 略過輸出的結果檔，避免重複讀取
        if file == "n8n_nodes_summary.json":
            continue
            
        summary = extract_node_info(file)
        if summary:
            all_nodes_summary.append(summary)

    # 輸出結果
    output_filename = "n8n_nodes_summary.json"
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(all_nodes_summary, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully processed {len(all_nodes_summary)} nodes.")
    print(f"Summary saved to: {output_filename}")
    
    # 簡易統計 token 縮減量 (估算)
    # 原始大小 vs 處理後大小
    original_size = sum(os.path.getsize(f) for f in json_files)
    new_size = os.path.getsize(output_filename)
    print(f"Original Data Size: {original_size/1024/1024:.2f} MB")
    print(f"Condensed Data Size: {new_size/1024/1024:.2f} MB")
    print(f"Reduction Ratio: {original_size/new_size:.1f}x")

if __name__ == "__main__":
    main()