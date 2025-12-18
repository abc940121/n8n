# GSS.QA (QA)

> 使用 GSS 對話管理平台提供的 「GSS.QA」 處理使用者的問題



## ◆ Schema

繼承自 [Base QA](BaseQA.md)，客製化問答節點

| 屬性    | 資料型態                                        | 必要屬性 | 描述                                       | 支援變數 | 版本 |
| ------------- | ----------------------------------------------- | -------- | --------------------------------------------------- | ------------- | ------------- |
| *Id*          | string                                          | Y        | Node ID `(唯一)`                                    | **X** | 1.0 |
| *Name*        | string                                          | N        | Node 名稱                                           | **X** | 1.0 |
| *Description* | string                                          | N        | Node 描述                                           | **X** | 1.0 |
| *Type*        | string                                          | Y        | Node 類型，值為 `qa.gssqa`                    | **X** | 1.0 |
| **IsPrompt** | boolean | Y | 是否提示或等候使用者輸入，預設值：`false` | **X** | 1.0 |
| **Prompt** | [MessageContent](../../Contents/MessageContent.md) | N        | 提示使用者輸入問題                           | **X** | 1.0 |
| **Retry** | [MessageContent](../../Contents/MessageContent.md) | N | 提示使用者找不到答案，提示換一個問法。`如果沒有設定會使用系統預設訊息` | **X** | 1.0 |
| **NoMatchMessage** | string | Y | 找不到問題的訊息 | **O** | 1.0 |
| **ApplicationId** | string | Y | GSS 對話管理平台的 App ID | **O** | 1.0 |
| **SubscriptionKey** | string | Y | GSS.AI Subscription Key | **O** | 1.0 |
| **AnswerCount** | string **(int string)**                       | Y        | 顯示的答案數量，預設 `3筆` **(限定 Intent 為 FAQ)** | **O** | 1.0 |
| **Confidence** | string **(double string)** | Y | 答案的信心指數最低標準，預設 `0.7`  **(限定 Intent 為 FAQ)** | **O** | 1.0 |
| **Role** | string | N | 角色身分 | **O** | 1.8 |
| **FlowBeginMode** | string | N | 切換其他 flow 的方式，預設：`default`  **`<計畫中>`** | **X** | 1.1 |
| **QuitAction** | [QuitAction](#-quit-action) | N | 跳脫提問的對話相關設定，不設定此 Property 則不顯示相關提示按鈕 | **X** | 1.0 |
| **FeedbackAction** | [FeedbackAction](#-feedback-action) | N | 問答回饋按鈕 | **X** | 1.0 |
| *Actions* | [NodeAction[]](../../Actions/NodeAction.md)     | Y        | Node 轉換行為 `(至少一個)` | **X** | 1.0 |
| *VariableActions* | [VariableAction[]](../../Variables/VariableAction.md) | N | 處理自訂變數 | **X** | 1.0 |

### ■ Quit Action

| 屬性    | 資料型態 | 必要屬性 | 描述                                                         | 支援變數 | 版本 |
| ------- | -------- | -------- | ------------------------------------------------------------ | -------- | ---- |
| Title   | string   | Y        | 標題                                                         | **O**    | 1.0  |
| Value   | string   | Y        | 指定關鍵字，其值必須符合 **Pattern** 規則                    | **X**    | 1.0  |
| Pattern | string   | Y        | 符合的格式，**不分大小寫**，以 Regular Expression 表示，預設：`^(quit)$` | **X**    | 1.0  |

### ■ Feedback Action

| 屬性        | 資料型態 | 必要屬性 | 描述                                 | 支援變數 | 版本 |
| ----------- | -------- | -------- | ------------------------------------ | -------- | ---- |
| IsEnabled   | boolean  | Y        | 是否啟用問答回饋，預設值：`false`    | **X**    | 1.0  |
| ActionTitle | string   | Y        | 問答回饋按鈕標題                     | **O**    | 1.0  |
| ActionReply | string   | Y        | 使用者點擊問答回饋後，Bot 回覆的訊息 | **O**    | 1.0  |

### ■ Flow Begin Mode

| 類型          | 描述                                              | 版本 |
| ------------- | ------------------------------------------------- | ---- |
| `default`     | 同  `switch_flow`                                 | 1.1  |
| `begin_flow`  | 開始指定 Flow，當指定 Flow結束後會回到目前的 Node | 1.1  |
| `switch_flow` | 切換指定 Flow，當指定 Flow結束後直接結束對話      | 1.1  |



## ◆ Node Lifecycle

### ■ 輸入

* **使用者訊息 (User Message)**
    * 文字訊息
* **節點設定 (Node Setting)**
    * **IsPrompt** ─ 是否要顯示提示訊息
    * **Prompt** ─ 發送給提示使用者的訊息
    * **Actions** ─ 依據使用者輸入，轉換到對應的 Node
        * **`限定 1 個`**
            * **強烈建議 Node Action Type 設為 "none"**
* **卡片範本檔**
    * [卡片範本檔設定說明](QAGss/GssQA_TemplateCard.md)
* **系統設定 (AppSetting.json)**
    * 請參考  [AppSetting](..\..\..\AppSetting.md#5-相關的服務) 
        * GSS QA 相關設定，接設定在 AppSetting.json

### ■ 節點運作

> 當啟用 Prompt 時，需要等候使用者輸入

* **節點運作請參考這張流程圖**

![](QAGss/QAGssQA-Lifecycle.png)



* **PromptQuestionAsync**
    * 當啟用 Prompt 時，顯示 Prompt 的內容，等候使用者輸入
* **QueryAnswerAsync**
    * 使用 GSS.QA 的設定，去呼叫對應的服務，並取的 Answer
* **ShowAnswerAsync**
    * 顯示可能的答案
* **EndQuestionAsync**
    * 依據使用者點選的答案，決定接下來的處理：
        * **繼續提問 (`Continue`)** ─ 繼續處理使用者的提問，並且會自動略過  Prompt 訊息
        * **切換指定流程 `(SwitchFlow)`** ─ 強制切換至指定 Flow，切換方式是先清空 Dialog Stack 再 Begin Dialog
        * **使用者輸入離開訊息** ─ 結束目前的問答，繼續下一個指定的對話節點 (Node)
        * **回報錯誤的答案 `(Feedback)`** ─ 提供使用者回報
* **SendFeedbackAsync**
    * 處理完問題會報後，繼續處理使用者的提問，並且會自動略過  Prompt 訊息

### ■ 可使用的變數

* **在 Variable Action**
    * [**自動變數**](../../Variables/Variable.md#-自動變數)
    * [**自訂變數**](../../Variables/Variable.md#-自訂變數)
* **在 Node Action**
    * 無

### ■ 輸出

* **Node Output**
    * 下一個節點取值
        * **`$.NodeOutput.From.NodeId`** ─ 從哪一個 Node 輸出
        * **`$.NodeOutput.From.FlowId`** ─ 從哪一個 Flow 輸出
        * ...

```json
{
    "Type": "null",
    "Data": null,
    "From": {
        "BotId": "",
        "FlowId": "",
        "FlowName": "",
        "NodeId": "",
        "NodeName": "",
        "NodeType": "qa.gssqa",
        "Date": ""
    }
}
```





## ◆ GSS 管理平台 API Answer Result



### ■ Example

```json
{
    "Query": "你是誰啊？",
    "TopAnswer": {
        "Type" : "text",
        "Question": "你還好嗎?",
        "Answer": "你問了一個好問題",
        "Value": "你還好嗎?",
        "Confidence": "0.87"
    },
    "OtherAnswers": [
        {
            "Type": "text",
            "Question": "我是誰？",
            "Answer": "電影─我是誰？",
            "Value": "我是誰？",            
            "Confidence": "0.78"
        },
        {
            "Type": "link",
            "Question": "問天氣",
            "Answer": "Google 天氣",
            "Value": "https://www.google.com.tw/search?q=天氣",
            "Confidence": "0.04"
        },
        {
            "Type": "flow",
            "Question": "開始請假",
            "Answer": "點擊這裡，開始請假",
            "Value": "flow_000002",
            "Confidence": "0.01"
        }
    ]
}
```



### ■ Answer

| 屬性         | 資料型態                            | 描述           |
| ------------ | ----------------------------------- | -------------- |
| Query        | string                              | 使用者問的問題 |
| TopAnswer    | [AnswerContent](#-answer-content)   | 最佳答案       |
| OtherAnswers | [AnswerContent[]](#-answer-content) | 其他問題       |

### ■ Answer Content

| 屬性       | 資料型態                   | 描述                                       |
| ---------- | -------------------------- | ------------------------------------------ |
| Type       | string                     | 答案類型                                   |
| Question   | string                     | 問題，例如：`text`、`link`、`flow`、`none` |
| Answer     | string                     | 答案                                       |
| Value      | string                     | 其他資料，例如：超連結、流程對話 ID ...    |
| Confidence | string (**double string**) | 答案的信心度                               |

* **Text Answer**
    * 文字答案
    * 如果 Channel 有支援 Markdown，可以使用 Markdown 語法

```json
{
    "Type" : "text",
    "Question": "你還好嗎?",
    "Answer": "你問了一個好問題",
    "Value": "你還好嗎?",
    "Confidence": "0.87"
}
```

* **Refrence Link**
  * 參考連結

```json
{
    "Type": "link",
    "Question": "問天氣",
    "Answer": "Google 天氣",
    "Value": "https://www.google.com.tw/search?q=天氣",
    "Confidence": "0.87"
}
```

* **Switch Answer Flow**
    * 轉到其他對話流程

```json
{
    "Type": "flow",
    "Question": "開始請假",
    "Answer": "點擊這裡，開始請假",
    "Value": "flow_000002",
    "Confidence": "0.87"
}
```

* **No Answer**
    * 找不到符合的答案

```json
{
    "Type": "none",
    "Question": "找不到問題",
    "Answer": "不好意思，我不太清楚這個問題",
    "Value": "",
    "Confidence": "0"
}
```

* **Error**
    *  GSS 對話管理平台服務發生錯誤時
        * 取得 RASA NLU、Deep Pavlov 或是 GSS 對話管理平台的問答集答案時，發生錯誤
    * 訊息同 No Answer 的訊息，但會記錄錯誤資訊

```json
{
    "Type": "error",
    "Question": "系統發生錯誤",
    "Answer": "不好意思，我不太清楚這個問題",
    "Value": "",
    "Confidence": "0"
}
```



## ◆ Example



```json
{
    "Id": "node_00001",
    "Name": "GSS QA Sample Node",
    "Description": "",
    "Type": "qa.gssqa",
    "ApplicationId": "MoeaFaqBot",
    "SubscriptionKey": "",
    "Confidence": "0.7",
    "AnswerCount":"3",
    "Actions": [
        {
            "Rules": [],
            "Type": "none",
            "Priority": 50,
            "NextNodeId": "node_00001"
        }
    ],
    "Prompt": null,
    "Retry": {
        "Type": "text",
        "Text": "我找不到這個問題的答案，請試試別的問法"
    },
    "NoMatchText": "不好意思，我不太清楚這個問題",
    "QuitAction": {
        "Title": "結束提問",
        "Value": "quit",
        "Pattern": "^(quit|exit)$"
    },
    "IsPrompt": false
}
```