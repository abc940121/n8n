# Trace 

> 偵錯節點



## ◆ Schema

繼承自 [Base Trace Node](../BaseTrace.md)

| 屬性              | 資料型態                                              | 必要屬性 | 描述                          | 支援變數 | 版本 |
| ----------------- | ----------------------------------------------------- | -------- | ----------------------------- | -------- | ---- |
| *Id*              | string                                                | Y        | Node ID                       | **X**    | 1.1  |
| *Name*            | string                                                | N        | Node 名稱                     | **X**    | 1.1  |
| *Description*     | string                                                | N        | Node 描述                     | **X**    | 1.1  |
| *Type*            | string                                                | Y        | Node 類型，值為 `trace` | **X**    | 1.1  |
| **Messages** | [MessageContent[]](../../MessageContent.md) | N | 顯示訊息 | **X** | 1.1 |
| **TraceName** | string | Y | Trace 名稱 | **O** | 1.1 |
| **TraceLabel** | string | N | Trace 標籤 | **O** | 1.1 |
| **TraceValueType** | string | N | Trace 資料的資料類型 | **O** | 1.1 |
| **TraceValue** | object | Y | Trace 資料 | **O** | 1.1 |
| *Actions*         | [NodeAction[]](../../Actions/NodeAction.md)           | Y        | Node 轉換行為 `(最多一個)`    | **X**    | 1.1  |
| *VariableActions* | [VariableAction[]](../../Variables/VariableAction.md) | N        | 處理自訂變數                  | **X**    | 1.1  |



## ◆ Node Lifecycle

### ■ 輸入

* **使用者訊息 (User Message)**
    * 無
* **節點設定 (Node Setting)**
    * **Message** ─ 發送給使用者需要的內容 (1個)
    * **Messages** ─  發送給使用者需要的內容 (多個)
        * **Message** 與 **Messages** 二擇一選擇
    * **TraceValue**  ─  要檢視的資料，可以帶入任何 [**變數**](../../Variables/Variable.md#)
        * 透過這個設定可以瀏覽目前所有的變數的值
    * **Actions** ─ 依據使用者輸入，轉換到對應的 Node
        * **`限定 1 個`**
        * **強烈建議 Node Action Type 設為 "none"**

### ■ 節點運作

> **不會等候使用者輸入**，因此設計時需要留意無窮迴圈

* **OnBeginNode**  `(Turn 1)`
    * **Step.1** 顯示訊息內容
    * **Step.2** 顯示 Trace 內容
        * 在 Emulator 和 Web Chat 會收到 Trace Message，[請參考這裡](https://docs.microsoft.com/en-us/azure/bot-service/using-trace-activities?view=azure-bot-service-4.0&tabs=csharp#to-use-a-trace-activity)
    * **Step.3** 取出下一個節點 (Node)
    * **Step.4** 結束目前節點，進到下一個節點

### ■ 可使用的變數

* **在 Variable Action、Next Node Id 中可使用的變數**
    * [**自動變數**](../../Variables/Variable.md#-自動變數)
    * [**自訂變數**](../../Variables/Variable.md#-自訂變數)
* **在 Node Action**
    * 無

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
        "Type": "null",
    	"Data": null,
        "From": {
            "BotId": "",
            "FlowId": "",
            "FlowName": "",
            "NodeId": "",
            "NodeName": "",
            "NodeType": "trace",
            "Date": ""
        }
    }
    ```



## ◆ Example

* **設定範例**

```json
{
    "Id": "node_00001",
    "Name": "Show Result",
    "Description": "",
    "Type": "trace",
    "Actions": [
        {
            "Rules": [],
            "Type": "none",
            "Priority": 50,
            "NextNodeId": ""
        }
    ],
    "Messages": [
        {
            "Type": "text",
            "Text": "{{$.Variables.GetResults.Data[0]}}"
        }
    ],
    "TraceName": "Call GET Request (Json Array)",
    "TraceLabel": "Debug Call GET Request (Json Array)",
    "TraceValueType": "",
    "TraceValue": "$.Variables.GetResults"
}
```

* **在 Emulator 或是 Web Chat 收到的訊息內容**
    * **Activity Type 為 `trace`**

```json
{
    "id": "Activity Id",
    "channelId": "emulator",
    "conversation": {
        "id": "Conversation Id"
    },
    "from": {
        "id": "CallApiBot",
        "name": "Bot",
        "role": "bot"
    },
    "recipient": {
        "id": "User",
        "role": "user"
    },
    "serviceUrl": "http://localhost:5164",
    "type": "trace",
    "name": "Call GET Request (Json Array)",
    "label": "Debug Call GET Request (Json Array)",
    "valueType": "Object",
    "value": {
        "Data": [
            {
                "birth": "1912-10-10",
                "id": "ROC",
                "name": "中華民國"
            },
            {
                "birth": "1776-07-04",
                "id": "USA",
                "name": "美利堅合眾國"
            },
            {
                "birth": "1945-08-15",
                "id": "KOR",
                "name": "大韓民國"
            },
            {
                "birth": "1949-10-01",
                "id": "POC",
                "name": "中華人民共和國"
            }
        ],
        "IsSuccessStatusCode": true,
        "StatusCode": "200",
        "Text": ""
    }
}
```





