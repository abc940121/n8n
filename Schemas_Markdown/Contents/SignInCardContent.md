# SignIn Card Content

> 靜態的SignIn Card訊息



## ◆ Channel Support

| Channel 類型            | 是否支援 | 備註                                                         |
| ----------------------- | -------- | ------------------------------------------------------------ |
| Emulator                | **O**    |                                                              |
| Web Chat、iota Chat Bot | **O**    |                                                              |
| iota                    | **O**    | 1. 舊版 iota 不支援 Carousel 卡片排版<br />2. 實作上會轉換成 Adaptive Card |
| LINE                    | **O**    | 1. 實作上會轉換成 LINE Flex Message<br />2. ~~卡片 PostBack 按鈕回覆的值是放在 Activity.Text~~ |
| Teams                   | **O**    | 卡片按鈕皆視為 ImBack                                        |
| Slack                   | **O**    | 1. 實作上會轉換成 Slack Block Kit 訊息<br />2. 回覆的內容為專用格式 |
| Webex                   | **O**    | 1. 實作上會轉換成 Adaptive Card<br />2. 按鈕數量最多5個      |
| Facebook Messenger      | **O**    | 卡片按鈕皆視為 ImBack                                        |
| WhatsApp                | **O**    | 1. 卡片按鈕皆視為 ImBack<br />2. 按鈕如果同時有 OpenUrl 和 ImBack 會拆成兩個卡片 |
| Telegram                | **O**    | 卡片按鈕皆視為 PostBack                                      |
| M+                      | **▲**    | 1. 按鈕不支援開啟連結<br />2. 按鈕標題 = 點擊後回覆文字，卡片按鈕皆視為 ImBack<br />3. 標題字數不得超過 500個字 |
| WeChat (微信個人號)     | **X**    |                                                              |
| WeCom (企業微信)        | **O**    | 1. 不支援 Carousel 卡片排版<br />2. 不支援群組對話           |
| DingTalk                | **O**    | 不支援按鈕、Carousel 卡片排版                                |
| Apple Business Chat     | **X**    | 目前暫時不支援<br />(Apple Business Chat 有支援類似卡片的訊息) |



## ◆ Schema

繼承自 [MessageContent](MessageContent.md)

| 屬性    | 資料型態                                       | 必要屬性 | 描述                     | 支援變數 | 版本 |
| ------- | ---------------------------------------------- | -------- | ------------------------ | -------- | ---- |
| *Type*  | string                                         | Y        | 類型，值為 `signin.card` | **X**    | 1.0  |
| **Text** | string                                         | N        | 標題內容                 | **O**    | 1.0  |
| **Buttons** | [ButtonContent[]](Components/ButtonContent.md) | N        | 按鈕                     | **X**    | 1.0  |
| *QuickReply* | [ButtonContent[]](Components/ButtonContent.md) | N | 快速回覆按鈕                | **X**    | 1.1  |
| *ChannelDataPayload* | object | N | Channel Data Payload，[使用限制](../Components/ChannelDataPayload.md) | **O** | 1.14 |



## ◆ Screenshots

![](Screenshots/SignInCardContent.jpg)



## ◆ Example

### ● 靜態卡片標題內容

```json
{
    "Type": "signin.card",
    "Text": "This is text",
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
    "Type": "signin.card",
    "Text": "You say {{$.Message.text}}",
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