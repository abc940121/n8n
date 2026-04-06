import json
import os
import re

INPUT_FILE = r"c:\Users\User\Desktop\C.ai_project\2026_4_7\model_2\n8n_predicted_workflows_v2_clean.jsonl"
OUTPUT_DIR = r"c:\Users\User\Desktop\C.ai_project\2026_4_7\model_2\sample_workflows"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def extract_json(text):
    if not text: return None
    text = text.strip()
    try: return json.loads(text)
    except: pass
    # Remove markdown blocks
    if text.startswith('```'):
        lines = text.split('\n')
        text = '\n'.join([l for l in lines if not l.strip().startswith('```')])
        try: return json.loads(text)
        except: pass
    # Regex extract
    m = re.search(r'\{.*\}', text, re.DOTALL)
    if m:
        try: return json.loads(m.group())
        except: pass
    return None

lines = []
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    for line in f:
        if line.strip():
            lines.append(json.loads(line))

print(f"Total clean lines: {len(lines)}")

# Pick top 3 with most nodes (most complex/interesting)
candidates = []
for item in lines:
    wf = extract_json(item['predicted'])
    if wf and isinstance(wf, dict) and 'nodes' in wf:
        node_count = len(wf.get('nodes', []))
        conn_count = len(wf.get('connections', {}))
        candidates.append((node_count, conn_count, item['id'], item['prompt'], wf))

candidates.sort(reverse=True)
top3 = candidates[:3]

for i, (nc, cc, wid, prompt, wf) in enumerate(top3, 1):
    # n8n import format needs: name, nodes, connections
    n8n_import = {
        "name": f"Model2 Generated - {prompt[:60]}",
        "nodes": wf.get("nodes", []),
        "connections": wf.get("connections", {}),
        "active": False,
        "settings": {},
        "id": str(wid)
    }
    out_path = os.path.join(OUTPUT_DIR, f"workflow_{i}_id{wid}.json")
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(n8n_import, f, ensure_ascii=False, indent=2)
    print(f"[{i}] ID={wid} | 節點數={nc} | 連線數={cc}")
    print(f"    Prompt: {prompt[:80]}")
    print(f"    儲存至: {out_path}")
    print()

print("完成！你可以把上面 3 個 JSON 檔案，直接在 n8n UI 的 Import Workflow 貼上測試！")
