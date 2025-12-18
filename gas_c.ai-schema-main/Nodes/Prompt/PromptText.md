# Prompt Text

>  請求使用者的輸入，並且等候 User 答覆後，處理後續的事情



## ◆ Schema

繼承自 [Base Prompt](BasePrompt.md)

| 屬性  | 資料型態                                   | 必要屬性 | 描述                                                | 支援變數 | 版本    |
| ----------- | ------------------------------------------ | -------- | ------------------------------------------------------------ | ----------------- | ----------------- |
| *Id*        | string                                     | Y        | Node ID                                                      | **X** | 1.0     |
| *Name*      | string                                     | N        | Node 名稱                                                    | **X** | 1.0     |
| *Description* | string                                     | N        | Node 描述                                                    | **X** | 1.0     |
| *Type*      | string                                     | Y        | Node 類型，值為 `prompt.text`                                | **X** | 1.0     |
| **Prompt** | [MessageContent](../../Contents/MessageContent.md) | Y        | 提示使用者需要的內容，例如：文字、卡片 | **X** | 1.0 |
| **Retry** | [MessageContent](../../Contents/MessageContent.md) | N | 提示使用者輸入錯誤，未設定時沿用 **Prompt** 的設定 | **X** | 1.0 |
| **RetryMaxCount** | int | N | 重新輸入最大次數，預設為 `-1` (沒有限制次數)  **`<計畫中>`** | **X** | 1.1 |
| **Validator** | [RuleConditions](BasePrompt.md#-prompt-validator) | N        | 驗證使用者輸入的格式                                         | **X** | 1.0 |
| *Actions*   | [NodeAction[]](../../Actions/NodeAction.md) | N        | Node 轉換行為 | **X** | 1.0     |
| *VariableActions* | [VariableAction[]](../../Variables/VariableAction.md) | N | 處理自訂變數 | **X** | 1.0 |



## ◆ Node Lifecycle

### ■ 輸入

* **使用者訊息 (User Message)**
    * 文字訊息、卡片資料訊息、圖片或是附件檔

* **節點設定 (Node Setting)**
    * **Prompt** ─ 發送給使用者需要的內容
    * **Retry** ─ 提示使用者輸入錯誤，未設定時沿用 **Prompt** 的設定
    * **Validator** ─ 驗證使用者輸入，如果輸入錯誤需要要求使用者重新輸入一次，下一個 Node 還是自己
        * **`不支援的 Validator Rule`**
            * [**Intent**](../../Rules/IntentRule.md)
    * **Actions** ─ 依據使用者輸入，轉換到對應的 Node
        * **`不支援的 Node Action Rule`**
            * [**Intent**](../../Rules/IntentRule.md)

### ■ 節點運作

> 需要等候使用者輸入

* **OnBeginNode**  `(Turn 1)`
    * **Step.1-1** 顯示 Prompt 的內容
    * **Step.1-2** 等候使用者輸入
* **OnContinueNode** `(Turn 2)`
    * **Step.2-1** 取得使用的輸入
    * **Step.2-2** 使用 Validator 驗證使用者的輸入
        * **Step.2-2b** 輸入驗證不合法時，顯示 Retry 訊息內容
        * **Step.2-2b** 重新提問
    * **Step.2-3** 依據使用者的輸入決定下一個要前往的 Dialog Node


### ■ 可使用的變數

* **在 Validator Action 中可使用的變數**
    * **`$.Text`** ─ 使用者輸入的文字訊息
    * **`$.Value`** ─ 使用者點擊卡片按鈕的資料
    * **`$.Attachments`** ─ 使用者上傳圖片或是附件檔
* **在 Variable Action、Next Node ID 中可使用的變數**
    * [**自動變數**](../../Variables/Variable.md#-自動變數)
        * **`$.Message.Text`** ─ 使用者輸入的文字訊息 `(建議 Trigger Type 為 after_node 時使用)`
        * **`$.Message.Value`** ─ 使用者點擊卡片按鈕的資料 `(建議 Trigger Type 為 after_node 時使用)`
        * **`$.Message.Attachments`** ─ 使用者上傳圖片或是附件檔 `(建議 Trigger Type 為 after_node 時使用)`
    * [**自訂變數**](../../Variables/Variable.md#-自訂變數)
* **在 Node Action Rules 中可使用的變數**
    * **`$.Text`** ─ 使用者輸入的文字訊息
    * **`$.Value`** ─ 使用者點擊卡片按鈕的資料
    * **`$.Attachments`** ─ 使用者上傳圖片或是附件檔

```json
{
    "Text": "",
    "Value": {},
    "Attachments": [],
    
    "UserId": "",
    "UserName": "",
    "BotId": "",
    "ChannelId": "",
    "IsGroup": false,
    "ChannelData": {}
}
```

### ■ 輸出

* **Node Output 後可使用的變數**
    * 下一個節點取值
        * **`$.NodeOutput.Data.Text`** ─ 使用者輸入的文字訊息
        * **`$.NodeOutput.Data.Value`** ─ 使用者點擊卡片按鈕的資料
        * **`$.NodeOutput.Data.Attachments`** ─ 使用者上傳圖片或是附件檔
        * **`$.NodeOutput.From.NodeId`** ─ 從哪一個 Node 輸出
        * **`$.NodeOutput.From.FlowId`** ─ 從哪一個 Flow 輸出
        * ...

```json
{
    "Type": "UserMessage",
	"Data": {
        "Text": "",
        "Value": {},
        "Attachments": [],
        
        "UserId": "",
        "UserName": "",
        "BotId": "",
        "ChannelId": "",
        "IsGroup": false,
        "ChannelData": {}
    },
    "From": {
        "BotId": "",
        "FlowId": "",
        "FlowName": "",
        "NodeId": "",
        "NodeName": "",
        "NodeType": "prompt.text",
        "Date": ""
    }
}
```



## ◆ Example

```json
{
    "Id": "node_00002",
    "Name": "PromptTextNode",
    "Description": "",
    "Type": "prompt.text",
    "Prompt": {
        "Type": "text",
        "Text": "Continue? (Yes/No)"
    },
    "Retry": {
        "Type": "text",
        "Text": "Input error."
    },
    "Validator": {},
    "Actions": [
        {
            "Rules": [
                {
                    "Type": "text",
                    "Condition": "exactly",
                    "Value": "yes",
                    "IsNegative": false,
                    "IgnoreCase": true
                }
            ],
            "Type": "and",
            "Priority": 50,
            "NextNodeId": "node_00001"
        },
        {
            "Rules": [
                {
                    "Type": "text",
                    "Condition": "exactly",
                    "Value": "no",
                    "IsNegative": false,
                    "IgnoreCase": true
                }
            ],
            "Type": "and",
            "Priority": 50,
            "NextNodeId": "node_00003"
        },
        {
            "Rules": [],
            "Type": "otherwise",
            "Priority": 25,
            "NextNodeId": ""
        }
    ]
}
```

