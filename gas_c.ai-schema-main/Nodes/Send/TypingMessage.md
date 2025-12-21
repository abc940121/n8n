# Typing Message

> 主要用於發送帶有打字效果的文字訊息給 User，**不會等候使用者輸入**

> 實驗性質的對話節點，目前限 Web Chat 4.18版以上支援



## ◆ Schema

繼承自 [Base Node](../BaseDialogNode.md)

| 屬性 | 資料型態 | 必要屬性 | 描述                          | 支援變數                    | 版本             |
| -------- | ------ | -------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| *Id* | string                                  | Y        | Node ID `(唯一)`                                    | **X**                               | 1.0                       |
| *Name*  | string                                  | N        | 名稱                                           | **X**                                     | 1.0                              |
| *Description* | string                                  | N        | 描述                                           | **X**                                     | 1.0                              |
| *Type*  | string                                  | Y        | 類型，值為 `typing.message`     | **X**             | 1.0                              |
| **Text** | string | Y | 文字訊息 | **O** | 2.10 |
| **TypingInterval** | int | N | 打字的間隔時間，預設值：`500` (500毫秒) | **X** | 2.10 |
| **DisableTyping** | boolean | N | 是否停止打字效果，預設值：`false` | **X** | 2.10 |
| *Actions* | [NodeAction[]](../../Actions/NodeAction.md) | Y        | Node 轉換行為，**`限定1個，且 RuleType 必須為 "none"`** | **X** | 1.0 |
| *VariableActions* | [VariableAction[]](../../Variables/VariableAction.md) | N | 處理自訂變數 | **X** | 1.0 |



## ◆ Node Lifecycle

### ■ 輸入

* **使用者訊息 (User Message)**
    * 無

* **節點設定 (Node Setting)**
    * **Message** ─ 發送給使用者需要的內容 (1個)
    * **Messages** ─  發送給使用者需要的內容 (多個)
        * **Message** 與 **Messages** 二擇一選擇
    * **Actions** ─ 依據使用者輸入，轉換到對應的 Node
        * **`限定 1 個`**
        * **強烈建議 Node Action Type 設為 "none"**

### ■ 節點運作

> **不會等候使用者輸入**，因此設計時需要留意無窮迴圈

* **OnBeginNode**  `(Turn 1)`
  
    * **Step.1** 顯示訊息內容
    * **Step.2** 取出下一個節點 (Node)
    
    * **Step.3** 結束目前節點，進到下一個節點

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
        "NodeType": "sending.message",
        "Date": ""
    }
}
```



## ◆ Example

```json
{
    "Id": "node_00001",
    "Name": "TypingTextNode",
    "Description": "",
    "Type": "typing.message",
    "Text": "Hello World",
    "TypingInterval": 500,
    "DisableTyping": false,
    "Actions": [
        {
            "Rules": [],
            "Type": "none",
            "Priority": 50,
            "NextNodeId": "node_00002"
        }
    ]
}
```



