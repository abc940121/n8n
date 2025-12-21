# End Module Flow

>  結束目前的模組流程



## ◆ Schema

繼承自 [Base Node](../BaseDialogNode.md)

| 屬性  | 資料型態                                 | 必要屬性 | 描述                                       | 支援變數 | 版本 |
| ----------- | ---------------------------------------- | -------- | --------------------------------------------------- | ---------- | ---------- |
| *Id*        | string                                   | Y        | Node ID `(唯一，且不得和Node ID重複)`               | **X** | 1.0 |
| *Name*      | string                                   | N        | Node 名稱                                           | **X** | 1.0 |
| *Description* | string                                   | N        | Node 描述                                           | **X** | 1.0 |
| *Type*      | string                                   | Y        | Node 類型，值為 `flow.module.end` | **X** | 1.0 |
| *Message* | [MessageContent](../../MessageContent.md) | N | 訊息內容 `(二擇一)` | **X** | 1.0 |
| *Messages* | [MessageContent[]](../../MessageContent.md) | N | 多個訊息內容 `(二擇一)` | **X** | 1.0 |
| **ReturnValue** | [FlowReturnValue](#-flow-return-value) | N | 模組流程輸出資料 (回傳值) | **X** | 1.10 |
| *Actions*   | [NodeAction[]](../../Actions/NodeAction.md) | Y        | Node 轉換行為 `(0個)` | **X** | 1.0 |
| *VariableActions* | [VariableAction[]](../../Variables/VariableAction.md) | N | 處理自訂變數 | **X** | 1.0 |

### ■ Flow Return Value

| 屬性                             | 資料型態 | 必要屬性 | 描述   | 支援變數 | 版本 |
| -------------------------------- | -------- | -------- | ------ | -------- | ---- |
| [Type](#-flow-return-value-type) | string   | Y        | 類型   | **X**    | 1.2  |
| Value                            | object   | Y        | 回傳值 | **O**    | 1.2  |

#### ● Flow Return Value Type

> 輸出資料的取值類型，設定方式可[參考這裡](../../Variables/VariableAction.md#-get-value)

| 指派方式/類型       | 描述             |
| ------------------- | ---------------- |
| string              | 文字             |
| string.json         | JSON文字         |
| number              | 數字             |
| boolean             | 布林值           |
| object              | 物件             |
| array               | 陣列             |
| variable            | 指派其他變數的值 |
| evaluate_expression | 公式表達式       |



## ◆ Node Lifecycle

### ■ 輸入

* **使用者訊息 (User Message)**
    * 無

* **節點設定 (Node Setting)**
    * **Actions** ─ 依據使用者輸入，轉換到對應的 Node
        * **`為 0 個`**

### ■ 節點運作

> **不會等候使用者輸入**，因此設計時需要留意無窮迴圈

* **OnBeginNode**  `(Turn 1)`
* **Step.1** 結束目前的模組流程對話

#### ● Dialog Flow Sequence


```mermaid
sequenceDiagram
    participant MainFlow
    participant ModuleFlow_01
    participant ModuleFlow_02
    
    MainFlow ->> MainFlow: Run Node
    MainFlow ->> ModuleFlow_01: Begin Flow "Module_01"
    ModuleFlow_01 ->> ModuleFlow_01: Run Node
    ModuleFlow_01 ->> ModuleFlow_02: Begin Flow "Module_02"
    ModuleFlow_02 ->> ModuleFlow_02: Run Node
    ModuleFlow_02 -->> ModuleFlow_01: End Flow "Module_02"
    ModuleFlow_01 ->> ModuleFlow_01: Run Node
    ModuleFlow_01 -->> MainFlow: End Flow "Module_01"
    MainFlow ->> MainFlow: Run Node
```

### ■ 可使用的變數

* **在 Variable Action 中可使用的變數**
    * [**自動變數**](../../Variables/Variable.md#-自動變數)
    * [**自訂變數**](../../Variables/Variable.md#-自訂變數)
* **在 Node Action**
    * 無

### ■ 輸出

* **Node Output 後可使用的變數**
    * 下一個節點取值
        * **`$.NodeOutput.Data`** ─ Node 輸出資料 (回傳值)
        * **`$.NodeOutput.From.NodeId`** ─ 從哪一個 Node 輸出
        * **`$.NodeOutput.From.FlowId`** ─ 從哪一個 Flow 輸出
        * ...
    
```json
{
    "Type": "string",
    "Data": {},
    "From": {
        "BotId": "",
        "FlowId": "",
        "FlowName": "",
        "NodeId": "",
        "NodeName": "",
        "NodeType": "flow.module.end",
        "Date": ""
    }
}
```



## ◆ Example



```json
{
    "Id": "node_00002",
    "Name": "End Module Flow",
    "Description": "",
    "Type": "flow.module.end",
    "Actions": [],
    "ReturnValue": {
        "Type": "string",
        "Value": "Thanks"
    }
}
```