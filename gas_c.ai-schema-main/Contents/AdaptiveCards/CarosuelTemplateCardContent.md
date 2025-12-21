# Carousel Template Adaptive Card Content

> 範本多卡片



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
| Webex                   | **X**    | 1. Adaptive Card 支援的版本為 **1.3**<br />2. 按鈕數量最多5個 |
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
| *Type*               | string                                                       | Y        | 類型，值為 `adaptive.card.carousel_template`                 | **X**    | 1.31 |
| **TemplateId**       | string                                                       | Y        | [套版卡片](../../../TemplateCard/TemplatCard.md)的 Template ID  **`(不得重複)`** | **X**    | 1.31 |
| **Content**          | string                                                       | Y        | Adaptive Card Json 內容                                      | **X**    | 1.31 |
| **Parameters**       | Dictionary<string, [AdaptiveCardParameter](#-adaptive-card-parameter)> | N        | 卡片綁定所需要的參數，Key 為參數名稱  **(不得重複)**         | **X**    | 1.31 |
| **DataSource**       | string                                                       | Y        | 指定資料來源 (變數) **`[1]`**                                | **O**    | 1.31 |
| **Layout**           | string                                                       | N        | 卡片的排版，預設值: `carousel` **`[2]`**                     | **X**    | 1.31 |
| *QuickReply*         | [ButtonContent[]](Components/ButtonContent.md)               | N        | 快速回覆按鈕                                                 | **X**    | 1.31 |
| *ChannelDataPayload* | object                                                       | N        | Channel Data Payload，[使用限制](../Components/ChannelDataPayload.md) **`[3]`** | **O**    | 1.31 |

* **`[1]`** DataSource 的設定
    * 變數值為一個陣列，會依據陣列長度產生對應的卡片數量
    * 變數值為一個物件，會自動的轉換成物件陣列，但卡片只會有一張
    * 未指定值 (空字串)，會以 **[範本卡片 (Template Card)](TemplateCardContent.md)** 格式建立一張卡片
* **`[2]`** 卡片的排版
    * 卡片的排版
        * **carousel** ─ 左右並排
        * **list** ─ 上下排列
    * 如果與 [CarouselContent](../CarouselContent.md) 搭配使用時，只會套用最外層的設定值
    * 舊版 iota Channel 只支援 **list**
* **`[3]`** **變數綁定的資料不是來自 Data Source**

### ● Adaptive Card Parameter

| 屬性      | 資料型態 | 必要屬性 | 描述                                                         | 支援變數 | 版本 |
| --------- | -------- | -------- | ------------------------------------------------------------ | -------- | ---- |
| **Type**  | string   | Y        | 參數的類型                                                   | **X**    | 1.22 |
| **Value** | object   | Y        | 參數的值                                                     | `[1]`    | 1.22 |
| *Options* | object   | N        | 僅提供 UI 顯示參數輸入，詳細請參照 [套版卡片 Template Option](../../../TemplateCard/TemplatCard.md#-template-option) | **X**    | 1.22 |

* `[1]` 是否支援變數會以 **Type** 的值而定
    * **Type** 為 `use_expression` 時
        * 變數綁定來自指定的 Data Source
    * **Type** 為 `plain` 時
        * 不支援任何變數
    * **Type** 為 `variable` 時，使用 Data Source 指定屬性，不處理任何運算
        * 變數綁定來自指定的 Data Source
        * 如果設定多組變數時，只會使用第一個變數
        * 例如："`{{$.Prop1.PropA}} {{$.Prop2}}`"，只會取出變數 `$.Prop1.PropA` 的值

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
| `use_expression` | Argument Value 會處理任何資料綁定，變數綁定來自指定的 Data Source |
| `plain`          | Argument Value 不處理任何資料綁定 **`(不處理任何變數運算)`** |
| `variable`       | 指派指定變數，變數綁定來自指定的 Data Source，不處理任何資料綁定，只處理1個變數 **`(不處理任何變數運算)`** |



## ◆ Example

### ● Data Source 物件為一層

* **指定 Data Source 之變數**
    * `$.Variables.LevelTemplateData`

```json
[
    {
        "Applicant": "Jack Poker",
        "StartDate": "2023-11-11 08:30",
        "Hours": "8",
        "Type": "特休假",
        "Subject": "搭郵輪度假"
    },
    {
        "Applicant": "Queen Poker",
        "StartDate": "2023-12-12 08:30",
        "Hours": "8",
        "Type": "生理假",
        "Subject": "迎接大姨媽"
    },
    {
        "Applicant": "Joker Poker",
        "StartDate": "2023-04-01 08:30",
        "Hours": "8",
        "Type": "公假",
        "Subject": "舉辦愚人節活動"
    }
]
```

* **Content JSON**

```json
{
    "Type": "adaptive.card.carousel_template",
    "TemplateId": "Template-000001",
    "Layout": "carousel",
    "Content": "{\"type\":\"AdaptiveCard\",\"$schema\":\"http://adaptivecards.io/schemas/adaptive-card.json\",\"version\":\"1.2\",\"body\":[{\"type\":\"TextBlock\",\"text\":\"請假明細\",\"wrap\":true,\"size\":\"Large\",\"weight\":\"Bolder\"},{\"type\":\"Container\",\"items\":[{\"type\":\"ColumnSet\",\"columns\":[{\"type\":\"Column\",\"width\":3,\"items\":[{\"type\":\"TextBlock\",\"text\":\"申請人\",\"wrap\":true,\"weight\":\"Bolder\"}]},{\"type\":\"Column\",\"width\":7,\"items\":[{\"type\":\"TextBlock\",\"text\":\"${Applicant}\",\"wrap\":true}]}]}]},{\"type\":\"ColumnSet\",\"columns\":[{\"type\":\"Column\",\"width\":3,\"items\":[{\"type\":\"TextBlock\",\"wrap\":true,\"text\":\"請假類別\",\"weight\":\"Bolder\"}]},{\"type\":\"Column\",\"width\":7,\"items\":[{\"type\":\"TextBlock\",\"text\":\"${Type}\",\"wrap\":true}]}]},{\"type\":\"ColumnSet\",\"columns\":[{\"type\":\"Column\",\"width\":3,\"items\":[{\"type\":\"TextBlock\",\"wrap\":true,\"text\":\"請假日期\",\"weight\":\"Bolder\"}]},{\"type\":\"Column\",\"width\":7,\"items\":[{\"type\":\"TextBlock\",\"text\":\"${StartDate}\",\"wrap\":true}]}]},{\"type\":\"ColumnSet\",\"columns\":[{\"type\":\"Column\",\"width\":3,\"items\":[{\"type\":\"TextBlock\",\"wrap\":true,\"text\":\"請假時數\",\"weight\":\"Bolder\"}]},{\"type\":\"Column\",\"width\":7,\"items\":[{\"type\":\"TextBlock\",\"text\":\"${Hours}\",\"wrap\":true}]}]},{\"type\":\"ColumnSet\",\"columns\":[{\"type\":\"Column\",\"width\":3,\"items\":[{\"type\":\"TextBlock\",\"text\":\"請假事由\",\"wrap\":true,\"weight\":\"Bolder\"}]},{\"type\":\"Column\",\"width\":7,\"items\":[{\"type\":\"TextBlock\",\"text\":\"${Subject}\",\"wrap\":true}]}]}],\"actions\":[{\"type\":\"Action.Submit\",\"title\":\"送出\",\"data\":{\"Action\":\"Submit\"}}]}",
    "Parameters": [
        {
            "Name": "Applicant",
            "Type": "use_expression",
            "Value": "{{$.Applicant}}"
        },
        {
            "Name": "Type",
            "Type": "use_expression",
            "Value": "{{$.Type}}"
        },
        {
            "Name": "StartDate",
            "Type": "use_expression",
            "Value": "{{$.StartDate}}"
        },
        {
            "Name": "Hours",
            "Type": "use_expression",
            "Value": "{{$.Hours}}"
        },
        {
            "Name": "Subject",
            "Type": "use_expression",
            "Value": "{{$.Subject}}"
        }
    ],
    "DataSource": "$.Variables.LevelTemplateData"
}
```



---

## ● Data Source 物件為二層 (使用指定變數)

* **指定 Data Source 之變數**
    * `$.Variables.LevelTemplateData`

```json
[
    {
        "Applicant": "Jack Poker",
        "Data": {
			"StartDate": "2023-11-11 08:30",
	        "Hours": "8",
    	    "Type": "特休假",
        	"Subject": "搭郵輪度假"            
        }
    },
    {
        "Applicant": "Queen Poker",
        "Data": {
            "StartDate": "2023-12-12 08:30",
    	    "Hours": "8",
	        "Type": "生理假",
        	"Subject": "迎接大姨媽"
        }
    },
    {
        "Applicant": "Joker Poker",
        "Data": {
            "StartDate": "2023-04-01 08:30",
	        "Hours": "8",
    	    "Type": "公假",
        	"Subject": "舉辦愚人節活動"
        }
    }
]
```

* **Content JSON**

```json
{
    "Type": "adaptive.card.carousel_template",
    "TemplateId": "Template-000001",
    "Layout": "carousel",
    "Content": "{\"type\":\"AdaptiveCard\",\"$schema\":\"http://adaptivecards.io/schemas/adaptive-card.json\",\"version\":\"1.2\",\"body\":[{\"type\":\"TextBlock\",\"text\":\"請假明細\",\"wrap\":true,\"size\":\"Large\",\"weight\":\"Bolder\"},{\"type\":\"Container\",\"items\":[{\"type\":\"ColumnSet\",\"columns\":[{\"type\":\"Column\",\"width\":3,\"items\":[{\"type\":\"TextBlock\",\"text\":\"申請人\",\"wrap\":true,\"weight\":\"Bolder\"}]},{\"type\":\"Column\",\"width\":7,\"items\":[{\"type\":\"TextBlock\",\"text\":\"${Applicant}\",\"wrap\":true}]}]}]},{\"type\":\"ColumnSet\",\"columns\":[{\"type\":\"Column\",\"width\":3,\"items\":[{\"type\":\"TextBlock\",\"wrap\":true,\"text\":\"請假類別\",\"weight\":\"Bolder\"}]},{\"type\":\"Column\",\"width\":7,\"items\":[{\"type\":\"TextBlock\",\"text\":\"${Type}\",\"wrap\":true}]}]},{\"type\":\"ColumnSet\",\"columns\":[{\"type\":\"Column\",\"width\":3,\"items\":[{\"type\":\"TextBlock\",\"wrap\":true,\"text\":\"請假日期\",\"weight\":\"Bolder\"}]},{\"type\":\"Column\",\"width\":7,\"items\":[{\"type\":\"TextBlock\",\"text\":\"${StartDate}\",\"wrap\":true}]}]},{\"type\":\"ColumnSet\",\"columns\":[{\"type\":\"Column\",\"width\":3,\"items\":[{\"type\":\"TextBlock\",\"wrap\":true,\"text\":\"請假時數\",\"weight\":\"Bolder\"}]},{\"type\":\"Column\",\"width\":7,\"items\":[{\"type\":\"TextBlock\",\"text\":\"${Hours}\",\"wrap\":true}]}]},{\"type\":\"ColumnSet\",\"columns\":[{\"type\":\"Column\",\"width\":3,\"items\":[{\"type\":\"TextBlock\",\"text\":\"請假事由\",\"wrap\":true,\"weight\":\"Bolder\"}]},{\"type\":\"Column\",\"width\":7,\"items\":[{\"type\":\"TextBlock\",\"text\":\"${Subject}\",\"wrap\":true}]}]}],\"actions\":[{\"type\":\"Action.Submit\",\"title\":\"送出\",\"data\":{\"Action\":\"Submit\"}}]}",
    "Parameters": [
        {
            "Name": "Applicant",
            "Type": "use_expression",
            "Value": "{{$.Applicant}}"
        },
        {
            "Name": "Type",
            "Type": "use_expression",
            "Value": "{{$.Data.Type}}"
        },
        {
            "Name": "StartDate",
            "Type": "use_expression",
            "Value": "{{$.Data.StartDate}}"
        },
        {
            "Name": "Hours",
            "Type": "use_expression",
            "Value": "{{$.Data.Hours}}"
        },
        {
            "Name": "Subject",
            "Type": "use_expression",
            "Value": "{{$.Data.Subject}}"
        }
    ],
    "DataSource": "$.Variables.LevelTemplateData"
}
```



