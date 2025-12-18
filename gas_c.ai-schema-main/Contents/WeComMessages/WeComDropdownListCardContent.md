# WeCom Dropdown List Card

> 下拉選單卡片



## ◆ Screenshot  



![](https://wework.qpic.cn/wwpic/977007_JDisThiPRXam-GG_1628758163/0)



## ◆ Schema

繼承自 [MessageContent](MessageContent.md)

| 屬性             | 資料型態                                     | 必要屬性 | 描述                                 | 支援變數 | 版本 |
| ---------------- | -------------------------------------------- | -------- | ------------------------------------ | -------- | ---- |
| *Type*           | string                                       | Y        | 類型，值為 `wecom.card.dropdownlist` | **X**    | 1.21 |
| **Title**        | string                                       | Y        | 標題，字數最多 **16** 個字           | **O**    | 1.21 |
| **Text**         | string                                       | N        | 內文，字數最多 **160** 個字          | **O**    | 1.21 |
| **DropdownList** | [WeComDropdownList](#-wecom-dropdown-list)[] | Y        | 下拉選單，至少**1**個、最多**3**個   | **X**    | 1.21 |
| **SubmitButton** | [WeComSubmitButton](#-wecom-submit-button)   | Y        | 送出的按鈕                           | **X**    | 1.21 |

### ● WeCom Dropdown List

| 屬性    | 資料型態                                                  | 必要屬性 | 描述                                                         | 支援變數 | 版本 |
| ------- | --------------------------------------------------------- | -------- | ------------------------------------------------------------ | -------- | ---- |
| Key     | string                                                    | Y        | 下拉選單的 Key，用於處理識別 User Submit 哪一個選項，字數最多 **1024** 個字 | **O**    | 1.21 |
| Title   | string                                                    | Y        | 下拉選單上方的標題                                           | **O**    | 1.21 |
| Options | [WeComDropdownListOption](#-wecom-dropdown-list-option)[] | Y        | 下拉選單選項，至少**1**個、最多**10**個                      | **X**    | 1.21 |

### ● WeCom Dropdown List Option

| 屬性  | 資料型態 | 必要屬性 | 描述                           | 支援變數 | 版本 |
| ----- | -------- | -------- | ------------------------------ | -------- | ---- |
| Title | string   | Y        | 選項標題，字數最多 **16** 個字 | **O**    | 1.21 |
| Value | string   | Y        | 選項值，字數最多 **128** 個字  | **O**    | 1.21 |

### ● WeCom Submit Button

| 屬性  | 資料型態 | 必要屬性 | 描述                           | 支援變數 | 版本 |
| ----- | -------- | -------- | ------------------------------ | -------- | ---- |
| Title | string   | Y        | 按鈕標題，字數最多 **10** 個字 | **O**    | 1.21 |
| Value | string   | Y        | 按鈕值，字數最多 **1024** 個字 | **O**    | 1.21 |





---

## ◆ Submit 後回傳內容

* Bot 收到的 Submit 資料 (Activity)
    * Key 對應各自的下拉選單


```json
{
    "Type": "message",
    "Value": {
        "taskId": "<WeCom Task Id>",
        "eventKey": "<Submit Button Value>",
        "cardType": "vote_interaction",
        "data": {
            "<Key 1>": "<Value 1>",
            "<Key 2>": "<Value 2>"
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



```json
{
    "Type": "wecom.card.dropdownlist",
    "Title": "Title",
    "Text": "Text",
    "DropdownList": [
        {
            "Key": "Key1",
            "Title": "Key 1",
            "Options": [
                {
                    "Title": "Value 1",
                    "Value": "1"
				},
                {
                    "Title": "Value 2",
                    "Value": "2"
				},
                {
                    "Title": "Value 3",
                    "Value": "3"
				}
            ]
        }
    ],
    "SubmitButton": {
        "Title": "Send",
        "Value": "submit"
    }
}
```

