
# -*- coding: utf-8 -*-
"""
Chain Reasoner (Type-level)
- Train a link predictor on consecutive Type transitions from observed chains
- Score an arbitrary candidate chain by aggregating predicted edge strengths
"""

import json
import numpy as np
import pandas as pd
import networkx as nx
from typing import List, Tuple

# ============================
# Config
# ============================
NUM_FACTORS = 48
LEARNING_RATE = 0.004
NUM_ITERATIONS = 1200
REGULARIZATION = 0.05


def load_chains(path: str) -> List[List[str]]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["chains"]


def chains_to_weighted_edges(chains: List[List[str]]) -> Tuple[nx.DiGraph, dict]:
    """
    Build a directed multigraph aggregated as a DiGraph with frequency weights.
    Returns (G, freq) where freq[(u,v)] = count
    """
    G = nx.DiGraph()
    freq = {}
    for ch in chains:
        # expand simple consecutive pairs
        for i in range(len(ch) - 1):
            u, v = ch[i], ch[i+1]
            freq[(u, v)] = freq.get((u, v), 0) + 1
    for (u, v), w in freq.items():
        G.add_edge(u, v, weight=float(w))
    return G, freq


def build_interaction_matrix(G: nx.DiGraph, freq: dict) -> Tuple[np.ndarray, list]:
    nodes = sorted(list(G.nodes()))
    n = len(nodes)
    M = np.zeros((n, n), dtype=float)
    for (u, v), w in freq.items():
        i, j = nodes.index(u), nodes.index(v)
        M[i, j] = w  # frequency as weight
    # normalize to [0,1] by max (avoid 0 if empty)
    if M.max() > 0:
        M = M / M.max()
    return M, nodes


def compute_weighted_loss(interaction_matrix, P, Q, reg):
    prediction = P @ Q.T
    error = interaction_matrix - prediction
    weight = (interaction_matrix > 0).astype(float) * 2.0 + 1.0  # known edges 2x weight
    loss = np.sum(weight * (error ** 2))
    loss += reg * (np.sum(P**2) + np.sum(Q**2))
    return loss


def train_mf(M, k=NUM_FACTORS, lr=LEARNING_RATE, steps=NUM_ITERATIONS, reg=REGULARIZATION, seed=42):
    rng = np.random.default_rng(seed)
    n = M.shape[0]
    P = rng.random((n, k)) * 0.01
    Q = rng.random((n, k)) * 0.01
    for it in range(steps):
        pred = P @ Q.T
        error = M - pred
        weight = (M > 0).astype(float) * 2.0 + 1.0
        # gradients
        P_grad = -2 * (weight * error) @ Q + 2 * reg * P
        Q_grad = -2 * (weight * error).T @ P + 2 * reg * Q
        P -= lr * P_grad
        Q -= lr * Q_grad
        if it % 100 == 0 or it == steps-1:
            print(f"Iter {it}/{steps}: loss={compute_weighted_loss(M, P, Q, reg):.4f}")
    return P, Q


class ChainReasoner:
    def __init__(self, chains: List[List[str]]):
        self.chains = chains
        self.G, self.freq = chains_to_weighted_edges(chains)
        self.M, self.nodes = build_interaction_matrix(self.G, self.freq)
        if len(self.nodes) == 0:
            raise ValueError("No nodes found from chains.")
        self.P, self.Q = train_mf(self.M)

        # Prediction matrix in [0,1]-ish range after MF; clip to be safe
        self.pred = np.clip(self.P @ self.Q.T, 0.0, 1.0)
        self.pred_df = pd.DataFrame(self.pred, index=self.nodes, columns=self.nodes)

    def edge_score(self, u: str, v: str) -> float:
        if u not in self.nodes or v not in self.nodes:
            return 0.0
        return float(self.pred_df.loc[u, v])

    def score_chain(self, chain: List[str], aggregate: str = "geom") -> dict:
        """
        Score a candidate chain by combining edge scores.
        aggregate:
          - 'mean': arithmetic mean of edge scores
          - 'min':  minimum edge score (bottleneck)
          - 'geom': geometric mean (penalizes small links)
        Returns dict with per-edge scores and overall score.
        """
        edges = [(chain[i], chain[i+1]) for i in range(len(chain)-1)]
        edge_scores = [self.edge_score(u,v) for (u,v) in edges]
        # Avoid zero for geometric mean; add epsilon
        eps = 1e-8
        if len(edge_scores) == 0:
            overall = 0.0
        else:
            if aggregate == "mean":
                overall = float(np.mean(edge_scores))
            elif aggregate == "min":
                overall = float(np.min(edge_scores))
            else:
                overall = float(np.exp(np.mean(np.log(np.array(edge_scores) + eps))))

        return {
            "chain": chain,
            "edges": [{"u": u, "v": v, "score": s} for (u,v), s in zip(edges, edge_scores)],
            "overall": overall
        }


def main():
    # Load observed chains (type-level)
    CHAINS_PATH = r"C:\Users\User\Desktop\C.ai_project\All_chains_name_to_name.json"
    with open(CHAINS_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    chains = data["chains"]

    cr = ChainReasoner(chains)

    # Demo chains
    demo1 = ["輸入", "Echo", "填寫滿意度調查"]
    demo2 = ["設定文章摘要初始值", "判斷是否已有文章", "功能說明", "偵測文章語系", "判斷IM", "文章摘要設定(ac)", "是否摘要其他文章"]
    demo3 = ["呼叫語音轉文字API", "API是否呼叫成功", "API呼叫失敗"]
    

    for ch in [demo1, demo2, demo3]:
        res = cr.score_chain(ch, aggregate="geom")
        print("Chain:", res["chain"])
        print("Edges:", res["edges"])
        print("Overall (geom):", f"{res['overall']:.4f}")
        print("-"*60)

    # Save the prediction matrix
    out_pred = r"C:\Users\User\Desktop\C.ai_project\output.csv"
    cr.pred_df.to_csv(out_pred, encoding="utf-8-sig")
    print("Saved transition score matrix to:", out_pred)


if __name__ == "__main__":
    main()
