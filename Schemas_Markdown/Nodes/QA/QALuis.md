# Microsoft LUIS.AI (QA)

> 使用 Microsoft LUIS 處理使用者的 QA



## ◆ Schema

繼承自 [Base QA](BaseQA.md)

| 屬性 | 資料型態 | 必要屬性 | 描述 | 支援變數 | 版本 |
| --------- | ------ | -------- | ------------ | --------- | --------- |
| *Id*        | string                                  | Y        | Node ID                                    | **X**                 | 1.0                      |
| *Name*      | string                                  | N        | Node 名稱                                           | **X**                         | 1.0                              |
| *Description* | string                                  | N        | Node 描述                                           | **X**                        | 1.0                             |
| *Type*      | string                                  | Y        | Node 類型，值為 `qa.luis`                      | **X**                         | 1.0                              |
| **IsPrompt** | boolean | Y | 是否提示或等候使用者輸入，預設值：true | **X** | 1.0 |
| **Prompt** | [MessageContent](../../Contents/MessageContent.md) | N | 顯示一些提示訊息 | **X** | 1.0 |
| **Region** | string | Y | Azure LUIS 地區 (服務的主機)，預設 Free Key為 `westus` | **O** | 1.0 |
| **ApplicationId** | string | Y        | LUIS Application Id | **O** | 1.0 |
| **SubscriptionKey** | string | Y | LUIS Subscription Key | **O** | 1.0 |
| *Actions*   | [NodeAction[]](../../Actions/NodeAction.md) | Y        | Node 轉換行為 `(至少一個)` | **X** | 1.0 |
| *VariableAcstions* | [VariableAction[]](../../Variables/VariableAction.md) | N | 處理自訂變數 | **X** | 1.0 |



## ◆ Node Lifecycle

### ■ 輸入

* **使用者訊息 (User Message)**
    * 文字訊息

* **節點設定 (Node Setting)**
    * **IsPrompt** ─ 是否要顯示提示訊息
    * **Prompt** ─ 發送給提示使用者的訊息
    * **Region** ─ LUIS 所佈署的 Region
    * **ApplicationId** ─ LUIS 的 App Id
    * **SubscriptionKey** ─ LUIS 的 LUIS Subscription Key  
    * **Actions** ─ 依據使用者輸入，轉換到對應的 Node
        * **`支援的 Node Action Rule`**
            *  [**Intent**](../../Rules/IntentRule.md)
            *  [**JsonPath**](../../Rules/JsonPathRule.md)
            *  [**Evaluate Expression**](../../Rules/EvaluateExpressionRule.md)
            *  [**Composite**](../../Rules/CompositeRule.md)

### ■ 節點運作

> 當啟用 Prompt 時，需要等候使用者輸入

* **OnBeginNode**  `(Turn 1)`
    * **啟用 Prompt 時**
        * **Step.1-1** 顯示 Prompt 訊息內容
        * **Step.1-2** 等候使用者提問
    * **未啟用 Prompt 時**
        * 直接從 `Turn 2` 開始
* **OnContinueNode** `(Turn 2)`
    * **Step.2-1** 取得使用的輸入
    * **Step.2-2** 透過 LUIS 判斷使用者的意圖
    * **Step.2-3** 依據使用者的意圖決定下一個要前往的 Dialog Node


### ■ 可使用的變數

* **在 Variable Action、Next Node Id 中可使用的變數**
    * [**自動變數**](../../Variables/Variable.md#-自動變數)
        * **`$.NodeOutput.Data.TopIntent.Intent`** 
            * 分數最高的意圖 `(建議 Trigger Type 為 after_node 時使用)`
        * **`$.NodeOutput.Data.TopIntent.Score`**
            * 分數最高的意圖的信心指數 `(建議 Trigger Type 為 after_node 時使用)`
        * **`$.NodeOutput.Data.Query`**
            * 使用者提問的內容 `(建議 Trigger Type 為 after_node 時使用)`
        * ...
    * [**自訂變數**](../../Variables/Variable.md#-自訂變數)
* **在 Node Action**
    * **`$.TopIntent.Intent`** ─ 分數最高的意圖
    * **`$.TopIntent.Score`** ─ 分數最高的意圖的信心指數 
    * **`$.Query`** ─ 使用者提問的內容
    * ...

```json
{
    "TopIntent": {
        "Intent": "None",
        "Score": 0.8
    },
    "Intents": [
        {
            "Intent": "None",
            "Score": 0.8
        }
    ],
    "Entities": [
        {
            "Entity": "",
            "Value": "",
            "Score": 0.8,
            "StartIndex": 0,
            "EndIndex": 0,
            "Resolution": {}
        }
    ],
    "Query": ""
}
```

### ■ 輸出

* **Node Output**

```json
{
    "Type": "NluResult",
	"Data": {
        "TopIntent": {
            "Intent": "None",
            "Score": 0.8
        },
        "Intents": [
            {
                "Intent": "None",
                "Score": 0.8
            }
        ],
        "Entities": [
            {
                "Entity": "",
                "Score": 0.8,
                "StartIndex": 0,
                "EndIndex": 0,
                "Resolution": {}
            }
        ],
        "Query": ""
    },
    "From": {
        "BotId": "",
        "FlowId": "",
        "FlowName": "",
        "NodeId": "",
        "NodeName": "",
        "NodeType": "qa.luis",
        "Date": ""
    }
}
```



## ◆ Example



```json
{
    "Id": "node_00001",
    "Name": "Help Intent",
    "Description": "",
    "Type": "qa.luis",
    "IsPrompt": false,
    "Region": "westus",
    "ApplicationId": "",
    "SubscriptionKey": "",
    "Actions": [
        {
            "Rules": [
                {
                    "Type": "intent",
                    "Intent": "Faq",
                    "Score": 0.4
                }
            ],
            "Type": "and",
            "Priority": 50,
            "NextNodeId": "node_00002"
        },
        {
            "Rules": [
                {
                    "Type": "intent",
                    "Intent": "Greeting",
                    "Score": 0.4
                }
            ],
            "Type": "and",
            "Priority": 50,
            "NextNodeId": "node_00003"
        },
        {
            "Rules": [
                {
                    "Type": "intent",
                    "Intent": "ApplyLeave",
                    "Score": 0.4
                }
            ],
            "Type": "and",
            "Priority": 50,
            "NextNodeId": "node_00004"
        },
        {
            "Rules": [],
            "Type": "otherwise",
            "Priority": 50,
            "NextNodeId": "node_00005"
        }
    ],
    "Prompt": null
}
```


