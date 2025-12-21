# M+ 雙向訊息

> * 對應 M+ 雙向訊息，M+專用訊息
> * 主要用於卡片式一問一答



## ◆ Screenshot  

![](Screenshots/HeroCard.png)



## ◆ Channel Support

| Channel 類型        | 是否支援 | 備註                                                         |
| ------------------- | -------- | ------------------------------------------------------------ |
| Emulator            | **O**    |                                                              |
| Web Chat            | **O**    |                                                              |
| iota、iota Chat Bot | **O**    | 1. 舊版 iota 不支援 Carousel 卡片排版<br />2. 實作上會轉換成 Adaptive Card |
| LINE                | **O**    | 1. 實作上會轉換成 LINE Flex Message<br />2. 圖片只支援 JPG 和 PNG，檔案上限 1 MB，需要 HTTPS |
| Teams               | **O**    | 卡片按鈕皆視為 ImBack                                        |
| Slack               | **O**    | 1. 實作上會轉換成 Slack Block Kit 訊息<br />2. 回覆的內容為專用格式 |
| Webex               | **O**    | 實作上會轉換成 Adaptive Card                                 |
| Facebook Messenger  | **O**    | 卡片按鈕皆視為 ImBack                                        |
| WhatsApp            | **O**    | 1. 卡片按鈕皆視為 ImBack<br />2. 按鈕如果同時有 OpenUrl 和 ImBack 會拆成兩個卡片 |
| Telegram            | **O**    | 卡片按鈕皆視為 PostBack                                      |
| M+                  | **O**    | 1. 按鈕 = 回覆文字，卡片按鈕皆視為 ImBack<br />2. 標題文字字數總和不得超過 500個字 |
| WeChat (微信個人號) | **X**    |                                                              |
| WeCom (企業微信)    | **O**    | 1. 不支援 Carousel 卡片排版<br />2. 不支援圖片顯示<br />3. 不支援群組對話 |
| DingTalk            | **X**    |                                                              |
| Apple Business Chat | **X**    |                                                              |



## ◆ Schema

繼承 [MessageContent](MessageContent.md)

| 屬性        | 資料型態      | 必要屬性 | 描述                             | 支援變數 | 版本 |
| ----------- | ------------- | -------- | -------------------------------- | -------- | ---- |
| *Type*      | string        | Y        | 類型，值為 `mplus.questionnaire` | **X**    | 1.2? |
| **Text**    | string        | N        | 標題、內文，最多 500個字         | **O**    | 1.2? |
| **Images**  | MPlusImage[]  | N        | 圖片連結，最多3個                | **X**    | 1.2? |
| **Buttons** | MPlusButton[] | Y        | 卡片按鈕，至少需要1個            | **X**    | 1.2? |
| **Payload** | MPlusPayload  | N        | 其他選項                         | **X**    | 1.2? |

### ■ M+ Image

| 屬性 | 資料型態 | 必要屬性 | 描述                                                         | 支援變數 | 版本 |
| ---- | -------- | -------- | ------------------------------------------------------------ | -------- | ---- |
| Url  | string   | Y        | 圖片連結<br />只支援 JPG 和 PNG檔案格式，檔案大小不得超過 40 MB<br />不支援 Base64 Image Url | **O**    | 1.2? |

### ■ M+ Button

| 屬性  | 資料型態 | 必要屬性 | 描述                                   | 支援變數 | 版本 |
| ----- | -------- | -------- | -------------------------------------- | -------- | ---- |
| Title | string   | Y        | 按鈕標題，同時也是按鈕點擊後送出的內容 | **O**    | 1.2? |

### ■ M+ Payload

| 屬性               | 資料型態 | 必要屬性 | 描述                                                         | 支援變數 | 版本 |
| ------------------ | -------- | -------- | ------------------------------------------------------------ | -------- | ---- |
| ButtonLayout       | string   | N        | 按鈕顯示排版，預設值：`6`<br />‧`4` ：以文字輸入取代按鈕<br />‧`5`：按鈕左右並排顯示<br />‧`6`：按鈕上下並排顯示 | **X**    | 1.2? |
| IsCritical         | boolean  | N        | 是否為緊急訊息，預設值：`false`                              | **X**    | 1.2? |
| IsAcceptMultiReply | boolean  | N        | 按鈕是否允許多次點擊，預設值：`true`                         | **X**    | 1.2? |





---

## ◆ Example



```json
{
    "Type": "mplus.questionnaire",
    "Text": "Title",
    "Images": [
    	{
            "Url": ""
        }
    ],
    "Buttons": [
        {
            "Title": "yes"
        },
        {
            "Title": "no"
        }
    ],
    "Payload": {
        "ButtonLayout": "6",
        "IsCritical": false,
        "IsAcceptMultiReply": true
    }
}
```

