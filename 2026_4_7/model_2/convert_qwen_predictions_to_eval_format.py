import json
import os
import re
from datetime import datetime

# ================= 設定區 =================
INPUT_FILE = r"c:\Users\User\Desktop\C.ai_project\2026_4_7\n8n_predicted_workflows_v2.jsonl"
EVAL_BASE_DIR = r"c:\Users\User\Desktop\C.ai_project\2026_4_7\n8n_workflow_generator\outputs_qwen35_ft_v2"
OUTPUT_DIR = os.path.join(EVAL_BASE_DIR, "llm_generated_workflows")
# ==========================================

def extract_json(text_content):
    """
    從模型生成的純文字回答中，萃取出合法的 JSON 物件 (Dict)。
    這包含多層偵錯 (直接讀取 -> 去掉 Markdown block -> 正則表示式 -> 退回式括號搜索)
    與原評分腳本的 LLMWorkflowGenerator 行為保持一致。
    """
    if not text_content:
        return None
    
    text_content = text_content.strip()
    
    # Try direct parse
    try:
        return json.loads(text_content)
    except json.JSONDecodeError:
        pass
        
    # Remove markdown formatting
    if text_content.startswith('```'):
        lines = text_content.split('\n')
        text_content_no_md = '\n'.join([
            line for line in lines
            if not line.strip().startswith('```')
        ])
        try:
            return json.loads(text_content_no_md)
        except json.JSONDecodeError:
            pass

    # Try heuristic 1: Regex
    json_match = re.search(r'\{.*\}', text_content, re.DOTALL)
    if json_match:
        try:
            return json.loads(json_match.group())
        except json.JSONDecodeError:
            pass
            
    # Try heuristic 2: Truncated JSON
    start = text_content.find("{")
    if start != -1:
        for end in range(len(text_content) - 1, start, -1):
            if text_content[end] != "}":
                continue
            try:
                candidate = text_content[start:end + 1]
                return json.loads(candidate)
            except json.JSONDecodeError:
                continue
                
    return None

def main():
    if not os.path.exists(INPUT_FILE):
        print("="*60)
        print(f"找不到輸入檔案: {INPUT_FILE}")
        print("💡 請確定推論完成後，將 NCHC 上的檔案 `scp` 下載到這裡再執行此腳本！")
        print("指令參考: scp u4439705@nano5.nchc.org.tw:/work/u4439705/n8n_predicted_workflows_v2.jsonl .")
        print("="*60)
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    success_count = 0
    fail_count = 0
    
    print("\n📦 開始轉換 JSONL 格式至 Evaluation 相容格式...")
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            
            data = json.loads(line)
            template_id = str(data.get("id"))
            predicted_text = data.get("predicted", "")
            
            llm_response = extract_json(predicted_text)
            
            # 建立剛好符合 ResultSaver 與原腳本所期待的結構成員
            result = {
                "template_id": template_id,
                "llm_response": llm_response,
                "usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}, # 補上 Dummy Token Usage 免得計算成本崩潰
                "error": None if llm_response else "Failed to parse JSON response from generated string",
                "generated_at": datetime.now().isoformat()
            }
            
            out_path = os.path.join(OUTPUT_DIR, f"generated_{template_id}.json")
            with open(out_path, "w", encoding="utf-8") as out_f:
                json.dump(result, out_f, ensure_ascii=False, indent=2)
                
            if llm_response:
                success_count += 1
            else:
                fail_count += 1
                
    print(f"\n✅ 轉換完成！")
    print(f"  總共處理了 {success_count + fail_count} 筆模板。")
    print(f"  🟢 成功解析 JSON 的數量: {success_count}")
    print(f"  🔴 解析失敗 (破皮/中斷): {fail_count}")
    print(f"  📂 JSON 檔案保存在: {OUTPUT_DIR}")
    print("\n你可以切換到 n8n_workflow_generator 資料夾，直接用下面的指令執行最後的評分了：")
    print("  cd n8n_workflow_generator")
    print("  python scripts/run_evaluation.py --config evaluation/config/qwen_eval_config.yaml\n")

if __name__ == "__main__":
    main()
