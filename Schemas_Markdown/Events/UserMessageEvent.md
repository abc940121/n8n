# User Message Event

> 使用者訊息處理，用於過濾特定訊息內容



## ◆ Trigger Condition (觸發條件)

- 只要達到以下條件會執行此 Event 的 Action
  1. **IsEnable** 必需啟用
  2. [Flow Condition](BaseEvent.md#-flow-condition) 需要符合
      * **`注意：如果尚未開始對話、對話已經結束時，Flow Id、Node Id 有可能為空白`**
  3. 訊息類型 (Activity Type) 為 `message`
  4. 使用者訊息符合 [Message Condition](#-message-condition) 所定義的 [Rule](../Rules/BaseRule.md)



## ◆ Schema

繼承 [BaseEvent](BaseEvent.md)

| 屬性                  | 資料型態                                | 必要屬性 | 描述                                                     | 變數支援 | 版本 |
| --------------------- | --------------------------------------- | -------- | -------------------------------------------------------- | ---- | ---- |
| *Id*                  | string                                  | Y        | ID                                                       | **X** | 1.0  |
| *Description*         | string                                  | N        | 敘述                                                     | **X** | 1.0  |
| *Type*                | string                                  | Y        | Event 類型，值為 `message`                               | **X** | 1.0  |
| **MessageConditions** | [RuleConditions](#-message-condition) | Y        | 觸發條件規則，在這裡會依據條件規則去判斷是否處理這個訊息 | **X** | 1.0  |
| **Action**            | [EventAction](EventAction.md) | Y        | 當事件成立時的動作                                       | **X** | 1.0  |
| **Priority**          | number                                  | Y        | Hook 事件的優先順序，範圍 0 ~ 100，預設值：50            | **X** | 1.0  |
| *FlowConditions* | [FlowCondition[]](BaseEvent.md#-flow-condition) | N        | 在指定**對話流程 ID**或**對話節點 ID**中使用，預設值：空陣列 `(不限定對話流程或節點)` | **X** | 1.1 |
| *IsEnable*            | boolean                                 | Y        | 是否啟用，true: 啟用、false: 停用                        | **X** | 1.0  |

### ■ Message Condition

#### ● Schema

| 屬性      | 資料型態                           | 必要屬性 | 描述                           | 版本 |
| --------- | ---------------------------------- | -------- | ------------------------------ | ---- |
| **Rules** | [BaseRule[]](../Rules/BaseRule.md) | Y        | 觸發條件規則                   | 1.0  |
| **Type**  | string                             | Y        | 多組條件的判斷，預設值為 `and` | 1.0  |

#### ● Condition Type

| 類型             | 描述                               | 版本                             |
| :--------------- | ------------------------------------------- | ---------------- |
| **and** | 所有的條件都須符合 | 1.0 |
| **or** | 只要有一個條件符合 | 1.0 |

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
        * **`$.ChannelData`** ─ Channel Data，內容依照各個 Channel 而定
    * **訊息資訊**
        * **`$.Text`** ─ 使用者輸入的文字訊息
        * **`$.Value`** ─ 使用者點擊卡片按鈕的資料
        * **`$.Attachments`** ─ 使用者上傳圖片或是附件檔

```json
{
    "ChannelId": "",
    "UserId": "",
    "UserName": "",
    "BotId": "",
    "IsGroup": false,
    
    "Text": "",
    "Value": {},
    "Attachments": [],
    "ChannelData": {}
}
```



## ◆ Example



```json
{
    "Id": "Quit",
    "Description": "離開命令",
    "Type": "message",
    "MessageConditions": {
        "Rules": [
            {
                "Type": "regex",
                "Pattern": "^(quit|exit)$",
                "IsNegative": false,
                "IgnoreCase": false
            }
        ],
        "Type": "or"
    },
    "Action": {
        "Type": "flow",
        "FlowId": "flow_00002",
        "IsInterrupt": true
    },
    "Priority": 50,
    "FlowConditions": [],
    "IsEnable": true
}
```

