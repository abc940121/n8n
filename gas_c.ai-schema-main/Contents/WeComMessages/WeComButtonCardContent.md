# WeCom 按鈕卡片

> 靜態的按鈕訊息



## ◆ Screenshot  







## ◆ Channel Support

| Channel 類型            | 是否支援 | 備註                                                         |
| ----------------------- | -------- | ------------------------------------------------------------ |
| Emulator                | **O**    |                                                              |
| Web Chat、iota Chat Bot | **O**    |                                                              |
| iota                    | **O**    | 1. 舊版 iota 不支援 Carousel 卡片排版<br />2. 實作上會轉換成 Adaptive Card |
| LINE                    | **O**    | 1. 實作上會轉換成 LINE Flex Message<br />2. 圖片只支援 JPG 和 PNG，檔案上限 1 MB，需要 HTTPS |
| Teams                   | **O**    | 卡片按鈕皆視為 ImBack                                        |
| Slack                   | **O**    | 1. 實作上會轉換成 Slack Block Kit 訊息<br />2. 回覆的內容為專用格式 |
| Facebook Messenger      | **O**    | 卡片按鈕皆視為 ImBack                                        |
| WhatsApp                | **O**    | 1. 卡片按鈕皆視為 ImBack<br />2. 按鈕如果同時有 OpenUrl 和 ImBack 會拆成兩個卡片 |
| Telegram                | **O**    | 卡片按鈕皆視為 PostBack                                      |
| M+                      | **▲**    | 1. 按鈕不支援開啟連結<br />2. 按鈕 = 回覆文字，卡片按鈕皆視為 ImBack<br />3. 標題與文字字數總和不得超過 500個字 |
| WeChat (微信個人號)     | **X**    |                                                              |
| WeCom (企業微信)        | **O**    | 1. 不支援群組對話                                            |
| DingTalk                | **▲**    | 不支援圖片、標題 (Title)、按鈕、Carousel 卡片排版            |
| Apple Business Chat     | **X**    |                                                              |



## ◆ Schema

繼承自 [MessageContent](MessageContent.md)

| 屬性         | 資料型態                                     | 必要屬性 | 描述                           | 支援變數 | 版本 |
| ------------ | -------------------------------------------- | -------- | ------------------------------ | -------- | ---- |
| *Type*       | string                                       | Y        | 類型，值為 `wecom.card.button` | **X**    | 1.20 |
| **Title**    | string                                       | Y        | 主標題，字數最多 **36** 個字   | **O**    | 1.20 |
| **Subtitle** | string                                       | N        | 副標題，字數最多 **44** 個字   | **O**    | 1.20 |
| **Text**     | string                                       | N        | 內文，字數最多 **160** 個字    | **O**    | 1.20 |
| **Buttons**  | [WeComButtonAction](#-wecom-button-action)[] | Y        | 按鈕，最少**1**個、最多**6**個 | **X**    | 1.20 |

### ● WeCom Button Action

| 屬性  | 資料型態 | 必要屬性 | 描述                           | 支援變數 | 版本 |
| ----- | -------- | -------- | ------------------------------ | -------- | ---- |
| Type  | string   | Y        | 類型                           | **X**    | 1.20 |
| Title | string   | Y        | 按鈕標題，字數最多 **10** 個字 | **O**    | 1.20 |
| Value | string   | Y        | 按鈕值，字數最多 **1024** 個字 | **O**    | 1.20 |
| Style | string   | N        | 按鈕樣式，預設值：`default`    | **X**    | 1.20 |

* **Button Type**

| 按鈕類型   | 描述                | 版本 |
| ---------- | ------------------- | ---- |
| `submit`   | 回覆訊息 (Postback) | 1.20 |
| `open_url` | 開啟連結            | 1.20 |

* **Button Style**

| 按鈕類型     | 描述                | 版本 |
| ------------ | ------------------- | ---- |
| `default`    | 預設樣式 (藍底白字) | 1.20 |
| `blue_text`  | 藍字按鈕            | 1.20 |
| `red_text`   | 紅字按鈕            | 1.20 |
| `black_text` | 黑字按鈕            | 1.20 |



---

## ◆ WeCom Button Action 為 `Submit` 時的回傳內容

* Bot 收到的 Submit 資料 (Activity)

```json
{
    "Type": "message",
    "Value": {
        "taskId": "<WeCom Task Id>",
        "eventKey": "<Button Value>",
        "cardType": "button_interaction"
    }
}
```

### ■ 可使用的變數

* **在 Variable Action、Next Node 中可使用的變數**
    * **`$.Message.eventKey`** ─ 使用者點擊卡片按鈕的資料內
    * **`$.Message.taskId`** ─ 使用者點擊卡片的 Task Id
* **在 Prompt Node Action 中可使用的變數**
    * **`$.Value.eventKey`** ─ 使用者點擊卡片按鈕的資料內容
    * **`$.Message.taskId`** ─ 使用者點擊卡片的 Task Id



---

## ◆ Example



```json
{
    "Type": "wecom.card.button",
    "Title": "Title",
    "Subtitle": "Subtitle",
    "Text": "Text",
    "Buttons": [
        {
            "Type": "submit",
            "Title": "Send",
            "Value": "1",
            "Style": "default"
        },
        {
            "Type": "open_url",
            "Title": "Open",
            "Value": "https://www.gss.com.tw",
            "Style": "blue_text"
		}
    ]
}
```





