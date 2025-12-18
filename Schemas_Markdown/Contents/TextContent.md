

# Text Content

>  靜態的文字訊息



## ◆ Channel Support



| Channel 類型            | 是否支援 | 備註                                             |
| ----------------------- | -------- | ------------------------------------------------ |
| Emulator                | **O**    | 支援 Markdown 語法                               |
| Web Chat、iota Chat Bot | **O**    | 支援 Markdown 語法                               |
| iota                    | **O**    |                                                  |
| LINE                    | **O**    | 文字長度上限 2000 字                             |
| Teams                   | **O**    | 支援 Markdown 語法<br />整個訊息物件上限 28 KB   |
| Slack                   | **▲**    | 支援 Slack Markdown 語法，非標準的 Markdown 語法 |
| Webex                   | **O**    | 支援部分 Markdown 語法                           |
| Facebook Messenger      | **O**    | 文字長度上限 2000 字                             |
| WhatsApp                | **O**    | 文字長度上限 4096 字                             |
| Telegram                | **O**    | 部分支援 Markdown 語法<br />文字長度上限 4096 字 |
| M+                      | **O**    |                                                  |
| WeChat (微信個人號)     | **O**    |                                                  |
| WeCom (企業微信)        | **O**    | 支援部分 Markdown 語法                           |
| DingTalk                | **O**    | 支援部分 Markdown 語法                           |
| Apple Business Chat     | **O**    |                                                  |



## ◆ Schema

繼承自 [MessageContent](MessageContent.md)

| 屬性                 | 資料型態                                       | 必要屬性 | 描述                                                         | 支援變數 | 版本 |
| -------------------- | ---------------------------------------------- | -------- | ------------------------------------------------------------ | -------- | ---- |
| *Type*               | string                                         | Y        | 類型，值為 `text`                                            | **X**    | 1.0  |
| **Text**             | string                                         | Y        | 文字                                                         | **O**    | 1.0  |
| *QuickReply*         | [ButtonContent[]](Components/ButtonContent.md) | N        | 快速回覆按鈕                                                 | **X**    | 1.1  |
| *ChannelDataPayload* | object                                         | N        | Channel Data Payload，[使用限制](../Components/ChannelDataPayload.md) | **O**    | 1.14 |



## ◆ Example

### ● 靜態文字

```json
{
    "Type": "text",
    "Text": "Hello",
    "QuickReply": [
        {
            "Type": "imBack",
            "Title": "選單",
            "Value": "menu"
        },
        {
            "Type": "imBack",
            "Title": "求助",
            "Value": "help"
        }
    ]
}
```



### ●  動態文字 (使用變數)

* 透過輸入 `{{變數名稱}}` 將變數的值帶入
* 變數可以[參考這裡](../Variables/Variable.md) 

```json
{
    "Type": "text",
    "Text": "Hello {{$.Conversation.UserName}}",
    "QuickReply": [
        {
            "Type": "imBack",
            "Title": "選單",
            "Value": "menu"
        },
        {
            "Type": "imBack",
            "Title": "求助",
            "Value": "help"
        }
    ]
}
```

```json
{
    "Type": "text",
    "Text": "You say {{$.Message.Text}}",
    "QuickReply": [
        {
            "Type": "imBack",
            "Title": "選單",
            "Value": "menu"
        },
        {
            "Type": "imBack",
            "Title": "求助",
            "Value": "help"
        }
    ]
}
```



