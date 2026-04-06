"""
n8n Workflow Import 測試腳本
用途：驗證移除 sticky note 後的 workflow JSON 是否可以成功 import 到 n8n
使用方式：python3 test_n8n_import.py
"""

import json
import uuid
import time
import urllib.request
import urllib.error
import ssl

# ========== 設定 ==========
N8N_URL = "https://widm-n8n.csie.ncu.edu.tw"
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhMDFiNzdjYS1mZDMxLTQ3NzAtYjg0Yi05Y2ZhMjNiMWExMDciLCJpc3MiOiJuOG4iLCJhdWQiOiJwdWJsaWMtYXBpIiwiaWF0IjoxNzY3ODAxNjkwfQ.WhgYGt6AzVNHMVwiaHiISGjLwM-q4jdax9Tyr7uktz8"
JSONL_PATH = "n8n_training_data_v2_humanized.jsonl"
TEST_SAMPLE_SIZE = 20   # 測試幾筆（建議先用 20，全跑要改成 1963）
CLEANUP = True          # 測試後自動刪除匯入的 workflow
# ==========================


def get_target_node(t):
    if isinstance(t, dict):
        return t.get('node')
    elif isinstance(t, list) and len(t) > 0:
        return t[0]
    return None


def strip_sticky_notes(wf_dict):
    """移除所有 stickyNote 節點及其連線"""
    nodes = wf_dict.get('nodes', []) or []
    connections = wf_dict.get('connections', {}) or {}
    sticky_names = set()
    clean_nodes = []
    for n in nodes:
        if 'stickyNote' in n.get('type', ''):
            sticky_names.add(n.get('name', ''))
        else:
            clean_nodes.append(n)
    clean_connections = {}
    for src_name, conn_val in connections.items():
        if src_name in sticky_names:
            continue
        clean_conn = {}
        for output_key, targets_list in (conn_val or {}).items():
            clean_targets = []
            for targets in (targets_list or []):
                if isinstance(targets, list):
                    clean_t = [t for t in targets if get_target_node(t) not in sticky_names]
                    clean_targets.append(clean_t)
                else:
                    clean_targets.append(targets)
            clean_conn[output_key] = clean_targets
        clean_connections[src_name] = clean_conn
    wf_dict['nodes'] = clean_nodes
    wf_dict['connections'] = clean_connections
    return wf_dict


def fix_missing_ids(wf_dict):
    """為缺少 id 的 node 自動補 UUID（舊格式相容）"""
    nodes = wf_dict.get('nodes', []) or []
    for node in nodes:
        if not node.get('id'):
            node['id'] = str(uuid.uuid4())
    return wf_dict


def fix_dangling_connections(wf_dict):
    """移除指向不存在節點的連線"""
    nodes = wf_dict.get('nodes', []) or []
    connections = wf_dict.get('connections', {}) or {}
    node_names = set(n.get('name', '') for n in nodes)

    clean_connections = {}
    for src_name, conn_val in connections.items():
        if src_name not in node_names:
            continue  # 來源不存在，直接跳過
        clean_conn = {}
        for output_key, targets_list in (conn_val or {}).items():
            clean_targets = []
            for targets in (targets_list or []):
                if isinstance(targets, list):
                    clean_t = [
                        t for t in targets
                        if get_target_node(t) is None or get_target_node(t) in node_names
                    ]
                    clean_targets.append(clean_t)
                else:
                    clean_targets.append(targets)
            clean_conn[output_key] = clean_targets
        clean_connections[src_name] = clean_conn

    wf_dict['connections'] = clean_connections
    return wf_dict


def prepare_workflow(wf_dict, name="TEST_IMPORT"):
    """準備可匯入的 workflow dict"""
    wf = dict(wf_dict)
    wf = strip_sticky_notes(wf)
    wf = fix_missing_ids(wf)
    wf = fix_dangling_connections(wf)
    wf['name'] = name
    # 'active' 是 read-only 欄位，不可在建立時傳入
    wf.pop('active', None)
    # 確保有 settings
    if 'settings' not in wf:
        wf['settings'] = {}
    return wf


def api_call(method, path, data=None):
    """呼叫 n8n API"""
    url = f"{N8N_URL}/api/v1{path}"
    headers = {
        'X-N8N-API-KEY': API_KEY,
        'Content-Type': 'application/json',
    }
    body = json.dumps(data).encode('utf-8') if data else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            return resp.status, json.loads(resp.read())
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read())
    except Exception as e:
        return 0, {'error': str(e)}


def test_api_connection():
    """測試 API 是否可連線"""
    print("🔌 測試 API 連線...")
    status, data = api_call('GET', '/workflows?limit=1')
    if status == 200:
        print(f"✅ API 連線成功")
        return True
    else:
        print(f"❌ API 連線失敗: HTTP {status} - {data}")
        return False


def test_import_workflow(wf_dict, record_idx):
    """測試匯入單一 workflow，回傳 (success, workflow_id, error_msg)"""
    name = f"__TEST_{record_idx:04d}__"
    wf = prepare_workflow(wf_dict, name=name)

    status, resp = api_call('POST', '/workflows', wf)
    if status in (200, 201):
        wf_id = resp.get('id')
        return True, wf_id, None
    else:
        return False, None, f"HTTP {status}: {resp.get('message', str(resp))[:200]}"


def delete_workflow(wf_id):
    """刪除測試用的 workflow"""
    status, _ = api_call('DELETE', f'/workflows/{wf_id}')
    return status in (200, 204)


def main():
    print("=" * 60)
    print("n8n Workflow Import 測試")
    print("=" * 60)

    # 1. 測試 API 連線
    if not test_api_connection():
        print("\n請確認 N8N_URL 和 API_KEY 是否正確")
        return

    # 2. 載入資料
    print(f"\n📂 載入 {JSONL_PATH}...")
    with open(JSONL_PATH, 'r', encoding='utf-8') as f:
        lines = [json.loads(l) for l in f]
    print(f"   共 {len(lines)} 筆，測試前 {TEST_SAMPLE_SIZE} 筆")

    # 3. 逐筆測試
    print(f"\n🧪 開始測試 import...")
    results = {'success': 0, 'fail': 0, 'errors': []}
    created_ids = []

    for i in range(min(TEST_SAMPLE_SIZE, len(lines))):
        item = lines[i]
        try:
            wf_dict = json.loads(item['output'])
        except json.JSONDecodeError as e:
            results['fail'] += 1
            results['errors'].append((i + 1, f'JSON parse error: {e}'))
            print(f"  ❌ Record {i+1:4d}: JSON 解析失敗")
            continue

        success, wf_id, err = test_import_workflow(wf_dict, i + 1)
        if success:
            results['success'] += 1
            if wf_id:
                created_ids.append(wf_id)
            print(f"  ✅ Record {i+1:4d}: 成功 (id={wf_id})")
        else:
            results['fail'] += 1
            results['errors'].append((i + 1, err))
            print(f"  ❌ Record {i+1:4d}: 失敗 - {err[:80]}")

        time.sleep(0.2)  # 避免打太快

    # 4. 清理
    if CLEANUP and created_ids:
        print(f"\n🗑️  清理 {len(created_ids)} 個測試 workflow...")
        for wf_id in created_ids:
            delete_workflow(wf_id)
            time.sleep(0.1)
        print("   清理完成")

    # 5. 結果報告
    print(f"\n{'=' * 60}")
    print(f"📊 測試結果")
    print(f"   ✅ 成功: {results['success']} / {TEST_SAMPLE_SIZE}")
    print(f"   ❌ 失敗: {results['fail']} / {TEST_SAMPLE_SIZE}")
    if results['errors']:
        print(f"\n   失敗詳情:")
        for idx, err in results['errors'][:10]:
            print(f"   - Record {idx}: {err}")
    print("=" * 60)


if __name__ == '__main__':
    main()
