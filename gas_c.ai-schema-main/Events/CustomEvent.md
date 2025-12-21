# Custom Event

>  通知訊息處理



## ◆ Trigger Condition (觸發條件)

- **只要達到以下條件會執行此 Event 的 Action，判斷之先後順序**
  1. **IsEnable** 必需啟用
  2. [Flow Condition](BaseEvent.md#-flow-condition) 需要符合
      * **`注意：如果尚未開始對話、對話已經結束時，Flow Id、Node Id 有可能為空白`**
  3. 訊息類型 (Activity Type) 為 `event`
  4. EventActivity.Name 與 EventName 相符時 (不分大小寫)
  5. 自訂事件之自訂觸發條件 (**ActionConditions**) 需符合條件



## ◆ Schema

繼承 [BaseEvent](BaseEvent.md)

| 屬性          | 資料型態                     | 必要屬性 | 描述                                                         | 支援變數 | 版本 |
| ------------- | ---------------------------- | -------- | ------------------------------------------------------------ | -------- | ---- |
| *Id*          | string                       | Y        | ID                                                         | **X**    | 1.0  |
| *Description* | string                       | N        | 敘述                                                         | **X**    | 1.0  |
| *Type*        | string                       | Y        | Event 類型，值為 `event`                                     | **X**    | 1.0  |
| **EventName** | string                       | Y        | 符合的Event 名稱，在這裡會依據 Event Name去判斷是否處理這個訊息 | **O**    | 1.0  |
| **ActionConditions** | [EventActionCondition](#-custom-event-action-condition) | N        | 自訂事件之自訂觸發條件，會在動作 (包含變數操作) 之前判斷，預設值：**為空** (沒有條件限制) | **X** | 1.10 |
| **Action**    | [EventAction](EventAction.md) | Y        | 當事件成立時的動作                                           | **X**    | 1.0  |
| **Priority**  | number                       | Y        | Hook 事件的優先順序，範圍 0 ~ 100，預設值：50                | **X**    | 1.0  |
| *FlowConditions* | [FlowCondition[]](BaseEvent.md#-flow-condition) | N        | 在指定**對話流程 ID**或**對話節點 ID**中使用，預設值：空陣列 `(不限定對話流程或節點)` | **X**    | 1.1 |
| *IsEnable*    | boolean                      | Y        | 是否啟用，true: 啟用、false: 停用                            | **X**    | 1.0  |

### ■ Custom Event Action Condition

#### ● Schema

| 屬性  | 資料型態                           | 必要屬性 | 描述                     | 版本 |
| ----- | ---------------------------------- | -------- | ------------------------ | ---- |
| Rules | [BaseRule[]](../Rules/BaseRule.md) | Y        | 條件                     | 1.10 |
| Type  | string                             | Y        | 變數操作，預設值為 `and` | 1.10 |

#### ● Event Action Condition Type

| Type    | Description        | Version |
| :------ | ------------------ | ------- |
| **and** | 所有的條件都須符合 | 1.10    |
| **or**  | 只要有一個條件符合 | 1.10    |

#### ● Condition Rule

* **`不支援的 Rule`**
    * [**Intent**](../Rules/IntentRule.md)
* **可使用的變數**
    * **基本對話資訊**
        * **`$.ChannelId`** ─ 發送此訊息所使用的 Channel ID
        * **`$.UserId`** ─ 發送此訊息的使用者 ID
        * **`$.UserName`** ─ 發送此訊息的使用者名稱
        * **`$.BotId`** ─ 發送此訊息的使用者名稱
        * **`$.IsGroup`** ─ 是否為群組
    * **Event 資訊**
        * **`$.EventName`** ─ Event 名稱
        * **`$.EventLabel`** ─ Event Label
        * **`$.EventValueType`** ─ Event Value 的資料類型
        * **`$.EventValue`** ─ Event Value，資料格式不限，可能為 string、number、boolean、object、array...

```json
{
    "ChannelId": "",
    "UserId": "",
    "UserName": "",
    "BotId": "",
    "IsGroup": false,
    
    "EventName": "",
    "EventLabel": "",
    "EventValueType": "",
    "EventValue": {}
}
```



## ◆ Example

### ● 使用 Message Event Action 

* **定義觸法的條件和行為**

```json
{
    "Id": "Forward Notify Event",
    "Description": "批示通知事件",
    "Type": "event",
    "ActionConditions": null,
    "EventName": "PushForwardLeave",
    "Action": {
        "Type": "message",
        "Messages": [
            {
                "Type": "text",
                "Text": "您有一筆假單待批示：\n* **請假類別**：{{$.Message.Value.LeaveType}}\n* **開始時間**：{{$.Message.Value.StartDate}}\n* **結束時間**：{{$.Message.Value.EndDate}}\n* **請假事由**：{{$.Message.Value.LeaveSubject}}"
            }
        ]
    },
    "Priority": 50,
    "FlowConditions": [],
    "IsEnable": true
}
```


* **Input  Activity `(Event Activity)`**
* **type** ─ 必須為 `event`
  * **name** ─  對應 Schema 所定義的 `EventName`
  * **value** ─  Event 所需的資料，資料的使用請參考  [自動變數](../Variables/Variable.md#-使用者訊息) 


```json
{
    "channelData": {},
    "channelId": "<Channel Id>",
    "conversation": {
        "id": "<Conversation Id>"
    },
    "entities": [],
    "from": {
        "id": "<User Id>",
        "name": "<User Name>"
    },
    "id": "<Activity Id>",
    "localTimestamp": "",
    "locale": "",
    "recipient": {
        "id": "<Bot Id>",
        "name": "<Bot Name>"
    },
    "serviceUrl": "<Bot Connector Url>",
    "timestamp": "",
    "name": "PushForwardLeave",
    "value": {
        "LeaveType": "特休假",
        "StartDate": "2019-08-01 08:30",
        "EndDate": "2019-08-01 17:30",
        "LeaveSubject": "特休"
    },
    "type": "event"
}
```



### ● 使用 Flow Event Action 

* **定義觸法的條件和行為**

```json
{
    "Id": "Forward Notify Event",
    "Description": "批示通知事件",
    "Type": "event",
    "ActionConditions": null,
    "EventName": "PushForwardLeave",
    "Action": {
        "Type": "flow",
        "FlowId": "flow_00004",
        "IsInterrupt": true
    },
    "Priority": 50,
    "FlowConditions": [],
    "IsEnable": true
}
```


* **Input  Activity `(Event Activity)`**

  * **type** ─ 必須為 `event`
  * **name** ─  對應 Schema 所定義的 `EventName`
  * **value** ─  Event 所需的資料，資料的使用請參考  [自動變數](../Variables/Variable.md#-使用者訊息) 


```json
{
    "channelData": {},
    "channelId": "<Channel Id>",
    "conversation": {
        "id": "<Conversation Id>"
    },
    "entities": [],
    "from": {
        "id": "<User Id>",
        "name": "<User Name>"
    },
    "id": "<Activity Id>",
    "localTimestamp": "",
    "locale": "",
    "recipient": {
        "id": "<Bot Id>",
        "name": "<Bot Name>"
    },
    "serviceUrl": "<Bot Connector Url>",
    "timestamp": "",
    "name": "PushForwardLeave",
    "value": {
        "LeaveType": "特休假",
        "StartDate": "2019-08-01 08:30",
        "EndDate": "2019-08-01 17:30",
        "LeaveSubject": "特休"
    },
    "type": "event"
}
```

