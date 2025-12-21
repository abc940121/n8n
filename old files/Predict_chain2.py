# -*- coding: utf-8 -*-
"""
基於矩陣分解的 Chain 評分與生成模型
Modified based on CausalInference_matrix_factorization_recommendation.py
"""

import numpy as np
import pandas as pd
import networkx as nx
import json
import os

class ChainRecommender:
    def __init__(self, json_file_path, num_factors=10, learning_rate=0.001, num_iterations=1000, regularization=0.1, pos_weight=1.0):
        """
        初始化推薦器
        :param json_file_path: JSON 檔案路徑
        :param num_factors: 潛在特徵數量 (Type 檔建議小一點, Name 檔建議大一點)
        :param learning_rate: 學習率
        :param num_iterations: 迭代次數
        :param regularization: 正則化參數
        """
        self.json_file_path = json_file_path
        self.num_factors = num_factors
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.regularization = regularization
        self.pos_weight = pos_weight  # 新增：動態權重參數
        
        # 內部變數
        self.G = None
        self.nodes = []
        self.node_to_idx = {}
        self.interaction_matrix = None
        self.P = None # User/Source matrix
        self.Q = None # Item/Target matrix
        self.recommendation_df = None

    def load_and_build_graph(self):
        """讀取 JSON 並構建 Knowledge Graph (Triples: A -> next_step -> B)"""
        print(f"正在讀取檔案: {self.json_file_path} ...")
        
        try:
            with open(self.json_file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f"錯誤: 找不到檔案 {self.json_file_path}")
            return False

        chains = data.get("chains", [])
        self.G = nx.DiGraph()
        triples_count = 0
        
        # 滑動視窗：將 Chain 拆解為 (Current, next_step, Next)
        for chain in chains:
            # 確保 chain 至少有兩個節點才能構成邊
            if len(chain) < 2:
                continue
            for i in range(len(chain) - 1):
                self.G.add_edge(chain[i], chain[i+1], relation="next_step")
                triples_count += 1
        
        print(f"圖構建完成。節點數: {len(self.G.nodes)}, 邊數: {triples_count}")
        self.nodes = list(self.G.nodes)
        self.node_to_idx = {node: i for i, node in enumerate(self.nodes)}
        return True

    def build_interaction_matrix(self):
        num_nodes = len(self.nodes)
        self.interaction_matrix = np.zeros((num_nodes, num_nodes))
        for source, target in self.G.edges():
            self.interaction_matrix[self.node_to_idx[source]][self.node_to_idx[target]] = 1 # 若有連接則設為 1  
        print("交互矩陣構建完成。")

    def train(self):
        """執行矩陣分解訓練 (梯度下降)"""
        num_nodes = len(self.nodes)
        np.random.seed(42) # 固定種子以重現結果
        self.P = np.random.rand(num_nodes, self.num_factors) * 0.1
        self.Q = np.random.rand(num_nodes, self.num_factors) * 0.1
        
        print(f"開始訓練... (Factors={self.num_factors}, LR={self.learning_rate}, Weight={self.pos_weight})")
        # 預先建立權重矩陣 (避免在迴圈中重複建立，提升效能)
        weight_matrix = np.ones_like(self.interaction_matrix)
        weight_matrix[self.interaction_matrix > 0] = self.pos_weight
        for i in range(self.num_iterations):
            prediction_matrix = np.dot(self.P, self.Q.T)
            error = self.interaction_matrix - prediction_matrix
            weighted_error = weight_matrix * error

            P_gradient = -2 * np.dot(weighted_error, self.Q) + 2 * self.regularization * self.P
            Q_gradient = -2 * np.dot(weighted_error.T, self.P) + 2 * self.regularization * self.Q
            
            # [修正關鍵] 梯度裁減 (Gradient Clipping)：防止梯度爆炸導致 NaN
            P_gradient = np.clip(P_gradient, -5, 5)
            Q_gradient = np.clip(Q_gradient, -5, 5)

            # 更新參數
            self.P -= self.learning_rate * P_gradient
            self.Q -= self.learning_rate * Q_gradient
            
            if i % 200 == 0:
                # 只計算有連接部分的權重誤差 (Weighted Loss)
                loss = np.sum(weight_matrix * (error ** 2)) + self.regularization * (np.sum(self.P**2) + np.sum(self.Q**2))
                print(f"Iteration {i}: Loss = {loss:.4f}")
        print("訓練完成。")
        final_matrix = np.dot(self.P, self.Q.T)
        self.recommendation_df = pd.DataFrame(final_matrix, index=self.nodes, columns=self.nodes)

    def get_transition_score(self, source_node, target_node):
        """獲取兩個節點間的轉換分數 (A -> B 的可能性)"""
        if source_node not in self.node_to_idx or target_node not in self.node_to_idx:
            return 0.0 # 若節點未曾出現在訓練資料中，回傳 0
        return self.recommendation_df.at[source_node, target_node]

    def score_chain(self, chain_list):
        """
        [核心功能] 對一條 Chain 進行評分
        邏輯：將 Chain 拆解為多個步驟，計算每一步的分數，最後取平均。
        """
        if len(chain_list) < 2:
            return 0.0 
        scores = []
        print(f"\n--- 評估 Chain: {chain_list} ---")
        for i in range(len(chain_list) - 1):
            score = self.get_transition_score(chain_list[i], chain_list[i+1])
            scores.append(score)
            print(f"Step '{chain_list[i]}' -> '{chain_list[i+1]}': {score:.4f}")    
        avg_score = np.mean(scores) if scores else 0.0
        print(f">> Chain 平均分數: {avg_score:.4f}")
        return avg_score

    def generate_next_steps(self, current_node, top_k=5):
        if current_node not in self.recommendation_df.index:
            print(f"節點 '{current_node}' 不在知識圖譜中。")
            return []
            
        # 取得該列所有分數，並排序
        predictions = self.recommendation_df.loc[current_node].sort_values(ascending=False).head(top_k)
        print(f"\n基於 '{current_node}' 推薦的下一步:")
        for node, score in predictions.items():
            print(f" -> {node} (Score: {score:.4f})")            
        return predictions.index.tolist()

# ==========================================
# 主程式執行區
# ==========================================

if __name__ == "__main__":
    
    # --- 案例 1: 針對 "Type" 資料 (All_chains_type_to_type.json) ---
    # Type 的節點少，關係密集，可以使用較小的 NUM_FACTORS
    print("==========================================")
    print("CASE 1: 訓練 Type 模型")
    print("==========================================")
    
    type_model = ChainRecommender(
        json_file_path='All_chains_type_to_type.json', # 請確保檔案在同一目錄下
        num_factors=8,          # Type 類別較少，不需要太大的維度
        learning_rate=0.005,     # 可以稍微大一點
        num_iterations=1000,
        regularization=0.2,
        pos_weight=1.0
    )
    
    if type_model.load_and_build_graph():
        type_model.build_interaction_matrix()
        type_model.train()
        type_model.score_chain(["flow.begin", "prompt.text", "sending.message"])
        type_model.generate_next_steps("prompt.text")

    # --- 案例 2: 針對 "Name" 資料 (All_chains_name_to_name.json) ---
    # Name 的節點多，矩陣稀疏，需要較大的 NUM_FACTORS 來捕捉特徵
    print("\n==========================================")
    print("CASE 2: 訓練 Name 模型")
    print("==========================================")
    
    name_model = ChainRecommender(
        json_file_path='All_chains_name_to_name.json',
        num_factors=60,         # Name 節點多，增加特徵維度
        learning_rate=0.005,    
        num_iterations=2000,    # 增加迭代次數以確保收斂
        regularization=0.1,     # 增加正則化防止過擬合
        pos_weight=50.0
    )
    
    if name_model.load_and_build_graph():
        name_model.build_interaction_matrix()
        name_model.train()
        name_model.score_chain(["輸入", "Echo", "前往 滿意度調查"])
        name_model.score_chain(["輸入", "發票OCR", "前往 滿意度調查"])
        name_model.generate_next_steps("輸入")
        