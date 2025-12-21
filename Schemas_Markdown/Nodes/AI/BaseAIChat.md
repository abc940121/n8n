# Base AI Chat

> 整合各 AI Chat 服務之基底屬性

* 目前支援的 AI 服務
    * [Azure Open AI](AzureOpenAIChat.md)
* 未來預計支援的 AI 服務
    * Open AI
    * Gemini
    * Ollama
    * ...



## ◆ Schema

繼承自 [Base Node](../BaseDialogNode.md)

| 屬性                   | 資料型態                                              | 必要屬性 | 描述                                                         | 支援變數 | 版本 |
| ---------------------- | ----------------------------------------------------- | -------- | ------------------------------------------------------------ | -------- | ---- |
| *Id*                   | string                                                | Y        | Node ID                                                      | **X**    | 1.0  |
| *Name*                 | string                                                | N        | Node 名稱                                                    | **X**    | 1.0  |
| *Description*          | string                                                | N        | Node 描述                                                    | **X**    | 1.0  |
| *Type*                 | string                                                | Y        | Node 類型，值為 `ai.aoai.chat`                               | **X**    | 1.0  |
| **ChatMessageHistory** | string                                                | N        | 先前的訊息，請指定一個變數名稱<br />變數值需為一個 [AIChatMessage](#-ai-chat-message)[] 格式 | **O**    | 2.10 |
| **ChatMessages**       | [AIChatMessage](#-ai-chat-message)[]                  | Y        | 最新的訊息 (Chat Completions API)                            | **X**    | 2.10 |
| *Actions*              | [NodeAction[]](../../Actions/NodeAction.md)           | Y        | Node 轉換行為 `(至少一個)`                                   | **X**    | 1.0  |
| *VariableActions*      | [VariableAction[]](../../Variables/VariableAction.md) | N        | 處理自訂變數                                                 | **X**    | 1.0  |

### ■ AI Chat Message

| 屬性    | 資料型態 | 必要屬性 | 描述                                                         | 支援變數 | 版本 |
| ------- | -------- | -------- | ------------------------------------------------------------ | -------- | ---- |
| Role    | string   | Y        | 角色<br />● `system` ：系統<br />● `user` ：使用者，其內容為使用者的訊息<br />● `assistant` ：Bot，其內容為 Bot 回覆的訊息<br />● `tool` ：Tool Calling，目前尚未支援 Tool Calling | **X**    | 2.10 |
| Content | string   | Y        | 訊息內容                                                     | **O**    | 2.1  |