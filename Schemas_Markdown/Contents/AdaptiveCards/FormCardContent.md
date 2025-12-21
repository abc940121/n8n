# Adaptive Form Card Content

> 制式的Adaptive Card 訊息，表單卡片



## ◆ Screenshot

![](../Screenshots/FormCardContent.jpg)



## ◆ Channel Support

> [Adaptive Card 文件](https://adaptivecards.io/explorer/)

| Channel 類型            | 是否支援 | 備註                                                         |
| ----------------------- | -------- | ------------------------------------------------------------ |
| Emulator                | **O**    | Adaptive Card 支援的版本為 **1.3**                           |
| Web Chat、iota Chat Bot | **O**    | Adaptive Card 支援的版本為 **1.4**                           |
| iota                    | **O**    | Adaptive Card 支援的版本為 **1.5**                           |
| LINE                    | **X**    |                                                              |
| Teams                   | **O**    | 1. Adaptive Card 支援的版本為 **1.1**<br />2. 不支援 Audio 和 Video 等元件 |
| Slack                   | **X**    |                                                              |
| Webex                   | **O**    | 1. Adaptive Card 支援的版本為 **1.3**<br />2. 按鈕數量最多5個 |
| Facebook Messenger      | **X**    |                                                              |
| WhatsApp                | **X**    |                                                              |
| Telegram                | **X**    |                                                              |
| M+                      | **X**    |                                                              |
| WeChat (微信個人號)     | **X**    |                                                              |
| WeCom (企業微信)        | **X**    |                                                              |
| DingTalk                | **X**    |                                                              |
| Apple Business Chat     | **X**    |                                                              |



## ◆ Schema

繼承自 [MessageContent](../MessageContent.md)

| 屬性                 | 資料型態                                                     | 必要屬性 | 描述                                                         | 支援變數 | 版本  |
| -------------------- | ------------------------------------------------------------ | -------- | ------------------------------------------------------------ | -------- | ----- |
| Type                 | string                                                       | Y        | 類型，值為 `adaptive.card.form`                              | **X**    | 1.4   |
| Title                | string                                                       | N        | 標題                                                         | **O**    | 1.4   |
| **Forms**            | AdaptiveFormInput[]                                          | Y        | 表單輸入項目                                                 | **X**    | 1.4   |
| **Buttons**          | [AdaptiveButtonContent[]](ActionContent.md#adaptive-action-content) | N        | Card 按鈕                                                    | **X**    | 1.4   |
| **Styles**           | FormStyles                                                   | N        | 卡片樣式                                                     | **O**    | 1.4   |
| **DataSource**       | string                                                       | N        | 指定資料來源 (自訂變數)，設定預設值                          | **O**    | 1.4   |
| *QuickReply*         | [ButtonContent[]](Components/ButtonContent.md)               | N        | 快速回覆按鈕                                                 | **X**    | 1.1   |
| *ChannelDataPayload* | object                                                       | N        | Channel Data Payload，[使用限制](../Components/ChannelDataPayload.md) | **O**    | 1.14  |
| *Options*            | [MessageContentOption](../AdaptiveCardContent.md#-message-content-option) | `[1]`    | 訊息相關參數，僅限 [Bot 通知訊息服務 (ETA)](https://git.gss.com.tw/fpsbu/bot_event_trigger_service) 發送通知訊息使用 | **X**    | **X** |

* `[1]` 這個參數僅限 [Bot 通知訊息服務 (ETA)](https://git.gss.com.tw/fpsbu/bot_event_trigger_service) 發送通知訊息使用
    * 這個參數不適用 Bot Flow Engine 主程式，Bot Flow Engine 主程式只在 [appsettings.json 設定](



### ● Base Form Input

| 屬性    | 資料型態 | 必要屬性 | 描述                                                         | 支援變數 或 指定 DataSource | 版本 |
| ------- | -------- | -------- | ------------------------------------------------------------ | --------------------------- | ---- |
| *Id*    | string   | Y        | 輸入欄位 ID <br />**● `不得重複`**<br />**● `不得與 submit data 物件成員名稱重複`** | **X**                       | 1.4  |
| *Title* | string   | N        | 輸入欄位標題，預設值：空字串                                 | **O**                       | 1.4  |
| *Type*  | string   | Y        | 輸入欄位類型                                                 | **X**                       | 1.4  |

* **Form Input Type**

| 類型                               | 類型值      | 描述         |
| ---------------------------------- | ----------- | ------------ |
| **[Label](#-label)**               | `label`     | 靜態文字     |
| **[Image](#-image)**               | `image`     | 圖片         |
| **[Text](#-text-input)**           | `text`      | 文字輸入     |
| **[Number](#-number-input)**       | `number`    | 數字輸入     |
| **[Date](#-date-input)**           | `date`      | 日期輸入     |
| **[Time](#-time-input)**           | `time`      | 時間輸入     |
| **[Combo Box](#-combo-box-input)** | `combo_box` | 下拉選項輸入 |
| **[Radio Box](#-radio-box-input)** | `radio_box` | 單選輸入     |
| **[Check Box](#-check-box-input)** | `check_box` | 多選輸入     |
| **[Toggle](#-toggle-input)**       | `toggle`    | 勾選輸入     |

### ● Label

> 靜態文字

| 屬性                        | 資料型態                   | 必要屬性 | 描述                     | 支援變數 或 指定 DataSource | 版本 |
| --------------------------- | -------------------------- | -------- | ------------------------ | --------------------------- | ---- |
| *Id*                        | string                     | Y        | 欄位 ID **`(不得重複)`** | **X**                       | 1.4  |
| *Title*                     | string                     | Y        | 欄位標題                 | **O**                       | 1.4  |
| *Type*                      | string                     | Y        | 欄位類型，值為 `label`   | **X**                       | 1.4  |
| **Value**                   | string                     | N        | 欄位資料值，預設值：空白 | **O**                       | 1.4  |
| **[Styles](#-label-style)** | Dictionary<string, string> | N        | 欄位資料樣式             | **X**                       | 1.4  |

### ● Image

> 靜態圖片

| 屬性                        | 資料型態                   | 必要屬性 | 描述                     | 支援變數 或 指定 DataSource | 版本 |
| --------------------------- | -------------------------- | -------- | ------------------------ | --------------------------- | ---- |
| *Id*                        | string                     | Y        | 欄位 ID **`(不得重複)`** | **X**                       | 1.4  |
| *Title*                     | string                     | Y        | 欄位標題                 | **O**                       | 1.4  |
| *Type*                      | string                     | Y        | 欄位類型，值為 `image`   | **X**                       | 1.4  |
| **Value**                   | string                     | N        | 圖片連結，預設值：空白   | **O**                       | 1.4  |
| **[Styles](#-image-style)** | Dictionary<string, string> | N        | 圖片樣式                 | **X**                       | 1.4  |

> **`[1]` 變數和指定 DataSource 二選一，有設定指定 DataSource 就無法使用變數**

### ● Text Input

> 文字輸入

| 屬性                             | 資料型態                   | 必要屬性 | 描述                      | 支援變數 或 指定 DataSource | 版本 |
| -------------------------------- | -------------------------- | -------- | ------------------------- | --------------------------- | ---- |
| *Id*                             | string                     | Y        | 欄位 ID **`(不得重複)`**  | **X**                       | 1.4  |
| *Title*                          | string                     | Y        | 欄位標題                  | **O**                       | 1.4  |
| *Type*                           | string                     | Y        | 欄位類型，值為 `text`     | **X**                       | 1.4  |
| **Value**                        | string                     | N        | 預設值                    | **O**                       | 1.4  |
| **Placeholder**                  | string                     | N        | 提示文字                  | **O**                       | 1.4  |
| **[Styles](#-text-input-style)** | Dictionary<string, string> | N        | 文字輸入框樣式            | **X**                       | 1.4  |
| **IsRequired**                   | bool                       | N        | 是否必填，預設值：`false` | **X**                       | ??   |

> **`[1]` 變數和指定 DataSource 二選一，有設定指定 DataSource 就無法使用變數**

### ● Text Area

> 多行文字輸入

| 屬性                            | 資料型態                   | 必要屬性 | 描述                      | 支援變數 或 指定 DataSource | 版本 |
| ------------------------------- | -------------------------- | -------- | ------------------------- | --------------------------- | ---- |
| *Id*                            | string                     | Y        | 欄位 ID **`(不得重複)`**  | **X**                       | 1.7  |
| *Title*                         | string                     | Y        | 欄位標題                  | **O**                       | 1.7  |
| *Type*                          | string                     | Y        | 欄位類型，值為 `textarea` | **X**                       | 1.7  |
| **Value**                       | string                     | N        | 預設值                    | **O**                       | 1.7  |
| **Placeholder**                 | string                     | N        | 提示文字                  | **O**                       | 1.7  |
| **[Styles](#-text-area-style)** | Dictionary<string, string> | N        | 文字輸入框樣式            | **X**                       | 1.7  |
| **IsRequired**                  | bool                       | N        | 是否必填，預設值：`false` | **X**                       | ??   |

> **`[1]` 變數和指定 DataSource 二選一，有設定指定 DataSource 就無法使用變數**

### ● Number Input

> 數字輸入

| 屬性                               | 資料型態                   | 必要屬性 | 描述                      | 支援變數 或 指定 DataSource | 版本 |
| ---------------------------------- | -------------------------- | -------- | ------------------------- | --------------------------- | ---- |
| *Id*                               | string                     | Y        | 欄位 ID **`(不得重複)`**  | **X**                       | 1.4  |
| *Title*                            | string                     | Y        | 欄位標題                  | **O**                       | 1.4  |
| *Type*                             | string                     | Y        | 欄位類型，值為 `number`   | **X**                       | 1.4  |
| **Value**                          | string (Number String)     | N        | 預設值                    | **O**                       | 1.4  |
| **Placeholder**                    | string                     | N        | 提示文字                  | **O**                       | 1.4  |
| **[Styles](#-number-input-style)** | Dictionary<string, string> | N        | 數字輸入框樣式            | **X**                       | 1.4  |
| **IsRequired**                     | bool                       | N        | 是否必填，預設值：`false` | **X**                       | ??   |

> **`[1]` 變數和指定 DataSource 二選一，有設定指定 DataSource 就無法使用變數**

### ● Date Input

> 日期輸入

| 屬性                             | 資料型態                   | 必要屬性 | 描述                      | 支援變數 或 指定 DataSource | 版本 |
| -------------------------------- | -------------------------- | -------- | ------------------------- | --------------------------- | ---- |
| *Id*                             | string                     | Y        | 欄位 ID **`(不得重複)`**  | **X**                       | 1.4  |
| *Title*                          | string                     | Y        | 欄位標題                  | **O**                       | 1.4  |
| *Type*                           | string                     | Y        | 欄位類型，值為 `date`     | **X**                       | 1.4  |
| **Value**                        | string (Date String)       | N        | 預設值                    | **O**                       | 1.4  |
| **[Styles](#-date-input-style)** | Dictionary<string, string> | N        | 日期輸入框樣式            | **X**                       | 1.4  |
| **IsRequired**                   | bool                       | N        | 是否必填，預設值：`false` | **X**                       | ??   |

> **`[1]` 變數和指定 DataSource 二選一，有設定指定 DataSource 就無法使用變數**

### ● Time Input

> 時間輸入

| 屬性                             | 資料型態                   | 必要屬性 | 描述                      | 支援變數 或 指定 DataSource | 版本 |
| -------------------------------- | -------------------------- | -------- | ------------------------- | --------------------------- | ---- |
| *Id*                             | string                     | Y        | 欄位 ID **`(不得重複)`**  | **X**                       | 1.4  |
| *Title*                          | string                     | Y        | 欄位標題                  | **O**                       | 1.4  |
| *Type*                           | string                     | Y        | 欄位類型，值為 `time`     | **X**                       | 1.4  |
| **Value**                        | string (Time String)       | N        | 預設值                    | **O**                       | 1.4  |
| **[Styles](#-time-input-style)** | Dictionary<string, string> | N        | 時間輸入框樣式            | **X**                       | 1.4  |
| **IsRequired**                   | bool                       | N        | 是否必填，預設值：`false` | **X**                       | ??   |

> **`[1]` 變數和指定 DataSource 二選一，有設定指定 DataSource 就無法使用變數**

### ● Toggle Input

> 勾選輸入

| 屬性                               | 資料型態                   | 必要屬性 | 描述                        | 支援變數 或 指定 DataSource | 版本 |
| ---------------------------------- | -------------------------- | -------- | --------------------------- | --------------------------- | ---- |
| *Id*                               | string                     | Y        | 欄位 ID **`(不得重複)`**    | **X**                       | 1.4  |
| *Title*                            | string                     | Y        | 欄位標題                    | **O**                       | 1.4  |
| *Type*                             | string                     | Y        | 欄位類型，值為 `toggle`     | **X**                       | 1.4  |
| **Value**                          | string                     | N        | 預設值                      | **O**                       | 1.4  |
| **Label**                          | string                     | N        | 勾選輸入標題                | **O**                       | 1.4  |
| **ValueOn**                        | string                     | Y        | 符合勾選的值，預設： `True` | **O**                       | 1.4  |
| **[Styles](#-toggle-input-style)** | Dictionary<string, string> | N        | 多選輸入樣式                | **X**                       | 1.4  |
| **IsRequired**                     | bool                       | N        | 是否必填，預設值：`false`   | **X**                       | ??   |

> **`[1]` 變數和指定 DataSource 二選一，有設定指定 DataSource 就無法使用變數**

### ● Combo Box Input

> 下拉選單輸入

| 屬性                                                      | 資料型態                             | 必要屬性 | 描述                       | 支援變數 或 指定 DataSource | 版本 |
| --------------------------------------------------------- | ------------------------------------ | -------- | -------------------------- | --------------------------- | ---- |
| *Id*                                                      | string                               | Y        | 欄位 ID **`(不得重複)`**   | **X**                       | 1.4  |
| *Title*                                                   | string                               | Y        | 欄位標題                   | **O**                       | 1.4  |
| *Type*                                                    | string                               | Y        | 欄位類型，值為 `combo_box` | **X**                       | 1.4  |
| **Value**                                                 | string                               | N        | 預設值                     | **O**                       | 1.4  |
| **Choices**                                               | [FormChoiceSet[]](#-form-choice-set) | Y        | 下拉選項                   | **O**                       | 1.4  |
| **ChoiceDataSource**                                      | string                               | N        | 下拉選項來源 (變數)        | **O**                       | 1.5  |
| **[Styles](#-combo-box-radio-box-check-box-input-style)** | Dictionary<string, string>           | N        | 下拉選單樣式               | **X**                       | 1.4  |
| **IsRequired**                                            | bool                                 | N        | 是否必填，預設值：`false`  | **X**                       | ??   |

> **`[1]` 變數和指定 DataSource 二選一，有設定指定 DataSource 就無法使用變數**

### ● Radio Box Input

> 單選輸入

| 屬性                                                      | 資料型態                             | 必要屬性 | 描述                       | 支援變數 或 指定 DataSource | 版本 |
| --------------------------------------------------------- | ------------------------------------ | -------- | -------------------------- | --------------------------- | ---- |
| *Id*                                                      | string                               | Y        | 欄位 ID **`(不得重複)`**   | **X**                       | 1.4  |
| *Title*                                                   | string                               | Y        | 欄位標題                   | **O**                       | 1.4  |
| *Type*                                                    | string                               | Y        | 欄位類型，值為 `radio_box` | **X**                       | 1.4  |
| **Value**                                                 | string                               | N        | 預設值                     | **O**                       | 1.4  |
| **Choices**                                               | [FormChoiceSet[]](#-form-choice-set) | Y        | 單選輸入選項               | **O**                       | 1.4  |
| **ChoiceDataSource**                                      | string                               | N        | 下拉選項來源 (變數)        | **O**                       | 1.5  |
| **[Styles](#-combo-box-radio-box-check-box-input-style)** | Dictionary<string, string>           | N        | 單選輸入樣式               | **X**                       | 1.4  |
| **IsRequired**                                            | bool                                 | N        | 是否必填，預設值：`false`  | **X**                       | ??   |

> **`[1]` 變數和指定 DataSource 二選一，有設定指定 DataSource 就無法使用變數**

### ● Check Box Input

> 多選輸入

| 屬性                                                      | 資料型態                             | 必要屬性 | 描述                       | 支援變數 或 指定 DataSource | 版本 |
| --------------------------------------------------------- | ------------------------------------ | -------- | -------------------------- | --------------------------- | ---- |
| *Id*                                                      | string                               | Y        | 欄位 ID **`(不得重複)`**   | **X**                       | 1.4  |
| *Title*                                                   | string                               | Y        | 欄位標題                   | **O**                       | 1.4  |
| *Type*                                                    | string                               | Y        | 欄位類型，值為 `check_box` | **X**                       | 1.4  |
| **Value**                                                 | string (CSV String)                  | N        | 預設值                     | **O**                       | 1.4  |
| **Choices**                                               | [FormChoiceSet[]](#-form-choice-set) | Y        | 多選輸入選項               | **O**                       | 1.4  |
| **ChoiceDataSource**                                      | string                               | N        | 下拉選項來源 (變數)        | **O**                       | 1.4  |
| **[Styles](#-combo-box-radio-box-check-box-input-style)** | Dictionary<string, string>           | N        | 多選輸入樣式               | **X**                       | 1.4  |
| **IsRequired**                                            | bool                                 | N        | 是否必填，預設值：`false`  | **X**                       | ??   |

#### Form Choice Set

| 屬性  | 資料型態 | 描述 | 支援變數 或 指定 DataSource | 版本 |
| ----- | -------- | ---- | --------------------------- | ---- |
| Title | string   | 標題 | **O**                       | 1.4  |
| Value | string   | 值   | **O**                       | 1.4  |

#### Form Choice DataSource

*  資料格式需要符合下面的格式
*  如果 Choices 有設定時，將會被覆寫

```json
[
    {
        "Title": "Title-1",
        "Value": "Value1"
    },
    {
        "Title": "Title-2",
        "Value": "Value2"
    }
]
```



## ◆ Example

### ■ 未指定 DataSource

> 當 DataSource 未設定時，預設使用所有的自動變數與自訂變數

![](../Screenshots/FormCardContent.jpg)

```json
{
    "Type": "adaptive.card.form",
    "Title": "請假申請單",
    "Forms": [
        {
            "Type": "text",
            "Id": "Applicant",
            "Title": "申請人*",
            "Value": "{{$.Conversation.UserName}}",
            "Placeholder": "請輸入請假申請人",
            "Styles": {
                "TitleColor": "Attention"
            }
        },
        {
            "Type": "label",
            "Id": "Agent",
            "Title": "填單人",
            "Value": "{{$.Conversation.UserName}}",
            "Styles": {
                "LabelColor": "Accent"
            }
        },
        {
            "Type": "combo_box",
            "Id": "LeaveType",
            "Title": "請假類別*",
            "Value": "00001",
            "Choices": [
                {
                    "Title": "特休假",
                    "Value": "00001"
                },
                {
                    "Title": "事假",
                    "Value": "00002"
                },
                {
                    "Title": "病假",
                    "Value": "00003"
                }
            ],
            "Styles": {
                "TitleColor": "Attention"
            }
        },
        {
            "Type": "date",
            "Id": "LeaveDate",
            "Title": "開始日期*",
            "Value": "2020-04-04",
            "Styles": {
                "TitleColor": "Attention",
                "InputMin": "2020-03-01",
                "InputMax": "2020-05-01"
            }
        },
        {
            "Type": "time",
            "Id": "LeaveTime",
            "Title": "開始時間*",
            "Value": "08:30",
            "Styles": {
                "TitleColor": "Attention"
            }
        },
        {
            "Type": "number",
            "Id": "LeaveHours",
            "Title": "請假時數*",
            "Value": "",
            "Placeholder": "請輸入請假時數 (0.5 ~ 8)",
            "Styles": {
                "TitleColor": "Attention",
                "InputMin": "0.5",
                "InputMax": "8"
            }
        },
        {
            "Type": "text",
            "Id": "LeaveSubject",
            "Title": "請假事由",
            "Value": "",
            "Placeholder": "請輸入請假事由",
            "Styles": {
                "IsTextArea": "true",
                "TextMaxLength": "300"
            }
        },
        {
            "Type": "toggle",
            "Id": "IsNotify",
            "Title": "請假通知",
            "Value": "true",
            "ValueOn": "true",
            "Label": "發送請假通知"
        },
        {
            "Type": "check_box",
            "Id": "Participant",
            "Title": "通知對象",
            "Value": "Level-0,Level-2",
            "Choices": [
                {
                    "Title": "代理人",
                    "Value": "Level-0"
                },
                {
                    "Title": "部門主管",
                    "Value": "Level-2"
                },
                {
                    "Title": "執行長",
                    "Value": "Level-1"
                }
            ]
        },
        {
            "Type": "radio_box",
            "Id": "NotifyType",
            "Title": "通知方式",
            "Value": "iota",
            "Choices": [
                {
                    "Title": "發送電子郵件通知",
                    "Value": "e-mail"
                },
                {
                    "Title": "發送iota訊息通知",
                    "Value": "iota"
                },
                {
                    "Title": "自行通知",
                    "Value": "custom"
                }
            ]
        }
    ],
    "Buttons": [
        {
            "Type": "submit.data",
            "Title": "送出",
            "Value": {
                "Action": "Send"
            },
            "Style": "positive"
        },
        {
            "Type": "submit.data",
            "Title": "取消",
            "Value": {
                "Action": "Cancel"
            },
            "Style": "destructive"
        }
    ],
    "Styles": {
        "CardTitleColor": "Accent",
        "CardTitleSize": "ExtraLarge",
        "CardTitleWeight": "Bolder"
    },
    "DataSource": ""
}
```



### ■ 指定 DataSource

![](../Screenshots/FormCardContent.jpg)

* **變數名稱** ─ `$.Variables.LeaveForms`

```json
{
    "Applicant": "張三",
    "Agent": "{{$.Conversation.UserName}}",
    "LeaveDate": "{{=> DateTime.Today.ToString(\"yyyy-MM-dd\");}}",
    "MinLeaveDate": "{{=> DateTime.Today.AddMonths(-1).ToString(\"yyyy-MM-dd\");}}",
    "MaxLeaveDate": "{{=> DateTime.Today.AddMonths(1).ToString(\"yyyy-MM-dd\");}}",
    "LeaveTime": "09:00",
    "LeaveHours": "8",
    "LeaveType": "00001",
    "LeaveSubject": "特休"
}
```

* **Json**
    * **`Forms 能夠使用的變數只限 Data Source 指定的內容，因此不支援自動變數與自訂變數`**
    * 若要使用自動變數、自訂變數，請將所需的資料事先匯入到 DataSource

```json
{
    "Type": "adaptive.card.form",
    "Title": "請假申請單",
    "Forms": [
        {
            "Type": "text",
            "Id": "Applicant",
            "Title": "申請人*",
            "Value": "{{$.Applicant}}",
            "Placeholder": "請輸入請假申請人",
            "Styles": {
                "TitleColor": "Attention"
            }
        },
        {
            "Type": "label",
            "Id": "Agent",
            "Title": "填單人",
            "Value": "{{$.Agent}}",
            "Styles": {
                "LabelColor": "Accent"
            }
        },
        {
            "Type": "combo_box",
            "Id": "LeaveType",
            "Title": "請假類別*",
            "Value": "{{$.LeaveType}}",
            "Choices": [
                {
                    "Title": "特休假",
                    "Value": "00001"
                },
                {
                    "Title": "事假",
                    "Value": "00002"
                },
                {
                    "Title": "病假",
                    "Value": "00003"
                }
            ],
            "Styles": {
                "TitleColor": "Attention"
            }
        },
        {
            "Type": "date",
            "Id": "LeaveDate",
            "Title": "開始日期*",
            "Value": "{{$.LeaveDate}}",
            "Styles": {
                "TitleColor": "Attention",
                "InputMin": "{{$.MinLeaveDate}}",
                "InputMax": "{{$.MaxLeaveDate}}"
            }
        },
        {
            "Type": "time",
            "Id": "LeaveTime",
            "Title": "開始時間*",
            "Value": "{{$.LeaveTime}}",
            "Styles": {
                "TitleColor": "Attention"
            }
        },
        {
            "Type": "number",
            "Id": "LeaveHours",
            "Title": "請假時數*",
            "Value": "{{$.LeaveHours}}",
            "Placeholder": "請輸入請假時數 (0.5 ~ 8)",
            "Styles": {
                "TitleColor": "Attention",
                "InputMin": "0.5",
                "InputMax": "8"
            }
        },
        {
            "Type": "text",
            "Id": "LeaveSubject",
            "Title": "請假事由",
            "Value": "{{$.LeaveSubject}}",
            "Placeholder": "請輸入請假事由",
            "Styles": {
                "IsTextArea": "true",
                "TextMaxLength": "300"
            }
        },
        {
            "Type": "toggle",
            "Id": "IsNotify",
            "Title": "請假通知",
            "Value": "true",
            "ValueOn": "true",
            "Label": "發送請假通知"
        },
        {
            "Type": "check_box",
            "Id": "Participant",
            "Title": "通知對象",
            "Value": "Level-0,Level-2",
            "Choices": [
                {
                    "Title": "代理人",
                    "Value": "Level-0"
                },
                {
                    "Title": "部門主管",
                    "Value": "Level-2"
                },
                {
                    "Title": "執行長",
                    "Value": "Level-1"
                }
            ]
        },
        {
            "Type": "radio_box",
            "Id": "NotifyType",
            "Title": "通知方式",
            "Value": "iota",
            "Choices": [
                {
                    "Title": "發送電子郵件通知",
                    "Value": "e-mail"
                },
                {
                    "Title": "發送iota訊息通知",
                    "Value": "iota"
                },
                {
                    "Title": "自行通知",
                    "Value": "custom"
                }
            ]
        }
    ],
    "Buttons": [
        {
            "Type": "submit.data",
            "Title": "送出",
            "Value": {
                "Action": "Send"
            },
            "Style": "positive"
        },
        {
            "Type": "submit.data",
            "Title": "取消",
            "Value": {
                "Action": "Cancel"
            },
            "Style": "destructive"
        }
    ],
    "Styles": {
        "CardTitleColor": "Accent",
        "CardTitleSize": "ExtraLarge",
        "CardTitleWeight": "Bolder"
    },
    "DataSource": "$.Variables.LeaveForms"
}
```



## ◆ Style Options

> 有需要在使用，沒有設定的項目會使用預設值

### ■ Form Style

> 全域樣式

| 屬性                                                         | 資料型態                   | 必要屬性 | 描述                                                         | 支援變數 | 版本 |
| ------------------------------------------------------------ | -------------------------- | -------- | ------------------------------------------------------------ | -------- | ---- |
| **[Card](#-from-card-st)**                                   | Dictionary<string, string> | N        | Form Card                                                    | **O**    | 1.5  |
| **[Label](#-label-style)**                                   | Dictionary<string, string> | N        | [Label](#-label) Style                                       | **O**    | 1.5  |
| **[Image](#-image-style)**                                   | Dictionary<string, string> | N        | [Image](#-image) Style                                       | **O**    | 1.5  |
| **[TextInput](#-text-input-style)**                          | Dictionary<string, string> | N        | [Text Input](#-text-input) Style                             | **O**    | 1.5  |
| **[NumberInput](#-number-input-style)**                      | Dictionary<string, string> | N        | [Number Input](#-number-input) Style                         | **O**    | 1.5  |
| **[DateInput](#-date-input-style)**                          | Dictionary<string, string> | N        | [DateInput](#-date-input) Style                              | **O**    | 1.5  |
| **[TimeInput](#-time-input-style)**                          | Dictionary<string, string> | N        | [Time Input](#-time-input) Style                             | **O**    | 1.5  |
| **[ChoiceInput](#-combo-box-radio-box-check-box-input-style)** | Dictionary<string, string> | N        | ● [Combo Box Input](#-combo-box-input) Style<br />● [Radio Box Input](#-radio-box-input) Style<br />● [Check Box Input](#-check-box-inpit) Style | **O**    | 1.5  |
| **[ToggleInput](#-toggle-input-style)**                      | Dictionary<string, string> | N        | [Toggle Input](#-toggle-input) Style                         | **O**    | 1.5  |



### ■ Form Card Style

> 卡片樣式

| 樣式選項           | 說明                                      | 支援變數 | 參考                                                         |
| ------------------ | ----------------------------------------- | -------- | ------------------------------------------------------------ |
| CardTitleColor     | [**卡片**] 標題字型顏色，預設： `Default` | **X**    | [Text Block - Color](https://adaptivecards.io/explorer/TextBlock.html) |
| CardTitleSize      | [**卡片**] 標題字型大小，預設： `Medium`  | **X**    | [Text Block - Size](https://adaptivecards.io/explorer/TextBlock.html) |
| CardTitleWeight    | [**卡片**] 標題字型粗細，預設： `Bolder`  | **X**    | [Text Block - Weight](https://adaptivecards.io/explorer/TextBlock.html) |
| CardTitleAlignment | [**卡片**] 標題對齊方式，預設： `Left`    | **X**    | [Text Block - Horizontal Alignment](https://adaptivecards.io/explorer/TextBlock.html) |
| FormTitleWidth     | 標題寬度                                  | **X**    | 按照比例                                                     |
| FormInputWidth     | 輸入欄寬度                                | **X**    | 按照比例                                                     |
| FormLayout         | 標題和輸入欄的排版，預設： `Horizontal`   | **X**    | ● `Horizontal`：標題和輸入欄左右排列<br />● `Vertical`：標題和輸入欄上下並列 |



### ■ Form Input Style

#### ● Basic Style

> 所有輸入欄通用欄位樣式

| 樣式選項  | 說明                                                         | 支援變數 | 參考                                                         |
| --------- | ------------------------------------------------------------ | -------- | ------------------------------------------------------------ |
| Separator | 與前一個輸入欄之間是否需要分隔線，預設： `false`             | **X**    | `true` or `false`                                            |
| Spacing   | 與前一個輸入欄的間隔，預設：<br />● 當 FormLayout 為 Horizonta時，預設：`Small` <br />● 當 FormLayout 為 Vertical時，預設：`Medium` | **X**    | [Container - Spacing](https://adaptivecards.io/explorer/Container.html) |



> 各別輸入欄位樣式

#### ● Label Style

| 樣式選項       | 說明                               | 支援變數 | 參考                                                         |
| -------------- | ---------------------------------- | -------- | ------------------------------------------------------------ |
| TitleColor     | 欄位標題字型顏色，預設： `default` | **X**    | [Text Block - Color](https://adaptivecards.io/explorer/TextBlock.html) |
| LabelColor     | 欄位資料字型顏色，預設： `default` | **X**    | [Text Block - Color](https://adaptivecards.io/explorer/TextBlock.html) |
| LabelSize      | 欄位資料字型大小，預設： `default` | **X**    | [Text Block - Size](https://adaptivecards.io/explorer/TextBlock.html) |
| LabelWeight    | 欄位資料字型粗細，預設： `default` | **X**    | [Text Block - Weight](https://adaptivecards.io/explorer/TextBlock.html) |
| LabelWrap      | 欄位資料自動換行，預設： `true`    | **X**    | [Text Block - Wrap](https://adaptivecards.io/explorer/TextBlock.html) |
| LabelAlignment | 欄位資料對齊，預設： `left`        | **X**    | [Text Block - Alignment](https://adaptivecards.io/explorer/TextBlock.html) |

#### ● Image Style

| 樣式選項   | 說明                               | 支援變數 | 參考                                                         |
| ---------- | ---------------------------------- | -------- | ------------------------------------------------------------ |
| TitleColor | 欄位標題字型顏色，預設： `default` | **X**    | [Text Block - Color](https://adaptivecards.io/explorer/TextBlock.html) |
| ImageSize  | 欄位資料字型大小，預設： `default` | **X**    | [Image - Size](https://adaptivecards.io/explorer/Image.html) |
| ImageStyle | 欄位資料字型粗細，預設： `default` | **X**    | [Image - Style](https://adaptivecards.io/explorer/Image.html) |

#### ● Text Input Style

| 樣式選項      | 說明                                     | 支援變數 | 參考                                                         |
| ------------- | ---------------------------------------- | -------- | ------------------------------------------------------------ |
| TitleColor    | 欄位標題字型顏色，預設： `default`       | **X**    | [Text Block - Color](https://adaptivecards.io/explorer/TextBlock.html) |
| IsTextArea    | 是否為多行輸入，預設： `false`           | **X**    | [Input Text - IsMultiline](https://adaptivecards.io/explorer/Input.Text.html) |
| TextMaxLength | 最大文字輸入長度，預設： `0`  (沒有限制) | **X**    | [Input Text - MaxLength](https://adaptivecards.io/explorer/Input.Text.html) |
| TextStyle     | 文字輸入樣式，預設： `default`           | **X**    | [Input Text - Style](https://adaptivecards.io/explorer/Input.Text.html) |

#### ● Text Area Style

| 樣式選項      | 說明                                     | 支援變數 | 參考                                                         |
| ------------- | ---------------------------------------- | -------- | ------------------------------------------------------------ |
| TitleColor    | 欄位標題字型顏色，預設： `default`       | **X**    | [Text Block - Color](https://adaptivecards.io/explorer/TextBlock.html) |
| TextMaxLength | 最大文字輸入長度，預設： `0`  (沒有限制) | **X**    | [Input Text - MaxLength](https://adaptivecards.io/explorer/Input.Text.html) |
| TextStyle     | 文字輸入樣式，預設： `default`           | **X**    | [Input Text - Style](https://adaptivecards.io/explorer/Input.Text.html) |

#### ● Number Input Style

| 樣式選項   | 說明                                           | 支援變數 | 參考                                                         |
| ---------- | ---------------------------------------------- | -------- | ------------------------------------------------------------ |
| TitleColor | 欄位標題字型顏色，預設： `default`             | **X**    | [Text Block - Color](https://adaptivecards.io/explorer/TextBlock.html) |
| InputMin   | 最小值，預設： `N/A ` (沒有限制，依照前端控制) | **O**    | [Input Number - Min](https://adaptivecards.io/explorer/Input.Number.htmll) |
| InputMax   | 最大值，預設： `N/A` (沒有限制，依照前端控制)  | **O**    | [Input Number - Max](https://adaptivecards.io/explorer/Input.Number.htmll) |

#### ● Date Input Style

| 樣式選項   | 說明                                           | 支援變數 | 參考                                                         |
| ---------- | ---------------------------------------------- | -------- | ------------------------------------------------------------ |
| TitleColor | 欄位標題字型顏色，預設： `default`             | **X**    | [Text Block - Color](https://adaptivecards.io/explorer/TextBlock.html) |
| InputMin   | 最大值，預設： `N/A ` (沒有限制，依照前端控制) | **O**    | [Input Date - Min](https://adaptivecards.io/explorer/Input.Date.html) |
| InputMax   | 最小值，預設： `N/A` (沒有限制，依照前端控制)  | **O**    | [Input Date - Max](https://adaptivecards.io/explorer/Input.Date.html) |

#### ● Time Input Style

| 樣式選項   | 說明                                           | 支援變數 | 參考                                                         |
| ---------- | ---------------------------------------------- | -------- | ------------------------------------------------------------ |
| TitleColor | 欄位標題字型顏色，預設： `default`             | **X**    | [Text Block - Color](https://adaptivecards.io/explorer/TextBlock.html) |
| InputMin   | 最大值，預設： `N/A ` (沒有限制，依照前端控制) | **O**    | [Input Time - Min](https://adaptivecards.io/explorer/Input.Time.html) |
| InputMax   | 最小值，預設： `N/A` (沒有限制，依照前端控制)  | **O**    | [Input Time - Max](https://adaptivecards.io/explorer/Input.Time.html) |

#### ● Combo Box, Radio Box, Check Box Input Style

| 樣式選項   | 說明                               | 支援變數 | 參考                                                         |
| ---------- | ---------------------------------- | -------- | ------------------------------------------------------------ |
| TitleColor | 欄位標題字型顏色，預設： `default` | **X**    | [Text Block - Color](https://adaptivecards.io/explorer/TextBlock.html) |
| LabelWrap  | 自動換行，預設： `false`           | **X**    | [Input Choice Set - Wrap](https://adaptivecards.io/explorer/Input.ChoiceSet.html) |

#### ● Toggle Input Style

| 樣式選項   | 說明                               | 支援變數 | 參考                                                         |
| ---------- | ---------------------------------- | -------- | ------------------------------------------------------------ |
| TitleColor | 欄位標題字型顏色，預設： `default` | **X**    | [Text Block - Color](https://adaptivecards.io/explorer/TextBlock.html) |
| LabelWrap  | 自動換行，預設： `false`           | **X**    | [Input Toggle - Wrap](https://adaptivecards.io/explorer/Input.Toggle.html) |



