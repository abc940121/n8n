# QA

* **QA** ─ Bot 被動等候 User 提問，並答覆 User 的問題 
  * [Regex](QARegex.md)
  * [LUIS.AI](QALuis.md)
  * [GSS.AI](QAGssAI.md)
  * [GSS.QA](QAGssQA.md)

## ◆ Schema

繼承自 [Base Node](../BaseDialogNode.md)

| 屬性              | 資料型態                                              | 必要屬性 | 描述                       | 支援變數 | 版本 |
| ----------------- | ----------------------------------------------------- | -------- | -------------------------- | -------- | ---- |
| *Id*              | string                                                | Y        | Node ID `(唯一)`           | **X**    | 1.0  |
| *Name*            | string                                                | N        | Node 名稱                  | **X**    | 1.0  |
| *Description*     | string                                                | N        | Node 描述                  | **X**    | 1.0  |
| *Type*            | string                                                | Y        | Node 類型                  | **X**    | 1.0  |
| **Prompt**        | [MessageContent](../../Contents/MessageContent.md)    | N        | 提示使用者輸入問題         | **X**    | 1.0  |
| **IsPrompt**      | boolean                                               | Y        | 是否提示或等候使用者輸入   | **X**    | 1.0  |
| *Actions*         | [NodeAction[]](../../Actions/NodeAction.md)           | Y        | Node 轉換行為 `(至少一個)` | **X**    | 1.0  |
| *VariableActions* | [VariableAction[]](../../Variables/VariableAction.md) | N        | 處理自訂變數               | **X**    | 1.0  |



