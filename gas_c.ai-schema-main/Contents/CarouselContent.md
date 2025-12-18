# Carousel Content

>  多卡片的訊息



## ◆ Channel Support

| Channel 類型            | 是否支援 | 備註                                                         |
| ----------------------- | -------- | ------------------------------------------------------------ |
| Emulator                | **O**    |                                                              |
| Web Chat、iota Chat Bot | **O**    |                                                              |
| iota                    | **O**    | 舊版 iota不支援                                              |
| LINE                    | **▲**    | 建議請改使用[LINE Flex Carousel](FlexMessages/LineFlexCarouselCardContent.md) |
| Teams                   | **O**    |                                                              |
| Slack                   | **X**    |                                                              |
| Webex                   | **X**    |                                                              |
| Facebook Messenger      | **O**    |                                                              |
| WhatsApp                | **X**    |                                                              |
| Telegram                | **X**    |                                                              |
| M+                      | **X**    |                                                              |
| WeChat (微信個人號)     | **X**    |                                                              |
| WeCom (企業微信)        | **X**    |                                                              |
| DingTalk                | **X**    |                                                              |
| Apple Business Chat     | **X**    |                                                              |



## ◆ Schema

繼承自 [MessageContent](MessageContent.md)

| 屬性        | 資料型態                              | 必要屬性 | 描述                                   | 支援變數 | 版本 |
| ----------- | ------------------------------------- | -------- | -------------------------------------- | -------- | ---- |
| *Type*      | string                                | Y        | 類型，值為 `carousel`                  | **X**    | 1.1  |
| **Text**    | string                                | N        | 文字內容                               | **O**    | 1.1  |
| **Attachments** | [MessageContent[]](MessageContent.md) | Y        | 卡片訊息內容，**`只支援部分訊息類型`** | **X**    | 1.1  |
| **Layout**  | string                                | Y        | 卡片的排版，預設值: `carousel`        | **X**    | 1.1  |
| *QuickReply* | [ButtonContent[]](Components/ButtonContent.md) | N | 快速回覆按鈕                | **X**    | 1.1  |
| *ChannelDataPayload* | object | N | Channel Data Payload，[使用限制](../Components/ChannelDataPayload.md) | **O** | 1.14 |

* **Attachments**
    * `只支援以下 Message Content`
        * [Hero Card](HeroCardContent.md)
        * [SignIn Card](SignInCardContent.md)
        * [Receipt Card](ReceiptCardContent.md)
        * [Animation Card](AnimationCardContent.md)
        * [Audio Card](AudioCardContent.md) 
        * [Video Card](VideoCardContent.md) 
        * [Adaptive Card](AdaptiveCardContent.md)
        * [Adaptive Fact Card](AdaptiveCards/FactCardContent.md)
        * [Adaptive List Card](AdaptiveCards/ListCardContent.md)
        * [Adaptive Grid Card](AdaptiveCards/GridCardContent.md)
        * [Adaptive Template Card](AdaptiveCards/TemplateCardContent.md)
        * [Adaptive Carousel Template Card](AdaptiveCards/CarosuelTemplateCardContent.md)
    * LINE Channel 建議改使用 [LINE Flex Carousel](FlexMessages/LineFlexCarouselCardContent.md)
    * Teams Channel 不支援 Audio Card、Video Card

> **如果設定上述以外的 Message Content，則不被處理**

* **Layout**
    * 卡片的排版
        * **carousel** ─ 左右並排
        * **list** ─ 上下排列
    * LINE Channel 只支援 **carousel**，降低使用 LINE Push API 的使用次數
    * 舊版 iota Channel 只支援 **list**



## ◆ Example

### ● 靜態卡片標題內容

```json
{
    "Type": "carousel",
    "Text": "This is text",
    "Layout": "carousel",
    "Attachments": [
        {
            "Type": "signin.card",
            "Text": "",
            "Buttons": [
                {
                    "Type": "imBack",
                    "Title": "Button 01",
                    "Value": "1"
                }
            ]
        },
        {
            "Type": "signin.card",
            "Text": "",
            "Buttons": [
                {
                    "Type": "imBack",
                    "Title": "Button 02",
                    "Value": "2"
                }
            ]
        }
    ],
}
```



### ● 動態卡片標題內容

* 透過輸入 `{{變數名稱}}` 將變數的值帶入
* 變數可以[參考這裡](../Variables/Variable.md) 

```json
{
    "Type": "carousel",
    "Text": "You say {{$.Message.text}}",
    "Layout": "carousel",
    "Attachments": [
        {
            "Type": "signin.card",
            "Text": "",
            "Buttons": [
                {
                    "Type": "imBack",
                    "Title": "Button 01",
                    "Value": "1"
                }
            ]
        },
        {
            "Type": "signin.card",
            "Text": "",
            "Buttons": [
                {
                    "Type": "imBack",
                    "Title": "Button 02",
                    "Value": "2"
                }
            ]
        }
    ],
}
```

