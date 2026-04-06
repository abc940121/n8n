import json

m2_path = r"c:\Users\User\Desktop\C.ai_project\2026_4_7\model_2\create_train_messages.jsonl"
m3_path = r"c:\Users\User\Desktop\C.ai_project\2026_4_7\model_3\create_highfreq_no_sticky_prefixed_train_messages.jsonl"

def analyze(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        print(f"File: {path.split('\\')[-1]}")
        print(f"Total Lines: {len(lines)}")
        if lines:
            data = json.loads(lines[0])
            for msg in data["messages"]:
                if msg["role"] == "user":
                    print(f"User Prompt Prefix: {msg['content'][:150]}...")
            print("-" * 40)

analyze(m2_path)
analyze(m3_path)
