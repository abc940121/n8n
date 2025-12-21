# Adaptive Card Content

> 靜態的Adaptive Card 訊息

* **Adaptive Card Content 衍生類型**
  * **[Fact Adaptive Card Content](AdaptiveCards/FactCardContent.md)** ─ 明細卡片 (制式 Adaptive Card 訊息)
  * **[List Adaptive Card Content](AdaptiveCards/ListCardContent.md)** ─ 清單卡片 (制式 Adaptive Card 訊息)
  * **[Grid Adaptive Card Content](AdaptiveCards/GridCardContent.md)** ─ 表格卡片 (制式 Adaptive Card 訊息)
  * **[Form Adaptive Card Content](AdaptiveCards/FormCardContent.md)** ─ 表單卡片 (制式 Adaptive Card 訊息)
  * **[Template Adaptive Card Content](AdaptiveCards/TemplateCardContent.md)** ─ 範本卡片
  * **[Carousel Template Adaptive Card Content](AdaptiveCards/CarosuelTemplateCardContent.md)** ─ 範本多卡片



## ◆ Channel Support

> [Adaptive Card 文件](https://adaptivecards.io/explorer/)

| Channel 類型            | 是否支援 | 相容的版本 | 備註                         |
| ----------------------- | -------- | ---------- | ---------------------------- |
| Emulator                | **O**    | 1.3        |                              |
| Web Chat、iota Chat Bot | **O**    | 1.4        |                              |
| iota                    | **O**    | 1.5        |                              |
| LINE                    | **X**    | N/A        |                              |
| Teams                   | **O**    | 1.1        | 不支援 Audio 和 Video 等元件 |
| Slack                   | **X**    | N/A        |                              |
| Webex                   | **O**    | 1.3        | 按鈕數量最多5個              |
| Facebook Messenger      | **X**    | N/A        |                              |
| WhatsApp                | **X**    | N/A        |                              |
| Telegram                | **X**    | N/A        |                              |
| M+                      | **X**    | N/A        |                              |
| WeChat (微信個人號)     | **X**    | N/A        |                              |
| WeCom (企業微信)        | **X**    | N/A        |                              |
| DingTalk                | **X**    | N/A        |                              |
| Apple Business Chat     | **X**    | N/A        |                              |



## ◆ Schema

繼承 [MessageContent](MessageContent.md)

| 屬性       | 資料型態                                       | 必要屬性 | 描述                       | 支援變數 | 版本 |
| ---------- | ---------------------------------------------- | -------- | -------------------------- | -------- | ---- |
| *Type*     | string                                         | Y        | 類型，值為 `adaptive.card` | **X**    | 1.0  |
| **Text**   | string                                         | N        | 文字訊息                   | **O**    | 1.0  |
| **Content** | string                                        | `[1]`    | Adaptive Card Json 內容<br />● 資料綁定的資料來源<br />　　■ 不設定 `DataSource` ： Bot 的變數<br />　　■ 設定 `DataSource` ： 使用 DataSouce 指定的變數資料 | **O**    | 1.0  |
| **ContentSource** | string | `[1]` | Adaptive Card Json 內容取自指定的變數值`(有設定時會覆蓋掉 Content 的設定)`<br />● 資料綁定的資料來源<br />　　■ 不設定 `DataSource` ： Bot 的變數<br />　　■ 設定 `DataSource` ： 使用 DataSouce 指定的變數資料 | **O** | 1.11 |
| **DataSource** | string | N | 指定資料來源 (自訂變數)，`(有設定時會使用 Adaptive Card Templating 處理資料綁定)` | **O** | 1.6 |
| *QuickReply* | [ButtonContent[]](Components/ButtonContent.md) | N | 快速回覆按鈕                | **X**    | 1.1  |
| *ChannelDataPayload* | object                                           | N        | Channel Data Payload，[使用限制](../Components/ChannelDataPayload.md) | **O**    | 1.14  |
| *Options* | [MessageContentOption](#-message-content-option) | `[2]` | 訊息相關參數，僅限 [Bot 通知訊息服務 (ETA)](https://git.gss.com.tw/fpsbu/bot_event_trigger_service) 發送通知訊息使用 | **X** | **X** |

* `[1]` **ContentSource** 和 **Content** 必填其中一個。如果有指定 **ContentSource** 時，**Content** 可以為空。反之 **Content** 則是必填
* `[2]` 這個參數僅限 [Bot 通知訊息服務 (ETA)](https://git.gss.com.tw/fpsbu/bot_event_trigger_service) 發送通知訊息使用
    * 這個參數不適用 Bot Flow Engine 主程式，Bot Flow Engine 主程式只在 [appsettings.json 設定](../../AppSetting.md)



### ● Message Content Option

| 屬性                           | 描述                                                     |
| ------------------------------ | -------------------------------------------------------- |
| **AdaptiveCard**               | Adaptive Card 參數設定                                   |
| **AdaptiveCard.SchemaVersion** | 使用的 Adaptive Card Schema Version，預設值為 `1.0`      |
| **AdaptiveCard.HotfixVersion** | 使用的  Adaptive Card Hotfix Version，預設值為 `2021.02` |

* **SchemaVersion ─** 使用的 Adaptive Card Schema Version，預設值為 `1.0`
    * **Stable Version：** `1.0` ~ `1.3`
    * **Preview Version：** `1.4` ~ `1.5`
    * 需要留意一下 Channel 是否支援較新的版本，建議可以選擇比較低的版本
* **HotfixVersion ─** 使用的  Adaptive Card Hotfix Version，預設值為 `2021.02`
    * `2018.03` ─ 初始版本，為處理任何 Hotfix
    * `2021.02` ─ 修復 Adaptive Card Number Inupit 預設值的問題，需確認 Channel 的版本是否為較新的版本
        * **C.AI Bot Builder 提供的 Web Chat：** `v1.13+`
        * **iota：** `v1.10+`

```json
{
    "Options": {
        "AdaptivCard": {
            "SchemaVersion": "1.2",
            "HotfixVersion": "2021.02"
        }
    }
}
```



## ◆ Example

### ● 不指定 ContentSource & DataSource  (不使用 Adaptive Card Templating)

> 可以透過 `{{變數名(Json Path)}}` 動態塞入資料

```json
{
    "Type": "adaptive.card",
    "Text": "請說出你要我做什麼?",
    "Content": "{\"type\":\"AdaptiveCard\",\"body\":[{\"type\":\"Container\",\"items\":[{\"type\":\"TextBlock\",\"text\":\"Hi {{$.Conversation.UserName}}\"}]}],\"actions\":[{\"type\":\"Action.Submit\",\"title\":\"第一個選項 (Text)\",\"data\":\"1\"},{\"type\":\"Action.Submit\",\"title\":\"第二個選項 (Text)\",\"data\":\"2\"},{\"type\":\"Action.Submit\",\"title\":\"第三個選項 (Value)\",\"data\":{\"Action\":\"Quit\"}}],\"$schema\":\"http://adaptivecards.io/schemas/adaptive-card.json\",\"version\":\"1.0\"}",
    "ContentSource": "",
    "DataSource": ""
}
```



### ● 不指定 ContentSource、指定 DataSource (使用 Adaptive Card Templating)

> 動態塞入資料會以指定的 DataSource (自訂變數) 為主

* **變數名稱** ─ `$.Variables.CardData`

```json
[
    {
        "Id": 1,
        "Name": "Ace",
        "Style": "黑桃"
    },
    {
        "Id": 11,
        "Name": "Jack",
        "Style": "方塊"
    },
    {
        "Id": 12,
        "Name": "Queen",
        "Style": "愛心"
    },
    {
        "Id": 13,
        "Name": "King",
        "Style": "梅花"
    },
    {
        "Id": 14,
        "Name": "Joke",
        "Style": "無"
    }
]
```

* **訊息內容**

```json
{
    "Type": "adaptive.card",
    "Text": "請說出你要我做什麼?",
    "Content": "{\"type\":\"AdaptiveCard\",\"$schema\":\"http://adaptivecards.io/schemas/adaptive-card.json\",\"version\":\"1.2\",\"body\":[{\"type\":\"Container\",\"items\":[{\"type\":\"ColumnSet\",\"columns\":[{\"type\":\"Column\",\"width\":20,\"items\":[{\"type\":\"TextBlock\",\"horizontalAlignment\":\"Right\",\"size\":\"Medium\",\"weight\":\"Bolder\",\"text\":\"數字\"}]},{\"type\":\"Column\",\"width\":60,\"items\":[{\"type\":\"TextBlock\",\"size\":\"Medium\",\"weight\":\"Bolder\",\"text\":\"名稱\"}]},{\"type\":\"Column\",\"width\":60,\"items\":[{\"type\":\"TextBlock\",\"size\":\"Medium\",\"weight\":\"Bolder\",\"text\":\"花色\"}]}],\"style\":\"emphasis\"},{\"$data\":\"${Cards}\",\"type\":\"ColumnSet\",\"columns\":[{\"type\":\"Column\",\"width\":20,\"items\":[{\"type\":\"TextBlock\",\"$when\":\"${or(equals(Style, '愛心'), equals(Style, '方塊'))}\",\"text\":\"${string(Id)}\",\"horizontalAlignment\":\"Right\",\"weight\":\"Bolder\",\"color\":\"Attention\"},{\"type\":\"TextBlock\",\"$when\":\"${or(equals(Style, '黑桃'), equals(Style, '梅花'))}\",\"text\":\"${string(Id)}\",\"horizontalAlignment\":\"Right\",\"weight\":\"Bolder\",\"color\":\"Dark\"},{\"type\":\"TextBlock\",\"$when\":\"${equals(Style, '無')}\",\"text\":\"${string(Id)}\",\"horizontalAlignment\":\"Right\",\"weight\":\"Bolder\",\"color\":\"Accent\"}]},{\"type\":\"Column\",\"width\":60,\"items\":[{\"type\":\"TextBlock\",\"$when\":\"${or(equals(Style, '愛心'), equals(Style, '方塊'))}\",\"text\":\"${Name}\",\"weight\":\"Bolder\",\"color\":\"Attention\"},{\"type\":\"TextBlock\",\"$when\":\"${or(equals(Style, '黑桃'), equals(Style, '梅花'))}\",\"text\":\"${Name}\",\"weight\":\"Bolder\",\"color\":\"Dark\"},{\"type\":\"TextBlock\",\"$when\":\"${equals(Style, '無')}\",\"text\":\"${Name}\",\"weight\":\"Bolder\",\"color\":\"Accent\"}]},{\"type\":\"Column\",\"width\":60,\"items\":[{\"type\":\"TextBlock\",\"$when\":\"${or(equals(Style, '愛心'), equals(Style, '方塊'))}\",\"text\":\"${Style}\",\"weight\":\"Bolder\",\"color\":\"Attention\"},{\"type\":\"TextBlock\",\"$when\":\"${or(equals(Style, '黑桃'), equals(Style, '梅花'))}\",\"text\":\"${Style}\",\"weight\":\"Bolder\",\"color\":\"Dark\"},{\"type\":\"TextBlock\",\"$when\":\"${equals(Style, '無')}\",\"text\":\"${Style}\",\"weight\":\"Bolder\",\"color\":\"Accent\"}]}],\"style\":\"warning\"}]}]}",
    "ContentSource": "",
    "DataSource": "$.Variables.CardData"
}
```



### ● 指定 ContentSource、不指定 DataSource  (不使用 Adaptive Card Templating)

> 可以透過 `{{變數名(Json Path)}}` 動態塞入資料

* **變數名稱** ─ `$.Variables.CardContent`
    * 資料型態可以為字串或是物件

```json
"{\"type\":\"AdaptiveCard\",\"body\":[{\"type\":\"Container\",\"items\":[{\"type\":\"TextBlock\",\"text\":\"Hi {{$.Conversation.UserName}}\"}]}],\"actions\":[{\"type\":\"Action.Submit\",\"title\":\"第一個選項 (Text)\",\"data\":\"1\"},{\"type\":\"Action.Submit\",\"title\":\"第二個選項 (Text)\",\"data\":\"2\"},{\"type\":\"Action.Submit\",\"title\":\"第三個選項 (Value)\",\"data\":{\"Action\":\"Quit\"}}],\"$schema\":\"http://adaptivecards.io/schemas/adaptive-card.json\",\"version\":\"1.0\"}"
```

* **訊息內容**

```json
{
    "Type": "adaptive.card",
    "Text": "請說出你要我做什麼?",
    "Content": "",
    "ContentSource": "$.Variables.CardContent",
    "DataSource": ""
}
```



### ● 指定 ContentSource & DataSource (使用 Adaptive Card Templating)

> 動態塞入資料會以指定的 DataSource (自訂變數) 為主

* **變數名稱** ─ `$.Variables.CardContent`
    * 資料型態可以為字串或是物件

```json
"{\"type\":\"AdaptiveCard\",\"$schema\":\"http://adaptivecards.io/schemas/adaptive-card.json\",\"version\":\"1.2\",\"body\":[{\"type\":\"Container\",\"items\":[{\"type\":\"ColumnSet\",\"columns\":[{\"type\":\"Column\",\"width\":20,\"items\":[{\"type\":\"TextBlock\",\"horizontalAlignment\":\"Right\",\"size\":\"Medium\",\"weight\":\"Bolder\",\"text\":\"數字\"}]},{\"type\":\"Column\",\"width\":60,\"items\":[{\"type\":\"TextBlock\",\"size\":\"Medium\",\"weight\":\"Bolder\",\"text\":\"名稱\"}]},{\"type\":\"Column\",\"width\":60,\"items\":[{\"type\":\"TextBlock\",\"size\":\"Medium\",\"weight\":\"Bolder\",\"text\":\"花色\"}]}],\"style\":\"emphasis\"},{\"$data\":\"${Cards}\",\"type\":\"ColumnSet\",\"columns\":[{\"type\":\"Column\",\"width\":20,\"items\":[{\"type\":\"TextBlock\",\"$when\":\"${or(equals(Style, '愛心'), equals(Style, '方塊'))}\",\"text\":\"${string(Id)}\",\"horizontalAlignment\":\"Right\",\"weight\":\"Bolder\",\"color\":\"Attention\"},{\"type\":\"TextBlock\",\"$when\":\"${or(equals(Style, '黑桃'), equals(Style, '梅花'))}\",\"text\":\"${string(Id)}\",\"horizontalAlignment\":\"Right\",\"weight\":\"Bolder\",\"color\":\"Dark\"},{\"type\":\"TextBlock\",\"$when\":\"${equals(Style, '無')}\",\"text\":\"${string(Id)}\",\"horizontalAlignment\":\"Right\",\"weight\":\"Bolder\",\"color\":\"Accent\"}]},{\"type\":\"Column\",\"width\":60,\"items\":[{\"type\":\"TextBlock\",\"$when\":\"${or(equals(Style, '愛心'), equals(Style, '方塊'))}\",\"text\":\"${Name}\",\"weight\":\"Bolder\",\"color\":\"Attention\"},{\"type\":\"TextBlock\",\"$when\":\"${or(equals(Style, '黑桃'), equals(Style, '梅花'))}\",\"text\":\"${Name}\",\"weight\":\"Bolder\",\"color\":\"Dark\"},{\"type\":\"TextBlock\",\"$when\":\"${equals(Style, '無')}\",\"text\":\"${Name}\",\"weight\":\"Bolder\",\"color\":\"Accent\"}]},{\"type\":\"Column\",\"width\":60,\"items\":[{\"type\":\"TextBlock\",\"$when\":\"${or(equals(Style, '愛心'), equals(Style, '方塊'))}\",\"text\":\"${Style}\",\"weight\":\"Bolder\",\"color\":\"Attention\"},{\"type\":\"TextBlock\",\"$when\":\"${or(equals(Style, '黑桃'), equals(Style, '梅花'))}\",\"text\":\"${Style}\",\"weight\":\"Bolder\",\"color\":\"Dark\"},{\"type\":\"TextBlock\",\"$when\":\"${equals(Style, '無')}\",\"text\":\"${Style}\",\"weight\":\"Bolder\",\"color\":\"Accent\"}]}],\"style\":\"warning\"}]}]}"
```

* **變數名稱** ─ `$.Variables.CardData`

```json
[
    {
        "Id": 1,
        "Name": "Ace",
        "Style": "黑桃"
    },
    {
        "Id": 11,
        "Name": "Jack",
        "Style": "方塊"
    },
    {
        "Id": 12,
        "Name": "Queen",
        "Style": "愛心"
    },
    {
        "Id": 13,
        "Name": "King",
        "Style": "梅花"
    },
    {
        "Id": 14,
        "Name": "Joke",
        "Style": "無"
    }
]
```

* **訊息內容**

```json
{
    "Type": "adaptive.card",
    "Text": "請說出你要我做什麼?",
    "Content": "",
    "ContentSource": "$.Variables.CardContent",
    "DataSource": "$.Variables.CardData"
}
```



