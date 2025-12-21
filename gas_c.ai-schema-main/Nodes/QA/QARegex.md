# Regular Expression (QA)

> 使用 Regular Expression 處理使用者的 QA



## ◆ Schema

繼承自 [Base QA](BaseQA.md)

| 屬性    | 資料型態                                        | 必要屬性 | 描述                                       | 支援變數 | 版本 |
| ------------- | ----------------------------------------------- | -------- | --------------------------------------------------- | ----------- | ----------- |
| *Id*          | string                                          | Y        | Node ID                                    | **X** | 1.0 |
| *Name*        | string                                          | N        | Node 名稱                                           | **X** | 1.0 |
| *Description* | string                                          | N        | Node 描述                                           | **X** | 1.0 |
| *Type*        | string                                          | Y        | Node 類型，值為 `qa.regex`                          | **X** | 1.0 |
| **IsPrompt** | boolean | Y | 是否提示或等候使用者輸入，預設值：true | **X** | 1.0 |
| **Prompt** | [MessageContent](../../Contents/MessageContent.md) | N        | 顯示一些提示訊息                                    | **X** | 1.0 |
| **Models**    | [RegexModel[]](#-regexmodel)                   | Y        | Regex Model                                         | **X** | 1.0 |
| *Actions*     | [NodeAction[]](../../Actions/NodeAction.md)     | Y        | Node 轉換行為 `(至少一個)` | **X** | 1.0 |
| *VariableActions* | [VariableAction[]](../../Variables/VariableAction.md) | N | 處理自訂變數 | **X** | 1.0 |

### ■ RegexModel

| 屬性 | 資料型態 | 必要屬性 | 描述 | 支援變數 | 版本 |
| -------- | ------ | -------- | ----------- | ----------- | ----------- |
| **Intent** | string | Y        |  意圖           |  **X**      |  1.0        |
| **Patterns** | string[] | Y | 符合此意圖句型          | **X**     | 1.0       |
| **IgnoreCase** | bool | N | 忽略大小寫，預設值 `true` | **X** | 1.0 |



## ◆ Node Lifecycle

### ■ 輸入

* **使用者訊息 (User Message)**
    * 文字訊息

* **節點設定 (Node Setting)**
    * **IsPrompt** ─ 是否要顯示提示訊息
    * **Prompt** ─ 發送給提示使用者的訊息
    * **Models** ─ 定義 Regular Expression 的判斷 Intent 規則
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
    * **Step.2-2** 透過已設定的 Regular Expression (Model) 判斷使用者的意圖
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
            "Score": 0.8
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
                "Value": "",
                "Score": 0.8,
                "StartIndex": 0,
                "EndIndex": 0
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
        "NodeType": "qa.regex",
        "Date": ""
    }
}
```



## ◆ Example



```json
{
    "Id": "node_00001",
    "Name": "QA with Regex",
    "Description": "",
    "Type": "qa.regex",
    "IsPrompt": false,
    "Models":[
        {
            "Intent": "Help",
            "Patterns": [ 
                "^(help)$"
            ],
            "IgnoreCase": true
        },
        {
            "Intent": "Quit",
            "Patterns": [
                "^(exit|quit)$"
            ],
            "IgnoreCase": true
        }
    ],
    "Actions": [
        {
            "Rules": [
                {
                    "Type": "intent",
                    "Intent": "Help",
                    "Score": 0.5
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
                    "Intent": "Quit",
                    "Score": 0.5
                }
            ],
            "Type": "and",
            "Priority": 50,
            "NextNodeId": "node_00003"
        },
        {
            "Rules": [],
            "Type": "none",
            "Priority": 50,
            "NextNodeId": "node_00004"
        }
    ],
    "Prompt": {
        "Type": "text",
        "Text": "What do you want to do?"
    }
}
```