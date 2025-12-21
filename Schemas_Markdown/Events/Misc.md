**以下只是單純紀錄有哪些 Activity Type 可以使用**

## Activity Type

| Type                      | Can use ? | Description                              |
| ------------------------- | --------- | ---------------------------------------- |
| Message                   | O         | 訊息 (可用來處理全域訊息)                |
| ~~ContactRelationUpdate~~ | X         | Bot 與 User 的關係 ? **`(用途不明)`**    |
| ConversationUpdate        | O         | 成員加入/離開 (可用來顯示初始訊息 )      |
| ~~Typing~~                | X         | 使用者打字 **`(用途不明)`**              |
| EndOfConversation         | O         | 結束對話 (可用於清空對話流程)            |
| Event                     | O         | 事件 (可用於處理通知)                    |
| Invoke                    | O         | 觸發 (屬性與Event相同，可用於處理通知)   |
| Trace                     | ?         | 紀錄活動                                 |
| DeleteUserData            | ?         | 刪除使用者資料、Bot State                |
| ~~MessageUpdate~~         | X         | 訊息更新 ? **`(用途不明)`**              |
| ~~MessageDelete~~         | X         | 訊息刪除 ? **`(用途不明)`**              |
| ~~InstallationUpdate~~    | X         | Bot 安裝/移除 Channel ? **`(用途不明)`** |
| ~~MessageReaction~~       | X         | 訊息反應行為 ? **`(用途不明)`**          |
| ~~Suggestion~~            | X         | 建議 ? **`(用途不明)`**                  |
| ~~Handoff~~               | X         | 對話轉移 ? **`(用途不明)`**              |
| ~~Delay~~                 | X         | 延遲 ? **`(用途不明)`**                  |
| ~~InvokeResponse~~        | X         | **`(用途不明)`**                         |









- 處理的型別
  - **Message** - 訊息，可用來處理全域訊息
  - **ContactRelationUpdate** - Bot 與 User 的關係 ?
    - Action
  - **ConversationUpdate** - 成員加入/離開，用於初始訊息 ?
    - MembersAdded
    - MembersRemoved
  - **Typing** - (X)
  - **EndOfConversation** - 結束對話，用於清空對話流程 ?
  - **Event** - 事件，處理 BackChannel 事件、訊息通知 ?
    - Name (String)
    - Value (Object)
    - RelatesTo (ConversationReference)
  - **Invoke** - 訊息通知 ?
    - Name (String)
    - Value (Object)
    - RelatesTo (ConversationReference)
  - **Trace** - 紀錄行為
    - Name
    - Label
    - ValueType
    - Value
    - RelatesTo (ConversationReference)
  - **DeleteUserData** - 刪除使用者資料
  - **MessageUpdate** - 訊息更新
  - **MessageDelete** - 訊息刪除
  - **InstallationUpdate** - Bot 安裝/移除 Channel ?
    - Action
  - **MessageReaction** - 訊息反應行為 ?
    - ReactionsAdded、ReactionsRemoved
  - **Suggestion** - 建議 ?
  - **Handoff** - 對話轉移 ?
  - **Delay** - 延遲 ?
  - **InvokeResponse** - ?