# WeCom 勾選卡片

> 勾選卡片



## ◆ Screenshot  

* **單選**



* **多選**





## ◆ Schema

繼承自 [MessageContent](MessageContent.md)

| 屬性              | 資料型態                                   | 必要屬性 | 描述                                          | 支援變數 | 版本 |
| ----------------- | ------------------------------------------ | -------- | --------------------------------------------- | -------- | ---- |
| *Type*            | string                                     | Y        | 類型，值為 `wecom.card.choice`                | **X**    | 1.21 |
| **Title**         | string                                     | Y        | 標題，字數最多 **16** 個字                    | **O**    | 1.21 |
| **Text**          | string                                     | N        | 內文，字數最多 **160** 個字                   | **O**    | 1.21 |
| **Key**           | string                                     | Y        | 卡片 Key，用於處理識別 User Submit 哪一張卡片 | **O**    | 1.21 |
| **ChoiceSet**     | [WeComChoiceSet](#-wecom-choice-set)[]     | Y        | 選項，最少**1**個、最多**20**個               | **X**    | 1.21 |
| **IsMultiSelect** | boolean                                    | Y        | 是否為多選，預設值：`false`                   | **X**    | 1.21 |
| **SubmitButton**  | [WeComSubmitAction](#-wecom-submit-action) | Y        | 送出的按鈕                                    | **X**    | 1.21 |

### ● WeCom Choice Set

| 屬性      | 資料型態 | 必要屬性 | 描述                           | 支援變數 | 版本 |
| --------- | -------- | -------- | ------------------------------ | -------- | ---- |
| Title     | string   | Y        | 選項標題，字數最多 **17** 個字 | **O**    | 1.21 |
| Value     | string   | Y        | 選項值，字數最多 **128** 個字  | **O**    | 1.21 |
| IsChecked | boolean  | N        | 是否預設勾選，預設值：`false`  | **X**    | 1.21 |

### ● WeCom Submit Action

| 屬性  | 資料型態 | 必要屬性 | 描述                           | 支援變數 | 版本 |
| ----- | -------- | -------- | ------------------------------ | -------- | ---- |
| Title | string   | Y        | 按鈕標題，字數最多 **10** 個字 | **O**    | 1.21 |
| Value | string   | Y        | 按鈕值，字數最多 **1024** 個字 | **O**    | 1.21 |



---

## ◆ Submit 後回傳內容

* Bot 收到的 Submit 資料 (Activity)

* **單選**

```json
{
    "Type": "message",
    "Value": {
        "taskId": "<WeCom Task Id>",
        "eventKey": "<Submit Button Value>",
        "cardType": "vote_interaction",
        "data": {
            "<Key>": "<Value>"
        }
    }
}
```

* **多選**
    * 以 `,` 間隔多個選項

```json
{
    "Type": "message",
    "Value": {
        "taskId": "<WeCom Task Id>",
        "eventKey": "<Submit Button Value>",
        "cardType": "vote_interaction",
        "data": {
            "<Key>": "<Value 1>,<Value 2>,<Value 3>"
        }
    }
}
```


### ■ 可使用的變數

* **在 Variable Action、Next Node 中可使用的變數**
    * **`$.Message.eventKey`** ─ 使用者點擊卡片按鈕的資料內
    * **`$.Message.data.<Your Key>`** ─ 使用者勾選的選項，Key 對應卡片設定的 **Key** 屬性
    * **`$.Message.taskId`** ─ 使用者點擊卡片的 Task Id
* **在 Prompt Node Action 中可使用的變數**
    * **`$.Value.eventKey`** ─ 使用者點擊卡片按鈕的資料內容
    * **`$.data.<Your Key>`** ─ 使用者勾選的選項，Key 對應卡片設定的 **Key** 屬性
    * **`$.Message.taskId`** ─ 使用者點擊卡片的 Task Id



---

## ◆ Example

* **單選**

```json
{
    "Type": "wecom.card.choice",
    "Title": "Title",
    "Text": "Text",
    "Key": "Question",
    "ChoiceSet": [
        {
            "Title": "Title 1",
            "Value": "1",
            "IsChecked": false
        },
        {
            "Title": "Title 2",
            "Value": "2",
            "IsChecked": false
        },
        {
            "Title": "Title 3",
            "Value": "3",
            "IsChecked": false
        }
    ],
    "IsMultiSelect": false,
    "SubmitButton": {
        "Title": "Send",
        "Value": "submit"
    }
}
```

* **多選**

```json
{
    "Type": "wecom.card.choice",
    "Title": "Title",
    "Text": "Text",
    "Key": "Question",
    "ChoiceSet": [
        {
            "Title": "Title 1",
            "Value": "1",
            "IsChecked": false
        },
        {
            "Title": "Title 2",
            "Value": "2",
            "IsChecked": false
        },
        {
            "Title": "Title 3",
            "Value": "3",
            "IsChecked": false
        }
    ],
    "IsMultiSelect": true,
    "SubmitButton": {
        "Title": "Send",
        "Value": "submit"
    }
}
```



