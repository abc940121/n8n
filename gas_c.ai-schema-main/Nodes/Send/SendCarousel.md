# Send Carousel

> 主要用於發送多張卡片，**不會等候使用者輸入**



## ◆ Schema

繼承自 [Base Node](../BaseDialogNode.md)

| 屬性  | 資料型態                                          | 必要屬性 | 描述                                                | 支援變數                                          | 版本 |
| ----------- | ------------------------------------------------- | -------- | ------------------------------------------------------------ | ---------- | ---------- |
| *Id*      | string                                            | Y        | Node ID `(唯一)`                                             | **X**                                        | 1.0 |
| *Name*      | string                                            | N        | Node 名稱                                                    | **X**                                               | 1.0 |
| *Description* | string                                            | N        | Node 描述                                                    | **X**                                               | 1.0 |
| *Type*      | string                                            | Y        | Node 類型，值為 `sending.carousel`                           | **X**                      | 1.0 |
| **Text** | string | N | 卡片訊息內容 | **O** | 1.0 |
| **Attachments** | [MessageContent[]](../../Contents/MessageContent.md) | Y        | 發送使用者需要的卡片，**`只支援部分訊息類型`**                 | **X**                                    | 1.0 |
| **AttachmentLayout** | string                                            | Y        | 卡片的排版，預設值: `carousel` | **X** | 1.0 |
| *Actions*   | [NodeAction[]](../../Actions/NodeAction.md)       | Y        | Node 轉換行為，**`限定1個，且 RuleType 必須為 "none"`** | **X** | 1.0 |
| *VariableActions* | [VariableAction[]](../../Variables/VariableAction.md) | N | 處理自訂變數 | **X** | 1.0 |



## ◆ Node Lifecycle

### ■ 輸入

* **使用者訊息 (User Message)**
    * 無

* **節點設定 (Node Setting)**
    * **Attachments** ─ 發送使用者需要的卡片內容
        * `只支援以下 Message Content`
            * [Hero Card](../../Contents/HeroCardContent.md)
            * [SignIn Card](../../Contents/SignInCardContent.md)
            * [Animation Card](../../Contents/AnimationCardContent.md)
            * [Audio Card](../../Contents/AudioCardContent.md)
            * [Video Card](../../Contents/VideoCardContent.md)
            * [Adaptive Card](../../Contents/AdaptiveCardContent.md)
    * **AttachmentLayout** ─ 卡片的排版
        * **`List`**─ 上下
        * **`carousel`** ─ 上左右
    * **Actions** ─ 依據使用者輸入，轉換到對應的 Node
        * **`限定 1 個`**
        * **強烈建議 Node Action Type 設為 "none"**

### ■ 節點運作

> **不會等候使用者輸入**，因此設計時需要留意無窮迴圈

* **OnBeginNode**  `(Turn 1)`

    * **Step.1** 顯示訊息內容
    * **Step.2** 取出下一個節點 (Node)

    * **Step.3** 結束目前節點，進到下一個節點

### ■ 可使用的變數

* **在 Variable Action、Next Node ID 中可使用的變數**
    * [**自動變數**](../../Variables/Variable.md#-自動變數)
    * [**自訂變數**](../../Variables/Variable.md#-自訂變數)
* **在 Node Action**
    * 無

### ■ 輸出

* **Node Output 後可使用的變數**
    * 下一個節點取值
        * **`$.NodeOutput.Data.Text`** ─ 使用者輸入的文字訊息
        * **`$.NodeOutput.Data.Value`** ─ 使用者點擊卡片按鈕的資料
        * **`$.NodeOutput.Data.Attachments`** ─ 使用者上傳圖片或是附件檔
        * **`$.NodeOutput.From.NodeId`** ─ 從哪一個 Node 輸出
        * **`$.NodeOutput.From.FlowId`** ─ 從哪一個 Flow 輸出
        * ...
    
```json
{
    "Type": "null",
    "Data": null,
    "From": {
        "BotId": "",
        "FlowId": "",
        "FlowName": "",
        "NodeId": "",
        "NodeName": "",
        "NodeType": "sending.carousel",
        "Date": ""
    }
}
```




## ◆ ExampleExample

### ■ 發送卡片訊息 (Carousel Hero Card)

```json
{
    "Id": "node_00001",
    "Name": "SendCarouselNode",
    "Description": "",
    "Type": "sending.carousel",
    "Actions": [
        {
            "Rules": [],
            "Type": "none",
            "Priority": 50,
            "NextNodeId": "node_00002"
        }
    ],
    "Attachments": [
        {
            "Type": "hero.card",
            "Title": "This is title",
            "Subtitle": "This is subtitle",
            "Text": "This is text",
            "ImageUrl": "https://www.gss.com.tw/icon.png",
            "IsThumbnail": true,
            "Buttons": [
                {
                    "Type": "imBack",
                    "Title": "Button 01",
                    "Value": "1"
                },
                {
                    "Type": "imBack",
                    "Title": "Button 02",
                    "Value": "2"
                }
            ]
        },
        {
            "Type": "hero.card",
            "Title": "This is title2",
            "Subtitle": "This is subtitle2",
            "Text": "This is text2",
            "ImageUrl": "https://www.gss.com.tw/icon.png",
            "IsThumbnail": true,
            "Buttons": [
                {
                    "Type": "imBack",
                    "Title": "Button 03",
                    "Value": "3"
                },
                {
                    "Type": "imBack",
                    "Title": "Button 04",
                    "Value": "4"
                }
            ]
        }
    ],
    "Layout": "carousel"
}
```



### ■ 發送卡片訊息 (Carousel Adaptive Card)

```json
{
    "Id": "node_00001",
    "Name": "SendCarouselNode",
    "Description": "",
    "Type": "sending.carousel",
    "Actions": [
        {
            "Rules": [],
            "Type": "none",
            "Priority": 50,
            "NextNodeId": "node_00002"
        }
    ],
    "Attachments": [
        {
        "Type": "adaptive.card",
        "Text": "請說出你要我做什麼?",
        "Content": "{\"type\":\"AdaptiveCard\",\"body\":[{\"type\":\"Container\",\"items\":[{\"type\":\"TextBlock\",\"text\":\"Hi {{$.Conversation.UserName}}\"}]}],\"actions\":[{\"type\":\"Action.Submit\",\"title\":\"第一個選項 (Text)\",\"data\":\"1\"},{\"type\":\"Action.Submit\",\"title\":\"第二個選項 (Text)\",\"data\":\"2\"},{\"type\":\"Action.Submit\",\"title\":\"第三個選項 (Value)\",\"data\":{\"Action\":\"Quit\"}}],\"$schema\":\"http://adaptivecards.io/schemas/adaptive-card.json\",\"version\":\"1.0\"}"
    	},
        {
        "Type": "adaptive.card",
        "Text": "請說出你要我做什麼?",
        "Content": "{\"type\":\"AdaptiveCard\",\"body\":[{\"type\":\"Container\",\"items\":[{\"type\":\"TextBlock\",\"text\":\"Hi {{$.Conversation.UserName}}\"}]}],\"actions\":[{\"type\":\"Action.Submit\",\"title\":\"第一個選項 (Text)\",\"data\":\"1\"},{\"type\":\"Action.Submit\",\"title\":\"第二個選項 (Text)\",\"data\":\"2\"},{\"type\":\"Action.Submit\",\"title\":\"第三個選項 (Value)\",\"data\":{\"Action\":\"Quit\"}}],\"$schema\":\"http://adaptivecards.io/schemas/adaptive-card.json\",\"version\":\"1.0\"}"
    	}
    ],
    "Layout": "carousel"
}
```







