# Event Content

> 互動事件



## ◆ Channel Support

| Channel 類型            | 是否支援 | 備註 |
| ----------------------- | -------- | ---- |
| Emulator                | **X**    |      |
| Web Chat、iota Chat Bot | **O**    |      |
| iota                    | **X**    |      |
| LINE                    | **X**    |      |
| Teams                   | **X**    |      |
| Slack                   | **X**    |      |
| Webex                   | **X**    |      |
| Facebook Messenger      | **X**    |      |
| WhatsApp                | **X**    |      |
| M+                      | **X**    |      |
| Telegram                | **X**    |      |
| WeChat (微信個人號)     | **X**    |      |
| WeCom (企業微信)        | **X**    |      |
| DingTalk                | **X**    |      |
| Apple Business Chat     | **X**    |      |



## ◆ Schema

繼承自 [MessageContent](MessageContent.md)

| 屬性                              | 資料型態 | 必要屬性 | 描述                                                         | 支援變數 | 版本 |
| --------------------------------- | -------- | -------- | ------------------------------------------------------------ | -------- | ---- |
| *Type*                            | string   | Y        | 類型，值為 `event`                                           | **X**    | 1.1  |
| **[MessageType](#-message-type)** | string   | Y        | 訊息類型                                                     | **X**    | 1.1  |
| **Name**                          | string   | Y        | 名稱                                                         | **O**    | 1.1  |
| **DataType**                      | string   | Y        | 資料的型態                                                   | **X**    | 1.1  |
| **Data**                          | string   | Y        | 資料                                                         | **O**    | 1.1  |
| *ChannelDataPayload*              | object   | N        | Channel Data Payload，[使用限制](../Components/ChannelDataPayload.md) | **O**    | 1.14 |

### ■ Message Type


| 訊息類型 | 值       | 描述                       |
| -------- | -------- | -------------------------- |
| Event    | `event`  | 事件                       |
| Inovke   | `invoke` | 觸發行為                   |
| Typing   | `typing` | 正在打字中... **(預設值)** |
| Trace    | `trace`  | 偵錯訊息                   |

* **Data Type**
    * `string`
    * `object`



---

## ◆ Example

### ● 發送 Event

* **腳本設定範例**

```json
{
    "Type": "event",
    "MessageType": "event",
    "EventName": "Open_Live_Chat",
    "DataType": "object",
    "Data": "{ \"UserName\": \"{{$.Variables.Profile.UserName}}\", \"UserEmail\": \"{{$.Variables.Profile.UserEmail}}\" }"
}
```

* **Channel 收到的訊息**

```json
{
	"type": "event",
	"name": "Open_Live_Chat",
	"value": {
        "userName": "Ace",
        "userEmail": "ace@noemail.com.tw"
    },
    "relatesTo": {
        "bot": {
            "id": "xxxBot",
            "name": "Bot"
        },
        "user": {
            "id": "a123456789",
            "name": "b456789"
        },
        ...
    },
    ...
}
```



### ● 發送 Invoke

* **腳本設定範例**

```json
{
    "Type": "event",
    "MessageType": "invoke",
    "EventName": "Open_Live_Chat",
    "DataType": "object",
    "Data": "{ \"UserName\": \"{{$.Variables.Profile.UserName}}\", \"UserEmail\": \"{{$.Variables.Profile.UserEmail}}\" }"
}
```

* **Channel 收到的訊息**

```json
{
	"type": "invoke",
	"name": "Open_Live_Chat",
	"value": {
        "userName": "Ace",
        "userEmail": "ace@noemail.com.tw"
    },
    "relatesTo": {
        "bot": {
            "id": "xxxBot",
            "name": "Bot"
        },
        "user": {
            "id": "a123456789",
            "name": "b456789"
        },
        ...
    },
    ...
}
```



### ● 發送 Typing

* **腳本設定範例**

```json
{
    "Type": "event",
    "MessageType": "typing",
    "EventName": "",
    "DataType": "",
    "Data": ""
}
```

* **Channel 收到的訊息**

```json
{
	"type": "typing",
    ...
}
```





### ● 發送 Trace

* **腳本設定範例**

```json
{
    "Type": "event",
    "MessageType": "trace",
    "EventName": "Show_Profile",
    "DataType": "object",
    "Data": "{ \"UserName\": \"{{$.Variables.Profile.UserName}}\", \"UserEmail\": \"{{$.Variables.Profile.UserEmail}}\" }"
}
```

* **Channel 收到的訊息**

```json
{
    "type": "trace",
    "name": "Show_Profile",
    "label": "",
    "valueType": "object",
    "value": {
        "userName": "Ace",
        "userEmail": "ace@noemail.com.tw"
    },
    ...
}
```





