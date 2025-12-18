# Adaptive Fact Card Content

> 制式的Adaptive Card 訊息，明細卡片



##  ◆ Screenshot  

* **單張明細卡片**

![](../Screenshots/FactCardContent.jpg)

* **多張明細卡片**

![](../Screenshots/FactCardContents.jpg)





## ◆ Channel Support

> [Adaptive Card 文件](https://adaptivecards.io/explorer/)

| Channel 類型            | 是否支援 | 備註                                                         |
| ----------------------- | -------- | ------------------------------------------------------------ |
| Emulator                | **O**    | Adaptive Card 支援的版本為 **1.3**                           |
| Web Chat、iota Chat Bot | **O**    | Adaptive Card 支援的版本為 **1.4**                           |
| iota                    | **O**    | Adaptive Card 支援的版本為 **1.5**                           |
| LINE                    | **O**    | 實作上會的轉成 LINE Flex Message                             |
| Teams                   | **O**    | 1. Adaptive Card 支援的版本為 **1.1**<br />2. 不支援 Audio 和 Video 等元件 |
| Slack                   | **X**    | 計畫中...                                                    |
| Webex                   | **O**    | 1. Adaptive Card 支援的版本為 **1.3**<br />2. 按鈕數量最多5個<br />3. 不支援多張卡片 |
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
| *Type*                        | string                                                       | Y        | 類型，值為 `adaptive.card.fact`                              | **X**    | 1.1   |
| **Title**                     | string                                                       | N        | 標題                                                         | **O**    | 1.1   |
| **ImageUrl**                  | string                                                       | N        | 圖片                                                         | **O**    | 1.1   |
| **Items**                     | [AdaptiveFactContent[]](#-adaptive-fact-content)             | N        | 明細表                                                       | **X**    | 1.1   |
| **Buttons**                   | [AdaptiveActionContent[]](ActionContent.md#adaptive-action-content) | N        | 按鈕                                                         | **X**    | 1.1   |
| **DataSource**                | string                                                       | Y        | 指定資料來源 (變數)                                          | **O**    | 1.1   |
| [**Styles**](#-style-options) | <string, string>                                             | N        | UI 樣式                                                      | **X**    | 1.1   |
| **Locale**                    | string                                                       | N        | 地區，用於處理Fact文字格式化，預設值為伺服器所使用的地區     | **X**    | 1.1   |
| *QuickReply*                  | [ButtonContent[]](Components/ButtonContent.md)               | N        | 快速回覆按鈕                                                 | **X**    | 1.1   |
| *ChannelDataPayload*          | object                                                       | N        | Channel Data Payload，[使用限制](../Components/ChannelDataPayload.md) | **O**    | 1.14  |
| *Options*                     | [MessageContentOption](../AdaptiveCardContent.md#-message-content-option) | `[1]`    | 訊息相關參數，僅限 [Bot 通知訊息服務 (ETA)](https://git.gss.com.tw/fpsbu/bot_event_trigger_service) 發送通知訊息使用 | **X**    | **X** |

* `[1]` 這個參數僅限 [Bot 通知訊息服務 (ETA)](https://git.gss.com.tw/fpsbu/bot_event_trigger_service) 發送通知訊息使用
    * 這個參數不適用 Bot Flow Engine 主程式，Bot Flow Engine 主程式只在 [appsettings.json 設定](../../AppSetting.md)



### ■ Adaptive Fact Content

| 屬性       | 資料型態 | 必要屬性 | 描述                                | 支援變數 或 指定 DataSource | 版本 |
| ---------- | -------- | -------- | ----------------------------------- | --------------------------- | ---- |
| Title      | string   | Y        | 標題                                | **O **                      | 1.1  |
| Text       | string   | Y        | 文字                                | **O**                       | 1.1  |
| TextType   | string   | N        | 文字資料型態，預設：`string`        | **X**                       | 1.1  |
| TextFormat | string   | N        | 文字顯示的格式，需指定 TextDataType | **X**                       | 1.1  |

* **Text Type**
    * `string` ─ 字串 (預設)
    * `integer` ─ 整數
    * `float` ─ 浮點數
    * `date` ─ 日期時間
    * `timespan` ─ 時間差
* **Text Format **
    * [標準數值格式字串](https://docs.microsoft.com/zh-tw/dotnet/standard/base-types/standard-numeric-format-strings)
    * [自訂數值格式字串](https://docs.microsoft.com/zh-tw/dotnet/standard/base-types/custom-numeric-format-strings)
    * [標準日期和時間格式字串](https://docs.microsoft.com/zh-tw/dotnet/standard/base-types/standard-date-and-time-format-strings)
    * [自訂日期與時間格式字串](https://docs.microsoft.com/zh-tw/dotnet/standard/base-types/custom-date-and-time-format-strings)
    * [標準 TimeSpan 格式字串](https://docs.microsoft.com/zh-tw/dotnet/standard/base-types/standard-timespan-format-strings)
    * [自訂 TimeSpan 格式字串](https://docs.microsoft.com/zh-tw/dotnet/standard/base-types/custom-timespan-format-strings)
* **Locale**
    * [Locale Code](http://www.codedigest.com/CodeDigest/207-Get-All-Language-Country-Code-List-for-all-Culture-in-C---ASP-Net.aspx)



## ◆ Example

### ■ 未指定 DataSource

> 當 DataSource 未設定時，預設使用所有的自動變數與自訂變數

* **輸出的卡片為單張明細卡片**

![](../Screenshots/FactCardContent.jpg)

```json
{
    "Type": "adaptive.card.fact",
    "Title": "請假明細",
    "ImageUrl": "",
    "Items": [
        {
            "Title": "申請人",
            "Text": "{{$.Conversation.UserName}}",
            "TextType": "string",
            "TextFormat": ""
        },
        {
            "Title": "假別",
            "Text": "特休假",
            "TextType": "string",
            "TextFormat": ""
        },
        {
            "Title": "請假日期",
            "Text": "2019-12-11 09:00",
            "TextType": "date",
            "TextFormat": "yyyy-MM-dd"
        },
        {
            "Title": "開始時間",
            "Text": "2019-12-11 09:00",
            "TextType": "date",
            "TextFormat": "HH:mm"
        },
        {
            "Title": "請假時數",
            "Text": "8",
            "TextType": "float",
            "TextFormat": "# hr"
        },
        {
            "Title": "請假事由",
            "Text": "特休",
            "TextType": "string",
            "TextFormat": ""
        }
    ],
    "Buttons": [
        {
            "Type": "submit.text",
            "Title": "送出",
            "Value": "1",
            "Style": "positive"
        },
        {
            "Type": "submit.text",
            "Title": "取消",
            "Value": "2",
            "Style": "default"
        }
    ],
    "DataSource": "",
    "Styles": {
        "TitleSize": "Large",
        "TitleColor": "Accent"
    },
    "Locale": ""
}
```



### ■ 指定 DataSouce (內容為一個物件)

* **輸出的卡片為單張明細卡片**

![](../Screenshots/FactCardContent.jpg)

* **變數名稱** ─ `$.Variables.LeaveInfo`

```json
{
    "Applicant": "張三",
    "LeaveType": "特休假",
    "StartDate": "2019-12-11 09:00",
    "LeaveHours": "8",
    "Subject": "特休"
}
```

* **Json**
    * **`Facts 能夠使用的變數只限 Data Source 指定的內容，因此不支援自動變數與自訂變數`**
    * 若要使用自動變數、自訂變數，請將所需的資料事先匯入到 DataSource

```json
{
    "Type": "adaptive.card.fact",
    "Title": "請假明細",
    "ImageUrl": "",
    "Items": [
        {
            "Title": "申請人",
            "Text": "{{$.Applicant}}",
            "TextType": "string",
            "TextFormat": ""
        },
        {
            "Title": "假別",
            "Text": "{{$.LeaveType}}",
            "TextType": "string",
            "TextFormat": ""
        },
        {
            "Title": "請假日期",
            "Text": "{{$.StartDate}}",
            "TextType": "date",
            "TextFormat": "yyyy-MM-dd"
        },
        {
            "Title": "開始時間",
            "Text": "{{$.StartDate}}",
            "TextType": "date",
            "TextFormat": "HH:mm"
        },
        {
            "Title": "請假時數",
            "Text": "{{$.LeaveHours}}",
            "TextType": "float",
            "TextFormat": "# hr"
        },
        {
            "Title": "請假事由",
            "Text": "{{$.Subject}}",
            "TextType": "string",
            "TextFormat": ""
        }
    ],
    "Buttons": [
        {
            "Type": "submit.text",
            "Title": "送出",
            "Value": "1",
            "style": "positive"
        },
        {
            "Type": "submit.text",
            "Title": "取消",
            "Value": "2",
            "style": "default"
        }
    ],
    "DataSource": "$.Variables.LeaveInfo",
    "Styles": {},
    "Locale": ""
}
```



### ■ 指定 DataSouce (內容為一個陣列)

* **輸出的卡片為多張明細卡片**

![](../Screenshots/FactCardContents.jpg)

* **變數名稱** ─ `$.Variables.UserProfiles`

```json
[
    {
        "Applicant": "張三",
        "LeaveType": "特休假",
        "StartDate": "2019-12-11 09:00",
        "LeaveHours": "8",
        "Subject": "特休"
    },
    {
        "Applicant": "張三",
        "LeaveType": "特休假",
        "StartDate": "2019-12-12 09:00",
        "LeaveHours": "8",
        "Subject": "特休"
    },
    {
        "Applicant": "張三",
        "LeaveType": "特休假",
        "StartDate": "2019-12-13 09:00",
        "LeaveHours": "8",
        "Subject": "特休"
    }
]
```

* **Json**
    * **`Facts 能夠使用的變數只限 Data Source 指定的內容，因此不支援自動變數與自訂變數`**
    * 若要使用自動變數、自訂變數，請將所需的資料事先匯入到 DataSource

```json
{
    "Type": "adaptive.card.fact",
    "Title": "請假明細",
    "ImageUrl": "",
    "Items": [
        {
            "Title": "申請人",
            "Text": "{{$.Applicant}}",
            "TextType": "string",
            "TextFormat": ""
        },
        {
            "Title": "假別",
            "Text": "{{$.LeaveType}}",
            "TextType": "string",
            "TextFormat": ""
        },
        {
            "Title": "請假日期",
            "Text": "{{$.StartDate}}",
            "TextType": "date",
            "TextFormat": "yyyy-MM-dd"
        },
        {
            "Title": "開始時間",
            "Text": "{{$.StartDate}}",
            "TextType": "date",
            "TextFormat": "HH:mm"
        },
        {
            "Title": "請假時數",
            "Text": "{{$.LeaveHours}}",
            "TextType": "float",
            "TextFormat": "# hr"
        },
        {
            "Title": "請假事由",
            "Text": "{{$.Subject}}",
            "TextType": "string",
            "TextFormat": ""
        }
    ],
    "Buttons": [
        {
            "Type": "submit.text",
            "Title": "送出",
            "Value": "1",
            "Style": "positive"
        },
        {
            "Type": "submit.text",
            "Title": "取消",
            "Value": "2",
            "Style": "default"
        }
    ],
    "DataSource": "$.Variables.LeaveInfo",
    "Styles": {},
    "Locale": ""
}
```



## ◆ Style Options

> 有需要在使用，沒有設定的項目會使用預設值

| 樣式選項       | 說明                           | 支援變數 | 參考                                                         |
| -------------- | ------------------------------ | -------- | ------------------------------------------------------------ |
| TitleSize      | 標題字型大小，預設： `Medium`  | **X**    | [Text Block - Size](https://adaptivecards.io/explorer/TextBlock.html) |
| TitleColor     | 標題字型顏色，預設： `Default` | **X**    | [Text Block - Color](https://adaptivecards.io/explorer/TextBlock.html) |
| TitleWeight    | 標題字型粗細，預設： `Bolder`  | **X**    | [Text Block - Weight](https://adaptivecards.io/explorer/TextBlock.html) |
| TitleAlignment | 標題對齊方式，預設： `Left`    | **X**    | [Text Block - Horizontal Alignment](https://adaptivecards.io/explorer/TextBlock.html) |
| ImageSize      | 圖片大小，預設：`Medium`       | **X**    | [Image - Size](https://adaptivecards.io/explorer/Image.html) |
| ImageStyle     | 圖片的風格                     | **X**    | [Image - Style](https://adaptivecards.io/explorer/Image.html) |
| CardLayout     | 卡片的排版，預設：`carousel`   | **X**    | ● **carousel**：左右並排<br />● **list**：上下排列           |

