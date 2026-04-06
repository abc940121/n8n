# N8N Agentic AI: Qwen 3.5 27B LLM 管線架構總結

這份文件記錄了我們在這段對話中，從「訓練資料預處理」➟「NCHC 叢集微調」➟「極速與長文本推論」➟「最終自動化評測」所用到的所有核心程式碼檔案及其扮演的關鍵角色。

---

## 📂 階段一：資料準備與預處理 (Data Preparation)

在讓模型踏入訓練場前，我們必須將原始的資料集打磨成 Qwen 3.5 看得懂的 OpenAI `messages` 格式，並抽出測試集。

1. **`prepare_testing_data.py`** & **`prepare_testing_data_v2.py`**
   - **作用**：測試集萃取器。
   - **說明**：解析 `templates_index.json`，隨機或依序抽出前 100 筆測試用的 Ground Truth，並把我們微調時使用的 `system` prompt 與 `user` prompt 套用在上面，打包成沒有包含答案的 `test_100_prompts.jsonl`，專供後續推論吃入。
2. **`create_train_messages.jsonl`**
   - **作用**：最終訓練語料庫。
   - **說明**：裡面包含了幾千筆標準的 `{"messages": [{"role": "system",...}, {"role": "user", ...}, {"role": "assistant", ...}]}` 對話結構。

---

## 📂 階段二：超級電腦微調 (NCHC Fine-Tuning)

利用 NCHC H200 的硬體優勢，把 n8n 繁複的圖學概念與 JSON 語法注入開源大模型。

1. **`train_qwen35_v2.py`**
   - **作用**：LoRA 微調核心練功爐。
   - **說明**：我們大幅修改了原有腳本，讓它支援 HuggingFace 最新版的 `ChatML/messages` 對話格式。它負責將基礎模型載入、套用高效率的 LoRA 降維注意力機制，最終將學習到的 N8N 語感輸出。
2. **`n8n_qwen35_lora_v2/` (資料夾)**
   - **作用**：微調的靈魂 (Adapter Weights)。
   - **說明**：微調的產出物，體積極小，但是包含了所有模型在這段期間學到的 N8N Node 與 Connection 知識。

---

## 📂 階段三：高速推論與難題克服 (Inference & Auto-Continuation)

生成階段我們經歷了多次演化，從最初的 4-bit 龜速生成，進化到了能夠扛住 32,768 Tokens 長文本的高速穩定推論。

1. **`predict_custom_v2.py`**
   - **作用**：最初的推論雛形（已淘汰）。
   - **說明**：使用基礎 4-bit 量化與 Adapter 掛載，但是速度太慢（一筆需要 6 分鐘以上）且容易發生 VRAM 釋放問題。
2. **`predict_custom_fast.py`**
   - **作用**：純 BF16 高速推論版。
   - **說明**：我們導入了 `merge_and_unload()` 技巧，把 LoRA 權重直接與主模型合體，搭配 BF16 精度，將速度提升了近乎四倍。但也發現固定 Token 上限（如 4096）仍會截斷大型工作流。
3. **`clean_truncated.py`** & **`analyze_good_generations.py`**
   - **作用**：資料巡檢與分析員。
   - **說明**：幫我們發現 100 筆測試中，有 69 筆是完美的，而 31 筆因為過於龐大被截斷，並將好的資料隔離出 `_clean.jsonl` 避免後續浪費算力重跑。
4. **`predict_custom_fast_continuation.py`**
   - **作用**：**最終極致推論版 (Auto-Continuation)**。
   - **說明**：導入了「無縫接力」邏輯。只要模型沒有生成句點 (`eos_token`)，在每次達到 4K Tokens 或 8K Tokens 時，它都會把先前的產出再餵回給大腦繼續寫，直到產生合法的 JSON 結尾！
5. **`n8n_predicted_workflows_v2.jsonl`**
   - **作用**：推理成品的最終卸貨區。

---

## 📂 階段四：自動化評分與橋接 (Evaluation Pipeline)

這是從 NCHC 戰場回到本機戰場的收尾工作。

1. **`convert_qwen_predictions_to_eval_format.py`**
   - **作用**：評估系統的橋接器。
   - **說明**：模型常常會輸出一大堆 `<think>` 或 Markdown 格式的閒聊解釋才丟出 JSON。這個腳本具備「雙向退回式搜索」的安全氣囊，能暴力剝除所有幹話，純粹萃取出最乾淨的 N8N JSON，並打包成舊有評分系統所要求的 `generated_ID.json` 格式。
2. **`qwen_eval_config.yaml`**
   - **作用**：評分環境設定檔。
   - **說明**：指定資料夾路徑與設定值，好讓舊有的 `gpt4` 評測腳本能乖乖跑去讀取我們 Qwen 的成果夾。
3. **`run_evaluation.py` (及附屬 evaluator 模組)**
   - **作用**：冷酷無情的自動閱卷官。
   - **說明**：這支你原先的腳本負責把我們產出的 JSON 轉換成圖學物件，並逐個比對每個節點 (Node) 與連線 (Connection)，產生了最終含有 `Node F1`、`Connection Accuracy` 與 `JSON Validity` 的學術評分報表 (`summary_statistics.json`)！
