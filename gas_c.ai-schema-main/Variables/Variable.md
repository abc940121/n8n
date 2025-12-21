# Variable

變數的規則遵循 JsonPath 的規則

* **變數類型**
  1. **[自動變數](#-自動變數)**
     * **[使用者訊息](#-使用者訊息)**
     * **[對話資訊](#-對話資訊)**
     * **[節點輸出值](#-節點輸出值)**
     * **[預設組態](#-預設組態)**
     * [**對話流程與節點資訊**](#-對話流程與節點資訊)
  2. **[自訂變數](#-自訂變數)**



## ◆ 自動變數

自動儲存的變數

### ● 使用者訊息

* 使用者輸入的訊息
* 當訊息進來時，自動儲存使用者的訊息
* 每次使用者訊息輸入，儲存的值都會變更




| 屬性        | 型態     | Source Variable     | Jsonpath                | 描述                     | 版本 |
| ----------- | -------- | ------------------- | ----------------------- | ------------------------ | ---- |
| Text        | string   | Activity.Text       | `$.Message.Text`        | 使用者發送的訊息         | 1.0  |
| Value       | object   | Activity.Value      | `$.Message.Value`       | 使用者發送的卡片資料訊息 | 1.0  |
| Attachments | object[] | Activity.Attachment | `$.Message.Attachments` | 使用者發送的附件訊息     | 1.0  |
| Id          | string   | Activity.Id         | `$.Message.Id`          | 訊息編號                 | 1.1  |
| TimeStamp   | string   |                     | `$.Message.TimeStamp`   | 收到的訊息時間           | 1.1  |



### ● 對話資訊

* Conversation 相關資訊
* 當訊息進來時，自動儲存使用者的 Conversation 相關資訊
* 每次使用者訊息輸入，儲存的值都會變更



| 屬性        | 型態    | Source Variable               | Jsonpath                     | 描述            | 版本 |
| ----------- | ------- | ----------------------------- | ---------------------------- | --------------- | ---- |
| UserId      | string  | Activity.From.Id              | `$.Conversation.UserId`      | 使用者ID        | 1.0  |
| UserName    | string  | Activity.From.Name            | `$.Conversation.UserName`    | 使用者名稱      | 1.0  |
| BotId       | string  | Activity.Recipient.Id         | `$.Conversation.BotId`       | Bot ID          | 1.0  |
| ChannelId   | string  | Activity.Channel.Id           | `$.Conversation.ChannelId`   | Channel ID      | 1.0  |
| IsGroup     | boolean | Activity.Conversation.IsGroup | `$.Conversation.IsGroup`     | 是否為群組      | 1.0  |
| Id          | string  | Activity.Conversation.Id      | `$.Conversation.Id`          | Conversation ID | 1.0  |
| ChannelData | object  | Activity.ChannelData          | `$.Conversation.ChannelData` | Channel Data    | 1.1  |



### ● 節點輸出值

* **`強烈不建議使用跨節點使用`**
* 依照節點的不同有各自的變數
* 前一個節點的輸入資料，**限定在後一個節點使用**，不建議在跨節點使用



| 屬性     | 資料型態 | Jsonpath                     | 描述           | 版本 |
| -------- | -------- | ---------------------------- | -------------- | ---- |
| Data     | object   | `$.NodeOutput.Data`          | 資料值         | 1.0  |
| Type     | string   | `$.NodeOutput.Type`          | 資料型態       | 1.0  |
| FlowId   | string   | `$.NodeOutput.From.FlowId`   | 輸出的流程 ID  | 1.1  |
| NodeId   | string   | `$.NodeOutput.From.NodeId`   | 輸出的節點 ID  | 1.1  |
| NodeName | stirng   | `$.NodeOutput.From.NodeName` | 輸出的節點名稱 | 1.1  |
| NodeType | string   | `$.NodeOutput.From.NodeType` | 輸出的節點類型 | 1.1  |



### ● 對話流程與節點資訊

紀錄對話流程與對話節點資訊，可用來 Debug 或寫 Log 使用

| 屬性     | 資料型態 | Jsonpath                 | 描述               | 版本 |
| -------- | -------- | ------------------------ | ------------------ | ---- |
| FlowId   | string   | `$.DialogState.FlowId`   | 目前的對話流程 ID  | 1.1  |
| FlowName | string   | `$.DialogState.FlowName` | 目前的對話流程名稱 | 1.1  |
| NodeId   | string   | `$.DialogState.NodeId`   | 目前的對話節點 ID  | 1.1  |
| NodeName | string   | `$.DialogState.NodeName` | 目前的對話節點名稱 | 1.1  |
| NodeType | string   | `$.DialogState.NodeType` | 目前的對話節點類型 | 1.1  |



### ● 預設組態

變數為唯讀變數，變數的值會在 BotScript 的 [Configs](../Bot.md#-BotConfig) 屬性被設定

* 變數命名限制
  * 只接受**英文字母 (含大小寫)**、**數字**、**底線**等字元，不接受**全形字元**和**空白字元**



| Variable (Jsonpath)                                   | 資料型態 | 描述              | 版本 |
| ----------------------------------------------------- | -------- | ----------------- | ---- |
| `$.Configs.<YourVariableName>`                        | object   | 預設變數 (第一層) | 1.0  |
| `$.Configs.<YourVariableRootName>.<YourVariableName>` | object   | 預設變數 (第二層) | 1.0  |



## ◆ 事件變數 (自動變數)

* 變數為唯讀變數，僅限 Event 觸發時使用，Event 結束時會清除
    * 依據不同的 Event 會有不同的內容

### ■ 所有事件通用

| Variable (Jsonpath)            | 資料型態 | 描述         | 版本 |
| ------------------------------ | -------- | ------------ | ---- |
| `$.EventVariables.ChannelId`   | string   | Channel ID   | 1.10 |
| `$.EventVariables.UserId`      | string   | User ID      | 1.10 |
| `$.EventVariables.UserName`    | string   | User Name    | 1.10 |
| `$.EventVariables.BotId`       | string   | Bot ID       | 1.10 |
| `$.EventVariables.IsGrpup`     | boolean  | Is Group     | 1.10 |
| `$.EventVariables.ChannelData` | object   | Channel Data | 1.10 |

### ■ [使用者訊息事件 (User Message Event)](../Events/UserMessageEvent.md)

| Variable (Jsonpath)            | 資料型態 | 描述     | 版本 |
| ------------------------------ | -------- | -------- | ---- |
| `$.EventVariables.Text`        | string   | 文字訊息 | 1.10 |
| `$.EventVariables.Value`       | object   | 資料     | 1.10 |
| `$.EventVariables.Attachments` | object[] | 卡片     | 1.10 |

### ■ [迎賓事件 (Greeting Event)](../Events/GreetingEvent.md)

| Variable (Jsonpath)                    | 資料型態 | 描述                                     | 版本 |
| -------------------------------------- | -------- | ---------------------------------------- | ---- |
| `$.EventVariables.JoinMembers`         | object[] | 加入的使用者，為一個陣列 (會包含自己)    | 1.10 |
| `$.EventVariables.JoinMembers[i].Id`   | string   | 加入的使用者中，第 i 個使用者ID          | 1.10 |
| `$.EventVariables.JoinMembers[i].Name` | string   | 第 i 個使用者Name                        | 1.10 |
| `$.EventVariables.EventHitCount`       | int      | 迎賓事件觸發的次數，第一次觸發時值為 `1` | 1.10 |
| `$.EventVariables.LastUpdateDate`      | object[] | 前一次迎賓事件觸發的時間                 | 1.10 |

### ■ [通知事件 (Notification Event)](../Events/NotificationEvent.md)、[自訂事件 (Custom Event)](../Events/CustomEvent.md)

| Variable (Jsonpath)               | 資料型態 | 描述                   | 版本 |
| --------------------------------- | -------- | ---------------------- | ---- |
| `$.EventVariables.EventName`      | string   | Event 名稱             | 1.10 |
| `$.EventVariables.EventLabel`     | string   | Event Label            | 1.10 |
| `$.EventVariables.EventValueType` | string   | Event Value 的資料類型 | 1.10 |
| `$.EventVariables.EventValue`     | object   | Event Value            | 1.10 |



## ◆ 自訂變數

需透過設定儲存的變數

* 變數命名限制
  * 只接受**英文字母 (含大小寫)**、**數字**、**底線**等字元，不接受**全形字元**和**空白字元**



| Variable (Jsonpath)                  | 資料型態 | 描述                    | 版本 |
| ------------------------------------ | -------- | ----------------------- | ---- |
| `$.Variables.<YourVariableName>`     | object   | 全域變數                | 1.0  |
| `$.FlowVariables.<YourVariableName>` | object   | 流程變數                | 1.2  |
| `$.NodeVariables.<YourVariableName>` | object   | 節點變數 **`<計畫中>`** | 1.2  |