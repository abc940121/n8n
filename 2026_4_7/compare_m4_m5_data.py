import json
import os

def analyze_jsonl(path, name):
    if not os.path.exists(path):
        return None
    
    with open(path, 'r', encoding='utf-8') as f:
        data = [json.loads(l) for l in f if l.strip()]
    
    total = len(data)
    # 分析平均輸出長度 (代表 workflow 複雜度)
    out_lens = []
    # 分析平均輸入長度 (代表 prompt 描述深度)
    in_lens = []
    
    system_prompt = "Unknown"
    
    for d in data:
        if 'messages' in d:
            # OpenAI FT / ChatML 格式
            for m in d['messages']:
                if m['role'] == 'user':
                    in_lens.append(len(m['content']))
                elif m['role'] == 'assistant':
                    out_lens.append(len(m['content']))
                elif m['role'] == 'system':
                    system_prompt = m['content']
        else:
            # 原始 Instruct 格式
            in_lens.append(len(d.get('instruction', '')) + len(d.get('input', '')))
            out_lens.append(len(d.get('output', '')))
            system_prompt = d.get('instruction', 'None')
            
    return {
        "name": name,
        "count": total,
        "avg_input": sum(in_lens) / len(in_lens) if in_lens else 0,
        "avg_output": sum(out_lens) / len(out_lens) if out_lens else 0,
        "max_output": max(out_lens) if out_lens else 0,
        "system_prompt": system_prompt
    }

m4_res = analyze_jsonl(r'model_4\v3_train_chat.jsonl', "Model 4")
m5_res = analyze_jsonl(r'model_5\qwen27b_v3_openai_ft_train_max16000.jsonl', "Model 5")

print("-" * 60)
print(f"{'維度':<15} | {'Model 4':<20} | {'Model 5':<20}")
print("-" * 60)
print(f"{'資料筆數':<15} | {m4_res['count']:<20} | {m5_res['count']:<20}")
print(f"{'平均輸入長度':<15} | {m4_res['avg_input']:<20.1f} | {m5_res['avg_input']:<20.1f}")
print(f"{'平均輸出長度':<15} | {m4_res['avg_output']:<20.1f} | {m5_res['avg_output']:<20.1f}")
print(f"{'最大輸出長度':<15} | {m4_res['max_output']:<20} | {m5_res['max_output']:<20}")
print("-" * 60)
print(f"\n[Model 4 System Prompt]:\n{m4_res['system_prompt'][:200]}...")
print(f"\n[Model 5 System Prompt]:\n{m5_res['system_prompt'][:200]}...")
