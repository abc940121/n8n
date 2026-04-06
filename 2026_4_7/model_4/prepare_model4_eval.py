"""
prepare_model4_eval.py
從 n8n_predicted_model4.jsonl 中：
1. 提取 ground_truth 存為模板 JSON
2. 提取 predicted 存為 LLM 生成結果 JSON
這樣就能接入現有的 n8n_workflow_generator 評估管道。
"""

import json
import os
import re
from datetime import datetime

# ── 路徑設定 ───────────────────────────────────────────────
BASE_DIR     = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE   = os.path.join(BASE_DIR, "n8n_predicted_model4.jsonl")

EVAL_BASE    = os.path.join(BASE_DIR, "..", "n8n_workflow_generator",
                            "evaluation", "outputs_qwen35_ft_model4")
TEMPLATES_DIR = os.path.join(EVAL_BASE, "templates")
GENERATED_DIR = os.path.join(EVAL_BASE, "llm_generated_workflows")


def extract_json(text: str) -> dict | None:
    """多層嘗試從文字中萃取合法 JSON"""
    if not text:
        return None
    text = text.strip()

    # 1. 直接解析
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # 2. 去掉 Markdown fences
    if text.startswith("```"):
        lines = text.split("\n")
        cleaned = "\n".join(l for l in lines if not l.strip().startswith("```"))
        try:
            return json.loads(cleaned)
        except json.JSONDecodeError:
            pass

    # 3. 正則搜尋 {...}
    m = re.search(r"\{.*\}", text, re.DOTALL)
    if m:
        try:
            return json.loads(m.group())
        except json.JSONDecodeError:
            pass

    # 4. 截斷 JSON 修復
    start = text.find("{")
    if start != -1:
        for end in range(len(text) - 1, start, -1):
            if text[end] != "}":
                continue
            try:
                return json.loads(text[start:end + 1])
            except json.JSONDecodeError:
                continue

    return None


def main():
    if not os.path.exists(INPUT_FILE):
        print(f"[ERROR] 找不到 {INPUT_FILE}")
        print("請先從 NCHC 下載：")
        print("  scp u4439705@nano5.nchc.org.tw:/work/u4439705/model_4/n8n_predicted_model4.jsonl model_4/")
        return

    os.makedirs(TEMPLATES_DIR, exist_ok=True)
    os.makedirs(GENERATED_DIR, exist_ok=True)

    ok_pred = fail_pred = ok_gt = fail_gt = 0

    print("📦 開始轉換 Model 4 推論結果...")
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            data        = json.loads(line)
            template_id = str(data.get("id", ""))
            predicted   = data.get("predicted", "")
            ground_truth = data.get("ground_truth", "")

            # ── 儲存 ground_truth 模板 ──
            gt_json = extract_json(ground_truth)
            if gt_json:
                # WorkflowNormalizer.normalize_ground_truth 期望的巢狀格式：
                # template_data['workflow']['workflow'] 才是實際的 workflow JSON
                wrapped = {
                    "id": template_id,
                    "workflow": {
                        "workflow": gt_json
                    }
                }
                gt_path = os.path.join(TEMPLATES_DIR, f"template_{template_id}.json")
                with open(gt_path, "w", encoding="utf-8") as gf:
                    json.dump(wrapped, gf, ensure_ascii=False, indent=2)
                ok_gt += 1
            else:
                fail_gt += 1

            # ── 儲存 predicted 生成結果 ──
            pred_json = extract_json(predicted)
            result = {
                "template_id":  template_id,
                "llm_response": pred_json,
                "usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0},
                "error": None if pred_json else "Failed to parse JSON",
                "generated_at": datetime.now().isoformat(),
            }
            gen_path = os.path.join(GENERATED_DIR, f"generated_{template_id}.json")
            with open(gen_path, "w", encoding="utf-8") as gf:
                json.dump(result, gf, ensure_ascii=False, indent=2)

            if pred_json:
                ok_pred += 1
            else:
                fail_pred += 1

    total = ok_pred + fail_pred
    print(f"\n✅ 轉換完成！共 {total} 筆")
    print(f"  📊 預測結果  - 成功: {ok_pred} | 失敗: {fail_pred}")
    print(f"  📊 Ground Truth - 成功: {ok_gt} | 失敗: {fail_gt}")
    print(f"\n  模板目錄:  {TEMPLATES_DIR}")
    print(f"  生成目錄:  {GENERATED_DIR}")
    print(f"\n⭐ JSON 有效率 (Prediction): {ok_pred/total*100:.1f}%")
    print("\n下一步：執行評估")
    print("  cd n8n_workflow_generator")
    print("  python evaluation/orchestration/run_evaluation.py --config evaluation/config/qwen_eval_config_model4.yaml")


if __name__ == "__main__":
    main()
