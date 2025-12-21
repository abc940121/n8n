# Adaptive Template Card Content

> 範本卡片



## ◆ Channel Support

> [Adaptive Card 文件](https://adaptivecards.io/explorer/)

| Channel 類型            | 是否支援 | 備註                                                         |
| ----------------------- | -------- | ------------------------------------------------------------ |
| Emulator                | **O**    | Adaptive Card 支援的版本為 **1.3**                           |
| Web Chat、iota Chat Bot | **O**    | Adaptive Card 支援的版本為 **1.4**                           |
| iota                    | **O**    | Adaptive Card 支援的版本為 **1.5**                           |
| LINE                    | **X**    |                                                              |
| Teams                   | **O**    | 1. Adaptive Card 支援的版本為 **1.1**<br />2. 不支援 Audio 和 Video 等元件 |
| Slack                   | **X**    |                                                              |
| Webex                   | **O**    | Adaptive Card 支援的版本為 **1.3**                           |
| Facebook Messenger      | **X**    |                                                              |
| WhatsApp                | **X**    |                                                              |
| Telegram                | **X**    |                                                              |
| M+                      | **X**    |                                                              |
| WeChat (微信個人號)     | **X**    |                                                              |
| WeCom (企業微信)        | **X**    |                                                              |
| DingTalk                | **X**    |                                                              |
| Apple Business Chat     | **X**    |                                                              |



## ◆ Schema

繼承自 [MessageContent](../MessageContent.md)

| 屬性                 | 資料型態                                                     | 必要屬性 | 描述                                                         | 支援變數 | 版本 |
| -------------------- | ------------------------------------------------------------ | -------- | ------------------------------------------------------------ | -------- | ---- |
| *Type*               | string                                                       | Y        | 類型，值為 `adaptive.card.template`                          | **X**    | 1.22 |
| **TemplateId**       | string                                                       | Y        | [套版卡片](../../../TemplateCard/TemplatCard.md)的 Template ID  **`(不得重複)`** | **X**    | 1.22 |
| **Content**          | string                                                       | Y        | Adaptive Card Json 內容                                      | **X**    | 1.22 |
| **Parameters**       | Dictionary<string, [AdaptiveCardParameter](#-adaptive-card-parameter)> | N        | 卡片綁定所需要的參數，Key 為參數名稱  **(不得重複)**         | **X**    | 1.22 |
| *QuickReply*         | [ButtonContent[]](Components/ButtonContent.md)               | N        | 快速回覆按鈕                                                 | **X**    | 1.22 |
| *ChannelDataPayload* | object                                                       | N        | Channel Data Payload，[使用限制](../Components/ChannelDataPayload.md) | **O**    | 1.22 |

### ● Adaptive Card Parameter

| 屬性      | 資料型態 | 必要屬性 | 描述                                                         | 支援變數 | 版本 |
| --------- | -------- | -------- | ------------------------------------------------------------ | -------- | ---- |
| **Type**  | string   | Y        | 參數的類型                                                   | **X**    | 1.22 |
| **Value** | object   | Y        | 參數的值                                                     | `[1]`    | 1.22 |
| *Options* | object   | N        | 僅提供 UI 顯示參數輸入，詳細請參照 [套版卡片 Template Option](../../../TemplateCard/TemplatCard.md#-template-option) | **X**    | 1.22 |

* `[1]` 是否支援變數會以 **Type** 的值而定
    * **Type** 為 `use_expression` 時，支援變數
    * **Type** 為 `plain` 時，不支援變數
    * **Type** 為 `variable` 時，直接使用指定變數的值，不處理任何運算
        * 如果設定多組變數時，只會使用第一個變數
        * 例如："`{{$.Variables.Var1}} {{$.Variables.Var2}}`"，只會取出變數 `$.Variables.Var1` 的值

#### ● Value Type

| 類型值    | 描述   |
| --------- | ------ |
| `string`  | 字串   |
| `int`     | 整數   |
| `double`  | 浮點數 |
| `boolean` | 布林   |
| `array`   | 陣列   |
| `object`  | 物件   |

#### ● Parameter Type

| 指派方式/類型    | 描述                                                         |
| ---------------- | ------------------------------------------------------------ |
| `use_expression` | Argument Value 會處理任何資料綁定                            |
| `plain`          | Argument Value 不處理任何資料綁定 **`(不處理任何變數運算)`** |
| `variable`       | 指派指定變數，不處理任何資料綁定，只處理1個變數 **`(不處理任何變數運算)`** |



## ◆ Example

### ● Parameters 為一層

* **自訂變數**
    * `$.Variables.LeaveTemplateData`

```json
{
    "Data": {
        "Applicant": "{{$.Conversation.UserName}}",
        "StartDate": "{{=> DateTime.Now.ToString(\"yyyy-MM-dd HH:mm\");}}",
        "Hours": "8",
        "Type": "特休假",
        "Subject": "特休"
    }
}
```

* **Content JSON**

```json
{
    "Type": "adaptive.card.template",
    "TemplateId": "Template-000001",
    "Content": "{\"type\":\"AdaptiveCard\",\"$schema\":\"http://adaptivecards.io/schemas/adaptive-card.json\",\"version\":\"1.2\",\"body\":[{\"type\":\"TextBlock\",\"text\":\"請假明細\",\"wrap\":true,\"size\":\"Large\",\"weight\":\"Bolder\"},{\"type\":\"Container\",\"items\":[{\"type\":\"ColumnSet\",\"columns\":[{\"type\":\"Column\",\"width\":3,\"items\":[{\"type\":\"TextBlock\",\"text\":\"申請人\",\"wrap\":true,\"weight\":\"Bolder\"}]},{\"type\":\"Column\",\"width\":7,\"items\":[{\"type\":\"TextBlock\",\"text\":\"${Applicant}\",\"wrap\":true}]}]}]},{\"type\":\"ColumnSet\",\"columns\":[{\"type\":\"Column\",\"width\":3,\"items\":[{\"type\":\"TextBlock\",\"wrap\":true,\"text\":\"請假類別\",\"weight\":\"Bolder\"}]},{\"type\":\"Column\",\"width\":7,\"items\":[{\"type\":\"TextBlock\",\"text\":\"${Type}\",\"wrap\":true}]}]},{\"type\":\"ColumnSet\",\"columns\":[{\"type\":\"Column\",\"width\":3,\"items\":[{\"type\":\"TextBlock\",\"wrap\":true,\"text\":\"請假日期\",\"weight\":\"Bolder\"}]},{\"type\":\"Column\",\"width\":7,\"items\":[{\"type\":\"TextBlock\",\"text\":\"${StartDate}\",\"wrap\":true}]}]},{\"type\":\"ColumnSet\",\"columns\":[{\"type\":\"Column\",\"width\":3,\"items\":[{\"type\":\"TextBlock\",\"wrap\":true,\"text\":\"請假時數\",\"weight\":\"Bolder\"}]},{\"type\":\"Column\",\"width\":7,\"items\":[{\"type\":\"TextBlock\",\"text\":\"${Hours}\",\"wrap\":true}]}]},{\"type\":\"ColumnSet\",\"columns\":[{\"type\":\"Column\",\"width\":3,\"items\":[{\"type\":\"TextBlock\",\"text\":\"請假事由\",\"wrap\":true,\"weight\":\"Bolder\"}]},{\"type\":\"Column\",\"width\":7,\"items\":[{\"type\":\"TextBlock\",\"text\":\"${Subject}\",\"wrap\":true}]}]}],\"actions\":[{\"type\":\"Action.Submit\",\"title\":\"送出\",\"data\":{\"Action\":\"Submit\"}}]}",
    "Parameters": [
        {
            "Name": "Applicant",
            "Type": "use_expression",
            "Value": "{{$.Variables.LeaveTemplateData.Applicant}}"
        },
        {
            "Name": "Type",
            "Type": "use_expression",
            "Value": "{{$.Variables.LeaveTemplateData.Type}}"
        },
        {
            "Name": "StartDate",
            "Type": "use_expression",
            "Value": "{{$.Variables.LeaveTemplateData.StartDate}}"
        },
        {
            "Name": "Hours",
            "Type": "use_expression",
            "Value": "{{$.Variables.LeaveTemplateData.Hours}}"
        },
        {
            "Name": "Subject",
            "Type": "use_expression",
            "Value": "{{$.Variables.LeaveTemplateData.Subject}}"
        }
    ]
}
```



---

## ● Parameters 為一層 (使用指定變數)

* **自訂變數**
    * `$.Variables.LeaveTemplateData`

```json
{
    "Data": {
        "Applicant": "{{$.Conversation.UserName}}",
        "StartDate": "{{=> DateTime.Now.ToString(\"yyyy-MM-dd HH:mm\");}}",
        "Hours": "8",
        "Type": "特休假",
        "Subject": "特休"
    }
}
```

* **Content JSON**

```json
{
     "Type": "adaptive.card.template",
     "TemplateId": "Template-000001",
     "Content": "{\"type\":\"AdaptiveCard\",\"$schema\":\"http://adaptivecards.io/schemas/adaptive-card.json\",\"version\":\"1.2\",\"body\":[{\"type\":\"TextBlock\",\"text\":\"請假明細\",\"wrap\":true,\"size\":\"Large\",\"weight\":\"Bolder\"},{\"type\":\"Container\",\"items\":[{\"type\":\"ColumnSet\",\"columns\":[{\"type\":\"Column\",\"width\":3,\"items\":[{\"type\":\"TextBlock\",\"text\":\"申請人\",\"wrap\":true,\"weight\":\"Bolder\"}]},{\"type\":\"Column\",\"width\":7,\"items\":[{\"type\":\"TextBlock\",\"text\":\"${Data.Applicant}\",\"wrap\":true}]}]}]},{\"type\":\"ColumnSet\",\"columns\":[{\"type\":\"Column\",\"width\":3,\"items\":[{\"type\":\"TextBlock\",\"wrap\":true,\"text\":\"請假類別\",\"weight\":\"Bolder\"}]},{\"type\":\"Column\",\"width\":7,\"items\":[{\"type\":\"TextBlock\",\"text\":\"${Data.Type}\",\"wrap\":true}]}]},{\"type\":\"ColumnSet\",\"columns\":[{\"type\":\"Column\",\"width\":3,\"items\":[{\"type\":\"TextBlock\",\"wrap\":true,\"text\":\"請假日期\",\"weight\":\"Bolder\"}]},{\"type\":\"Column\",\"width\":7,\"items\":[{\"type\":\"TextBlock\",\"text\":\"${Data.StartDate}\",\"wrap\":true}]}]},{\"type\":\"ColumnSet\",\"columns\":[{\"type\":\"Column\",\"width\":3,\"items\":[{\"type\":\"TextBlock\",\"wrap\":true,\"text\":\"請假時數\",\"weight\":\"Bolder\"}]},{\"type\":\"Column\",\"width\":7,\"items\":[{\"type\":\"TextBlock\",\"text\":\"${Data.Hours}\",\"wrap\":true}]}]},{\"type\":\"ColumnSet\",\"columns\":[{\"type\":\"Column\",\"width\":3,\"items\":[{\"type\":\"TextBlock\",\"text\":\"請假事由\",\"wrap\":true,\"weight\":\"Bolder\"}]},{\"type\":\"Column\",\"width\":7,\"items\":[{\"type\":\"TextBlock\",\"text\":\"${Data.Subject}\",\"wrap\":true}]}]}],\"actions\":[{\"type\":\"Action.Submit\",\"title\":\"送出\",\"data\":{\"Action\":\"Submit\"}}]}",
     "Parameters": [
         {
             "Name": "Data",
             "Type": "variable",
             "Value": "$.Variables.LeaveTemplateDataB.Data"
         }
     ]
 }
```



---

## ● Parameters 為二層

* **自訂變數**
    * `$.Variables.LeaveTemplateData`

```json
{
    "Data": {
        "Applicant": "{{$.Conversation.UserName}}",
        "StartDate": "{{=> DateTime.Now.ToString(\"yyyy-MM-dd HH:mm\");}}",
        "Hours": "8",
        "Type": "特休假",
        "Subject": "特休"
    }
}
```

* **Content JSON**

```json
{
     "Type": "adaptive.card.template",
     "TemplateId": "Template-000001",
     "Content": "{\"type\":\"AdaptiveCard\",\"$schema\":\"http://adaptivecards.io/schemas/adaptive-card.json\",\"version\":\"1.2\",\"body\":[{\"type\":\"TextBlock\",\"text\":\"請假明細\",\"wrap\":true,\"size\":\"Large\",\"weight\":\"Bolder\"},{\"type\":\"Container\",\"items\":[{\"type\":\"ColumnSet\",\"columns\":[{\"type\":\"Column\",\"width\":3,\"items\":[{\"type\":\"TextBlock\",\"text\":\"申請人\",\"wrap\":true,\"weight\":\"Bolder\"}]},{\"type\":\"Column\",\"width\":7,\"items\":[{\"type\":\"TextBlock\",\"text\":\"${Data.Applicant}\",\"wrap\":true}]}]}]},{\"type\":\"ColumnSet\",\"columns\":[{\"type\":\"Column\",\"width\":3,\"items\":[{\"type\":\"TextBlock\",\"wrap\":true,\"text\":\"請假類別\",\"weight\":\"Bolder\"}]},{\"type\":\"Column\",\"width\":7,\"items\":[{\"type\":\"TextBlock\",\"text\":\"${Data.Type}\",\"wrap\":true}]}]},{\"type\":\"ColumnSet\",\"columns\":[{\"type\":\"Column\",\"width\":3,\"items\":[{\"type\":\"TextBlock\",\"wrap\":true,\"text\":\"請假日期\",\"weight\":\"Bolder\"}]},{\"type\":\"Column\",\"width\":7,\"items\":[{\"type\":\"TextBlock\",\"text\":\"${Data.StartDate}\",\"wrap\":true}]}]},{\"type\":\"ColumnSet\",\"columns\":[{\"type\":\"Column\",\"width\":3,\"items\":[{\"type\":\"TextBlock\",\"wrap\":true,\"text\":\"請假時數\",\"weight\":\"Bolder\"}]},{\"type\":\"Column\",\"width\":7,\"items\":[{\"type\":\"TextBlock\",\"text\":\"${Data.Hours}\",\"wrap\":true}]}]},{\"type\":\"ColumnSet\",\"columns\":[{\"type\":\"Column\",\"width\":3,\"items\":[{\"type\":\"TextBlock\",\"text\":\"請假事由\",\"wrap\":true,\"weight\":\"Bolder\"}]},{\"type\":\"Column\",\"width\":7,\"items\":[{\"type\":\"TextBlock\",\"text\":\"${Data.Subject}\",\"wrap\":true}]}]}],\"actions\":[{\"type\":\"Action.Submit\",\"title\":\"送出\",\"data\":{\"Action\":\"Submit\"}}]}",
     "Parameters": [
         {
             "Name": "Data",
             "Type": "use_expression",
             "Value": {
                 "Applicant": "{{$.Variables.LeaveTemplateData.Data.Applicant}}",
                 "StartDate": "{{$.Variables.LeaveTemplateData.Data.StartDate}}",
                 "Hours": "{{$.Variables.LeaveTemplateData.Data.Hours}}",
                 "Type": "{{$.Variables.LeaveTemplateData.Data.Type}}",
                 "Subject": "{{$.Variables.LeaveTemplateData.Data.Subject}}"
             }
         }
     ]
 }
```







