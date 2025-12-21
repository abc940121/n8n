# GSS.AI (QA)

> 使用 GSS.AI (RASA NLU + Deep Pavlov)   處理使用者的意圖或是問題



## ◆ Schema

繼承自 [Base QA](BaseQA.md)

| 屬性    | 資料型態                                        | 必要屬性 | 描述                                       | 支援變數 | 版本 |
| ------------- | ----------------------------------------------- | -------- | --------------------------------------------------- | ----------- | ----------- |
| *Id*          | string                                          | Y        | Node ID                                    | **X** | 1.0 |
| *Name*        | string                                          | N        | Node 名稱                                           | **X** | 1.0 |
| *Description* | string                                          | N        | Node 描述                                           | **X** | 1.0 |
| *Type*        | string                                          | Y        | Node 類型，值為 `qa.gssai`                      | **X** | 1.0 |
| **IsPrompt** | boolean | Y | 是否提示或等候使用者輸入，預設值：false | **X** | 1.0 |
| **Prompt** | [MessageContent](../../Contents/MessageContent.md) | N        | 提示使用者輸入問題                           | **X** | 1.0 |
| **HostUrl** | string                                          | Y        | GSS.AI 的 Host URL             | **O** | 1.0 |
| **ApplicationId** | string | Y | GSS.AI 對應的 App Id | **O** | 1.0 |
| **SubscriptionKey** | string | Y | GSS.AI Subscription Key | **O** | 1.0 |
| **AnswerCount** | string **(int string)** | Y | 答案數量 | **O** | 1.0 |
| **Confidence**  | string **(double string)** | Y | 答案的信心指數 | **O** | 1.0 |
| *Actions*     | [NodeAction[]](../../Actions/NodeAction.md)     | Y        | Node 轉換行為 `(至少一個)` | **X** | 1.0 |
| *VariableActions* | [VariableAction[]](../../Variables/VariableAction.md) | N | 處理自訂變數 | **X** | 1.0 |



## ◆ Node Lifecycle

### ■ 輸入

* **使用者訊息 (User Message)**
    * 文字訊息

* **節點設定 (Node Setting)**
    * **IsPrompt** ─ 是否要顯示提示訊息
    * **Prompt** ─ 發送給提示使用者的訊息
    * **HostUrl** ─ GSS.AI 的 Host URL
    * **SubscriptionKey** ─ LUIS 的 LUIS Subscription Key
    * **AnswerCount**  ─ 答案數量
    * **Confidence**  ─ 答案的信心指數數量
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
        * **`$.NodeOutput.Data.TopIntent.TopAnswer.Answer`**
            * 分數最高的答案 `(建議 Trigger Type 為 after_node 時使用)`
        * **`$.NodeOutput.Data.TopIntent.TopAnswer.Question`**
            * 分數最高的問題題目 `(建議 Trigger Type 為 after_node 時使用)`
        * **`$.NodeOutput.Data.TopIntent.TopAnswer.Score`**
            * 分數最高的答案的信心指數  `(建議 Trigger Type 為 after_node 時使用)`
        * **`$.NodeOutput.Data.Query`**
            * 使用者提問的內容 `(建議 Trigger Type 為 after_node 時使用)`
        * ...
    * [**自訂變數**](../../Variables/Variable.md#-自訂變數)
* **在 Node Action**
    * **`$.TopIntent.Intent`** ─ 分數最高的意圖
    * **`$.TopIntent.Score`** ─ 分數最高的意圖的信心指數 
    * **`$.TopIntent.TopAnswer.Answer`** ─ 分數最高的答案
    * **`$.TopIntent.TopAnswer.Question`** ─ 分數最高的問題題目
    * **`$.TopIntent.TopAnswer.Score`** ─ 分數最高的答案的信心指數 
    * **`$.Query`** ─ 使用者提問的內容
    * ...

```json
{
    "TopIntent": {
        "Intent": "faq_0001",
        "Score": 0.8,
        "TopAnswer": {
            "Question": "",
            "Answer": "",
            "Score": 0.8
        },
        "OtherAnswers": [
            {
                "Question": "",
                "Answer": "",
                "Score": 0.8
            }
        ]
    },
    "Intents": [
        {
            "Intent": "Other",
            "Score": 0.8,
            "TopAnswer": {},
            "OtherAnswers": []
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
}
```

### ■ 輸出

* **Node Output**

```json
{
    "Type": "NluResult",
	"Data": {
        "TopIntent": {
            "Intent": "faq_0001",
            "Score": 0.8,
            "TopAnswer": {
                "Question": "",
                "Answer": "",
                "Score": 0.8
            },
            "OtherAnswers": [
                {
                    "Question": "",
                    "Answer": "",
                    "Score": 0.8
                }
            ]
        },
        "Intents": [
            {
                "Intent": "Other",
                "Score": 0.8,
                "TopAnswer": {},
                "OtherAnswers": []
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
        "NodeType": "qa.gssai",
        "Date": ""
    }
}
```



## ◆ QA Result Example

### ■ FAQ Intent

```json
{
    "TopIntent": {
        "Intent": "faq",
        "Score": 0.87
    },
    "Intents": [{
        "Intent": "faq",
        "Score": 0.87
    }],
    "Entities": [],
    "Query": "你是誰？",
    "TopAnswer": {
        "Question": "請問你是誰?",
        "Answer": "你問了很好的問題",
        "Score": 0.87
    },
    "OtherAnswers": [
        {
            "Question": "請問你要去哪裡?",
            "Answer": "這是個天大的秘密",
            "Score": 0.03
        }
    ],
    "Data": {}
}
```



### ■ Other Intent


```json
{
    "TopIntent": {
        "Intent": "ApplyLeave",
        "Score": 0.87
    },
    "Intents": [
        {
            "Intent": "ApplyLeave",
            "Score": 0.87
        }
    ],
    "Entities": [
        {
            "Entity": "LeaveAction",
            "Value": "請假",
            "Score": 0.87
        }
    ],
    "Query": "我想要請假",
    "TopAnswer": {
        "Question": "",
        "Answer": "",
        "Score": 0
    },
    "Answers": [],
    "Data": {}
}
```



### ■ None Intent

* **找不到「意圖」或是「答案」**

```json
{
    "TopIntent": {
        "Intent": "none",
        "Score": 0.0
    },
    "Intents": [{
        "Intent": "none",
        "Score": 0.0
    }],
    "Entities": [],
    "Query": "",
    "TopAnswer": {
        "Question": "",
        "Answer": "",
        "Score": 0
    },
    "Answers": [],
    "Data": {}
}
```



## ◆ Example



```json
{
	"Id": "node_00001",
	"Name": "GSS AI Sample",
	"Description": "",
	"Type": "qa.gssai",
	"HostUrl":"http://172.16.4.87:4000",
	"ApplicationId": "1",
    "SubscriptionKey": "",
    "AnswerCount": 3,
    "Confidence": 0.7,
	"Actions": [
		{
            "Rules": [
                {
                    "Type": "intent",
                    "Intent": "faq",
                    "Score": 0.4
                }
            ],
            "Type": "and",
            "Priority": 50,
            "NextNodeId": "node_00001"
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
	"Prompt": null,
    "IsPrompt": false
}
```

