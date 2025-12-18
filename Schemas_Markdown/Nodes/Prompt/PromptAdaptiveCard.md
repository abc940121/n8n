# Prompt Adaptive Card

## **(變更為 [Prompt Card](PromptCard.md))**



> 請求使用者的輸入 Adaptive Card 的回傳值



## ◆ Schema

繼承自 [Base Prompt](BasePrompt.md)

| 屬性      | 資料型態                                              | 必要屬性 | 描述                                      | 支援變數  | 版本    |
| --------------- | ----------------------------------------------------- | -------- | -------------------------------------------------- | ----------------- | --------------- |
| *Id*            | string                                                | Y        | Node ID                                            | **X** | 1.0     |
| *Name*          | string                                                | N        | Node 名稱                                          | **X** | 1.0     |
| *Description*   | string                                                | N        | Node 描述                                          | **X** | 1.0     |
| *Type*          | string                                                | Y        | Node 類型，值為 `prompt.adaptivecard`      | **X** | 1.0     |
| **Prompt**      | [MessageContent](../../Contents/MessageContent.md)    | Y        | 提示使用者需要的內容，例如：卡片                   | **X** | 1.0     |
| **Retry**       | [MessageContent](../../Contents/MessageContent.md)    | N        | 提示使用者輸入錯誤，未設定時沿用 **Prompt** 的設定 | **X** | 1.0     |
| **RetryMaxCount** | iny | N | 重新輸入最大次數，預設為 `-1` (沒有限制次數)  **`<計畫中>`** | **X** | 1.1 |
| **Validator**   | [RuleConditions](BasePrompt.md#-prompt-validator) | N        | 驗證使用者輸入的格式                          | **X** | 1.0 |
| *Actions*       | [NodeAction[]](../../Actions/NodeAction.md)           | N        | Node 轉換行為             | **X** | 1.0     |
| *VariableActions* | [VariableAction[]](../../Variables/VariableAction.md) | N | 處理自訂變數 | **X** | 1.0 |



## ◆ Node Lifecycle

### ■ 輸入

* **使用者訊息 (User Message)**
    * 文字訊息、卡片資料訊息、圖片或是附件檔

* **節點設定 (Node Setting)**
    * **Prompt** ─ 發送給使用者需要的內容
    * **Retry** ─ 提示使用者輸入錯誤，未設定時沿用 **Prompt** 的設定
    * **Validator** ─ 驗證使用者輸入，如果輸入錯誤需要要求使用者重新輸入一次，下一個 Node 還是自己
        * **`支援的 Validator Rule`**
            *  [**JsonPath**](../../Rules/JsonPathRule.md)
            * [**Evaluate Expression**](../../Rules/EvaluateExpressionRule.md)
            * [**Composite**](../../Rules/CompositeRule.md)
    * **Actions** ─ 依據使用者輸入，轉換到對應的 Node
        * **`支援的 Node Action Rule`**
            *  [**JsonPath**](../../Rules/JsonPathRule.md)
            * [**Evaluate Expression**](../../Rules/EvaluateExpressionRule.md)
            * [**Composite**](../../Rules/CompositeRule.md)

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
        "NodeType": "prompt.adaptive",
        "Date": ""
    }
}
```



## ◆ Example



### ■ PromptValidator Rule 和 NodeAction Rule 的設定

* **Rule Type 只支援：**
    * **[JsonPath](../../Rules/JsonPathRule.md)**  
    * **[Evaluate Expression](../../Rules/EvaluateExpressionRule.md)**
    * **[Composite](../../Rules/CompositeRule.md)**
* **卡片回傳文字訊息 (Activity.Text)**
  * Root Object 為 Activity，因此透過 $.Text 取得 Activity.Text 的目標
  * 與PromptText 的差異點是 PromptText 不需指定目標，其目標一律為 Activity.Text

```json
{
    "Type": "jsonpath",
    "SubRule": {
        "Type": "text",
        "Condition": "exactly",
        "Value": "1",
        "IsNegative": false,
        "IgnoreCase": true
    },
    "JsonPath": "$.Text"
}
```



* **卡片回傳物件訊息 (Activity.Value)**
  * Root Object 為 Activity，因此透過 $.Value 取得 Activity.Value 的目標

```json
{
    "Type": "jsonpath",
    "SubRule": {
        "Type": "text",
        "Condition": "exactly",
        "Value": "Send",
        "IsNegative": false,
        "IgnoreCase": true
    },
    "JsonPath": "$.Value.Action"
}
```



### ■ 完整範例



```json
{
    "Id": "node_00001",
    "Name": "Adaptive Card",
    "Description": "",
    "Type": "prompt.adaptivecard",
    "Prompt": {
        "Type": "adaptive.card",
        "Text": "請說出你要我做什麼?",
        "Content": "{\"type\":\"AdaptiveCard\",\"body\":[{\"type\":\"Container\",\"items\":[{\"type\":\"TextBlock\",\"text\":\"Hi {{$.Conversation.UserName}}\"}]}],\"actions\":[{\"type\":\"Action.Submit\",\"title\":\"第一個選項 (Text)\",\"data\":\"1\"},{\"type\":\"Action.Submit\",\"title\":\"第二個選項 (Text)\",\"data\":\"2\"},{\"type\":\"Action.Submit\",\"title\":\"第三個選項 (Value)\",\"data\":{\"Action\":\"Quit\"}}],\"$schema\":\"http://adaptivecards.io/schemas/adaptive-card.json\",\"version\":\"1.0\"}"
    },
    "Retry": 3,
    "Validator": {
        "Rules": [],
        "Type": "and"
    },
    "Actions": [
        {
            "Type": "and",
            "Rules": [
                {
                    "Type": "jsonpath",
                    "Rule": {
                        "Type": "text",
                        "Condition": "exactly",
                        "Value": "1",
                        "IsNegative": false,
                        "IgnoreCase": true
                    },
                    "JsonPath": "$.Text"
                }
            ],
            "Priority": 50,
            "NextNodeId": "node_00002"
        },
        {
            "Type": "and",
            "Rules": [
                {
                    "Type": "jsonpath",
                    "Rule": {
                        "Type": "text",
                        "Condition": "exactly",
                        "Value": "2",
                        "IsNegative": false,
                        "IgnoreCase": true
                    },
                    "JsonPath": "$.Text"
                }
            ],
            "Priority": 50,
            "NextNodeId": "node_00002"
        },
        {
            "Type": "and",
            "Rules": [
                {
                    "Type": "jsonpath",
                    "Rule": {
                        "Type": "text",
                        "Condition": "exactly",
                        "Value": "Quit",
                        "IsNegative": false,
                        "IgnoreCase": true
                    },
                    "JsonPath": "$.Value.Action"
                },
                {
                    "Type": "jsonpath",
                    "Rule": {
                        "Type": "text",
                        "Condition": "exactly",
                        "Value": "3",
                        "IsNegative": false,
                        "IgnoreCase": true
                    },
                    "JsonPath": "$.Text"
                }
            ],
            "Priority": 50,
            "NextNodeId": "node_00003"
        },
        {
            "Type": "none",
            "Rules": [],
            "Priority": 50,
            "NextNodeId": "node_00004"
        }
    ]
}
```

