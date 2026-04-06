import json
import os
import re
import statistics

CLEAN_FILE = r"c:\Users\User\Desktop\C.ai_project\2026_4_7\n8n_predicted_workflows_v2_clean.jsonl"

def extract_json(text_content):
    if not text_content: return None
    text_content = text_content.strip()
    try: return json.loads(text_content)
    except: pass
        
    if text_content.startswith('```'):
        lines = text_content.split('\n')
        text_content_no_md = '\n'.join([l for l in lines if not l.strip().startswith('```')])
        try: return json.loads(text_content_no_md)
        except: pass

    json_match = re.search(r'\{.*\}', text_content, re.DOTALL)
    if json_match:
        try: return json.loads(json_match.group())
        except: pass
    return None

def main():
    if not os.path.exists(CLEAN_FILE):
        print(f"Error: 找不到 {CLEAN_FILE}")
        return

    good_items = []
    nodes_counts = []
    edges_counts = []

    with open(CLEAN_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip(): continue
            data = json.loads(line)
            
            parsed_json = extract_json(data.get("predicted", ""))
            if parsed_json:
                nodes = parsed_json.get("nodes", [])
                connections = parsed_json.get("connections", {})
                
                # count total connections
                edges_count = 0
                if isinstance(connections, dict):
                    for src_node, outputs in connections.items():
                        if isinstance(outputs, dict):
                            for out_type, targets in outputs.items():
                                if isinstance(targets, list):
                                    for target_group in targets:
                                        if isinstance(target_group, list):
                                            edges_count += len(target_group)
                
                nodes_counts.append(len(nodes) if isinstance(nodes, list) else 0)
                edges_counts.append(edges_count)
                good_items.append({
                    "id": data.get("id"),
                    "nodes": len(nodes) if isinstance(nodes, list) else 0,
                    "edges": edges_count,
                    "name": parsed_json.get("name", "Unknown Workflow")
                })

    print("==================================================")
    print("📈 成功生成的 69 筆工作流分析報告")
    print("==================================================")
    print(f"✅ 總筆數: {len(good_items)}")
    print(f"📌 平均每個工作流的節點數 (Nodes): {statistics.mean(nodes_counts):.1f}")
    print(f"📌 平均每個工作流的連線數 (Connections): {statistics.mean(edges_counts):.1f}")
    print(f"📌 最多節點的工作流: 包含 {max(nodes_counts)} 個節點")
    print(f"📌 最少節點的工作流: 包含 {min(nodes_counts)} 個節點")
    
    print("\n🧐 隨機抽出前 3 筆範例看看品質:")
    for item in good_items[:3]:
        print(f"   - ID: {item['id']} | 名稱: {item['name']}")
        print(f"     ➔ 這個工作流創建了 {item['nodes']} 個節點和 {item['edges']} 條連線。")

if __name__ == "__main__":
    main()
