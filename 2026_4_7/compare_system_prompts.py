import json

with open(r'model_4\v3_train_chat.jsonl', 'r', encoding='utf-8') as f4:
    m4 = json.loads(f4.readline())
    s4 = next((m['content'] for m in m4['messages'] if m['role'] == 'system'), 'N/A')

with open(r'model_5\qwen27b_v3_openai_ft_train_max16000.jsonl', 'r', encoding='utf-8') as f5:
    m5 = json.loads(f5.readline())
    s5 = next((m['content'] for m in m5['messages'] if m['role'] == 'system'), 'N/A')

print("="*60)
print("【Model 4 System Prompt】")
print(s4)
print("\n" + "="*60)
print("【Model 5 System Prompt】")
print(s5)
print("="*60)

# 同時存檔供後續查閱
with open("system_prompt_comparison.txt", "w", encoding="utf-8") as out:
    out.write("Model 4 System Prompt:\n" + s4 + "\n\n")
    out.write("Model 5 System Prompt:\n" + s5 + "\n")
