# Qwen 3.5 27B Fine-Tuning 實驗總結報告

## 一、各模型效能數據對比

### 完整對比表

| 指標 | 歷史基準 | Model 2 | Model 3 | Model 4 | **Model 5** |
|------|---------|---------|---------|---------|-------------|
| **JSON 有效率** | 61.3% | 80.0% | 72.0% | **89.8%** | 79.2% |
| **Node F1** | 34.5% | 53.7% | 52.2% | 81.4% | **82.5%** ⭐ |
| **Connection F1** | 11.1% | 26.1% | 21.2% | 49.0% | **49.9%** ⭐ |
| **Parameter 準確率** | 28.0% | 40.9% | 41.3% | **43.7%** | 42.4% |
| 訓練資料平均輸出長度 | - | 11,959 | 10,172 | **13,386** | 10,889 |
| 測試樣本數 | 1,963 | 100 | 100 | 197 | 197 |
| 成功評估數 | 1,203 | 80 | 72 | 177 | 156 |
| 成功率 | 61.3% | 80.0% | 72.0% | **89.8%** | 79.2% |

### 模型說明

| 模型 | 訓練資料 | 筆數 | 訓練策略 |
|------|---------|------|---------|
| **歷史基準** | 另一資料夾（未納入本次紀錄） | ~1,963 | **已微調**（非原始 Qwen）|
| **Model 2** | `create_train_messages.jsonl` | 742 | QLoRA, 英文 Prompt, 4096 token |
| **Model 3** | `create_highfreq_no_sticky_prefixed_train_messages.jsonl` | ~742 | QLoRA, 高頻節點 + 移除便利貼 |
| **Model 4** | `qwen27b_v3_train.jsonl` | **1,766** | QLoRA, **中文 Prompt**, 8192 token |
| **Model 5** | `qwen27b_v3_openai_ft_train_max16000.jsonl` | 800 | QLoRA, 中文 Prompt, **16k 長序列** |

---

## 四、訓練技術細節

### Fine-Tuning 方法：QLoRA (Quantized LoRA)

所有模型（Model 2 以後）均使用 **QLoRA** 進行微調，聲稱同時擁有 LoRA 訓練效率与點數量減少暫存的優勢。

**核心概念：**
- **量化基礎模型**：以 **4-bit NF4**（NormalFloat4）量化載入 27B 參數，顏存佔用從 Full BF16 的 ≈ 54GB 降至 ≈ 14GB。
- **LoRA Adapter**：在量化的基礎模型上，插入可訓練的低秩矩陣（LoRA），只訓練約 **0.3% 的參數**。
- **計算精度**：實際計算使用 **BF16**（bfloat16），平衡精度與速度。

### 量化設定（BitsAndBytesConfig）

```python
BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",          # NormalFloat4 量化
    bnb_4bit_compute_dtype=torch.bfloat16,  # 前向計算用 BF16
    bnb_4bit_use_double_quant=True,     # 雙重量化，進一步行稏存
)
```

### LoRA 設定（所有模型相同）

| 參數 | 値 | 說明 |
|---|---|---|
| `r` (rank) | 16 | LoRA 適配器的秩，控制可訓練參數少|
| `lora_alpha` | 32 | 就相當於 learning rate scaling，建議為 r 的2 倍 |
| `lora_dropout` | 0.05 | 防止過擬合 |
| `target_modules` | q, k, v, o, gate, up, down proj | 全面覆蓋 Attention 與 FFN 層 |
| `task_type` | CAUSAL_LM | 因果式語言模型 |

### 訓練超參數

| 參數 | Model 2/3 | Model 4 | Model 5 |
|---|---|---|---|
| Epochs | 3 | 3 | 3 |
| Batch Size | 1 | 1 | 1 |
| Gradient Accumulation | 8 | 8 | 8 |
| **Effective Batch Size** | **8** | **8** | **8** |
| Learning Rate | 2e-4 | 2e-4 | 2e-4 |
| LR Scheduler | cosine | cosine | cosine |
| Warmup Ratio | 0.05 | 0.05 | 0.05 |
| Max Sequence Length | 4096 | 8192 | 8192 |
| Gradient Checkpointing | 未強制進行 | ✅ 開啟 | ✅ 開啟 |
| Precision | BF16 | BF16 | BF16 |
| Quantization | 4-bit NF4 | 4-bit NF4 | 4-bit NF4 |
| Flash Attention | 未安裝 | 未安裝 | 未安裝 |
| Hardware | H100 (NCHC) | H200 (NCHC) | H200 (NCHC) |

### Loss 計算方式

LoRA 微調的模型訓練目標是 標準的 **Causal LM Cross-Entropy Loss**，但只計算 **assistant 回應的 loss**，問題的部分（system + user）的 label 設為 `-100` 被忽略。

```
[system token…][-100][-100] [user token…][-100][-100] [assistant JSON token…][LOSS][LOSS]
```

### 推論設定

| 參數 | 値 | 說明 |
|---|---|---|
| `do_sample` | False | 確定性解碼（Greedy）|
| `max_new_tokens` | 8192 | 最大輸出長度 |
| `repetition_penalty` | 1.05 | 輕度懲罰重複內容 |
| `enable_thinking` | False | 關閉 Qwen3.5 思考模式，直接輸出 JSON |

---

## 二、重要資料清單

### 本機路徑（`C:\Users\User\Desktop\C.ai_project\2026_4_7\`）

| 用途 | 路徑 |
|------|------|
| **v3 訓練資料（原始）** | `my_qwen_test/qwen27b_v3_train.jsonl` |
| **v3 測試資料（原始）** | `my_qwen_test/qwen27b_v3_test.jsonl` |
| **v3 訓練資料（已轉換 Chat 格式）** | `model_4/v3_train_chat.jsonl` |
| **v3 驗證資料（已轉換 Chat 格式）** | `model_4/v3_valid_chat.jsonl` |
| **Model 4 推論結果** | `model_4/n8n_predicted_model4.jsonl` |
| **Model 4 評估結果** | `n8n_workflow_generator/evaluation/outputs_qwen35_ft_model4/evaluation_results/summary_statistics.json` |
| **Model 2** | `model_2/n8n_predicted_workflows_v2_clean.jsonl` |
| **Model 2 評估結果** | `n8n_workflow_generator/outputs_qwen35_ft_v2/evaluation_results/summary_statistics.json` |
| **Model 5 訓練資料** | `model_5/qwen27b_v3_openai_ft_train_max16000.jsonl` |
| **Model 5 推論結果** | `model_5/n8n_predicted_model5.jsonl` |
| **Model 5 評估結果** | `n8n_workflow_generator/evaluation/outputs_qwen35_ft_model5/evaluation_results/summary_statistics.json` |

### NCHC 路徑（`/work/u4439705/`）

| 用途 | 路徑 |
|------|------|
| **基礎模型** | `/work/u4439705/models/Qwen3.5-27B` |
| **Model 4 LoRA Adapter（最終）** | `/work/u4439705/n8n_qwen35_lora_model4/adapter_model.safetensors` |
| **Model 4 Checkpoint 備份** | `/work/u4439705/n8n_qwen35_lora_model4/checkpoint-600/` |
| **訓練腳本** | `/work/u4439705/model_4/train_model4.py` |
| **推論腳本** | `/work/u4439705/model_4/predict_model4.py` |
| **轉換後訓練資料** | `/work/u4439705/model_4/v3_train_chat.jsonl` |
| **轉換後驗證資料** | `/work/u4439705/model_4/v3_valid_chat.jsonl` |
| **推論結果** | `/work/u4439705/model_4/n8n_predicted_model4.jsonl` |
| **Model 5 LoRA Adapter** | `/work/u4439705/n8n_qwen35_lora_model5/` |
| **Model 5 訓練資料** | `/work/u4439705/model_5/qwen27b_v3_openai_ft_train_max16000.jsonl` |
| **Model 5 推論結果** | `/work/u4439705/model_5/n8n_predicted_model5.jsonl` |

---

## 三、觀察與未來改進方向

### 🔍 關鍵觀察

**1. 資料量是最大的驅動力**
- Model 3 與 Model 2 使用相同量的資料，效能幾乎沒有差異。
- Model 4 使用 2.4 倍資料量，Node F1 直接從 53.7% 跳升至 81.4%（+28%）。
- **結論：資料量比任何其他超參數調整都更重要。**

**2. 上下文完整性至關重要**
- Model 3 移除了便利貼（Sticky Note）上下文後，效能反而下降（72% vs 80% JSON validity）。
- n8n 的便利貼雖然不是可執行節點，但包含了工作流的語義描述，對模型理解設計意圖很關鍵。
- **結論：不要刪除任何訓練資料中的上下文資訊。**

**3. 中文 Prompt 與英文任務的兼容性**
- Model 4 用中文 Prompt 訓練，但輸出仍是標準的英文 JSON，效能大幅超越 Model 2。
- 這證明 Qwen 3.5 的多語言能力足以橋接中文理解與英文 JSON 生成。

**4. Connection F1 仍有巨大改進空間**
- 即使是最好的 Model 5，Connection F1 也只有 49.9%，離「完美連線」還差一半。
- 這是目前最主要的瓶頸：模型能正確識別節點類型，但無法準確還原節點之間的邏輯連接路徑。

**5. Model 5 的「高邏輯、低穩定」特性**
- Model 5 在資料量僅 800 筆（不到半數）的情況下，Node/Connection F1 皆反超 Model 4。
- 但 JSON 有效率從 89.8% 跌至 79.2%，顯示長序列訓練會增加輸出的不穩定性（截斷或括號錯誤）。
- **結論：長序列 (16k) 訓練顯著提升了單一樣本的學習深度，但需要更強的後處理或更多資料來維持穩定性。**

---

### 🚀 未來改進方向

#### 短期（資料層面）

1. **繼續擴大訓練資料**
   - 目前 1,766 筆的提升效果明顯，建議擴充到 3,000-5,000 筆。
   - 特別加強「複雜連線邏輯」的案例（如多分支、迴圈、條件判斷）。

2. **加入連線描述的訓練資料**
   - 在訓練樣本的 user prompt 中明確描述「A 節點的輸出連接到 B 節點」這類資訊。
   - 目前 v3 資料的 prompt 主要描述功能需求，對連線拓撲的描述較少。

3. **針對失敗案例（20 筆）進行分析**
   - 哪些類型的 workflow 最容易失敗？是節點數過多、特殊 node type、還是複雜連線？

#### 中期（模型層面）

4. **增加訓練 Epoch 或調整 Learning Rate**
   - 目前 Model 4 只訓練 3 個 Epoch，可以嘗試 5 Epoch 觀察是否有更多改善。

5. **後處理驗證層**
   - 加入 n8n node type 白名單驗證，自動過濾幻覺節點（之前出現的 `?` 節點）。
   - 在推論後自動修復常見的 JSON 結構問題。

#### 長期（架構層面）

6. **考慮兩階段生成**
   - Stage 1：先生成節點列表。
   - Stage 2：根據節點列表生成連線。
   - 這能讓模型在規劃連線時，已確知所有節點的存在。

7. **引入 Retrieval-Augmented Generation (RAG)**
   - 建立 n8n workflow 的向量資料庫，推論時找出語義相似的範例作為 few-shot 參考。

---

> **當前最佳模型**：Model 4（NCHC: `/work/u4439705/n8n_qwen35_lora_model4/`）
> Node F1: 81.4% | Connection F1: 49.0% | JSON 有效率: 89.8%
