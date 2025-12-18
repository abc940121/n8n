# Conversation Timeout Event

> 對話逾時處理



## ◆ Trigger Condition (觸發條件)

- 只要達到以下條件會執行此 Event 的 Action
  1. **IsEnable** 必需啟用
  2. [Flow Condition](BaseEvent.md#-flow-condition) 需要符合
      * **`注意：如果尚未開始對話、對話已經結束時，Flow Id、Node Id 有可能為空白`**
  3. 訊息類型 (Activity Type) 為 `message`
  4. 符合逾時 (Timeout) 的條件
      * **`注意：使用者的第一筆訊息不會符合逾時條件`**



## ◆ Schema

繼承 [BaseEvent](BaseEvent.md)

> 1個 Bot 建議最多 1 個 Conversation Timeout Event

| 屬性          | 資料型態                     | 必要屬性 | 描述                                                | 支援變數 | 版本 |
| ------------- | ---------------------------- | -------- | --------------------------------------------------- | ---- | ---- |
| *Id*          | string                       | Y        | ID                                                  | **X** | 1.1  |
| *Description* | string                       | N        | 敘述                                                | **X** | 1.1  |
| *Type*        | string                       | Y        | Event 類型，值為 `conversation.timeout`             | **X** | 1.1  |
| **Timeout**   | double                       | Y        | 逾時時間，單位以分鐘計算，預設值：`0`  (無 timeout) | **O** | 1.1  |
| **Action**    | [EventAction](EventAction.md) | Y        | 當事件成立時的動作                                  | **X** | 1.1  |
| **Priority**  | number                       | Y        | Hook 事件的優先順序，範圍 0 ~ 100，預設值：50       | **X** | 1.1  |
| *FlowConditions* | [FlowCondition[]](BaseEvent.md#-flow-condition) | N        | 在指定**對話流程 ID**或**對話節點 ID**中使用，預設值：空陣列 `(不限定對話流程或節點)` | **X** | 1.1 |
| *IsEnable*    | boolean                      | Y        | 是否啟用，true: 啟用、false: 停用                   | **X** | 1.1  |

> 註1：**Conversation Timeout Event** 最多限 1個

> 註2：當 Event 觸發後，不管 Event Action Type 是哪一個，皆會強制結束目前的對話 (Dialog Flow)



### ■ Timeout 的計算方式

> **本次使用者發送訊息的時間** ─ **前一次使用者發送訊息的時間** > **Timeout 時間 (分鐘)**



## ◆ Example



```json
{
    "Id": "Timeout",
    "Description": "逾時訊息",
    "Type": "conversation.timeout",
    "Timeout": 1,
    "Action": {
        "Type": "flow",
        "FlowId": "flow_00001",
        "IsInterrupt": true
    },
    "Priority": 50,
    "FlowConditions": [],
    "IsEnable": true
}
```