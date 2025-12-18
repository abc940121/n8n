# LINE Fact Card Content

> 制式的Line Flex Message 訊息，明細卡片



##  ◆ Screenshot  

* **單張明細卡片**

![](Screenshots/FactCardContent.jpg)

* **多張明細卡片**

![](Screenshots/FactCardContents.jpg)



## ◆ Channel Support

> [LINE Flex Message 文件](https://developers.line.biz/en/reference/messaging-api/#message-objects)

| Channel 類型        | 是否支援 | 備註                       |
| ------------------- | -------- | -------------------------- |
| Emulator            | **O**    | 實作上會轉成 Adaptive Card |
| Web Chat            | **O**    | 實作上會轉成 Adaptive Card |
| iota                | **O**    | 實作上會轉成 Adaptive Card |
| LINE                | **O**    |                            |
| Teams               | **O**    | 實作上會轉成 Adaptive Card |
| Slack               | **X**    |                            |
| Webex               | **O**    | 實作上會轉成 Adaptive Card |
| Facebook Messenger  | **X**    |                            |
| WhatsApp            | **X**    |                            |
| Telegram            | **X**    |                            |
| M+                  | **X**    |                            |
| WeChat (微信個人號) | **X**    |                            |
| WeCom (企業微信)    | **X**    |                            |
| DingTalk            | **X**    |                            |
| Apple Business Chat | **X**    |                            |



## ◆ Schema

繼承自 [MessageContent](../MessageContent.md)

| 屬性                          | 資料型態                                          | 必要屬性 | 描述                                                     | 支援變數 | 版本 |
| ----------------------------- | ------------------------------------------------- | -------- | -------------------------------------------------------- | -------- | ---- |
| *Type*                        | string                                            | Y        | 類型，值為 `line.flex.card.fact`                         | **X**    | 1.5  |
| **AltText**                   | string                                            | Y        | 聊天室清單顯示的文字                                     | **O**    | 1.5  |
| **Title**                     | string                                            | N        | 卡片標題                                                 | **O**    | 1.5  |
| **ImageUrl**                  | string                                            | N        | 卡片圖片                                                 | **O**    | 1.5  |
| **Items**                     | [LineFlexFactContent[]](#-line-flex-fact-content) | N        | 明細表                                                   | **X**    | 1.5  |
| **Buttons**                   | [LineFlexActionContent[]](ActionContent.md)       | N        | 卡片按鈕                                                 | **X**    | 1.5  |
| **DataSource**                | string                                            | Y        | 指定資料來源 (變數)                                      | **O**    | 1.5  |
| [**Styles**](#-style-options) | <string, string>                                  | N        | UI 樣式                                                  | **X**    | 1.5  |
| **Locale**                    | string                                            | N        | 地區，用於處理Fact文字格式化，預設值為伺服器所使用的地區 | **X**    | 1.5  |
| *QuickReply*                  | [LineButtonContent[]](LineActionContent.md)       | N        | 快速回覆按鈕                                             | **X**    | 1.1  |

> **AltText 必須要給值，值要給有效值字元、不能給空白字元**

* **AltText 在 LINE 上的顯示**

![](Screenshots/AltText.jpg)



### ■ Line Flex Fact Content

| 屬性       | 資料型態 | 必要屬性 | 描述                                | 支援變數 或 指定 DataSource | 版本 |
| ---------- | -------- | -------- | ----------------------------------- | --------------------------- | ---- |
| Title      | string   | Y        | 標題                                | **O**                       | 1.5  |
| Text       | string   | Y        | 文字                                | **O**                       | 1.5  |
| TextType   | string   | N        | 文字資料型態，預設：`string`        | **X**                       | 1.5  |
| TextFormat | string   | N        | 文字顯示的格式，需指定 TextDataType | **X**                       | 1.5  |

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

![](Screenshots/FactCardContent.jpg)

```json
{
    "Type": "line.flex.card.fact",
    "AltText": "您有一張假單待批示：{{$.Applicant}} 申請的請假申請單請您當代理人",
    "Title": "請假明細",
    "ImageUrl": "https://cai-ut.gss.com.tw/botbuilder/static/media/chatbot-logo.66b4aa8c.png",
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
            "Type": "message",
            "Title": "送出",
            "Value": "Send"
        },
        {
            "Type": "message",
            "Title": "取消",
            "Value": "Cancel"
        }
    ],
    "DataSource": "",
    "Styles": {
        "TitleSize": "xxl",
        "TitleColor": "#0061AD",
        "ImageSize": "lg"
    },
    "Locale": ""
}
```



### ■ 指定 DataSouce (內容為一個物件)

* **輸出的卡片為單張明細卡片**

![](Screenshots/FactCardContent.jpg)

* **變數名稱** ─ `$.Variables.LeaveInfo`

```json
{
    "WorkItemId": "wk201912070003",
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
    "Type": "line.flex.card.fact",
    "AltText": "您有多張假單待批示：{{$.Applicant}} 申請的請假申請單請您當代理人",
    "Title": "請假明細",
    "ImageUrl": "https://cai-ut.gss.com.tw/botbuilder/static/media/chatbot-logo.66b4aa8c.png",
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
            "Type": "message",
            "Title": "送出",
            "Value": "Send"
        },
        {
            "Type": "message",
            "Title": "取消",
            "Value": "Cancel"
        }
    ],
    "DataSource": "$.Variables.LeaveInfo",
    "Styles": {
        "TitleSize": "xxl",
        "TitleColor": "#0061AD",
        "ImageSize": "lg"
    },
    "Locale": ""
}
```



### ■ 指定 DataSouce (內容為一個陣列)

* **輸出的卡片為多張明細卡片**

![](Screenshots/FactCardContents.jpg)

* **變數名稱** ─ `$.Variables.LeaveInfoList`

```json
[
    {
        "WorkItemId": "wk201912070003",
        "Applicant": "張三",
        "LeaveType": "特休假",
        "StartDate": "2019-12-11 09:00",
        "LeaveHours": "8",
        "Subject": "特休"
    },
    {
        "WorkItemId": "wk201912090054",
        "Applicant": "張三",
        "LeaveType": "事假",
        "StartDate": "2019-12-12 09:00",
        "LeaveHours": "8",
        "Subject": "我有事"
    },
    {
        "WorkItemId": "wk201912100044",
        "Applicant": "張三",
        "LeaveType": "特休假",
        "StartDate": "2019-12-13 09:00",
        "LeaveHours": "8",
        "Subject": "休假"
    }
]
```

* **Json**
    * **`Facts 能夠使用的變數只限 Data Source 指定的內容，因此不支援自動變數與自訂變數`**
    * 若要使用自動變數、自訂變數，請將所需的資料事先匯入到 DataSource

```json
{
    "Type": "line.flex.card.fact",
    "Title": "請假明細",
    "ImageUrl": "https://cai-ut.gss.com.tw/botbuilder/static/media/chatbot-logo.66b4aa8c.png",
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
            "Type": "message",
            "Title": "送出",
            "Value": "{{$.WorkItemId}}#Send"
        },
        {
            "Type": "message",
            "Title": "取消",
            "Value":"{{$.WorkItemId}}#Cancel"
        }
    ],
    "DataSource": "$.Variables.LeaveInfoList",
    "Styles": {
        "TitleSize": "xxl",
        "TitleColor": "#0061AD",
        "ImageSize": "lg"
    },
    "Locale": ""
}
```



## ◆ Style Options

> 有需要在使用，沒有設定的項目會使用預設值

* [Flex Message Text Component 屬性參考](https://developers.line.biz/en/reference/messaging-api/#f-text)
* [Flex Message Image Component 屬性參考](https://developers.line.biz/en/reference/messaging-api/#f-image)
* [Flex Message Button Component 屬性參考](https://developers.line.biz/en/reference/messaging-api/#button)

| 樣式選項           | 說明                                                         | 支援變數 | 參考值                                                       |
| ------------------ | ------------------------------------------------------------ | -------- | ------------------------------------------------------------ |
| TitleSize          | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片標題字型大小，預設： `lg` | **X**    | `xxs`、`xs`、`sm`<br />、`md`、`lg`、`xl`、<br />`xxl`、`3x1`、`4xl`、`5xl` |
| TitleColor         | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片標題字型顏色，預設： `#0061AD` | **X**    | 符合 `#RRGGBB` or `#RRGGBBAA` 格式                           |
| TitleWeight        | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片標題字型粗細，預設： `bold` | **X**    | `regular`、`bold` (粗體)                                     |
| TitleStyle         | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片標題是否為斜體，預設： `normal` | **X**    | `normal`、`italic` (斜體)                                    |
| TitleDecoration    | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片標題是否加上底線或刪除線，預設： `none` | **X**    | `none`、`underline` (底線)、`line-through` (刪除線)          |
| TitleAlignment     | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片標題對齊方式，預設： `start` | **X**    | `start` (靠左)、`center` (置中)、`end` (靠右)                |
| ImageSize          | **[[Image]](https://developers.line.biz/en/reference/messaging-api/#f-image)** 圖片大小，預設：`md` | **X**    | `xxs`、`xs`、`sm`<br />、`md`、`lg`、`xl`、<br />`xxl`、`3x1`、`4xl`、`5xl`、`full` |
| ImageAspectMode    | **[[Image]](https://developers.line.biz/en/reference/messaging-api/#f-image)** 圖片長寬排版，預設：`cover` | **X**    | `fit` (符合圖片)、`cover` (延伸圖片)                         |
| ImageAspectRatio   | **[[Image]](https://developers.line.biz/en/reference/messaging-api/#f-image)** 圖片長寬比率，預設：`<無設定>` | **X**    | 符合 `{width}:{height}` 格式，例如：`1920:1080`              |
| ButtonHeight       | **[[Button]](https://developers.line.biz/en/reference/messaging-api/#button)** 按鈕大小，預設：`sm` | **X**    | `sm`、`md`                                                   |
| ButtonStyle        | **[[Button]](https://developers.line.biz/en/reference/messaging-api/#button)** 按鈕背景樣式，預設：`secondary` | **X**    | ● `link` ：連結<br />● `primary` ：白色標題、深色背景<br />● `secondary` ：黑色標題、淺色背景 |
| ButtonColor        | **[[Button]](https://developers.line.biz/en/reference/messaging-api/#button)** 按鈕背景顏色，預設：`<未設定>` | **X**    | 符合 `#RRGGBB` or `#RRGGBBAA` 格式                           |
| FactKeySize        | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 明細標題字型大小，預設： `xs` | **X**    | `xxs`、`xs`、`sm`<br />、`md`、`lg`、`xl`、<br />`xxl`、`3x1`、`4xl`、`5xl` |
| FactKeyColor       | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 明細標題字型顏色，預設： `#000000` | **X**    | 符合 `#RRGGBB` or `#RRGGBBAA` 格式                           |
| FactKeyWeight      | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 明細標題字型粗細，預設： `bold` | **X**    | `regular`、`bold` (粗體)                                     |
| FactKeyAlignment   | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片標題對齊方式，預設： `start` | **X**    | `start` (靠左)、`center` (置中)、`end` (靠右)                |
| FactValueSize      | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 明細項目字型大小，預設： `xs` | **X**    | `xxs`、`xs`、`sm`<br />、`md`、`lg`、`xl`、<br />`xxl`、`3x1`、`4xl`、`5xl` |
| FactValueColor     | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 明細項目字型顏色，預設： `#000000` | **X**    | 符合 `#RRGGBB` or `#RRGGBBAA` 格式                           |
| FactValueWeight    | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 明細項目字型粗細，預設： `regular` | **X**    | `regular`、`bold` (粗體)                                     |
| FactValueAlignment | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片標題對齊方式，預設： `start` | **X**    | `start` (靠左)、`center` (置中)、`end` (靠右)                |

