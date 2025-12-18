# LINE List Card Content

> 制式的Line Flex Message 訊息，清單卡片



##  ◆ Screenshot  

![](Screenshots/ListCardContent.jpg)



## ◆ Channel Support

> [LINE Flex Message 文件](https://developers.line.biz/en/reference/messaging-api/#message-objects)

| Channel 類型        | 是否支援 | 備註                       |
| ------------------- | -------- | -------------------------- |
| Emulator            | **O**    | 實作上會轉成 Adaptive Card |
| Web Chat            | **O**    | 實作上會轉成 Adaptive Card |
| iota                | **O**    | 實作上會轉成 Adaptive Card |
| LINE                | **O**    |                            |
| Teams               | **O**    | 實作上會轉成 Adaptive Card |
| Slack               | **X**    | 計畫中...                  |
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

| 屬性                          | 資料型態                                    | 必要屬性 | 描述                                                 | 支援變數 | 版本 |
| ----------------------------- | ------------------------------------------- | -------- | ---------------------------------------------------- | -------- | ---- |
| *Type*                        | string                                      | Y        | 類型，值為 `line.flex.card.list`                     | **X**    | 1.5  |
| **AltText**                   | string                                      | Y        | 聊天室清單顯示的文字                                 | **O**    | 1.5  |
| **Title**                     | string                                      | N        | 卡片標題                                             | **O**    | 1.5  |
| **Item**                      | [LineFlexListItem](#-line-flex-list-item)   | N        | 清單項目                                             | **X**    | 1.5  |
| **Buttons**                   | [LineActionContent[]](LineActionContent.md) | N        | 卡片按鈕                                             | **X**    | 1.5  |
| **DataSource**                | string                                      | Y        | 指定資料來源 (自訂變數)，**`必須指定`**              | **O**    | 1.5  |
| **EmptyDataText**             | string                                      | N        | 未指定資料來源時的提示訊息，有預設的提示訊息         | **O**    | 1.5  |
| [**Styles**](#-style-options) | <string, string>                            | N        | 清單的UI 樣式，沒有設定時，會使用預設樣式            | **X**    | 1.5  |
| **Locale**                    | string                                      | N        | 地區，用於處理文字格式化，預設值為伺服器所使用的地區 | **X**    | 1.5  |
| *QuickReply*                  | [LineButtonContent[]](LineActionContent.md) | N        | 快速回覆按鈕                                         | **X**    | 1.1  |

> **AltText 必須要給值，值要給有效值字元、不能給空白字元**

* **AltText 在 LINE 上的顯示**

![](Screenshots/AltText.jpg)



### ■ LINE Flex List Item

| 屬性     | 資料型態                                  | 必要屬性 | 描述             | 支援變數 或 指定 DataSource | 版本 |
| -------- | ----------------------------------------- | -------- | ---------------- | --------------------------- | ---- |
| Title    | string                                    | Y        | 標題             | **O**                       | 1.5  |
| Subtitle | string                                    | N        | 副標題           | **O**                       | 1.5  |
| Text     | string                                    | N        | 文字             | **O**                       | 1.5  |
| Tap      | [LineActionContent](LineActionContent.md) | N        | 清單項目點擊事件 | **X**                       | 1.5  |
| ImageUrl | string                                    | N        | 圖片             | **O**                       | 1.5  |



## ◆ Example

### ■ 指定 DataSource 內容

![](Screenshots/ListCardContent.jpg)

* **變數名稱** ─ `$.Variables.ITCompanies`

```json
[
    {
        "Name": "Facebook",
        "CName": "臉書",
        "Description": "Facebook是源於美國的社群網路服務及社會化媒體網站",
        "HomeUrl": "https://www.facebook.com/",
        "ImageUrl": "https://www.facebook.com/favorite.jpg"
    },
    {
        "Name": "Google",
        "CName": "谷歌",
        "Description": "Google是源自美國的跨國科技公司",
        "HomeUrl": "https://www.google.com.tw",
        "ImageUrl": "https://www.google.com.tw/favorite.jpg"
    },
    {
        "Name": "Microsoft",
        "CName": "微軟",
        "Description": "Microsoft是美國一家跨國電腦科技公司",
        "HomeUrl": "https://www.microsoft.com/",
        "ImageUrl": "https://www.microsoft.com/favorite.jpg"
    }
]
```

* **Json**

```json
{
    "Type": "line.flex.card.list",
    "AltText": "IT巨擘相關資訊",
    "Title": "IT巨擘",
    "Item": {
        "Title": "{{$.Name}}",
        "Subtitle": "{{$.CName}}",
        "Text": "{{$.Description}}",
        "Tap": {
            "Type": "url",
            "Value": "{{$.HomeUrl}}"
        },
        "ImageUrl": "{{$.ImageUrl}}"
    },
    "Buttons": [
        {
            "Type": "message",
            "Title": "返回",
            "Value": "1"
        }
    ],
    "DataSource": "$.Variables.ITCompanies",
    "EmptyDataText": "",
    "Styles": {
        "CardTitleSize": "xl",
        "CardTitleColor": "#0061AD",
        "ItemTextMaxLines": "3"
    }
}
```



## ◆ Style Options

> 有需要在使用，沒有設定的項目會使用預設值

* [Flex Message Text Component 屬性參考](https://developers.line.biz/en/reference/messaging-api/#f-text)
* [Flex Message Image Component 屬性參考](https://developers.line.biz/en/reference/messaging-api/#f-image)
* [Flex Message Box Component 屬性參考](https://developers.line.biz/en/reference/messaging-api/#box)
* [Flex Message Button Component 屬性參考](https://developers.line.biz/en/reference/messaging-api/#button)

| 樣式選項             | 說明                                                         | 支援變數 | 參考                                                         |
| -------------------- | ------------------------------------------------------------ | -------- | ------------------------------------------------------------ |
| CardTitleSize        | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片標題字型大小，預設： `lg` | **X**    | `xxs`、`xs`、`sm`<br />、`md`、`lg`、`xl`、<br />`xxl`、`3x1`、`4xl`、`5xl` |
| CardTitleColor       | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片標題字型顏色，預設： `#0061AD` | **X**    | 符合 `#RRGGBB` or `#RRGGBBAA` 格式                           |
| CardTitleWeight      | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片標題字型粗細，預設： `bold` | **X**    | `regular`、`bold` (粗體)                                     |
| CardTitleAlignment   | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片標題對齊方式，預設： `start` | **X**    | `start` (靠左)、`center` (置中)、`end` (靠右)                |
| CardTitleStyle       | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片標題是否為斜體，預設： `normal` | **X**    | `normal`、`italic` (斜體)                                    |
| CardTitleDecoration  | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片標題是否加上底線或刪除線，預設： `none` | **X**    | `none`、`underline` (底線)、`line-through` (刪除線)          |
| CardButtonHeight     | **[[Button]](https://developers.line.biz/en/reference/messaging-api/#button)** 按鈕大小，預設：`sm` | **X**    | `sm`、`md`                                                   |
| CardButtonStyle      | **[[Button]](https://developers.line.biz/en/reference/messaging-api/#button)** 按鈕背景樣式，預設：`secondary` | **X**    | ● `link` ：連結<br />● `primary` ：白色標題、深色背景<br />● `secondary` ：黑色標題、淺色背景 |
| CardButtonColor      | **[[Button]](https://developers.line.biz/en/reference/messaging-api/#button)** 按鈕背景顏色，預設：`<未設定>` | **X**    | 符合 `#RRGGBB` or `#RRGGBBAA` 格式                           |
| ItemSeparatorColor   | 表格框線顏色，預設： `<未設定>`                              | **X**    | 符合 `#RRGGBB` or `#RRGGBBAA` 格式                           |
| ItemContentAlignment | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片項目內文對齊方式，預設： `start` | **X**    | `start` (靠左)、`center` (置中)、`end` (靠右)                |
| ItemTitleWrap        | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片項目標題是否換行，預設： `false` | **X**    | 自動換行：`true`<br />不自動換行：`false`                    |
| ItemTitleSize        | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片項目標題字型大小，預設： `sm` | **X**    | `xxs`、`xs`、`sm`<br />、`md`、`lg`、`xl`、<br />`xxl`、`3x1`、`4xl`、`5xl` |
| ItemTitleColor       | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片項目標題字型顏色，預設： `#0061AD` | **X**    | 符合 `#RRGGBB` or `#RRGGBBAA` 格式                           |
| ItemTitleWeight      | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片項目標題字型粗細，預設： `bold` | **X**    | `regular`、`bold` (粗體)                                     |
| ItemTitleMaxLines    | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片項目標題最大行數，預設： `0` | **X**    | 數字 `1`~`N`，無限制：`0`                                    |
| ItemSubtitleWrap     | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片項目副標題是否換行，預設： `false` | **X**    | 自動換行：`true`<br />不自動換行：`false`                    |
| ItemSubtitleSize     | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片項目副標題字型大小，預設： `xs` | **X**    | `xxs`、`xs`、`sm`<br />、`md`、`lg`、`xl`、<br />`xxl`、`3x1`、`4xl`、`5xl` |
| ItemSubtitleColor    | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片項目副標題字型顏色，預設： `#767676` | **X**    | 符合 `#RRGGBB` or `#RRGGBBAA` 格式                           |
| ItemSubtitleWeight   | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片項目副標題字型粗細，預設： `regular` | **X**    | `regular`、`bold` (粗體)                                     |
| ItemSubtitleMaxLines | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片項目副標題最大行數，預設： `0` | **X**    | 數字 `1`~`N`，無限制：`0`                                    |
| ItemTextWrap         | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片項目內文是否換行，預設： `true` | **X**    | 自動換行：`true`<br />不自動換行：`false`                    |
| ItemTextSize         | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片項目內文字型大小，預設： `xs` | **X**    | `xxs`、`xs`、`sm`<br />、`md`、`lg`、`xl`、<br />`xxl`、`3x1`、`4xl`、`5xl` |
| ItemTextColor        | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片項目內文字型顏色，預設： `#000000` | **X**    | 符合 `#RRGGBB` or `#RRGGBBAA` 格式                           |
| ItemTextWeight       | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片項目內文字型粗細，預設： `regular` | **X**    | `regular`、`bold` (粗體)                                     |
| ItemTextMaxLines     | **[[Text]](https://developers.line.biz/en/reference/messaging-api/#f-text)** 卡片項目內文最大行數，預設： `0` | **X**    | 數字 `1`~`N`，無限制：`0`                                    |
| ItemImageSize        | **[[Image]](https://developers.line.biz/en/reference/messaging-api/#f-image)** 卡片項目圖片大小，預設：`sm` | **X**    | `xxs`、`xs`、`sm`<br />、`md`、`lg`、`xl`、<br />`xxl`、`3x1`、`4xl`、`5xl`、`full` |
| ItemImageAspectMode  | **[[Image]](https://developers.line.biz/en/reference/messaging-api/#f-image)** 卡片項目圖片長寬排版，預設：`fit` | **X**    | ● `fit` ： 符合圖片<br />● `cover` ：延伸圖片                |
| ItemImageAspectRatio | **[[Image]](https://developers.line.biz/en/reference/messaging-api/#f-image)** 卡片項目圖片長寬比率，預設：`<無設定>` | **X**    | 符合 `{width}:{height}` 格式，例如：`1920:1080`              |
| ItemImageLayout      | 卡片項目圖片的位置，預設：`Right`                            | **X**    | ● `None`：無圖片<br />● `Left`：在左側<br />● `Right`：在右側 |
| ItemBackground       | [**[Box](https://developers.line.biz/en/reference/messaging-api/#box)**] 背景顏色，預設： `<無設定>` | **X**    | 符合 `#RRGGBB` or `#RRGGBBAA` 格式                           |

