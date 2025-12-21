# Greeting Event

> 初始訊息、迎賓訊息



## ◆ Trigger Condition (觸發條件)

* **只要達到以下條件會執行此 Event 的 Action，判斷之先後順序**
  1. **IsEnable** 必需啟用
  2. [Flow Condition](BaseEvent.md#-flow-condition) 需要符合
      * **`注意1：迎賓訊息 Flow Id、Node Id 有可能為空白，原因是對話尚未開始`**
      * **`注意2：如果尚未開始對話、對話已經結束時，Flow Id、Node Id 有可能為空白`**
  3. 訊息類型 (Activity Type) 為 `conversationUpdate`
  4. 使用者加入與 Bot 的對話時
  5. 當 **IsEnabledAtFirst** 為啟用時，在這個對話此事件觸發次數為 0次
  6. 迎賓事件的自訂觸發條件 (**ActionConditions**) 需符合條件



## ◆ Schema

繼承 [BaseEvent](BaseEvent.md)

> 1個 Bot 建議最多 1 個 Greeting Event

| 屬性          | 資料型態                     | 必要屬性 | 描述                                          | 支援變數 | 版本 |
| ------------- | ---------------------------- | -------- | --------------------------------------------- | -------- | ---- |
| *ID*          | string                       | Y        | ID                                            | **X**    | 1.0  |
| *Description* | string                       | N        | 敘述                                          | **X**    | 1.0  |
| *Type*        | string                       | Y        | Event 類型，值為 `greeting`                   | **X**    | 1.0  |
| **IsEnabledAtFirst** | boolean | N | 是否只在對話的一次觸發時執行，預設值：`false` (允許多次觸發) | **X** | 1.10 |
| **ActionConditions** | [EventActionCondition](#-greeting-action-condition) | N | 迎賓事件的自訂觸發條件，會在動作 (包含變數操作) 之前判斷，預設值：**為空** (沒有條件限制) | **X** | 1.10 |
| **Action**    | [EventAction](#event-action) | Y        | 當事件成立時的動作                            | **X**    | 1.0  |
| *Priority*    | number                       | Y        | Hook 事件的優先順序，範圍 0 ~ 100，預設值：50 | **X**    | 1.0  |
| *FlowConditions* | [FlowCondition[]](BaseEvent.md#-flow-condition) | N        | 在指定**對話流程 ID**或**對話節點 ID**中使用，預設值：空陣列 `(不限定對話流程或節點)` | **X**    | 1.1 |
| *IsEnable*    | boolean                      | Y        | 是否啟用，true: 啟用、false: 停用             | **X**    | 1.0  |

### ■ Greeting Action Condition

#### ● Schema

| 屬性      | 資料型態                           | 必要屬性 | 描述                     | 版本 |
| --------- | ---------------------------------- | -------- | ------------------------ | ---- |
| **Rules** | [BaseRule[]](../Rules/BaseRule.md) | Y        | 條件                     | 1.10 |
| **Type**  | string                             | Y        | 變數操作，預設值為 `and` | 1.10 |

#### ● Event Action Condition Type

| Type    | Description        | Version |
| :------ | ------------------ | ------- |
| **and** | 所有的條件都須符合 | 1.10    |
| **or**  | 只要有一個條件符合 | 1.10    |

#### ● Condition Rule

* **`不支援的 Rule`**
    * [**Intent**](../Rules/IntentRule.md)
* **可使用的變數**
    * **對話資訊**
        * **`$.ChannelId`** ─ 發送此訊息所使用的 Channel ID
        * **`$.UserId`** ─ 發送此訊息的使用者 ID
        * **`$.UserName`** ─ 發送此訊息的使用者名稱
        * **`$.BotId`** ─ 發送此訊息的使用者名稱
        * **`$.IsGroup`** ─ 是否為群組
    * **迎賓資訊**
        * **`$.JoinMembers`** ─ 加入的使用者，為一個陣列 (會包含自己)
            * **`$.JoinMembers[i].Id`** ─ 第 i 個使用者ID
            * **`$.JoinMembers[i].Name`** ─ 第 i 個使用者Name
        * **`$.EventHitCount`** ─ 這一個事件觸發的次數，為整數，第一次觸發時值為 `1`
            * **只要前4個滿足觸發條件 (Trigger Condition 1~4)，次數就會往上增加 1次**
        * **`$.LastUpdateDate`** ─ 前一次事件觸發的時間
            * 為一個字串，字串格時為 `yyyy-MM-dd HH:mm:ss`，**使用時建議使用 [DateTimeRule](../Rules/DateTimeRule.md)**
            * **只要前4個滿足觸發條件 (Trigger Condition 1~4)，觸發的時間就會更新**

```json
{
    "ChannelId": "",
    "UserId": "",
    "UserName": "",
    "BotId": "",
    "IsGroup": false,
    
    "JoinMembers": [],
    "EventHitCount": 1,
    "LastEventHitDate": "2020-05-20 05:13:14"
}
```



## ◆ Example

* **不設定任何條件**

```json
{
    "Id": "Greeting",
    "Description": "迎賓訊息",
    "Type": "greeting",
    "IsEnabledAtFirst": false,
    "ActionConditions": null,
    "Action": {
        "Type": "message",
        "Messages": [
            {
                "Type": "text",
                "Text": "You say {{$.Message.Text}}"
            }
        ]
    },
    "Priority": 50,
    "FlowConditions": [
        {
            "Flow": "",
            "Nodes": []
        }
    ],
    "IsEnable": true
}
```



* **僅限第一次觸發時執行**

```json
{
    "Id": "Greeting",
    "Description": "迎賓訊息",
    "Type": "greeting",
    "IsEnabledAtFirst": true,
    "ActionConditions": null,
    "Action": {
        "Type": "message",
        "Messages": [
            {
                "Type": "text",
                "Text": "You say {{$.Message.Text}}"
            }
        ]
    },
    "Priority": 50,
    "FlowConditions": [
        {
            "Flow": "",
            "Nodes": []
        }
    ],
    "IsEnable": true
}
```



* **自訂觸發條件**
    * 僅限前三次觸發時執行
    * **注意：`IsEnabledAtFirst` 要調整為 `false`，否則第2~3次觸發時不會被執行**

```json
{
    "Id": "Greeting",
    "Description": "迎賓訊息",
    "Type": "greeting",
    "IsEnabledAtFirst": false,
    "ActionConditions": {
        "Rules": [
            {
                "Type": "jsonpath",
                "Rule": {
                    "Type": "integer",
                    "Condition": "<=",
                    "Value": 2,
                    "Value2": 0,
                    "IsNegative": false
                },
                "JsonPath": "$.EventHitCount"
            }
        ],
        "Type": "or"
    },
    "Action": {
        "Type": "message",
        "Messages": [
            {
                "Type": "text",
                "Text": "You say {{$.Message.Text}}"
            }
        ]
    },
    "Priority": 50,
    "FlowConditions": [
        {
            "Flow": "",
            "Nodes": []
        }
    ],
    "IsEnable": true
}
```



* **自訂觸發條件**
    * 與前一次觸發時執行需間隔一分鐘
    * **注意：`IsEnabledAtFirst` 要調整為 `false`，否則觸發第一次後就不會再被執行**

```json
{
    "Id": "Greeting",
    "Description": "迎賓訊息",
    "Type": "greeting",
    "IsEnabledAtFirst": false,
    "ActionConditions": {
        "Rules": [
            {
                "Type": "jsonpath",
                "Rule": {
                    "Type": "integer",
                    "Condition": "==",
                    "Value": 1,
                    "Value2": 0,
                    "IsNegative": false
                },
                "JsonPath": "$.EventHitCount"
            },
            {
                "Type": "evaluate_expression",
                "Expression": "(DateTime.Now - DateTime.Parse(\"{{$.LastUpdateDate}}\")).TotalMinutes > 1"
            }
        ],
        "Type": "or"
    },
    "Action": {
        "Type": "message",
        "Messages": [
            {
                "Type": "text",
                "Text": "You say {{$.Message.Text}}"
            }
        ]
    },
    "Priority": 50,
    "FlowConditions": [
        {
            "Flow": "",
            "Nodes": []
        }
    ],
    "IsEnable": true
}
```









