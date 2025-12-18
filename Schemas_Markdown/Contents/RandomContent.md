# Random Message Content

>  隨機的訊息



## ◆ Channel Support



| Channel 類型            | 是否支援 |
| ----------------------- | -------- |
| Emulator                | **O**    |
| Web Chat、iota Chat Bot | **O**    |
| iota                    | **O**    |
| LINE                    | **O**    |
| Teams                   | **O**    |
| Telegram                | **O**    |
| Slack                   | **O**    |
| Webex                   | **O**    |
| Facebook Messenger      | **O**    |
| WhatsApp                | **O**    |
| M+                      | **O**    |
| WeChat (微信個人號)     | **O**    |
| WeCom (企業微信)        | **O**    |
| DingTalk                | **O**    |
| Apple Business Chat     | **O**    |



## ◆ Schema

繼承自 [MessageContent](MessageContent.md)

| 屬性                 | 資料型態                              | 必要屬性 | 描述                                                         | 支援變數 | 版本 |
| -------------------- | ------------------------------------- | -------- | ------------------------------------------------------------ | -------- | ---- |
| *Type*               | string                                | Y        | 類型，值為 `random`                                          | **X**    | 1.0  |
| **Messages**         | [MessageContent[]](MessageContent.md) | Y        | 隨機訊息                                                     | **O**    | 1.21 |
| *ChannelDataPayload* | object                                | N        | Channel Data Payload，[使用限制](../Components/ChannelDataPayload.md) | **O**    | 1.14 |

* **Messages**
    * `不支援以下 Message Content`
        * [RandomMessageContent](RandomMessageContent.md)



## ◆ Example

### ● 靜態卡片標題內容

```json
{
    "Type": "random",
    "Messages": [
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



## ◆ Example

```json
{
    "Type": "random",
    "Messages": [
        {
            "Type": "hero.card",
            "Title": "要繼續對話嗎？",
            "Subtitle": "",
            "Text": "",
            "ImageUrl": "https://vital-chatbot.gsscloud.com/fileserver/api/file/blob/8fde2300-e213-480a-a6bf-6cfc64d2aab7.png",
            "IsThumbnail": false,
            "Buttons": [
                {
                    "Type": "imBack",
                    "Title": "繼續對話",
                    "Value": "yes"
                },
                {
                    "Type": "imBack",
                    "Title": "停止對話",
                    "Value": "no"
                }
            ]
        },
        {
            "Type": "signin.card",
            "Text": "要繼續對話嗎？",
            "Buttons": [
                {
                    "Type": "imBack",
                    "Title": "繼續對話",
                    "Value": "yes"
                },
                {
                    "Type": "imBack",
                    "Title": "停止對話",
                    "Value": "no"
                }
            ]
        },
        {
            "Type": "text",
            "Text": "要繼續對話嗎？ (Yes/No)",
            "QuickReply": [
                {
                    "Type": "imBack",
                    "Title": "繼續對話",
                    "Value": "yes"
                },
                {
                    "Type": "imBack",
                    "Title": "停止對話",
                    "Value": "no"
                }
            ]
        }
    ]
}
```















