# Vairable Decision

> 變數的操作、決策



## ◆ Schema

繼承自 [Base Node](../BaseDialogNode.md)

| 屬性                | 資料型態                                              | 必要屬性 | 描述                                   | 支援變數 | 版本 |
| ------------------- | ----------------------------------------------------- | -------- | -------------------------------------- | -------- | ---- |
| *Id*                | string                                                | Y        | Node ID `(唯一)`                       | **X**    | 1.0  |
| *Name*              | string                                                | N        | Node 名稱                              | **X**    | 1.0  |
| *Description*       | string                                                | N        | Node 描述                              | **X**    | 1.0  |
| *Type*              | string                                                | Y        | Node 類型，值為 `variable`             | **X**    | 1.0  |
| **VariableActions** | [VariableAction[]](../../Variables/VariableAction.md) | Y        | Variable 相關操作，按照 Array 順序處理 | **X**    | 1.0  |
| *Actions*           | [NodeAction[]](../../Actions/NodeAction.md)           | Y        | Node 轉換行為                          | **X**    | 1.0  |



## ◆ Node Lifecycle

### ■ 輸入

* **使用者訊息 (User Message)**
    * 無

* **節點設定 (Node Setting)**
    * **Actions** ─ 依據使用者輸入，轉換到對應的 Node
    * **`支援的 Node Action Rule`**
        *  [**JsonPath**](../../Rules/JsonPathRule.md)
        *  [**Evaluate Expression**](../../Rules/EvaluateExpressionRule.md)
        *  [**Composite**](../../Rules/CompositeRule.md)

### ■ 節點運作

> 1. 所有的處理都在 **VariableActions**
> 2. **不會等候使用者輸入**，因此設計時需要留意無窮迴圈

* **OnBeginNode**  `(Turn 1)`
    * **Step.1** 取出下一個節點 (Node)
    * **Step.2** 結束目前節點，進到下一個節點

### ■ 可使用的變數

* **在 Variable Action、Next Node Id 中可使用的變數**
    * [**自動變數**](../../Variables/Variable.md#-自動變數)
        * **`$.Message.Text`** ─ 使用者輸入的文字訊息 
        * **`$.Message.Value`** ─ 使用者點擊卡片按鈕的資料
        * **`$.Message.Attachments`** ─ 使用者上傳圖片或是附件檔 
        * **`$.Conversation.UserId`** ─ 使用者 ID
        * **`$.Conversation.UserName`** ─ 使用者 Name
        * ...
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
            "NodeType": "variable",
            "Date": ""
        }
    }
    ```



## ◆ Example

* **Node Action 可以使用自動變數和自訂變數作為判斷條件**

```json
{
    "Id": "node_00001",
    "Name": "Check Input",
    "Description": "",
    "Type": "variable",
    "Actions": [
        {
            "Rules": [
                {
                    "Type": "evaluate_expression",
                    "Expression": "String.IsNullOrEmpty(\"{{$.Message.Text}}\")"
                }
            ],
            "Type": "and",
            "Priority": 50,
            "NextNodeId": "node_00003"
        },
        {
            "Rules": [],
            "Type": "otherwise",
            "Priority": 50,
            "NextNodeId": "node_00002"
        }
    ]
}
```