# Trace Content

>  偵錯訊息



## ◆ Channel Support

| Channel Type            | Support | 備註                             |
| ----------------------- | ------- | -------------------------------- |
| Emulator                | **O**   |                                  |
| Web Chat、iota Chat Bot | **O**   | 基於效能問題，正式環境不建議使用 |
| iota                    | **X**   |                                  |
| LINE                    | **X**   |                                  |
| Teams                   | **X**   |                                  |
| Slack                   | **X**   |                                  |
| Webex                   | **X**   |                                  |
| WhatsApp                | **X**   |                                  |
| Facebook Messenger      | **X**   |                                  |
| M+                      | **X**   |                                  |
| WeChat (微信個人號)     | **X**   |                                  |
| WeCom (企業微信)        | **X**   |                                  |
| Teams                   | **X**   |                                  |
| Apple Business Chat     | **X**   |                                  |



## ◆ Schema

繼承自 [MessageContent](MessageContent.md)

| 屬性                 | 資料型態 | 必要屬性 | 描述                                                         | 支援變數 | 版本 |
| -------------------- | -------- | -------- | ------------------------------------------------------------ | -------- | ---- |
| *Type*               | string   | Y        | 類型，值為 `trace`                                           | **X**    | 1.1  |
| **Name**             | string   | Y        | 名稱                                                         | **O**    | 1.1  |
| **Label**            | string   | N        | 標籤                                                         | **O**    | 1.1  |
| **ValueType**        | string   | N        | 資料的資料類型                                               | **O**    | 1.1  |
| **Value**            | string   | Y        | 資料                                                         | **O**    | 1.1  |
| *ChannelDataPayload* | object   | N        | Channel Data Payload，[使用限制](../Components/ChannelDataPayload.md) | **O**    | 1.14 |



## ◆ Example

### ● 靜態文字

```json
{
    "Type": "trace",
    "Name": "Debug Conversation",
    "Label": "Info",
    "ValueType": "string",
    "Value": "Debug Test"
}
```



### ●  動態文字 (使用變數)

* 透過輸入 `{{變數名稱}}` 將變數的值帶入
* 變數可以[參考這裡](../Variables/Variable.md) 

```json
{
    "Type": "trace",
    "Name": "Debug User",
    "Label": "Info",
    "ValueType": "string",
    "Value": "User {{$.Conversation.UserId}}"
}
```

```json
{
    "Type": "trace",
    "Name": "Debug Message",
    "Label": "Info",
    "ValueType": "string",
    "Value": "You say {{$.Message.Text}}"
}
```