# Begin Module Flow

>  開啟模組流程 (Module Flow)，模組流程 (Module Flow) 結束後會繼續完成主流程 (Master flow) 後續的對話



## ◆ Schema

繼承自 [Base Node](../BaseDialogNode.md)

| 屬性 | 資料型態 | 必要屬性 | 描述   | 支援變數 | 版本 |
| ---------- | ------ | -------- | --------------- | ---------- | ---------- |
| *Id*        | string                                  | Y        | Node ID `(唯一，且不得和Node ID重複)`                | **X**           | 1.0                       |
| *Name*      | string                                  | N        | Node 名稱                                           | **X**                                      | 1.0                              |
| *Description* | string                                  | N        | Node 描述                                           | **X**                                      | 1.0                              |
| *Type*      | string                                  | Y        | Node 類型，值為 `flow.module.begin`     | **X**         | 1.0                              |
| *Message* | [MessageContent](../../MessageContent.md) | N | 訊息內容 `(二擇一)` | **X** | 1.0 |
| *Messages* | [MessageContent[]](../../MessageContent.md) | N | 多個訊息內容 `(二擇一)` | **X** | 1.0 |
| **FlowId** | string | Y        | 呼叫的 Module Flow ID | **X** | 1.10 |
| **Arguments** | Dictionary<string, [Argument](#-argument)> | Y | 指派呼叫的 Module Flow 的流程變數<br />**v1.14 以上的 Value 由 object 調整為 [Argument](#-argument)** | **X** | 1.14 |
| *Actions*   | [NodeAction[]](../../Actions/NodeAction.md) | Y        | Node 轉換行為 `(至少一個)`，即 Transition Condition | **X** | 1.0 |
| *VariableActions* | [VariableAction[]](../../Variables/VariableAction.md) | N | 處理自訂變數 | **X** | 1.0 |

### ● Argument

| 屬性   | 資料型態 | 必要屬性 | 描述                                 | 支援變數 | 版本 |
| ------ | -------- | -------- | ------------------------------------ | -------- | ---- |
| $Type  | string   | Y        | 引數的類型，預設值：`use_expression` | **X**    | 1.14 |
| $Value | object   | Y        | 引數的值                             | `[1]`    | 1.14 |

* `[1]` 是否支援變數會以 **Type** 的值而定
    * **$Type** 為 `use_expression` 時，支援變數
    * **$Type** 為 `plain` 時，不支援變數
    * **$Type** 為 `variable` 時，直接使用指定變數的值，不處理任何運算
        * 如果設定多組變數時，只會使用第一個變數
        * 例如："`{{$.Variables.Var1}} {{$.Variables.Var2}}`"，只會取出變數 `$.Variables.Var1` 的值

#### ● Argument Type

| 指派方式/類型    | 描述                                                         |
| ---------------- | ------------------------------------------------------------ |
| `use_expression` | 引數的值會處理任何資料綁定                                   |
| `plain`          | 引數的值不處理任何資料綁定 **`(不處理任何變數運算)`**        |
| `variable`       | 指派指定變數，不處理任何資料綁定，只處理1個變數 **`(不處理任何變數運算)`** |

* **v1.14 之前的 Arguments Schema**

```json
{
    "Type": "flow.module.begin",
    "FlowId": "module_000001",
    "Arguments": {
        "CardContent": "{{$.FlowVariables.CardContent}}",
        "Title": "Hello World"
    }
}
```

* **v1.14 之後的 Arguments Schema**

```json
{
    "Type": "flow.module.begin",
    "FlowId": "module_000001",
    "Arguments": {
        "CardContent": {
            "$Type": "use_expression",
            "$Value": "{{$.FlowVariables.CardContent}}"
        },
        "Title": {
            "$Type": "use_expression",
            "$Value": "Hello World"
        }
    }
}
```



## ◆ Node Lifecycle

### ■ 輸入

* **使用者訊息 (User Message)**
    * 無

* **節點設定 (Node Setting)**
    * **FlowId** ─  要呼叫的 Module Flow ID
    * **Actions** ─ 依據使用者輸入，轉換到對應的 Node

### ■ 節點運作

> **不會等候使用者輸入**，因此設計時需要留意無窮迴圈

* **OnBeginNode**  `(Turn 1)`

    * **Step.1-1** 依據 Module Flow Id 的設定，呼叫指定的 Module Flow
        * **Step.1-2a** 如果未指定 Module Flow 或是 Module Flow 不存在，則`繼續下一個 Node`
* **OnEndNode** `(Turn Final)`
    * **Step.F-1** 取出下一個節點 (Node)
    * **Step.F-2** 結束目前節點，進到下一個節點

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

* **在 Variable Action、Next Node ID  中可使用的變數**
    * [**自動變數**](../../Variables/Variable.md#-自動變數)
    * [**自訂變數**](../../Variables/Variable.md#-自訂變數)
* **在 Node Action Rules  中可使用的變數**
    * 下一個節點取值
        * **`$.NodeOutput.Data`** ─ Node 輸出資料 (回傳值)
            * **資料來源來自子流程之 [End Module Flow Node 的 Return Value](EndModuleFlow.md#-flow-return-value)**
            * **`必須搭配 End Module Flow Node，沒有搭配則為 Null`**
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
        "NodeType": "flow.module.begin",
        "Date": ""
    }
}
```



### ■ 輸出

* **Node Output 後可使用的變數**
    * 下一個節點取值
        * **`$.NodeOutput.From.Data`** ─ 子流程的輸出資料
            * **資料來源來自子流程之 [End Module Flow Node 的 Return Value](EndModuleFlow.md#-flow-return-value)**
            * **`必須搭配 End Current Flow Node，沒有搭配則為 Null`**
        * **`$.NodeOutput.From.NodeId`** ─ 從哪一個 Node 輸出
        * **`$.NodeOutput.From.FlowId`** ─ 從哪一個 Flow 輸出
        * ...
```json
{
    "Type": "null",
    "Data": {},
    "From": {
        "BotId": "",
        "FlowId": "",
        "FlowName": "",
        "NodeId": "",
        "NodeName": "",
        "NodeType": "flow.module.begin",
        "Date": ""
    }
}
```



## ◆ Example



```json
{
    "Id": "node_00001",
    "Name": "Begin Survey Module Flow",
    "Description": "",
    "Type": "flow.module.begin",
    "Actions": [
        {
            "Rules": [],
            "Type": "none",
            "Priority": 50,
            "NextNodeId": "node_00002"
        }
    ],
    "FlowId": "module_flow_00002",
    "Arguments": {
        "LeaveDate": {
            "Type": "plain",
            "Value": "2020-01-16"
        },
        "StartLeaveTime": {
            "Type": "plain",
            "Value": "08:30"
        },
        "EndLeaveTime": {
            "Type": "plain",
            "Value": "17:30"
        }
    }
}
```



