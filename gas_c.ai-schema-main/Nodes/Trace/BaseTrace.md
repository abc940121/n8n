# Base Trace Node

* **Trace Node** ─ 發送 Trace Activity 到 Chennel 端
* **Logger Node** ─ 寫 Log 到指定服務
* **Elk Node** ─ 發送資料到 ELK **`<計畫中>`**



## ◆ Schema

繼承自 [Base Node](../BaseDialogNode.md)

| 屬性              | 資料型態                                              | 必要屬性 | 描述                       | 支援變數 | 版本 |
| ----------------- | ----------------------------------------------------- | -------- | -------------------------- | -------- | ---- |
| *Id*              | string                                                | Y        | Node ID `(唯一)`           | **X**    | 1.1  |
| *Name*            | string                                                | N        | Node 名稱                  | **X**    | 1.1  |
| *Description*     | string                                                | N        | Node 描述                  | **X**    | 1.1  |
| *Type*            | string                                                | Y        | Node 類型                  | **X**    | 1.1  |
| *Actions*         | [NodeAction[]](../../Actions/NodeAction.md)           | Y        | Node 轉換行為 `(最多一個)` | **X**    | 1.1  |
| *VariableActions* | [VariableAction[]](../../Variables/VariableAction.md) | N        | 處理自訂變數               | **X**    | 1.1  |


