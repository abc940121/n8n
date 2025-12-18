# LINE Flex Carousel Card Content

> Line Flex Message 多卡片的訊息



## ◆ Channel Support

| Channel 類型        | 是否支援 | 備註 |
| ------------------- | -------- | ---- |
| Emulator            | **X**    |      |
| Web Chat            | **X**    |      |
| iota                | **X**    |      |
| LINE                | **O**    |      |
| Slack               | **X**    |      |
| Webex               | **X**    |      |
| Facebook Messenger  | **X**    |      |
| WhatsApp            | **X**    |      |
| Teams               | **X**    |      |
| Telegram            | **X**    |      |
| WeChat              | **X**    |      |
| WeCom               | **X**    |      |
| DingTalk            | **X**    |      |
| Apple Business Chat | **X**    |      |





## ◆ Schema

繼承自 [MessageContent](../MessageContent.md)

| 屬性                 | 資料型態                                    | 必要屬性 | 描述                                                         | 支援變數 | 版本 |
| -------------------- | ------------------------------------------- | -------- | ------------------------------------------------------------ | -------- | ---- |
| *Type*               | string                                      | Y        | 類型，值為 `line.flex.card.carousel`                         | **X**    | 1.23 |
| **AltText**          | string                                      | Y        | 聊天室清單顯示的文字                                         | **O**    | 1.23 |
| **Attachments**      | [MessageContent[]](../MessageContent.md)    | Y        | 卡片訊息內容，**`只支援部分訊息類型`**<br />**`(最多支援12張卡片)`** | **X**    | 1.23 |
| *QuickReply*         | [LineButtonContent[]](LineActionContent.md) | N        | 快速回覆按鈕                                                 | **X**    | 1.23 |
| *ChannelDataPayload* | object                                      | N        | Channel Data Payload，[使用限制](../Components/ChannelDataPayload.md) | **O**    | 1.23 |

* **Attachments**
    * `只支援以下 Message Content`
        * [Hero Card](../HeroCardContent.md)
        * [SignIn Card](../SignInCardContent.md)
        * [Receipt Card](../ReceiptCardContent.md)
        * [Animation Card](../AnimationCardContent.md)
        * [Line Flex Message](../LineFlexMessageContent.md)
        * [Line Flex Carousel Card](LineFlexCarouselCardContent.md)
        * [Line Flex Fact Card](LineFlexFactCardContent.md)
        * [Line Flex List Card](LineFlexListCardContent.md)
        * [Line Flex Grid Card](LineFlexGridCardContent.md)
        * [Line Flex Template Card](LineFlexTemplateCardContent.md)
        * [Line Flex Carousel Template Card](LineFlexCarouselTemplateCardContent.md)
        * [Adaptive Fact Card](../AdaptiveCards/FactCardContent.md)
        * [Adaptive List Card](../AdaptiveCards/ListCardContent.md)
        * [Adaptive Grid Card](../AdaptiveCards/GridCardContent.md)

> **如果設定上述以外的 Message Content，則不被處理**



## ◆ Example

### ● 靜態卡片標題內容

```json
{
    "Type": "line.flex.card.carousel",
    "AltText": "This is Carousel",
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
* 變數可以[參考這裡](../../Variables/Variable.md) 

```json
{
    "Type": "line.flex.card.carousel",
    "AltText": "You send {{$.Message.text}}",
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

