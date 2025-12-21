import json
import os

# ==========================================
# 設定：請確認這是你的檔案路徑
# ==========================================
target_folder = r'C:\Users\User\Desktop\C.ai_project\n8n node json\n8n_AI_Agent\node_schemas'
file_name = 'actionNetwork.json' # 我們先檢查這一個檔案
file_path = os.path.join(target_folder, file_name)

print(f"正在檢查檔案: {file_path}")

try:
    with open(file_path, 'r', encoding='utf-8') as f: # 如果報錯，試試 encoding='utf-8-sig'
        data = json.load(f)
        
        print("-" * 30)
        print("1. JSON 最外層的所有 Keys:")
        print(list(data.keys()))
        
        print("-" * 30)
        if 'credentials' in data:
            print("2. 找到 'credentials' 欄位 (在最外層):")
            print(json.dumps(data['credentials'], indent=2, ensure_ascii=False))
        else:
            print("2. [!] 最外層沒有找到 'credentials' 欄位。")
            
            # 嘗試搜尋常見的巢狀位置
            found = False
            # 檢查是否藏在 description 裡
            if 'description' in data and isinstance(data['description'], dict) and 'credentials' in data['description']:
                print("   -> 發現它藏在 'description' 裡面！")
                print(json.dumps(data['description']['credentials'], indent=2, ensure_ascii=False))
                found = True
            
            # 暴力搜尋：檢查所有第一層的欄位，看有沒有包含 'cred' 字眼的 key
            print("\n3. 搜尋含有 'cred' 的欄位:")
            for key in data.keys():
                if 'cred' in key.lower():
                    print(f"   -> 發現疑似欄位: '{key}'")
                    print(f"      內容: {data[key]}")
                    found = True
            
            if not found:
                print("   -> 完全找不到憑證相關資訊，可能是結構不同。")

except Exception as e:
    print(f"讀取錯誤: {e}")