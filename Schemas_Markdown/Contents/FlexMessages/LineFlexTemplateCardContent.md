# LINE Flex Message Template Card Content

> 範本卡片



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
| *Type*         | string                                                       | Y        | 類型，值為 `line.flex.card.template`                         | **X**    | 1.22 |
| **AltText**    | string                                                       | Y        | 聊天室清單顯示的文字                                         | **O**    | 1.22 |
| **TemplateId** | string                                                       | Y        | [套版卡片](../../../TemplateCard/TemplatCard.md)的 Template ID  **`(不得重複)`** | **X**    | 1.22 |
| **Content**    | string                                                       | Y        | LINE Flex Message Json Content<br />**使用 [AdaptiveCardTemplate](https://www.nuget.org/packages/AdaptiveCards.Templating) JSON 轉換引擎處理資料綁定)** | **X**    | 1.22 |
| **Parameters** | Dictionary<string, [FlexMessageParameter](#-flex-message-parameter)> | N        | 訊息綁定所需要的參數，Key 為參數名稱  **(不得重複)**         | **X**    | 1.22 |
| *QuickReply*   | [LineButtonContent[]](LineActionContent.md)                  | N        | 快速回覆按鈕                                                 | **X**    | 1.1  |

> **AltText 必須要給值，值要給有效值字元、不能給空白字元**

* **AltText 在 LINE 上的顯示**

![](D:\GSS_Projects\FPS-BotBuilder\Projects\GssBotBuilder-devlelop\Docs\Schema\Contents\FlexMessages\Screenshots\AltText.jpg)

### ● Flex Message Parameter

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
    "Type": "line.flex.card.template",
    "TemplateId": "Template-000001",
    "AltText": "你有1筆請假資訊",
    "Content": "{\"type\":\"bubble\",\"body\":{\"type\":\"box\",\"layout\":\"vertical\",\"contents\":[{\"type\":\"box\",\"layout\":\"vertical\",\"contents\":[{\"type\":\"text\",\"text\":\"請假資訊\",\"align\":\"center\",\"weight\":\"bold\",\"size\":\"xl\"}]},{\"type\":\"box\",\"layout\":\"vertical\",\"contents\":[{\"type\":\"box\",\"layout\":\"horizontal\",\"contents\":[{\"type\":\"text\",\"text\":\"申請人\",\"flex\":3,\"weight\":\"bold\"},{\"type\":\"text\",\"text\":\"${Data.Applicant}\",\"flex\":7}]}]},{\"type\":\"box\",\"layout\":\"vertical\",\"contents\":[{\"type\":\"box\",\"layout\":\"horizontal\",\"contents\":[{\"type\":\"text\",\"text\":\"請假類別\",\"flex\":3,\"weight\":\"bold\"},{\"type\":\"text\",\"text\":\"${Data.Type}\",\"flex\":7}]}]},{\"type\":\"box\",\"layout\":\"vertical\",\"contents\":[{\"type\":\"box\",\"layout\":\"horizontal\",\"contents\":[{\"type\":\"text\",\"text\":\"請假日期\",\"flex\":3,\"weight\":\"bold\"},{\"type\":\"text\",\"text\":\"${Data.StartDate}\",\"flex\":7}]}]},{\"type\":\"box\",\"layout\":\"vertical\",\"contents\":[{\"type\":\"box\",\"layout\":\"horizontal\",\"contents\":[{\"type\":\"text\",\"text\":\"請假時數\",\"weight\":\"bold\",\"flex\":3},{\"type\":\"text\",\"text\":\"${Data.Hours}\",\"flex\":7}]}]},{\"type\":\"box\",\"layout\":\"vertical\",\"contents\":[{\"type\":\"box\",\"layout\":\"horizontal\",\"contents\":[{\"type\":\"text\",\"text\":\"請假事由\",\"flex\":3,\"weight\":\"bold\"},{\"type\":\"text\",\"text\":\"${Data.Subject}\",\"flex\":7}]}]}]},\"footer\":{\"type\":\"box\",\"layout\":\"vertical\",\"contents\":[{\"type\":\"button\",\"action\":{\"type\":\"message\",\"label\":\"送出\",\"text\":\"Submit\"},\"style\":\"primary\",\"height\":\"sm\"}]}}",
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



