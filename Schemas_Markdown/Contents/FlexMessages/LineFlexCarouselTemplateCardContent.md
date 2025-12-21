# LINE Flex Message Carousel Template Card Content

> 範本多卡片



## ◆ Channel Support

> [LINE Flex Message 文件](https://developers.line.biz/en/reference/messaging-api/#message-objects)

| Channel 類型        | 是否支援 | 備註 |
| ------------------- | -------- | ---- |
| Emulator            | **X**    |      |
| Web Chat            | **X**    |      |
| iota                | **X**    |      |
| LINE                | **O**    |      |
| Slack               | **X**    |      |
| Webex               | **X**    |      |
| Facebook Messenger  | **X**    |      |
| WhatsApp            | **X**    |      |
| Teams               | **X**    |      |
| Telegram            | **X**    |      |
| WeChat              | **X**    |      |
| DingTalk            | **X**    |      |
| Apple Business Chat | **X**    |      |



## ◆ Schema

繼承自 [MessageContent](../MessageContent.md)

| 屬性           | 資料型態                                                     | 必要屬性 | 描述                                                         | 支援變數 | 版本 |
| -------------- | ------------------------------------------------------------ | -------- | ------------------------------------------------------------ | -------- | ---- |
| *Type*         | string                                                       | Y        | 類型，值為 `line.flex.card.carousel_template`                | **X**    | 1.22 |
| **AltText**    | string                                                       | Y        | 聊天室清單顯示的文字 **`[2]`**                               | **O**    | 1.22 |
| **TemplateId** | string                                                       | Y        | [套版卡片](../../../TemplateCard/TemplatCard.md)的 Template ID  **`(不得重複)`** | **X**    | 1.22 |
| **Content**    | string                                                       | Y        | LINE Flex Message Json Content<br />**使用 [AdaptiveCardTemplate](https://www.nuget.org/packages/AdaptiveCards.Templating) JSON 轉換引擎處理資料綁定)** | **X**    | 1.22 |
| **Parameters** | Dictionary<string, [FlexMessageParameter](#-flex-message-parameter)> | N        | 訊息綁定所需要的參數，Key 為參數名稱  **(不得重複)**         | **X**    | 1.22 |
| **DataSource** | string                                                       | Y        | 指定資料來源 (變數) **`[1]`**                                | **O**    | 1.31 |
| *QuickReply*   | [LineButtonContent[]](LineActionContent.md)                  | N        | 快速回覆按鈕                                                 | **X**    | 1.1  |

* **`[1]`** DataSource 的設定
    * 變數值為一個陣列，會依據陣列長度產生對應的卡片數量，最多12個
    * 變數值為一個物件，會自動的轉換成物件陣列，但卡片只會有一張
    * 未指定值 (空字串)，會以 **[LINE 範本卡片 (LINE Flex Template Card)](LineFlexTemplateCardContent.md)** 格式建立一張卡片
    * 由於 LINE 訊息的限制，Flex Message Carousel 卡片數量最多12張
        * **如果與 [LINE 範本卡片 (LINE Flex Template Card)](LineFlexTemplateCardContent.md) 搭配的話，需要留意這個一項限制**
* **`[2]`** AltText 必須要給值，值要給有效值字元、不能給空白字元
    * **變數綁定的資料不是來自 Data Source**
    * **AltText 在 LINE 上的顯示**

![](Screenshots/AltText.jpg)

### ● Flex Message Parameter

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
    "Type": "line.flex.card.carousel_template",
    "TemplateId": "Template-000001",
    "AltText": "你有1筆請假資訊",
    "Content": "{\"type\":\"bubble\",\"body\":{\"type\":\"box\",\"layout\":\"vertical\",\"contents\":[{\"type\":\"box\",\"layout\":\"vertical\",\"contents\":[{\"type\":\"text\",\"text\":\"請假資訊\",\"align\":\"center\",\"weight\":\"bold\",\"size\":\"xl\"}]},{\"type\":\"box\",\"layout\":\"vertical\",\"contents\":[{\"type\":\"box\",\"layout\":\"horizontal\",\"contents\":[{\"type\":\"text\",\"text\":\"申請人\",\"flex\":3,\"weight\":\"bold\"},{\"type\":\"text\",\"text\":\"${Data.Applicant}\",\"flex\":7}]}]},{\"type\":\"box\",\"layout\":\"vertical\",\"contents\":[{\"type\":\"box\",\"layout\":\"horizontal\",\"contents\":[{\"type\":\"text\",\"text\":\"請假類別\",\"flex\":3,\"weight\":\"bold\"},{\"type\":\"text\",\"text\":\"${Data.Type}\",\"flex\":7}]}]},{\"type\":\"box\",\"layout\":\"vertical\",\"contents\":[{\"type\":\"box\",\"layout\":\"horizontal\",\"contents\":[{\"type\":\"text\",\"text\":\"請假日期\",\"flex\":3,\"weight\":\"bold\"},{\"type\":\"text\",\"text\":\"${Data.StartDate}\",\"flex\":7}]}]},{\"type\":\"box\",\"layout\":\"vertical\",\"contents\":[{\"type\":\"box\",\"layout\":\"horizontal\",\"contents\":[{\"type\":\"text\",\"text\":\"請假時數\",\"weight\":\"bold\",\"flex\":3},{\"type\":\"text\",\"text\":\"${Data.Hours}\",\"flex\":7}]}]},{\"type\":\"box\",\"layout\":\"vertical\",\"contents\":[{\"type\":\"box\",\"layout\":\"horizontal\",\"contents\":[{\"type\":\"text\",\"text\":\"請假事由\",\"flex\":3,\"weight\":\"bold\"},{\"type\":\"text\",\"text\":\"${Data.Subject}\",\"flex\":7}]}]}]},\"footer\":{\"type\":\"box\",\"layout\":\"vertical\",\"contents\":[{\"type\":\"button\",\"action\":{\"type\":\"message\",\"label\":\"送出\",\"text\":\"Submit\"},\"style\":\"primary\",\"height\":\"sm\"}]}}",
    "Parameters": [
        {
            "Name": "Data",
            "Type": "use_expression",
            "Value": {
                "Applicant": "{{$.Applicant}}",
                "StartDate": "{{$.StartDate}}",
                "Hours": "{{$.Hours}}",
                "Type": "{{$.Type}}",
                "Subject": "{{$.Subject}}"
            }
        }
    ],
    "DataSource": "$.Variables.LevelTemplateData"
}
```







