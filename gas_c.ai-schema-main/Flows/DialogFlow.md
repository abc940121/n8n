# Dialog Flow

## ◆ Schema

對話流程

| 屬性         | 資料型態                                     | 必要屬性 | 描述                                            | 版本 |
| ------------ | -------------------------------------------- | -------- | ----------------------------------------------- | ---- |
| Id           | string                                       | Y        | Dialog Flow ID `(唯一)`                         | 1.0  |
| Name         | string                                       | N        | Dialog Flow 名稱                                | 1.0  |
| Description  | string                                       | N        | Dialog Flow 描述                                | 1.0  |
| IsModuleFlow | boolean                                      | N        | Dialog Flow 是否為一個模組流程，預設值：`false` | 1.10 |
| StartNodeId  | string                                       | Y        | 開始的 Node ID                                  | 1.0  |
| Nodes        | [BaseDialogNode](../Nodes/BaseDialogNode.md) | Y        | Dialog Node                                     | 1.0  |



### ■ Bot Lifecycle

```mermaid
stateDiagram
    note right of RunDialogFlow
        開始對話流程 or 繼續對話流程
    end note
    [*] --> RunDialogFlow: Start first dialog flow
    
    note right of RunDialogeNode
        開始對話節點
    end note
    RunDialogFlow --> RunDialogeNode: Get and run first dialog node
    
    note right of NextDialogNode
        對話節點結束，取得下一個對話節點
    end note
    RunDialogeNode --> NextDialogNode: End dialog node and get next one
    NextDialogNode --> RunDialogeNode: Run next dialog node
    NextDialogNode --> [*]: Unavailable dialog node
```



### ■ Module Flow 的限制

* **不支援以下 Node 的處理，遇到以下 Node 會直接 bypass**
    * [Begin Flow](../Nodes/FlowControl/BeginFlow.md)
    * [Switch Flow](../Nodes/FlowControl/SwitchFlow.md)
    * [End All Flow Node](../Nodes/FlowControl/EndAllFlow.md)



## ◆ Example

```json
{
    "Id": "flow_00001",
    "Name": "Master Flow",
    "Description": "This is demo bot",
    "IsModuleFlow": false,
    "StartNodeId": "node_00001",
    "Nodes": []
}
```

