# LINE Action Content



## ◆ Schema

| 屬性                      | 資料型態         | 必要屬性 | 描述                                 | 支援變數 | 版本 |
| ------------------------- | ---------------- | -------- | ------------------------------------ | -------- | ---- |
| Type                      | string           | Y        | 類型                                 | **X**    | 1.5  |
| Title                     | string           | Y        | 按鈕標題，對應 LINE Action Label     | **O**    | 1.5  |
| Value                     | string           | N        | 按鈕值                               | **O**    | 1.5  |
| Options                   | object           | N        | Channel 相關資訊                     | **X**    | 1.23 |
| [Styles](#-style-options) | <string, string> | N        | 按鈕樣式，**限 Flex Message Button** | **X**    | 1.5  |

### ● Button Type

| 按鈕類型         | 描述                                                         | LINE Action 屬性對應                                  | 版本 |
| ---------------- | ------------------------------------------------------------ | ----------------------------------------------------- | ---- |
| `message`        | 回覆訊息 (顯示文字)，[Message Action](https://developers.line.biz/en/reference/messaging-api/#message-action) | **Value** → **data**                                  | 1.5  |
| `postback`       | 回覆訊息 (隱藏文字)，[Postback Action](https://developers.line.biz/en/reference/messaging-api/#postback-action) | **Value** → **data**<br />**Title** → **displayText** | 1.5  |
| `uri`            | 開啟連結，[Uri Action](https://developers.line.biz/en/reference/messaging-api/#uri-action) | **Value** → **uri**                                   | 1.23 |
| `url`            | 開啟連結 **(舊版)**，[Uri Action](https://developers.line.biz/en/reference/messaging-api/#uri-action) | **Value** → **uri**                                   | 1.5  |
| `datetimepicker` | 選擇日期時間，[Datetime Picker Action](https://developers.line.biz/en/reference/messaging-api/#datetime-picker-action) | **Value** → **data**<br />**Options** → 其他屬性      | 1.23 |
| `location`       | 傳送位置資訊，[Location Aciotn](https://developers.line.biz/en/reference/messaging-api/#location-action)<br />**限 Quick Reply 使用** | N/A                                                   | 1.23 |
| `camera`         | 開啟相機，[Camera Aciotn](https://developers.line.biz/en/reference/messaging-api/#camera-action)<br />**限 Quick Reply 使用** | N/A                                                   | 1.23 |
| `cameraRoll`     | 上傳圖片，[Camera Roll Action](https://developers.line.biz/en/reference/messaging-api/#camera-roll-action)<br />**限 Quick Reply 使用** | N/A                                                   | 1.23 |

### ● Channel Data

* 當 **Type** = `postback`

| 屬性        | 資料型態 | 必要屬性 | 描述                                    | 支援變數 | 版本 |
| ----------- | -------- | -------- | --------------------------------------- | -------- | ---- |
| DisplayText | string   | N        | 顯示的文字，預設值：空字串 (使用 Title) | **O**    | 1.23 |

* 當 **Type** = `datetimepicker`
    * 內容對應 [LINE Datetime Picker Action](https://developers.line.biz/en/reference/messaging-api/#datetime-picker-action)

| 屬性    | 資料型態 | 必要屬性 | 描述                                 | 支援變數 | 版本 |
| ------- | -------- | -------- | ------------------------------------ | -------- | ---- |
| Data    | string   | N        | 資料，預設值：空字串 (使用 Value 值) | **O**    | 1.23 |
| Mode    | string   | Y        | 模式，預設值：`datetime`             | **O**    | 1.23 |
| Initial | string   | N        | 初始值                               | **O**    | 1.23 |
| Max     | string   | N        | 最大值                               | **O**    | 1.23 |
| Min     | string   | N        | 最小值                               | **O**    | 1.23 |



---

## ◆ 點擊 Action 後的回傳值

* **Postback Action**
    * `Text`、`Value` 對應變數的 `$.Message.Text`、`$.Message.Value`

```json
{
    "Text": "<這裡會放 LINE 的 Action.data>",
    "Value": {
        "postback": {
            "data": "<這裡會放 LINE 的 Action.data>",
            "params": "<這裡會放 LINE 的 Action.params>"
        }
    }
}
```

* **Datetime Picker Action (mode = `datetime`)**
    * `Text`、`Value` 對應變數的 `$.Message.Text`、`$.Message.Value`

```json
{
    "Text": "<這裡會放 LINE 的 Action.data>",
    "Value": {
        "postback": {
            "data": "<這裡會放 LINE 的 Action.data>",
            "params": {
                 "datetime": "<日期時間>"
            }
        }
    }
}
```

* **Datetime Picker Action (mode = `date`)**
    * `Text`、`Value` 對應變數的 `$.Message.Text`、`$.Message.Value`

```json
{
    "Text": "<這裡會放 LINE 的 Action.data>",
    "Value": {
        "postback": {
            "data": "<這裡會放 LINE 的 Action.data>",
            "params": {
                 "date": "<日期>"
            }
        }
    }
}
```

* **Datetime Picker Action (mode = `time`)**
    * `Text`、`Value` 對應變數的 `$.Message.Text`、`$.Message.Value`

```json
{
    "Text": "<這裡會放 LINE 的 Action.data>",
    "Value": {
        "postback": {
            "data": "<這裡會放 LINE 的 Action.data>",
            "params": {
                 "time": "<時間>"
            }
        }
    }
}
```

* **Location Picker Action**
    * `Text`、`Value` 對應變數的 `$.Message.Text`、`$.Message.Value`

```json
{
    "Type": "message",
    "Value": { 
        "location": { 
            "address": "10491台灣台北市中山區德惠街9號", 
            "longitude": 121.5247771, 
            "latitude": 25.0668995
        }
    }
}
```





---

## ◆ Example

* **Message Action**

```json
{
    "Type": "message",
    "Title": "Reply message",
    "Value": "your message"
}
```

* **Postback Action**

```json
{
    "Type": "postback",
    "Title": "Submit",
    "Value": {
        "action": "submit",
        "data": "your data"
    }
}
```

* **Uri Action**

```json
{
    "Type": "uri",
    "Title": "Open Line Hub",
    "Value": "https://hub.line.me/"
}
```

* **Datetime Picker Action**

```json
{
    "Type": "datetimepicker",
    "Title": "Button 04",
    "Value": "Choose a date",
    "Options": {
        "Mode": "date",
        "Initial": "2000-01-01",
        "Max": "2099-12-31",
        "Min": "1900-01-01d"
    }
}
```

* **Location Action**

```json
{
    "Type": "location",
    "Title": "Button 03",
    "Value": "Send Location"
}
```

* **Camera**

```json
{
    "Type": "camera",
    "Title": "Button 03",
    "Value": "Take a picture"
}
```

* **Camera Roll**

```json
{
    "Type": "camera_roll",
    "Title": "Button 03",
    "Value": "Take a picture"
}
```

* **Message Action + Style**
    * **Style 設定僅適用於 Flex Message**

```json
{
    "Type": "message",
    "Title": "Button 01",
    "Value": "1",
    "Styles": {
        "Style": "secondary",
        "Height": "sm"
    }
}
```



## ◆ Style Options

> 有需要在使用，沒有設定的項目會使用預設值

* [Flex Message Button Component 屬性參考](https://developers.line.biz/en/reference/messaging-api/#button)

| 樣式選項 | 說明                                                         | 支援變數 | 參考值                             |
| -------- | ------------------------------------------------------------ | -------- | ---------------------------------- |
| Style    | **[[Button]](https://developers.line.biz/en/reference/messaging-api/#button)** 按鈕樣式，預設：`secondary` | **X**    | `primary`、`secondary`、`link`     |
| Height   | **[[Button]](https://developers.line.biz/en/reference/messaging-api/#button)** 按鈕高度，預設：`sm` | **X**    | `sm`、`md`                         |
| Color    | **[[Button]](https://developers.line.biz/en/reference/messaging-api/#button)** 按鈕顏色，預設：`secondary` | **X**    | 符合 `#RRGGBB` or `#RRGGBBAA` 格式 |