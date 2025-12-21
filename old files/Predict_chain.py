# -*- coding: utf-8 -*-
"""
基於矩陣分解的 Chain 評分與生成模型 (V4 - 包含測試集與批次評分功能)
"""

import numpy as np    #數學運算的核心。我們後面所有的矩陣加減乘除（P dot Q^T）都是靠它。
import pandas as pd   #資料表工具。最後要把醜醜的矩陣變成漂亮的表格（有欄位名稱、索引）顯示給你看時使用。
import networkx as nx #圖學工具。雖然這版程式主要靠矩陣運算，但我們保留它用來處理節點與邊的關係概念。
import json           
import random
from sklearn.model_selection import train_test_split # 用來切分訓練集與測試集

class ChainRecommender:
    def __init__(self, json_file_path, num_factors=10, learning_rate=0.001, num_iterations=1000, regularization=0.1, pos_weight=1.0):
        # 接收外部傳進來的參數，並存在自己身上 (self)
        self.json_file_path = json_file_path
        self.num_factors = num_factors      # 特徵維度 (腦容量)：越大越能記細節，但也越慢
        self.learning_rate = learning_rate  # 學習率 (步伐)：太大會走過頭(NaN)，太小走不動
        self.num_iterations = num_iterations # 迭代次數 (讀書次數)
        self.regularization = regularization # 正則化 (懲罰項)：防止死記硬背
        self.pos_weight = pos_weight        # 正樣本權重：這就是我們為了救 Name 模型加的關鍵參數
        
        # 初始化內部變數 (先設為 None 或空清單)
        self.nodes = []                 # 所有的節點名稱列表 ['A', 'B', 'C'...]
        self.node_to_idx = {}           # 節點名稱到索引的對應字典 {'A':0, 'B':1, ...} 
        self.interaction_matrix = None  # 交互矩陣 (N x N 的二維陣列)
        self.P = None                   # 矩陣分解的 P 矩陣
        self.Q = None                   # 矩陣分解的 Q 矩陣
        self.recommendation_df = None   # 最終結果表
        
        # 存放分割後的資料
        self.train_chains = []
        self.test_chains = []

    def load_and_split_data(self, test_size=0.1):
        print(f"正在讀取檔案: {self.json_file_path} ...")
        # ... (省略讀取檔案的 try-except 錯誤處理，這是防呆用的) ...
        try:
            with open(self.json_file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f"錯誤: 找不到檔案 {self.json_file_path}")
            return False
        all_chains = data.get("chains", [])  # 取得所有的 chain，[]是如果找不到chains，不要報錯直接給空清單[]就好

        # 1. 先掃描一次所有 chain，找出所有可能的節點 (Universe of Nodes)
        # 這是為了確保矩陣大小固定，即使某個節點只出現在測試集，我們也要留位置給它(雖然會是全0)
        unique_nodes = set()  # 使用 set (集合) 是為了自動去除重複，確保每個節點只出現一次
        for chain in all_chains:
            for node in chain:
                unique_nodes.add(node)
        
        self.nodes = list(unique_nodes) # 轉回列表
        self.node_to_idx = {node: i for i, node in enumerate(self.nodes)} # 製作字典：給每個節點一個編號
        print(f"資料集總節點數: {len(self.nodes)}")
        
        # 2. 切分訓練集與測試集
        # 防呆：如果資料少於 10 條，切分就沒意義了
        if len(all_chains) > 10:
            self.train_chains, self.test_chains = train_test_split(all_chains, test_size=test_size, random_state=42)
            print(f"資料切分完成: 總共 {len(all_chains)} 條 -> 訓練集 {len(self.train_chains)} 條 / 測試集 {len(self.test_chains)} 條")
        else:
            self.train_chains = all_chains
            self.test_chains = []
            print("資料過少，不進行切分，全部用於訓練。")
        return True

    def build_interaction_matrix(self):
        """只使用 [訓練集] 來構建交互矩陣"""
        num_nodes = len(self.nodes) #先算總共有多少節點
        self.interaction_matrix = np.zeros((num_nodes, num_nodes)) #建立全0的矩陣
        
        edge_count = 0 #用來統計有多少邊
        for chain in self.train_chains:
            if len(chain) < 2: continue # 防呆：如果這條 Chain 只有 1 個節點則跳過
            for i in range(len(chain) - 1):
                u, v = chain[i], chain[i+1] # 當 i=0 時，u="A", v="B", 當 i=1 時，u="B", v="C"
                u_idx = self.node_to_idx[u] #用上一段建立的字典 (node_to_idx) 把文字換成數字索引，例如u="A" -> u_idx=5
                v_idx = self.node_to_idx[v]
                self.interaction_matrix[u_idx][v_idx] = 1  # 例如：在矩陣的第 5 列、第 12 行的位置填上 1，代表A->B存在
                edge_count += 1 #邊數+1
                
        print(f"交互矩陣構建完成 (基於訓練集)。矩陣內有 {edge_count} 個正向連接。")

    def train(self):
        """執行矩陣分解訓練"""
        num_nodes = len(self.nodes)
        np.random.seed(42)
        
        # --- [核心概念：P 與 Q] ---
        # 我們要把巨大的 Interaction Matrix 分解成兩個瘦長的矩陣 P 和 Q。
        # P (Source Matrix): 代表每個節點作為「起點」時的特性 (例如：這個人喜歡什麼類型的電影？)
        # Q (Target Matrix): 代表每個節點作為「終點」時的特性 (例如：這個電影有哪些類型？)
        # num_factors (特徵數): 每個節點有多少個「隱藏屬性」。(例如 8 個)
        self.P = np.random.rand(num_nodes, self.num_factors) * 0.1  #在還沒看過資料前，先隨便猜（Random），而且要猜得保守一點
        self.Q = np.random.rand(num_nodes, self.num_factors) * 0.1
        
        print(f"開始訓練... (Factors={self.num_factors}, LR={self.learning_rate}, Weight={self.pos_weight})")
        
        # --- [正樣本加權 (Positive Weighting)] ---
        # 這是這支程式能救活 Name 模型的關鍵！
        # 先建立一個跟 Interaction Matrix 一樣大的矩陣，裡面全填 1.0
        weight_matrix = np.ones_like(self.interaction_matrix)
        # 把那些「原本有連接 (值為 1)」的位置，權重改成 pos_weight (例如 50.0)
        weight_matrix[self.interaction_matrix > 0] = self.pos_weight

        for i in range(self.num_iterations):  #開始訓練
            prediction_matrix = np.dot(self.P, self.Q.T)  # prediction_matrix 就是模型目前認為的「各節點連接分數」
            error = self.interaction_matrix - prediction_matrix  #誤差=真實答案 (interaction_matrix) - 預測值 (prediction_matrix)
            weighted_error = weight_matrix * error  # 如果是重要的連接 (正樣本) 預測錯了，誤差會被放大 50 倍，強迫模型重視。

            P_gradient = -2 * np.dot(weighted_error, self.Q) + 2 * self.regularization * self.P  #計算梯度，修正(錯多少*對手特徵值大小)並踩煞車，防止過擬合
            Q_gradient = -2 * np.dot(weighted_error.T, self.P) + 2 * self.regularization * self.Q
            
            P_gradient = np.clip(P_gradient, -5, 5)  #.clip是一個安全閥，強迫值在-5~5
            Q_gradient = np.clip(Q_gradient, -5, 5)

            self.P -= self.learning_rate * P_gradient #更新參數
            self.Q -= self.learning_rate * Q_gradient
            
            if i % 500 == 0:  #每500次看一下現在的誤差多少，確認有在變好
                loss = np.sum(weight_matrix * (error ** 2)) + self.regularization * (np.sum(self.P**2) + np.sum(self.Q**2)) #loss=error+lamda*複雜度懲罰
                print(f"Iteration {i}: Loss = {loss:.4f}")

        print("訓練完成。")
        #訓練結束後，P和Q已經是最完美的狀態了
        final_matrix = np.dot(self.P, self.Q.T) # 把它們乘起來，得到最終的預測分數矩陣
        self.recommendation_df = pd.DataFrame(final_matrix, index=self.nodes, columns=self.nodes) #加上直行橫列的標籤

    def get_transition_score(self, source_node, target_node):
        """獲取分數 (包含防呆)"""
        # 如果起點或終點不在我們的訓練資料(DataFrame)裡面，代表這是全新的東西。
        # 模型沒看過，所以給它 0 分 (安全起見)
        if source_node not in self.recommendation_df.index or target_node not in self.recommendation_df.columns:
            return 0.0
        
        # 2. 取得原始分數 (可能是 1.05)
        raw_score = self.recommendation_df.at[source_node, target_node]
        
        # 3. [修正] 修剪分數：超過 1.0 就當作 1.0
        # 這樣就能解決 "1.05" 看起來不合理的問題，同時保留模型的高信心判斷
        if raw_score > 1.0:
            return 1.0
            
        return raw_score

    def score_chain(self, chain_list, verbose=True):
        """對單一 Chain 評分"""
        if len(chain_list) < 2: return 0.0 # 防呆：長度小於 2 沒辦法形成連接，給 0 分
        scores = []
        
        if verbose:  #verbose是詳細輸出模式的開關
            print(f"\n--- 評估 Chain: {chain_list} ---")
            
        for i in range(len(chain_list) - 1):  #迴圈算分數，迴圈 1: 算 A -> B，迴圈 2: 算 B -> C
            score = self.get_transition_score(chain_list[i], chain_list[i+1])
            scores.append(score) #把分數存起來
            if verbose:
                print(f"Step '{chain_list[i]}' -> '{chain_list[i+1]}': {score:.4f}")
                
        avg_score = np.mean(scores) if scores else 0.0  #計算平均分
        if verbose:
            print(f">> Chain 平均分數: {avg_score:.4f}")
        return avg_score

    def evaluate_test_set(self):
        """
        [新功能] 評估測試集表現
        邏輯：測試集是模型沒看過的 Chain，如果模型學得好，這些 Chain 的平均分數應該要顯著高於 0。
        """
        print(f"\n==========================================")
        print(f"開始評估測試集 (共 {len(self.test_chains)} 條)")
        print(f"==========================================")
        
        total_score = 0
        valid_chains = 0
        
        # 為了避免輸出太多，只印出前 3 條範例
        for idx, chain in enumerate(self.test_chains):
            is_verbose = (idx < 3)  #只有前3條chain會開啟verbose
            score = self.score_chain(chain, verbose=is_verbose) #這裡呼叫score_chain算分
            total_score += score
            valid_chains += 1
            
        avg_test_score = total_score / valid_chains if valid_chains > 0 else 0  #計算所有測試資料的總平均
        print(f"\n>>> 測試集整體平均分數: {avg_test_score:.4f}")
        print("(若此分數接近 0.5~0.9，代表模型具備預測未知路徑的能力)")

    def batch_score_chains(self, list_of_chains):
        """
        [新功能] 批次評分 n 條 Chain
        :param list_of_chains: [[A,B,C], [D,E], ...]
        :return: 依照分數排序後的結果
        """
        print(f"\n==========================================")
        print(f"執行批次評分 (共 {len(list_of_chains)} 條)")
        print(f"==========================================")
        
        results = []
        for chain in list_of_chains:
            score = self.score_chain(chain, verbose=False) #呼叫score_chain算分
            results.append({"chain": str(chain), "score": score}) #把chain轉成字串，跟分數一起存到result
            
        # 轉成 DataFrame 並排序
        df_results = pd.DataFrame(results).sort_values(by="score", ascending=False)
        
        print("評分排名 (前 5 名):")
        print(df_results.head(5))
        return df_results

# ==========================================
# 主程式執行區
# ==========================================

if __name__ == "__main__":
    
    # 請依據上次測試結果最好的參數進行設定
    
    # --- Case 1: Type 模型 ---
    print("\n[Case 1: Type 模型]")
    type_model = ChainRecommender(
        json_file_path='All_chains_type_to_type.json', 
        num_factors=8,          
        learning_rate=0.005,     
        num_iterations=1000,
        regularization=0.2,      
        pos_weight=1.0           
    )
    if type_model.load_and_split_data(): # 1.讀檔+切分資料
        type_model.build_interaction_matrix() #2.建立矩陣
        type_model.train() #3.訓練模型
        
        type_model.evaluate_test_set() # 4. 考試(驗證測試集)
        
        # 測試新的chain
        new_chains = [
            ["trace", "custom", "trace", "function", "variable", "flow.end.current"], # 真實資料
            ["flow.begin", "variable", "flow.end.current"],   # 合理
            ["flow.begin", "flow.end.current", "flow.begin"]   # 不合理
        ]
        type_model.batch_score_chains(new_chains) #評分新的chain


    # --- Case 2: Name 模型 ---
    print("\n[Case 2: Name 模型]")
    name_model = ChainRecommender(
        json_file_path='All_chains_name_to_name.json',
        num_factors=60,         
        learning_rate=0.005,    
        num_iterations=2000,    
        regularization=0.1,     
        pos_weight=50.0         
    )
    if name_model.load_and_split_data():
        name_model.build_interaction_matrix()
        name_model.train()
        
        # 1. 驗證測試集
        name_model.evaluate_test_set()

        # 2. 批次評分 n 條 Chain
        input_n_chains = [
            ["輸入", "Echo", "前往 滿意度調查"],           # 高分候選
            ["輸入", "發票OCR", "前往 滿意度調查"],         # 低分候選
            ["判斷是否為測試模式", "查詢員工手機條碼", "結束目前的腳本"], # 真實資料
            ["主選單", "手機條碼申請教學", "回首頁"]         # 亂接的
        ]
        name_model.batch_score_chains(input_n_chains)