import json

with open('model_5/qwen27b_v3_openai_ft_train_max16000.jsonl', 'r', encoding='utf-8') as f:
    lines = [json.loads(l) for l in f if l.strip()]

with open('model_5/qwen27b_v3_test_openai.jsonl', 'r', encoding='utf-8') as f:
    test_lines = [json.loads(l) for l in f if l.strip()]

print(f'訓練筆數: {len(lines)}')
print(f'測試筆數: {len(test_lines)}')
print(f'第 1 筆的 keys: {list(lines[0].keys())}')
first = lines[0]
if 'messages' in first:
    for m in first['messages']:
        role = m['role']
        content = m['content'][:100]
        print(f'  role={role}: {content}...')
else:
    for k, v in first.items():
        print(f'  {k}: {str(v)[:100]}')
