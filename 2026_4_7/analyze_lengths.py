import json
import os

def analyze_input_length(file_path):
    if not os.path.exists(file_path):
        return None
    
    lengths = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if not line.strip():
                    continue
                data = json.loads(line)
                # 取得 messages 中 role 為 user 的 content
                messages = data.get('messages', [])
                user_content = ""
                # 有些格式可能直接是 {"prompt": "...", "response": "..."}
                if not messages:
                    user_content = data.get('prompt', "")
                else:
                    for m in messages:
                        if m.get('role') == 'user':
                            user_content = m.get('content', "")
                            break
                
                if user_content:
                    lengths.append(len(user_content.strip()))
    except Exception as e:
        print(f"處理 {file_path} 時出錯: {e}")
        return None
    
    if not lengths:
        return None
        
    return {
        "min": min(lengths),
        "max": max(lengths),
        "avg": sum(lengths) / len(lengths),
        "count": len(lengths)
    }

base_path = r"c:\Users\User\Desktop\C.ai_project\2026_4_7"
files = {
    "Model 2": os.path.join(base_path, r"model_2\create_train_messages.jsonl"),
    "Model 3": os.path.join(base_path, r"model_3\create_highfreq_no_sticky_prefixed_train_messages.jsonl"),
    "Model 4": os.path.join(base_path, r"model_4\v3_train_chat.jsonl")
}

with open("length_results.txt", "w", encoding="utf-8") as out:
    header = "="*65 + "\n"
    header += f"{'模型':<10} | {'筆數':<6} | {'長度範圍 (字元)':<18} | {'平均長度':<10}\n"
    header += "-"*65 + "\n"
    out.write(header)
    print(header)

    for model_name, path in files.items():
        result = analyze_input_length(path)
        if result:
            range_str = f"{result['min']} ~ {result['max']}"
            line = f"{model_name:<10} | {result['count']:<6} | {range_str:<18} | {result['avg']:.1f}\n"
            out.write(line)
            print(line)
        else:
            line = f"{model_name:<10} | 找不到檔案或格式不符\n"
            out.write(line)
            print(line)
    out.write("="*65 + "\n")

