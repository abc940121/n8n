# WeCom Fact Card

> 明細卡片



## ◆ Screenshot  





## ◆ Schema

繼承自 [MessageContent](MessageContent.md)

| 屬性           | 資料型態                                     | 必要屬性 | 描述                                                     | 支援變數 | 版本 |
| -------------- | -------------------------------------------- | -------- | -------------------------------------------------------- | -------- | ---- |
| *Type*         | string                                       | Y        | 類型，值為 `wecom.card.fact`                             | **X**    | 1.21 |
| **Title**      | string                                       | Y        | 主標題，字數最多 **36** 個字                             | **O**    | 1.21 |
| **Subtitle**   | string                                       | N        | 副標題，字數最多 **44** 個字                             | **O**    | 1.21 |
| **Text**       | string                                       | N        | 內文，字數最多 **160** 個字                              | **O**    | 1.21 |
| **Items**      | [WeComFactItem](#-wecom-fact-item)[]         | Y        | 明細表，最多**5**筆資料                                  | **X**    | 1.21 |
| **Locale**     | string                                       | N        | 地區，用於處理Fact文字格式化，預設值為伺服器所使用的地區 | **X**    | 1.21 |
| **DataSource** | string                                       | Y        | 指定資料來源 (變數)                                      | **O**    | 1.21 |
| **Buttons**    | [WeComButtonAction](#-wecom-button-action)[] | Y        | 按鈕，最少**1**個、最多**6**個                           | **X**    | 1.21 |

### ● WeCom Fact Item

| 屬性       | 資料型態 | 必要屬性 | 描述                                 | 支援變數 | 版本 |
| ---------- | -------- | -------- | ------------------------------------ | -------- | ---- |
| Title      | string   | Y        | 標題                                 | **O**    | 1.21 |
| Text       | string   | Y        | 文字                                 | **O**    | 1.21 |
| TextType   | string   | N        | 文字資料型態，預設：`string`         | **X**    | 1.21 |
| TextFormat | string   | N        | 文字顯示的格式，需指定 Text DataType | **X**    | 1.21 |

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

### ● WeCom Button Action

| 屬性  | 資料型態 | 必要屬性 | 描述                           | 支援變數 | 版本 |
| ----- | -------- | -------- | ------------------------------ | -------- | ---- |
| Type  | string   | Y        | 類型                           | **X**    | 1.21 |
| Title | string   | Y        | 按鈕標題，字數最多 **10** 個字 | **O**    | 1.21 |
| Value | string   | Y        | 按鈕值，字數最多 **1024** 個字 | **O**    | 1.21 |
| Style | string   | N        | 按鈕樣式，預設值：`default`    | **X**    | 1.21 |

* **Button Type**

| 按鈕類型   | 描述                | 版本 |
| ---------- | ------------------- | ---- |
| `submit`   | 回覆訊息 (Postback) | 1.21 |
| `open_url` | 開啟連結            | 1.21 |

* **Button Style**

| 按鈕類型     | 描述                | 版本 |
| ------------ | ------------------- | ---- |
| `default`    | 預設樣式 (藍底白字) | 1.21 |
| `blue_text`  | 藍字按鈕            | 1.21 |
| `red_text`   | 紅字按鈕            | 1.21 |
| `black_text` | 黑字按鈕            | 1.21 |



---

## ◆ Submit Button 的回傳內容

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

### ■ 未指定 DataSource

```json
{
    "Type": "wecom.card.fact",
    "Title": "請假明細",
    "Subtitle": "",
    "Text": "",
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
            "Title": "請假時間",
            "Text": "2019-12-11 09:00",
            "TextType": "date",
            "TextFormat": "yyyy-MM-dd HH:mm"
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
    "DataSource": "",
    "Locale": "",
    "Buttons": [
        {
            "Type": "submit",
            "Title": "Send",
            "Value": "1",
            "Style": "default"
        },
        {
            "Type": "url",
            "Title": "Open",
            "Value": "https://gss.com.tw",
            "Style": "front_blue"
		}
    ]
}
```

### ■ 指定 DataSource

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

```json
{
    "Type": "wecom.card.fact",
    "Title": "請假明細",
    "Subtitle": "",
    "Text": "",
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
            "TextFormat": "yyyy-MM-dd HH:mm"
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
    "DataSource": "$.Variables.LeaveInfo",
    "Locale": "",
    "Buttons": [
        {
            "Type": "submit",
            "Title": "Send",
            "Value": "1",
            "Style": "default"
        },
        {
            "Type": "url",
            "Title": "Open",
            "Value": "https://gss.com.tw",
            "Style": "front_blue"
		}
    ]
}
```

