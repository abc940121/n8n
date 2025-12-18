# Event Action



## ◆ Base Event Action

| 屬性   | 資料型態 | 必要屬性 | 描述         | 版本 |
| ------ | -------- | -------- | ------------ | ---- |
| *Type* | string   | Y        | 觸發行為類型 | 1.0  |

### ■ Event Action Type

| 類型                                               | 值            | 描述                                | 版本 |
| -------------------------------------------------- | ------------- | ----------------------------------- | ---- |
| [Message Event Action](#-message-event-action)     | `message`     | 發送訊息                            | 1.0  |
| [Flow Event Action](#-flow-event-action)           | `flow`        | 執行流程                            | 1.0  |
| [Module Flow Action](#-module-event-action)        | `flow.module` | 執行模組流程                        | 1.10 |
| [Composite Event Action](#-composite-event-action) | `composite`   | 依照設定條件執行不同的 Event Action | 1.10 |



---



## ◆ Message Event Action

>  發送訊息，繼承 [BaseEventAction](#-base-event-action)

| 屬性              | 資料型態                                           | 必要屬性 | 描述                        | 版本 |
| ----------------- | -------------------------------------------------- | -------- | --------------------------- | ---- |
| *Type*            | string                                             | Y        | 觸發行為類型，值為`message` | 1.0  |
| **Messages**      | [MessageContent[]](../Contents/MessageContent)     | Y        | 訊息                        | 1.0  |
| *VariableActions* | [VariableAction[]](../Variables/VariableAction.md) | Y        | 變數操作                    | 1.0  |

> **Variable Actions**：
>
> * **before_node**：會在顯示訊息前處理
> * **after_node**：會在顯示訊息後處理



---



## ◆ Flow Event Action

> 開始流程，繼承 [BaseEventAction](#-base-event-action)

> 只要成功觸發這個 Action 必定會先清空目前的對話流程，執行 Action 所指定的對話流程

| 屬性              | 資料型態                                           | 必要屬性 | 描述                                                         | 變數支援 | 版本 |
| ----------------- | -------------------------------------------------- | -------- | ------------------------------------------------------------ | -------- | ---- |
| *Type*            | string                                             | Y        | 觸發行為類型，值為`flow`                                     | **X**    | 1.0  |
| **FlowId**        | string                                             | Y        | 流程 ID                                                      | **O**    | 1.0  |
| **Arguments**     | Dictionary<string, [Argument](#-argument)>         | N        | 指派呼叫的 Flow 的流程變數<br />**v1.14 以上的 Value 由 object 調整為 [Argument](#-argument)** | **X**    | 1.14 |
| *VariableActions* | [VariableAction[]](../Variables/VariableAction.md) | Y        | 變數操作                                                     | **X**    | 1.1  |

> **Variable Actions**：
>
> * 無論 TriggerType 如何設定，皆會在切換對話流程前處理

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
| `use_expression` | Argument Value 會處理任何資料綁定                            |
| `plain`          | Argument Value 不處理任何資料綁定**`(不處理任何變數運算)`**  |
| `variable`       | 指派指定變數，不處理任何資料綁定，只處理1個變數 **`(不處理任何變數運算)`** |

* **v1.14 之前的 Arguments Schema**

```json
{
    "Type": "flow",
    "FlowId": "flow_000001",
    "Arguments": {
        "CardContent": "{{$.FlowVariables.CardContent}}",
        "Title": "Hello World"
    }
}
```

* **v1.14 之後的 Arguments Schema**

```json
{
    "Type": "flow",
    "FlowId": "flow_000001",
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



---

## ◆ Module Flow Event Action

> 開始流程，繼承 [BaseEventAction](#-base-event-action)

> 只要成功觸發這個 Action 必定會先清空目前的對話流程，執行 Action 所指定的模組對話流程

| 屬性              | 資料型態                                           | 必要屬性 | 描述                                                         | 變數支援 | 版本 |
| ----------------- | -------------------------------------------------- | -------- | ------------------------------------------------------------ | -------- | ---- |
| *Type*            | string                                             | Y        | 觸發行為類型，值為`flow.module`                              | **X**    | 1.0  |
| **FlowId**        | string                                             | Y        | 流程 ID                                                      | **X**    | 1.10 |
| **Arguments**     | Dictionary<string, [Argument](#-argument)>         | N        | 指派呼叫的 Flow 的流程變數<br />**v1.14 以上的 Value 由 object 調整為 [Argument](#-argument)** | **X**    | 1.14 |
| *VariableActions* | [VariableAction[]](../Variables/VariableAction.md) | Y        | 變數操作                                                     | **X**    | 1.1  |

> **Variable Actions**：
>
> * 無論 TriggerType 如何設定，皆會在切換對話流程前處理

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
| `use_expression` | Argument Value 會處理任何資料綁定                            |
| `plain`          | Argument Value 不處理任何資料綁定 **`(不處理任何變數運算)`** |
| `variable`       | 指派指定變數，不處理任何資料綁定，只處理1個變數 **`(不處理任何變數運算)`** |

* **v1.14 之前的 Arguments Schema**

```json
{
    "Type": "flow.module",
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
    "Type": "flow.module",
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



## ◆ Composite Event Action

> 開始流程，繼承 [BaseEventAction](#-base-event-action)

> 可以依照設定條件執行不同的 Event Action

| 屬性                              | 資料型態                                           | 必要屬性 | 描述                           | 版本 |
| --------------------------------- | -------------------------------------------------- | -------- | ------------------------------ | ---- |
| *Type*                            | string                                             | Y        | 觸發行為類型，值為 `composite` | 1.10 |
| **[Conditions](#EventCondition)** | CompositeEventActionCondition[]                    | Y        | Event Action 邏輯判斷          | 1.10 |
| *VariableActions*                 | [VariableAction[]](../Variables/VariableAction.md) | Y        | 變數操作                       | 1.10 |

### ■ Composite Event Action Conditions

| 屬性     | 資料型態                               | 必要屬性 | 描述                           | 版本 |
| -------- | -------------------------------------- | -------- | ------------------------------ | ---- |
| Name     | string                                 | Y        | Action 的名稱或敘述            | 1.10 |
| Rules    | [BaseRule[]](../Rules/BaseRule.md)     | Y        | 條件                           | 1.10 |
| Type     | string                                 | Y        | 條件符合的方式，預設值為 `or`  | 1.10 |
| Priority | number                                 | Y        | Action的優先順序，範圍 0 ~ 100 | 1.10 |
| Action   | [BaseEventAction](#-base-event-action) | Y        | 當條件符合時，的處理動作       | 1.10 |

### ■ Type

| Type    | Description        | Version |
| :------ | ------------------ | ------- |
| **and** | 所有的條件都須符合 | 1.10    |
| **or**  | 只要有一個條件符合 | 1.10    |



> **Variable Actions**：
>
> * 無論 TriggerType 如何設定，皆會在切換對話流程前處理

