# Adaptive List Card Content

> 制式的Adaptive Card 訊息，清單卡片



##  ◆ Screenshot  

![](../Screenshots/ListCardContent.jpg)





## ◆ Channel Support

> [Adaptive Card 文件](https://adaptivecards.io/explorer/)

| Channel 類型            | 是否支援 | 備註                                                         |
| ----------------------- | -------- | ------------------------------------------------------------ |
| Emulator                | **O**    | Adaptive Card 支援的版本為 **1.3**                           |
| Web Chat、iota Chat Bot | **O**    | Adaptive Card 支援的版本為 **1.4**                           |
| iota                    | **O**    | daptive Card 支援的版本為 **1.5**                            |
| LINE                    | **O**    | 實作上會的轉成 LINE Flex Message                             |
| Teams                   | **O**    | 1. Adaptive Card 支援的版本為 **1.1**<br />2. 不支援 Audio 和 Video 等元件 |
| Slack                   | **X**    | 計畫中...                                                    |
| Webex                   | **O**    | Adaptive Card 支援的版本為 **1.3**                           |
| Facebook Messenger      | **X**    |                                                              |
| WhatsApp                | **X**    |                                                              |
| Telegram                | **X**    |                                                              |
| M+                      | **X**    |                                                              |
| WeChat(微信個人號)      | **X**    |                                                              |
| WeCom (企業微信)        | **X**    |                                                              |
| DingTalk                | **X**    |                                                              |
| Apple Business Chat     | **X**    |                                                              |



## ◆ Schema

繼承自 [MessageContent](../MessageContent.md)

| 屬性                          | 資料型態                                                     | 必要屬性 | 描述                                                         | 支援變數 | 版本  |
| ----------------------------- | ------------------------------------------------------------ | -------- | ------------------------------------------------------------ | -------- | ----- |
| *Type*                        | string                                                       | Y        | 類型，值為 `adaptive.card.list`                              | **X**    | 1.1   |
| **Title**                     | string                                                       | N        | 標題                                                         | **O**    | 1.1   |
| **Item**                      | [AdaptiveListItem](#-adaptive-list-item)                     | N        | 清單項目                                                     | **X**    | 1.1   |
| **Buttons**                   | [AdaptiveButtonContent[]](ActionContent.md#adaptive-action-content) | N        | Adaptive Card 按鈕                                           | **X**    | 1.1   |
| **DataSource**                | string                                                       | Y        | 指定資料來源 (自訂變數)，**僅用於 List Item**，**`必須指定`** | **O**    | 1.1   |
| **EmptyDataText**             | string                                                       | N        | 未指定資料來源時的提示訊息，有預設的提示訊息                 | **O**    | 1.1   |
| [**Styles**](#-style-options) | <string, string>                                             | N        | 清單的UI 樣式，沒有設定時，會使用預設樣式                    | **X**    | 1.1   |
| **Locale**                    | string                                                       | N        | 地區，用於處理文字格式化，預設值為伺服器所使用的地區         | **X**    | 1.1   |
| *QuickReply*                  | [ButtonContent[]](Components/ButtonContent.md)               | N        | 快速回覆按鈕                                                 | **X**    | 1.1   |
| *ChannelDataPayload*          | object                                                       | N        | Channel Data Payload，[使用限制](../Components/ChannelDataPayload.md) | **O**    | 1.14  |
| *Options*                     | [MessageContentOption](../AdaptiveCardContent.md#-message-content-option) | `[1]`    | 訊息相關參數，僅限 [Bot 通知訊息服務 (ETA)](https://git.gss.com.tw/fpsbu/bot_event_trigger_service) 發送通知訊息使用 | **X**    | **X** |

* `[1]` 這個參數僅限 [Bot 通知訊息服務 (ETA)](https://git.gss.com.tw/fpsbu/bot_event_trigger_service) 發送通知訊息使用
    * 這個參數不適用 Bot Flow Engine 主程式，Bot Flow Engine 主程式只在 [appsettings.json 設定



### ■ Adaptive List Item

| 屬性     | 資料型態                                                     | 必要屬性 | 描述             | 支援變數 或 指定 DataSource | 版本 |
| -------- | ------------------------------------------------------------ | -------- | ---------------- | --------------------------- | ---- |
| Title    | string                                                       | Y        | 標題             | **O**                       | 1.1  |
| Subtitle | string                                                       | N        | 副標題           | **O**                       | 1.1  |
| Text     | string                                                       | N        | 文字             | **O**                       | 1.1  |
| Tap      | [AdaptiveSelectActionContent](ActionContent.md#adaptive-select-action-content) | N        | 清單項目點擊事件 | **X**                       | 1.1  |
| ImageUrl | string                                                       | N        | 圖片             | **O**                       | 1.1  |



## ◆ Example

### ■ 指定 DataSource 內容

![](../Screenshots/ListCardContent.jpg)

* **變數名稱** ─ `$.Variables.CardTitle`

```json
"護國神山"
```

* **變數名稱** ─ `$.Variables.ITCompanies`

```json
[
    {
        "Name": "Facebook",
        "Description": "Facebook是源於美國的社群網路服務及社會化媒體網站...",
        "HomeUrl": "https://www.facebook.com/",
        "ImageUrl": "https://www.facebook.com/favorite.jpg"
    },
    {
        "Name": "Google",
        "Description": "Google是源自美國的跨國科技公司...",
        "HomeUrl": "https://www.google.com.tw",
        "ImageUrl": "https://www.google.com.tw/favorite.jpg"
    },
    {
        "Name": "Microsoft",
        "Description": "Microsoft是美國一家跨國電腦科技公司...",
        "HomeUrl": "https://www.microsoft.com/",
        "ImageUrl": "https://www.microsoft.com/favorite.jpg"
    }
]
```

* **Json**

```json
{
    "Type": "adaptive.card.list",
    "Title": "IT巨擘 ({{$.Variables.CardTitle}})",
    "Item": {
        "Title": "{{$.Name}}",
        "Subtitle": "",
        "Text": "{{$.Description}}",
        "Tap": {
            "Type": "open.url",
            "Value": "{{$.HomeUrl}}"
        },
        "ImageUrl": "{{$.ImageUrl}}"
    },
    "Buttons": [
        {
            "Type": "submit.text",
            "Title": "返回",
            "Value": "1",
            "Style": "default"
        }
    ],
    "DataSource": "$.Variables.ITCompanies",
    "EmptyDataText": "",
    "Styles": {
        "TitleColor": "Accent",
        "ItemBackground": "emphasis"
    }
}
```



## ◆ Style Options

> 有需要在使用，沒有設定的項目會使用預設值

| 樣式選項             | 說明                                            | 支援變數 | 參考                                                         |
| -------------------- | ----------------------------------------------- | -------- | ------------------------------------------------------------ |
| CardTitleColor       | [**清單卡片**] 標題字型顏色，預設： `Default`   | **X**    | [Text Block - Color](https://adaptivecards.io/explorer/TextBlock.html) |
| CardTitleSize        | [**清單卡片**] 標題字型大小，預設： `Medium`    | **X**    | [Text Block - Size](https://adaptivecards.io/explorer/TextBlock.html) |
| CardTitleWeight      | [**清單卡片**] 標題字型粗細，預設： `Bolder`    | **X**    | [Text Block - Weight](https://adaptivecards.io/explorer/TextBlock.html) |
| CardTitleAlignment   | [**清單卡片**] 標題對齊方式，預設： `Left`      | **X**    | [Text Block - Horizontal Alignment](https://adaptivecards.io/explorer/TextBlock.html) |
| ItemContentAlignment | [**清單項目**] 內文對齊方式，預設： `Left`      | **X**    | [Text Block - Horizontal Alignment](https://adaptivecards.io/explorer/TextBlock.html) |
| ItemTitleWrap        | [**清單項目**] 標題是否換行，預設： `false`     | **X**    | [Text Block - Wrap](https://adaptivecards.io/explorer/TextBlock.html) |
| ItemTitleSize        | [**清單項目**] 標題字型大小，預設： `Medium`    | **X**    | [Text Block - Size](https://adaptivecards.io/explorer/TextBlock.html) |
| ItemTitleColor       | [**清單項目**] 標題字型顏色，預設： `Default`   | **X**    | [Text Block - Color](https://adaptivecards.io/explorer/TextBlock.html) |
| ItemTitleWeight      | [**清單項目**] 標題字型粗細，預設： `Bolder`    | **X**    | [Text Block - Weight](https://adaptivecards.io/explorer/TextBlock.html) |
| ItemTitleMaxLines    | [**清單項目**] 標題最大行數，預設： `0`         | **X**    | [Text Block - Max Lines](https://adaptivecards.io/explorer/TextBlock.html) |
| ItemSubtitleWrap     | [**清單項目**] 副標題是否換行，預設： `false`   | **X**    | [Text Block - Wrap](https://adaptivecards.io/explorer/TextBlock.html) |
| ItemSubtitleSize     | [**清單項目**] 副標題字型大小，預設： `Default` | **X**    | [Text Block - Size](https://adaptivecards.io/explorer/TextBlock.html) |
| ItemSubtitleColor    | [**清單項目**] 副標題字型顏色，預設： `Default` | **X**    | [Text Block - Color](https://adaptivecards.io/explorer/TextBlock.html) |
| ItemSubtitleWeight   | [**清單項目**] 副標題字型粗細，預設： `Default` | **X**    | [Text Block - Weight](https://adaptivecards.io/explorer/TextBlock.html) |
| ItemSubtitleMaxLines | [**清單項目**] 副標題最大行數，預設： `0`       | **X**    | [Text Block - Max Lines](https://adaptivecards.io/explorer/TextBlock.html) |
| ItemTextWrap         | [**清單項目**] 內文是否換行，預設： `true`      | **X**    | [Text Block - Wrap](https://adaptivecards.io/explorer/TextBlock.html) |
| ItemTextSize         | [**清單項目**] 內文字型大小，預設： `Small`     | **X**    | [Text Block - Size](https://adaptivecards.io/explorer/TextBlock.html) |
| ItemTextColor        | [**清單項目**] 內文字型顏色，預設： `Default`   | **X**    | [Text Block - Color](https://adaptivecards.io/explorer/TextBlock.html) |
| ItemTextWeight       | [**清單項目**] 內文字型粗細，預設： `Lighter`   | **X**    | [Text Block - Weight](https://adaptivecards.io/explorer/TextBlock.html) |
| ItemTextMaxLines     | [**清單項目**] 內文最大行數，預設： `0`         | **X**    | [Text Block - Max Lines](https://adaptivecards.io/explorer/TextBlock.html) |
| ItemImageSize        | [**清單項目**] 圖片大小，預設：`Large`          | **X**    | [Image - Size](https://adaptivecards.io/explorer/Image.html) |
| ItemImageLayout      | [**清單項目**] 圖片的位置，預設：`Right`        | **X**    | ● **None**：無圖片<br />● **Left**：在左側<br />● **Right**：在右側 |
| ItemImageStyle       | [**清單項目**] 圖片的風格                       | **X**    | [Image - Style](https://adaptivecards.io/explorer/Image.html) |
| ItemBackground       | [**清單項目**] 背景 Style 或 背景圖片           | **O**    | [Container - Style](https://adaptivecards.io/explorer/Container.html) |

