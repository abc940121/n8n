# Base Event

> 主要用來處理迎賓訊息、對話訊息過濾、通知訊息、互動事件處理、對話逾時處理



## ◆ Schema

| 屬性             | 資料型態                                 | 必要屬性 | 描述                                                         | 支援變數 | 版本 |
| ---------------- | ---------------------------------------- | -------- | ------------------------------------------------------------ | -------- | ---- |
| *ID*             | string                                   | Y        | ID                                                           | **X**    | 1.0  |
| *Description*    | string                                   | N        | 敘述                                                         | **X**    | 1.0  |
| *Type*           | string                                   | Y        | Event 類型                                                   | **X**    | 1.0  |
| *Action*         | [BaseEventAction](EventAction.md)        | Y        | 當事件成立時的動作                                           | **X**    | 1.0  |
| *Priority*       | number                                   | Y        | Hook 事件的優先順序，範圍 0 ~ 100，預設值：50                | **X**    | 1.0  |
| *FlowConditions* | [FlowCondition[]](#-bot-event-condition) | N        | 在指定**對話流程 ID**或**對話節點 ID**中使用，預設值：空陣列 `(不限定對話流程或節點)` | **X**    | 1.1  |
| *IsEnable*       | boolean                                  | Y        | 是否啟用，true: 啟用、false: 停用                            | **X**    | 1.0  |

### ■ Flow Condition

> 指定**對話流程 ID**或**對話節點 ID**中啟用

> 條件判斷優先順序以陣列的順序先後判斷

| 屬性  | 資料型態 | 必要屬性 | 描述                                                         | 支援變數 | 版本 |
| ----- | -------- | -------- | ------------------------------------------------------------ | -------- | ---- |
| Type  | string   | Y        | 檢查類型，預設值：`none` `(不限定對話流程、節點)`            | **X**    | 1.1  |
| Value | string   | Y        | 在指定對話流程、節點啟用<br />多個對話流程/節點時以 `,` 間隔  **(v1.14 Update)** | **X**    | 1.1  |

* **Flow Condition Type**
    * `none` ─ 不限定對話流程、對話節點
    * `flow` ─ 在指定對話流程啟用
    * `flow.empty` ─ 對話流程為空白時啟用，例如：尚未開始對話、對話已經結束
    * `flow.excluded` ─ 指定名單以外的對話流程啟用  **(v1.14 New)**
    * `node` ─ 指定對話節點啟用
    * `node.excluded` ─ 指定名單以外的對話節點啟用  **(v1.14 New)**

> * **註1：如果尚未開始對話、對話已經結束時，Flow Id、Node Id 有可能為空白**
> * **註2：迎賓訊息 Flow Id、Node Id 有可能為空白，原因是對話尚未開始**



## ◆ Bot Event Hook 優先權：

1. **IsEnable 必需啟用**
2. **Flow Condition 需要成立**
3. **Bot Event Hook 條件成立者**
4. **Bot Event Hook 的 Priority 最高者**
5. **Bot Event Hook Event Array 最前面者**



## ◆ Message Event Type

| 類型                                                | Type Value             | Activity Type        | 描述         | 版本 |
| --------------------------------------------------- | ---------------------- | -------------------- | ------------ | ---- |
| [Greeting Event](GreetingEvent.md)                  | `greeting`             | `conversationUpdate` | 迎賓         | 1.0  |
| [User Message](UserMessageEvent.md)                 | `message`              | `message`            | 使用者訊息   | 1.0  |
| [Notification](NotificationEvent.md)                | `notification`         | `event` or  `invoke` | 通知事件     | 1.0  |
| [Custom Event](CustomEvent.md)                      | `event`                | `event`              | 自訂事件     | 1.0  |
| [Conversation Timeout](ConversationTimeoutEvent.md) | `conversation.timeout` | `message`            | 對話逾時處理 | 1.1  |

