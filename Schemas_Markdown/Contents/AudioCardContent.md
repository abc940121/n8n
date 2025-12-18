# Audio Card Content

> 靜態的Video Card訊息，可以嵌入 MP3 內容



## ◆ Channel Support



| Channel 類型            | 是否支援 | 備註                                                         |
| ----------------------- | -------- | ------------------------------------------------------------ |
| Emulator                | **O**    |                                                              |
| Web Chat、iota Chat Bot | **O**    |                                                              |
| iota                    | **O**    | 1. 舊版 iota不支援 Carousel 卡片排版<br />2. 實作上會轉換成 Adaptive Card |
| LINE                    | **▲**    | 1. 實作上會轉換成 2則訊息 Audio Message + LINE Flex Message<br />2. ~~卡片 PostBack 按鈕回覆的值是放在 Activity.Text~~<br />3. 檔案只支援 MP3，檔案上限 10 MB，需要 HTTPS |
| Teams                   | **X**    |                                                              |
| Slack                   | **X**    |                                                              |
| Webex                   | **O**    | 1. 實作上會轉換成 Adaptive Card<br />2. 按鈕數量最多5個      |
| Facebook Messenger      | **X**    |                                                              |
| WhatsApp                | **▲**    | 1. 實作上會轉換成 2則訊息 Audio Message + Card Message<br />2. 檔案上限 16 MB |
| Telegram                | **X**    |                                                              |
| M+                      | **X**    |                                                              |
| WeChat (微信個人號)     | **X**    |                                                              |
| WeCom (企業微信)        | **X**    |                                                              |
| DingTalk                | **X**    |                                                              |
| Apple Business Chat     | **X**    |                                                              |



## ◆ Schema

繼承自 [MessageContent](MessageContent.md)

| 屬性     | 資料型態                                         | 必要屬性 | 描述                    | 支援變數 | 版本 |
| -------- | ------------------------------------------------ | -------- | ----------------------- | -------- | ---- |
| *Type*   | string                                           | Y        | 類型，值為 `audio.card` | **X**    | 1.0  |
| **Title** | string                                           | N        | 標題                    | **O**    | 1.0  |
| **Subtitle** | string                                           | N        | 副標題                  | **O**    | 1.0  |
| **Text** | string                                           | N        | 內容                    | **O**    | 1.0  |
| **Audio** | [MediaContent](Components/MediaSourceContent.md) | N        | 音樂                    | **X**    | 1.0  |
| **Buttons** | [ButtonContent[]](Components/ButtonContent.md)   | N        | 按鈕                    | **X**    | 1.0  |
| *QuickReply* | [ButtonContent[]](Components/ButtonContent.md) | N | 快速回覆按鈕                | **X**    | 1.1  |
| *ChannelDataPayload* | object | N | Channel Data Payload，[使用限制](../Components/ChannelDataPayload.md) | **O** | 1.14 |



## ◆ Screenshots

![](Screenshots/AudioCardContent.jpg)



## ◆ Example

### ● 靜態卡片標題內容

```json
{
    "Type": "audio.card",
    "Title": "This is title",
    "Subtitle": "This is subtitle",
    "Text": "This is text",
    "Audio": {
        "Url": "https://www.gss.com.tw/audio.mp3"
    },
    "Buttons": [
        {
            "Type": "imBack",
            "Title": "Button 01",
            "Value": "1"
        },
        {
            "Type": "imBack",
            "Title": "Button 02",
            "Value": "2"
        }
    ]
}
```



### ● 動態卡片標題內容

* 透過輸入 `{{變數名稱}}` 將變數的值帶入
* 變數可以[參考這裡](../Variables/Variable.md) 

```json
{
    "Type": "audio.card",
    "Title": "Hi {{$.Conversation.UserName}}",
    "Subtitle": "",
    "Text": "You say {{$.Message.text}}",
    "Audio": {
        "Url": "https://www.gss.com.tw/audio.mp3"
    },
    "Buttons": [
        {
            "Type": "imBack",
            "Title": "Button 01",
            "Value": "1"
        },
        {
            "Type": "imBack",
            "Title": "Button 02",
            "Value": "2"
        }
    ]
}
```

