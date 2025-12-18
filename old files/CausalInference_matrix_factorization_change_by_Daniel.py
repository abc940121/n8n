# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 23:51:27 2024

@author: vinsent825
"""
 
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
import networkx as nx
import matplotlib.pyplot as plt

# Step 1: 構建知識圖貌 (Knowledge Graph)


triples = [
    ('獲得時間戳記', '無需符合任何條件', '取得手機號碼'),
    ('取得手機號碼', '當以下規則都成立時:{{rule}}', '結束目前腳本'),
    ('取得手機號碼', '前述所有規則都不符合時', '查無任何手機號碼'),
    ('查無任何手機號碼', '無需符合任何條件', '手機條碼申請教學'),
    ('執行SQL指令', '無需符合任何條件', '是否成功'),
    ('是否成功', '無需符合任何條件', '判斷回傳Data是否存在'),
    ('判斷回傳Data是否存在', '當以下規則都成立時:{{rule}}', '(成功)看DBModule'),
    ('判斷回傳Data是否存在', '前述所有規則都不符合時', '(失敗)看DBModule'),
    ('(成功)看DBModule', '無需符合任何條件', '結束'),
    ('(失敗)看DBModule', '無需符合任何條件', '顯示錯誤'),
    ('組SQL', '無需符合任何條件', '修改員工的手機條碼'),
    ('修改員工的手機條碼', '無需符合任何條件', '手機條碼修改完成'),
    ('手機條碼修改完成', '無需符合任何條件', '結束目前的腳本'),
    ('組SQL', '無需符合任何條件', '新增員工的手機條碼'),
    ('新增員工的手機條碼', '無需符合任何條件', '手機條碼設定完成'),
    ('手機條碼設定完成', '無需符合任何條件', '結束目前的腳本'),
    ('組SQL', '無需符合任何條件', '查詢員工的手機條碼'),
    ('查詢員工的手機條碼', '無需符合任何條件', '處理回傳結果'),
    ('查詢員工的手機條碼', '無需符合任何條件', '查詢結果'),
    ('處理回傳結果', '無需符合任何條件', '回傳結果'),
    ('查詢結果', '無需符合任何條件', '回傳結果'),
    ('判斷是否為測試模式', '當以下規則都成立時:{{rule}}', '設定假資料(有設定)'),
    ('判斷是否為測試模式', '前述所有規則都不符合時', '查詢員工手機條碼'),
    ('設定假資料(有設定)', '無需符合任何條件', '結束目前的腳本'),
    ('查詢員工手機條碼', '無需符合任何條件', '結束目前的腳本'),
    ('呼叫API發生錯誤', '無需符合任何條件', '跳轉回主選單'),
    ('跳轉回主選單', '無需符合任何條件', '結束所有腳本'),
    ('變數初始', '無需符合任何條件', '檢核員工是否有設定手機條碼'),
    ('檢核員工是否有設定手機條碼', '無需符合任何條件', '判斷是否已綁定手機條碼'),
    ('判斷是否已綁定手機條碼', '當以下規則都成立時:{{rule}}', '手機條碼未設定'),
    ('判斷是否已綁定手機條碼', '前述所有規則都不符合時', '手機條碼已設定'),
    ('判斷是否為測試模式', '當以下規則都成立時:{{rule}}', '設定表單初始值(假資料)'),
    ('判斷是否為測試模式', '前述所有規則都不符合時', '設定表單預設值'),
    ('設定表單初始值(假資料)', '無需符合任何條件', '查詢手機條碼'),
    ('設定表單預設值', '無需符合任何條件', '查詢手機條碼'),
    ('查詢手機條碼', '當以下規則都成立時:{{rule}}', '顯示資料'),
    ('查詢手機條碼', '前述所有規則都不符合時', '無法辨識輸入內容'),
    ('顯示資料', '無需符合任何條件', '[API]取得手機條碼'),
    ('[API]取得手機條碼', '無需符合任何條件', '手機條碼修改'),
    ('無法辨識輸入內容', '無需符合任何條件', '主選單'),
    ('手機條碼修改', '無需符合任何條件', '判斷按鈕動作'),
    ('判斷按鈕動作', '當以下規則都成立時:{{rule}}', '[API]手機條碼設定'),
    ('判斷按鈕動作', '當以下規則都成立時:{{rule}}', '[API]手機條碼修改'),
    ('判斷按鈕動作', '前述所有規則都不符合時', '無法辨識輸入內容'),
    ('[API]手機條碼設定', '無需符合任何條件', '[功能]手機條碼維護'),
    ('[API]手機條碼修改', '無需符合任何條件', '[功能]手機條碼維護'),
    ('無法辨識輸入內容', '無需符合任何條件', '手機條碼修改'),
    ('OCR變數設定', '無需符合任何條件', 'OCR文字辨識結果'),
    ('台新證券小幫手主選單', '當以下規則都成立時:{{rule}}', '[腳本]中文翻譯合約摘要'),
    ('台新證券小幫手主選單', '前述所有規則都不符合時', '[腳本]台新腦模擬中文翻譯合約摘要'),
    ('檔案上傳', '無需符合任何條件', '附件轉圖片連結'),
    ('附件轉圖片連結', '無需符合任何條件', '上傳成功提示'),
    ('台新證券小幫手功能選單', '當以下規則都成立時:{{rule}}', '中文翻譯提示'),
    ('台新證券小幫手功能選單', '當以下規則都成立時:{{rule}}', '內容摘要提示'),
    ('中文翻譯提示', '無需符合任何條件', '中文翻譯'),
    ('內容摘要提示', '無需符合任何條件', '合約摘要'),
    ('上傳成功提示', '無需符合任何條件', '台新證券小幫手功能選單'),
    ('處理完成結果', '無需符合任何條件', '結果輸出提示'),
    ('結果輸出提示', '無需符合任何條件', '選擇下一步'),
    ('中文翻譯', '無需符合任何條件', '處理完成結果'),
    ('合約摘要', '無需符合任何條件', '處理完成結果'),
    ('選擇下一步', '當以下規則都成立時:{{rule}}', '台新證券小幫手功能選單'),
    ('檔案上傳', '無需符合任何條件', 'OCR文字辨識'),
    ('OCR文字辨識', '無需符合任何條件', '上傳成功提示'),
    ('上傳成功提示', '無需符合任何條件', '翻譯或摘要'),
    ('翻譯或摘要', '當以下規則都成立時:{{rule}}', '中文翻譯提示'),
    ('翻譯或摘要', '當以下規則都成立時:{{rule}}', '內容摘要提示'),
    ('內容摘要提示', '無需符合任何條件', '內容摘要'),
    ('中文翻譯', '無需符合任何條件', '批次呼叫AOAI'),
    ('內容摘要', '無需符合任何條件', '批次呼叫AOAI'),
    ('批次呼叫AOAI', '前述所有規則都不符合時', 'API錯誤'),
    ('API錯誤', '無需符合任何條件', 'API錯誤返回主選單'),
    ('批次呼叫AOAI', '當以下規則都成立時:{{rule}}', '輸出資料整合'),
    ('輸出資料整合', '無需符合任何條件', '處理完成結果'),
    ('結果輸出提示', '無需符合任何條件', '功能選單'),
    ('功能選單', '當以下規則都成立時:{{rule}}', '翻譯或摘要'),
    ('API參數設定', '無需符合任何條件', '檔案上傳'),
    ('檔案上傳', '無需符合任何條件', '文字檔轉文字'),
    ('文字檔轉文字', '無需符合任何條件', 'Message變數設定'),
    ('Message變數設定', '無需符合任何條件', '批次呼叫AOAI'),
    ('Message變數設定', '無需符合任何條件', '偵錯'),
    ('批次呼叫AOAI', '無需符合任何條件', '測試輸出'),
    ('滿意度調查', '無需符合任何條件', '回迎賓'),
    ('輸入', '無需符合任何條件', 'Echo'),
    ('Echo', '當以下規則都成立時:{{rule}}', '前往滿意度調查'),
    ('Echo', '前述所有規則都不符合時', '填寫滿意度調查'),
    ('等待user輸入QA數量', '無需符合任何條件', '等待使用者上傳檔案'),
    ('等待使用者上傳檔案', '無需符合任何條件', '產生FAQ'),
    ('產生FAQ', '無需符合任何條件', '再次檢核並輸出'),
    ('再次檢核並輸出', '無需符合任何條件', '顯示三版結果'),
    ('等待使用者上傳檔案', '無需符合任何條件', '發票OCR'),
    ('發票OCR', '無需符合任何條件', '顯示發票'),
    ('顯示發票', '當以下規則有一個成立時:{{rule}}', '送出'),
    ('顯示發票', '前述所有規則都不符合時', '編輯'),
    ('編輯', '無需符合任何條件', '編輯發票'),
    ('編輯發票', '無需符合任何條件', '結果'),
    ('結果', '當以下規則有一個成立時:{{rule}}', '送出!'),
    ('結果', '無需符合任何條件', '等待使用者上傳檔案'),
    ('等待使用者上傳檔案', '無需符合任何條件', '系統處理訊息'),
    ('系統處理訊息', '無需符合任何條件', '支票OCR'),
    ('支票OCR', '無需符合任何條件', '檢查json'),
    ('檢查json', '無需符合任何條件', '發票掃描結果預覽'),
    ('發票掃描結果預覽', '當以下規則有一個成立時:{{rule}}', '送出'),
    ('發票掃描結果預覽', '當以下規則有一個成立時:{{rule}}', '發票掃描結果預覽'),
    ('發票掃描結果預覽', '當以下規則有一個成立時:{{rule}}', '回首頁'),
    ('發票掃描結果預覽', '無需符合任何條件', 'temp'),
    ('temp', '當以下規則都成立時:{{rule}}', 'API發送'),
    ('temp', '前述所有規則都不符合時', '回首頁'),
    ('API發送', '無需符合任何條件', '送出!'),
    ('送出!', '當以下規則都成立時:{{rule}}', '回首頁'),
    ('送出!', '當以下規則有一個成立時:{{rule}}', '等待使用者上傳檔案'),
    ('請敘述你想繪製的圖片', '無需符合任何條件', 'LLM製圖詠唱咒語'),
    ('LLM製圖詠唱咒語', '無需符合任何條件', '詠唱中'),
    ('詠唱中', '無需符合任何條件', '從6個prompt選一個生圖'),
    ('從6個prompt選一個生圖', '無需符合任何條件', '詠唱中'),
    ('詠唱中', '無需符合任何條件', '生圖'),
    ('生圖', '無需符合任何條件', 'result'),
    ('result', '當以下規則都成立時:{{rule}}', '請敘述你想繪製的圖片'),
    ('輸入特徵', '無需符合任何條件', 'LLM'),
    ('LLM', '無需符合任何條件', 'LLM結果'),
    ('等待使用者上傳檔案', '無需符合任何條件', '利用LLM將履歷轉為json'),
    ('利用LLM將履歷轉為json', '無需符合任何條件', '請輸入該職缺的"條件要求'),
    ('請輸入該職缺的"條件要求"', '無需符合任何條件', '職缺條件標準化'),
    ('職缺條件標準化', '無需符合任何條件', '根據LLM判斷履歷是否符合職缺要求'),
    ('根據LLM判斷履歷是否符合職缺要求', '無需符合任何條件', '123'),
    ('123', '無需符合任何條件', '123'),
    ('輸入特徵', '前述所有規則都不符合時', 'LLM'),
    ('輸入特徵', '當以下規則都成立時:{{rule}}', '模擬資料'),
    ('模擬資料', '無需符合任何條件', 'LLM'),
    ('LLM', '無需符合任何條件', '提示詞'),
    ('提示詞', '無需符合任何條件', 'API發送'),
    ('API發送', '無需符合任何條件', 'jsonparse'),
    ('jsonparse', '無需符合任何條件', 'url'),
    ('輸入訊息', '無需符合任何條件', '語音轉文字'),
    ('語音轉文字', '無需符合任何條件', '檢查文法'),
    ('檢查文法', '無需符合任何條件', '取得對話及生成吉卜力圖片'),
    ('取得對話及生成吉卜力圖片', '無需符合任何條件', '顯示結果'),
    ('語音轉文字', '無需符合任何條件', '未命名'),
    ('未命名', '當以下規則都成立時:{{rule}}', '把對話畫成吉卜力圖片'),
    ('未命名', '前述所有規則都不符合時', '取消'),
    ('把對話畫成吉卜力圖片', '無需符合任何條件', '未命名-2'),
    ('取消', '無需符合任何條件', '輸入訊息'),
    ('等待user輸入QA數量', '無需符合任何條件', 'TEMP'),
    ('TEMP', '無需符合任何條件', '等待使用者上傳檔案'),
    ('等待使用者上傳檔案', '無需符合任何條件', '利用LLM產生問題'),
    ('利用LLM產生問題', '無需符合任何條件', '轉成特定json格式'),
    ('轉成特定json格式', '無需符合任何條件', 'adcard'),
    ('adcard', '無需符合任何條件', 'adcard'),
    ('等待user上傳檔案', '無需符合任何條件', '以表格摘要訪談記錄'),
    ('以表格摘要訪談記錄', '無需符合任何條件', '翻譯英、韓'),
    ('翻譯英、韓', '無需符合任何條件', '顯示三版結果'),
    ('選單', '當以下規則都成立時:{{rule}}', 'PPT產生器'),
    ('選單', '當以下規則都成立時:{{rule}}', '圖片生成小助手'),
    ('選單', '當以下規則都成立時:{{rule}}', '教育訓練題目生成'),
    ('選單', '當以下規則都成立時:{{rule}}', '履歷比對'),
    ('選單', '當以下規則都成立時:{{rule}}', '發票OCR'),
    ('選單', '當以下規則都成立時:{{rule}}', '鋼筆銷售'),
    ('PPT產生器', '無需符合任何條件', '回選單'),
    ('圖片生成小助手', '無需符合任何條件', '回選單'),
    ('教育訓練題目生成', '無需符合任何條件', '回選單'),
    ('履歷比對', '無需符合任何條件', '回選單'),
    ('發票OCR', '無需符合任何條件', '回選單'),
    ('鋼筆銷售', '無需符合任何條件', '回選單'),
    ('選擇難易度', '無需符合任何條件', '呼叫「LLM 模組」模組'),
    ('呼叫「LLM 模組」模組', '無需符合任何條件', '判斷有無說服成功'),
    ('判斷有無說服成功', '當以下規則有一個成立時:{{rule}}', '成功提示'),
    ('判斷有無說服成功', '前述所有規則都不符合時', '回傳'),
    ('成功提示', '當以下規則都成立時:{{rule}}', '再來一次'),
    ('回傳', '無需符合任何條件', '繼續對話'),
    ('再來一次', '無需符合任何條件', '選擇難易度'),
    ('繼續對話', '無需符合任何條件', '呼叫「LLM 模組」模組')    
]


# 使用 networkx 構建知識圖貌
G = nx.DiGraph()  # Directed graph to represent the causal relationship

for triple in triples:
    source, relation, target = triple
    G.add_edge(source, target, relation=relation)

# Step 2: 構建影響因子與缺陷之間的交互矩陣
nodes = list(G.nodes)
num_nodes = len(nodes)
interaction_matrix = np.zeros((num_nodes, num_nodes))

# 構建交互矩陣，其中如果有邊則設為1
for edge in G.edges(data=True):
    source, target, relation = edge
    source_index = nodes.index(source)
    target_index = nodes.index(target)
    interaction_matrix[source_index][target_index] = 1

print("Interaction Matrix:")
print(interaction_matrix)

# Step 3: 初始化矩陣 P 和 Q
NUM_FACTORS = 64
LEARNING_RATE = 0.003  # Reduced learning rate to avoid gradient explosion
NUM_ITERATIONS = 1500
REGULARIZATION = 0.05  # Increased regularization to stabilize training

P = np.random.rand(num_nodes, NUM_FACTORS) * 0.005  # Smaller initialization to avoid large values
Q = np.random.rand(num_nodes, NUM_FACTORS) * 0.005

# Step 4: 定義加正演的損失函數

def compute_weighted_loss(interaction_matrix, P, Q):
    prediction_matrix = P.dot(Q.T)
    error = interaction_matrix - prediction_matrix
    weight_matrix = (interaction_matrix > 0).astype(float)  # Assign higher weight to non-zero elements
    loss = np.sum(weight_matrix * (error ** 2))  # Weighted loss
    reg_term = REGULARIZATION * (np.sum(P ** 2) + np.sum(Q ** 2))
    return loss + reg_term

# Step 5: 滑動進行更新

def gradient_descent(interaction_matrix, P, Q, num_iterations, learning_rate):
    for i in range(num_iterations):
        prediction_matrix = P.dot(Q.T)
        if np.isnan(prediction_matrix).any():
            print(f"NaN detected in prediction matrix at iteration {i}")
            break

        error = interaction_matrix - prediction_matrix

        if np.isnan(error).any():
            print(f"NaN detected in error matrix at iteration {i}")
            break

        P_gradient = -2 * error.dot(Q) + 2 * REGULARIZATION * P
        Q_gradient = -2 * error.T.dot(P) + 2 * REGULARIZATION * Q

        if np.isnan(P_gradient).any() or np.isnan(Q_gradient).any():
            print(f"NaN detected in gradients at iteration {i}")
            break

        P -= learning_rate * P_gradient
        Q -= learning_rate * Q_gradient

        if np.isnan(P).any() or np.isnan(Q).any():
            print(f"NaN detected in P or Q at iteration {i}")
            break

        if i % 100 == 0:
            loss = compute_weighted_loss(interaction_matrix, P, Q)
            print(f"Iteration {i}: Loss = {loss:.4f}")

    return P, Q

# Step 6: 訓練 P 和 Q
P_trained, Q_trained = gradient_descent(interaction_matrix, P, Q, NUM_ITERATIONS, LEARNING_RATE)

# Step 7: 生成最終的推薦矩陣
recommendation_matrix = P_trained.dot(Q_trained.T)
if np.isnan(recommendation_matrix).any():
    print("Recommendation matrix contains NaN values. Debug is required.")

# Step 8: 將矩陣結果與節點對應
recommendation_df = pd.DataFrame(recommendation_matrix, index=nodes, columns=nodes)

# Step 9: 定義函數來預測特定因子的關係

def predict_relationships(factor_name=None, defect_name=None, top_k=None):
    """
    由高到低排序輸出預測關係分數。
    - factor_name: 查「列」→ 從該節點指向其他節點的分數（out-links）
    - defect_name: 查「欄」→ 其他節點指向該節點的分數（in-links）
    - top_k: 只顯示前 K 名（預設顯示全部）
    """
    if factor_name is not None:
        if factor_name in recommendation_df.index:
            s = recommendation_df.loc[factor_name].sort_values(ascending=False)
            if top_k is not None:
                s = s.head(top_k)
            print(f"Predicted relationships for factor '{factor_name}' (desc):\n{s}")
        else:
            print(f"Factor '{factor_name}' not found in the graph.")
    elif defect_name is not None:
        if defect_name in recommendation_df.columns:
            s = recommendation_df[defect_name].sort_values(ascending=False)
            if top_k is not None:
                s = s.head(top_k)
            print(f"Predicted relationships for defect '{defect_name}' (desc):\n{s}")
        else:
            print(f"Defect '{defect_name}' not found in the graph.")
    else:
        print("Please provide either factor_name or defect_name.")

#我自己加的
import random
count=len(triples)
print("共有項目數:", count)
i=random.randint(0, count-1)
first=triples[i][0]
last=triples[i][2]


# Step 10: 使用範例
predict_relationships(factor_name=first, top_k=10)  
predict_relationships(defect_name=last, top_k=10)  
