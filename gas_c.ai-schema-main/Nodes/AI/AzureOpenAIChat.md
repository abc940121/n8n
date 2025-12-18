# Azure Open AI Chat

> 整合 Azure Open AI Chat Completions API



## ◆ Schema

繼承自 [Base AI Node](BaseAIChat.md)

| 屬性                 | 資料型態                                              | 必要屬性 | 描述                                                         | 支援變數 | 版本 |
| -------------------- | ----------------------------------------------------- | -------- | ------------------------------------------------------------ | -------- | ---- |
| *Id*                 | string                                                | Y        | Node ID                                                      | **X**    | 1.0  |
| *Name*               | string                                                | N        | Node 名稱                                                    | **X**    | 1.0  |
| *Description*        | string                                                | N        | Node 描述                                                    | **X**    | 1.0  |
| *Type*               | string                                                | Y        | Node 類型，值為 `ai.aoai.chat`                               | **X**    | 1.0  |
| **Endpoint**         | AOAIChatEndpoint                                      | Y        | Azure Open AI Endpoint 設定                                  | **X**    | 2.10 |
| **Options**          | AOAIChatOptions                                       | N        | Chat Completions API 除了訊息之外的選項，[文件參考](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference#completions) | **X**    | 2.10 |
| *ChatMessageHistory* | string                                                | N        | 先前的訊息，請指定一個變數名稱<br />變數值需為一個 [AIChatMessage](BaseAIChat.md#-ai-chat-message)[] 格式 | **O**    | 2.10 |
| *ChatMessages*       | [AIChatMessage](BaseAIChat.md#-ai-chat-message)[]     | Y        | 最新的訊息 (Chat Completions API)                            | **X**    | 2.10 |
| *Actions*            | [NodeAction[]](../../Actions/NodeAction.md)           | Y        | Node 轉換行為 `(至少一個)`                                   | **X**    | 1.0  |
| *VariableActions*    | [VariableAction[]](../../Variables/VariableAction.md) | N        | 處理自訂變數                                                 | **X**    | 1.0  |

### ■ `AOAIChatEndpoint` (Azure Open AI Endpoint)

| 屬性         | 資料型態 | 必要屬性 | 描述                      | 支援變數 | 版本 |
| ------------ | -------- | -------- | ------------------------- | -------- | ---- |
| Url          | string   | Y        | Endpoint Url              | **O**    | 2.10 |
| DeploymentId | string   | Y        | 在 Azure 中部署的模型名稱 | **O**    | 2.10 |
| ApiKey       | string   | Y        | Azure API Key             | **O**    | 2.10 |

### ■ `AOAIChatOptions` (Azure Open AI Chat Completions Options)

| 屬性      | 資料型態 | 必要屬性 | 描述                                           | 支援變數 | 版本 |
| --------- | -------- | -------- | ---------------------------------------------- | -------- | ---- |
| Stream    | boolean  | Y        | 是否啟用 Chat Stream，預設值：`true`           | **O**    | 2.10 |
| MaxTokens | int      | N        | 最大使用的 Token 數，預設值：`16` (官方預設值) | **O**    | 2.10 |



## ◆ Node Lifecycle

### ■ 輸入

* **使用者訊息 (User Message)**
    * 無
* **節點設定 (Node Setting)**
    * **Endpoint** ─ Azure Open AI Endpoint 參數設定
    * **Chat Message History**
        * 先前的對話內容，為一個變數
        * 變數值為一個 ` AIChatMessage[] `，內容包含系統訊息、使用者的訊息和 Bot 回覆的訊息
    * **Chat Messages**
        * 最新的訊息，可以包含系統訊息、使用者的訊息
        * 在前一個節點需要搭配 Prompt Text 對話節點取得使用者輸入的訊息
    * **Options** ─ 其他可選的參數設定

### ■ 節點運作

> * **不會等候使用者輸入，需要搭配 Prompt Text 對話節點**
> * **強烈建議需要留意設計時需要留意無窮迴圈，以避免服務的費用暴增**

* **OnBeginNode**  `(Turn 1)`
    * **Step.1** 收集先前的對話內容 (**Chat Message History**) 與最新的訊息 (**Chat Messages**)
    * **Step.2** 發送 Azure Open AI Chat Completions API
    * **Step.3** 顯示 Azure Open AI Chat Completions API 回傳的文字結果

### ■ 可使用的變數

* **在 Variable Action、Next Node ID 中可使用的變數**
    * [**自動變數**](../../Variables/Variable.md#-自動變數)
    * [**自訂變數**](../../Variables/Variable.md#-自訂變數)
* **在 Node Action Rule 中可使用的變數**
    * **`$[i].Role`** ─ 角色
    * **`$[i].Content`** ─ 訊息內容

```json
[
    {
        "Role": "user",
        "Content": "1+1=?"
    },
    {
        "Role": "assistant",
        "Content": "2"
    }
]
```

### ■ 輸出

* **Node Output 後可使用的變數**
    * 下一個節點取值
        * **`$.NodeOutput.Data`** ─ 對話內容，Json 物件 (JToken)
        * **`$.NodeOutput.Data[i].Role`** ─ 角色
        * **`$.NodeOutput.Data[i].Content`** ─ 訊息內容

```json
{
	"Data": [
        {
            "Role": "user",
            "Content": "1+1=?"
        },
        {
            "Role": "assistant",
            "Content": "2"
        }
    ],
    "From": {
        "BotId": "",
        "FlowId": "",
        "FlowName": "",
        "NodeId": "",
        "NodeName": "",
        "NodeType": "request.raw.json",
        "Date": ""
    }
}
```



## ◆ Example

### ■ Azure Open AI Chat (獨立的新對話)

* `node_00001` ：搭配 Prompt Text 對話節點，提供使用者輸入想要問的問題，如範例的節點 
* `node_00002` ：將使用者在上個節點的輸入問題發送到 Azure Open AI Chat API，並且顯示其結果

```json
[
    {
        "Id": "node_00001",
        "Name": "Prompt Message",
        "Description": "Prompt",
        "Type": "prompt.text",
        "Prompt": {
            "Type": "text",
            "Text": "請輸入您的問題"
        },
        "Actions": [
            {
                "Rules": [],
                "Type": "none",
                "Priority": 50,
                "NextNodeId": "node_00002"
            }
        ],
        "VariableActions": []
    },
    {
        "Id": "node_00002",
        "Name": "QA with Regex",
        "Description": "",
        "Type": "ai.aoai.chat",
        "Endpoint": {
            "Url": "https://your-resource-name.openai.azure.com/",
            "DeploymentId": "your-model-name",
            "ApiKey": "<Your API Key>"
        },
        "ChatMessageHistory": "",
        "ChatMessages": [
            {
                "Role": "user",
                "Content": "{{$.NodeOutput.Data.Text}}"
            }
        ],
        "Options": {
            "Stream": true
        },
        "Actions": [
            {
                "Rules": [],
                "Type": "none",
                "Priority": 50,
                "NextNodeId": "node_00001"
            }
        ],
        "VariableActions": []
    }
]
```



---

### ■ Azure Open AI Chat (沿續先前的對話)

* `node_00001` ：搭配 Prompt Text 對話節點，提供使用者輸入想要問的問題，如範例的節點 
* `node_00002` ：將使用者在上個節點的輸入問題發送到 Azure Open AI Chat API，並且顯示其結果
    * 在對話節點後將輸入的結果 `$.NodeOutput.Data` 存入到一個變數，提供下一輪對話使用
        * 變數和變數名稱請自行管理
    * `ChatMessageHistory`：指定一個變數，變數值為先前對話的內容
        * 透過這樣的方式達到延續先前的對話的效果

```json
[
    {
        "Id": "node_00001",
        "Name": "Prompt Message",
        "Description": "Prompt",
        "Type": "prompt.text",
        "Prompt": {
            "Type": "text",
            "Text": "請輸入您的問題"
        },
        "Actions": [
            {
                "Rules": [],
                "Type": "none",
                "Priority": 50,
                "NextNodeId": "node_00002"
            }
        ],
        "VariableActions": []
    },
    {
        "Id": "node_00002",
        "Name": "QA with Regex",
        "Description": "",
        "Type": "ai.aoai.chat",
        "Endpoint": {
            "Url": "https://your-resource-name.openai.azure.com/",
            "DeploymentId": "your-model-name",
            "ApiKey": "<Your API Key>"
        },
        "ChatMessageHistory": "$.FlowVariables.ChatMessageHistory",
        "ChatMessages": [
            {
                "Role": "user",
                "Content": "{{$.NodeOutput.Data.Text}}"
            }
        ],
        "Options": {
            "ChatStream": true
        },
        "Actions": [
            {
                "Rules": [],
                "Type": "none",
                "Priority": 50,
                "NextNodeId": "node_00001"
            }
        ],
        "VariableActions": [
            {
                "Type": "variable.set",
                "TriggerType": "after_node",
                "Variable": "ChatMessageHistory",
                "VariableType": "flow",
                "AssignValue": "$.NodeOutput.Data",
                "AssignValueType": "variable"
            }
        ]
    }
]
```



---

#### ■ Azure Open AI Chat 搭配 Tool calling

> 尚未提供支援





