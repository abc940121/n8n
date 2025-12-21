# Message Content

> 訊息內容



## ◆ Schema

> 基底屬性

| 屬性                   | 資料型態                                       | 必要屬性 | 描述                                                         | 支援變數 | 版本 |
| ---------------------- | ---------------------------------------------- | -------- | ------------------------------------------------------------ | -------- | ---- |
| **Type**               | string                                         | Y        | 類型 ([Message Content Type](#-message-content-type))        | **X**    | 1.0  |
| **QuickReply**         | [ButtonContent[]](Components/ButtonContent.md) | N        | 快速回覆按鈕                                                 | **X**    | 1.1  |
| **ChannelDataPayload** | object                                         | N        | Channel Data Payload，[使用限制](Components/ChannelDataPayload.md) | **O**    | 1.14 |



### ● Quick Reply 支援

> 下方一次性快速回覆的按鈕

| Channel 類型            | 是否支援 | 備註                                               |
| ----------------------- | -------- | -------------------------------------------------- |
| Emulator                | **O**    |                                                    |
| Web Chat、iota Chat Bot | **O**    |                                                    |
| iota                    | **X**    |                                                    |
| LINE                    | **▲**    | 僅在手機版支援<br />只支援訊息回覆，不支援開啟連結 |
| Teams                   | **X**    | 整個訊息物件上限 28 KB                             |
| Slack                   | **X**    |                                                    |
| Webex                   | **X**    |                                                    |
| Facebook Messenger      | **▲**    | 只支援訊息回覆，不支援開啟連結                     |
| WhatsApp                | **X**    |                                                    |
| Telegram                | **?**    |                                                    |
| WeChat (微信公眾號)     | **X**    |                                                    |
| WeCom (微信企業號)      | **X**    |                                                    |
| DingTalk                | **X**    |                                                    |
| Apple Business Chat     | **X**    | 目前暫不提供支援<br />(Apple Business Chat 有支援) |

### ● Channel Data Payload 支援

> Channel Data 內容

| Channel 類型            | 是否支援 | 備註                     |
| ----------------------- | -------- | ------------------------ |
| Emulator                | **O**    |                          |
| Web Chat、iota Chat Bot | **O**    |                          |
| iota                    | **X**    |                          |
| LINE                    | **X**    | 僅拿來放 Flex Message    |
| Teams                   | **X**    |                          |
| Slack                   | **O**    | 僅拿來放 Slack Block Kit |
| Webex                   | **O**    | 僅拿來放訊息推送的對象   |
| Facebook Messenger      | **X**    |                          |
| WhatsApp                | **X**    |                          |
| Telegram                | **X**    |                          |
| WeChat (微信公眾號)     | **X**    |                          |
| WeCom (微信企業號)      | **X**    | 僅拿來卡片、模板卡片     |
| DingTalk                | **X**    |                          |
| Apple Business Chat     | **X**    |                          |



---

## ◆ Message Content 類型

* **一般訊息**
    * **支援 Markdown 的 Channel：** Emulator、Web Chat、iota Chat Bot、Teams
    * **支援非標準 Markdown 的 Channel：** Slack、Webex、Telegram、WeCom、DingTalk
    * **只支援純文字 的 Channel：** iota、LINE、Facebook Messenger、WhatsApp、M+、WeChat、Apple Business Chat


| 訊息內容 (Content)                 | 類型 ID       | 描述         | 版本 |
| ---------------------------------- | ------------- | ------------ | ---- |
| [None](NoneContent.md)             | `none`        | 空訊息       | 1.0  |
| [Text](TextContent.md)             | `text`        | 文字內容     | 1.0  |
| [Random Text](RandomText.md)       | `text.random` | 隨機文字內容 | 1.2  |
| [Random Content](RandomContent.md) | `random`      | 隨機訊息     | 1.22 |

* **僅 Web Chat 支援的訊息**
    * **支援的 Channel：**  Web Chat、iota Chat Bot


| 訊息內容 (Content)                 | 類型 ID      | 描述     | 版本 |
| ---------------------------------- | ------------ | -------- | ---- |
| [Event](EventContent.md)           | `event`      | Event    | 1.0  |
| [Attachment](AttachmentContent.md) | `attachment` | 附件卡片 | 1.1  |
| [Trace](TraceContent.md)           | `trace`      | 偵錯訊息 | 1.1  |

* **卡片訊息**
    * **支援的 Channel：**  Web Chat、iota Chat Bot、iota、LINE、Webex
        * Webex 對於按鈕數量最多5個
    * **部分支援的 Channel：**
        * **Teams：** 不支援 Receipt Card、Audio Card、Video Card
        * **Slack：** 只支援 Hero Card、Signin Card、Animation Card
        * **WeCom (微信企業號)：** 只支援 Hero Card、Signin Card
        * **WhatsApp**：不支援 Receipt Card


| 訊息內容 (Content)                                           | 類型 ID               | 描述                                | 版本 |
| ------------------------------------------------------------ | --------------------- | ----------------------------------- | ---- |
| [Hero Card](HeroCardContent.md)                              | `hero.card`           | 一般卡片                            | 1.0  |
| [SignIn Card](SignInCardContent.md)                          | `signin.card`         | 登入卡片                            | 1.0  |
| [Animation Card](AnimationCardContent.md)                    | `animation.card`      | 圖片卡片 (JPG、PNG、GIF)            | 1.0  |
| [Receipt Card](ReceiptCardContent.md)                        | `receipt.card`        | 收據卡片                            | 1.1  |
| [Audio Card](AudioCardContent.md)                            | `audio.card`          | 音樂卡片 (MP3、WAV)                 | 1.0  |
| [Video Card](VideoCardContent.md)                            | `video.card`          | 影片卡片 (Youtube、MP4)             | 1.0  |

* **Adaptive Card 訊息**
    * **支援 1.5 版的 Channel：** iota
    * **支援 1.4 版的 Channel：** Web Chat、iota Chat Bot
    * **支援 1.3 版的 Channel：** Emulator、Webex
        * Webex 對於按鈕數量最多5個
    * **支援 1.1 版的 Channel：** Teams

| 訊息內容 (Content)                                           | 類型 ID                           | 描述                       | 版本 |
| ------------------------------------------------------------ | --------------------------------- | -------------------------- | ---- |
| [Adaptive Card](AdaptiveCardContent.md)                      | `adaptive.card`                   | Adaptive Card              | 1.0  |
| [Adaptive Fact Card](AdaptiveCards/FactCardContent.md)       | `adaptive.card.fact`              | 明細卡片 (Adaptive Card)   | 1.1  |
| [Adaptive List Card](AdaptiveCards/ListCardContent.md)       | `adaptive.card.list`              | 清單卡片 (Adaptive Card)   | 1.1  |
| [Adaptive Grid Card](AdaptiveCards/GridCardContent.md)       | `adaptive.card.grid`              | 表格卡片 (Adaptive Card)   | 1.1  |
| [Adaptive Form Card](AdaptiveCards/FormCardContent,md)       | `adaptive.card.form`              | 表單卡片 (Adaptive Card)   | 1.4  |
| [Adaptive Template Card](AdaptiveCards/TemplateCardContent.md) | `adaptive.card.template`          | 範本卡片 (Adaptive Card)   | 1.22 |
| [Adaptive Carousel Template Card](AdaptiveCards/CarosuelTemplateCardContent.md) | `adaptive.card.carousel_template` | 範本多卡片 (Adaptive Card) | 1.31 |

* **多個卡片**
    * **支援的 Channel：** Web Chat、iota Chat Bot、iota、LINE、Teams 


| 訊息內容 (Content)             | 類型 ID    | 描述     | 版本 |
| ------------------------------ | ---------- | -------- | ---- |
| [Carousel](CarouselContent.md) | `carousel` | 多個卡片 | 1.0  |

* **LINE 專用的訊息**
    * **支援的 Channel：** LINE

| 訊息內容 (Content)                                           | 類型 ID                            | 描述                                | 版本 |
| ------------------------------------------------------------ | ---------------------------------- | ----------------------------------- | ---- |
| [LINE Sticker](LineStickerContent.md)                        | `line.sticker`                     | LINE 貼圖 (**`LINE 專用`**)         | 1.28 |
| [LINE Flex Message](LineFlexMessageContent.md)               | `line.flex`                        | LINE Flex Message (**`LINE 專用`**) | 1.5  |
| [LINE Flex Carousel](FlexMessages/LineFlexCarouselCardContent.md) | `line.flex.card.carousel`          | LINE 多張卡片(**`LINE 專用`**)      | 1.23 |
| [LINE Flex Fact Card](FlexMessages/LineFlexFactCardContent.md) | `line.flex.card.fact`              | 明細卡片 (**`LINE 專用`**)          | 1.5  |
| [LINE Flex List Card](LineFlexListCardContent)               | `line.flex.card.list`              | 清單卡片 (**`LINE 專用`**)          | 1.5  |
| [LINE Flex Grid Card](FlexMessages/LineFlexGridCardContent.md) | `line.flex.card.grid`              | 表格卡片 (**`LINE 專用`**)          | 1.5  |
| [LINE Flex Template Card](FlexMessages/LineFlexTemplateCardContent.md) | `line.flex.card.template`          | 範本卡片 (**`LINE 專用`**)          | 1.22 |
| [LINE Flex Carousel Template Card](FlexMessages/LineFlexCarouselTemplateCardContent.md) | `line.flex.card.carousel_template` | 範本多卡片 (**`LINE 專用`**)        | 1.31 |

* **Slack 專用訊息**

| 訊息內容 (Content)                                          | 類型 ID                 | 描述                                | 版本   |
| ----------------------------------------------------------- | ----------------------- | ----------------------------------- | ------ |
| [Slack Card](SlackContent.md)                               | `slack.blocks`          | Slack Block 卡片 (**`Slack 專用`**) | 1.27   |
| [Slack List Card](SlackMessages/ListCardContent.md)         | `slack.blocks.list`     | 清單卡片(**`Slack 專用`**)          | 計畫中 |
| [Slack Form Card](SlackMessages/FormCardContent.md)         | `slack.blocks.form`     | 表單卡片(**`Slack 專用`**)          | 計畫中 |
| [Slack Template Card](SlackMessages/TemplateCardContent.md) | `slack.blocks.template` | 範本卡片 (**`Slack 專用`**)         | 1.27   |

* **WeCom (微信企業號) 專用的訊息**
    * **支援的 Channel：** WeCom (微信企業號) 
    * [微信企業號支援的訊息類型](WeComMessageContent.md)

| 訊息內容 (Content)                                           | 類型 ID                   | 描述                   | 版本 |
| ------------------------------------------------------------ | ------------------------- | ---------------------- | ---- |
| [WeCom Text](WeComMessages/WeComTextContent.md)              | `wecom.text`              | 文字內容               | 1.21 |
| [WeCom Fact Card](WeComMessages/WeComFactCardContent.md)     | `wecom.card.fact`         | 明細卡片               | 1.21 |
| [WeCom Button Card](WeComMessages/WeComButtonCardContent.md) | `wecom.card.button`       | 按鈕卡片               | 1.21 |
| [WeCom Image Card](WeComMessages/WeComImageCardContent.md)   | `wecom.card.image`        | 圖文卡片 (無按鈕)      | 1.21 |
| [WeCom Choice Card](WeComMessages/WeComChoiceCardContent.md) | `wecom.card.choice`       | 勾選卡片               | 1.21 |
| [WeCom Dropdown List Card](WeComMessages/WeComDropdownListCardContent.md) | `wecom.card.dropdownlist` | 多組下拉選單卡片       | 1.21 |
| [WeCom Template Card](WeComTemplateCardContent.md)           | `wecom.card.template`     | 企業微信 Template Card | 1.21 |

