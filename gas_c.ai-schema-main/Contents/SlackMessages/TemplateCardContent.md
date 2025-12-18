# Slack Template Card Content

> 範本卡片



## ◆ Channel Support

> [Slack Block Kit 文件](https://api.slack.com/reference/block-kit/blocks)

| Channel 類型        | 是否支援 | 備註 |
| ------------------- | -------- | ---- |
| Emulator            | **X**    |      |
| Web Chat            | **X**    |      |
| iota                | **X**    |      |
| LINE                | **X**    |      |
| Teams               | **X**    |      |
| Slack               | **O**    |      |
| Webex               | **X**    |      |
| Facebook Messenger  | **X**    |      |
| Telegram            | **X**    |      |
| M+                  | **X**    |      |
| WeChat (微信個人號) | **X**    |      |
| WeCom (企業微信)    | **X**    |      |
| DingTalk            | **X**    |      |
| Apple Business Chat | **X**    |      |



## ◆ Schema

繼承 [MessageContent](MessageContent.md)

| 屬性           | 資料型態                                                     | 必要屬性 | 描述                                                         | 支援變數 | 版本 |
| -------------- | ------------------------------------------------------------ | -------- | ------------------------------------------------------------ | -------- | ---- |
| *Type*         | string                                                       | Y        | 類型，值為 `slack.blocks.template`                           | **X**    | 1.0  |
| **TemplateId** | string                                                       | Y        | [套版卡片](../../../TemplateCard/TemplatCard.md)的 Template ID  **`(不得重複)`** | **X**    | 1.2? |
| **Content**    | string                                                       | Y        | Slack Block Kit Json Content                                 | **O**    | 1.2? |
| **Parameters** | Dictionary<string, [SlackBlockCardParameter](#-slack-block-card-parameter)> | N        | 快速回覆按鈕                                                 | **X**    | 1.2? |

### ● Slack Block Card Parameter

| 屬性      | 資料型態 | 必要屬性 | 描述                                                         | 支援變數 | 版本 |
| --------- | -------- | -------- | ------------------------------------------------------------ | -------- | ---- |
| **Type**  | string   | Y        | 參數的類型                                                   | **X**    | 1.2? |
| **Value** | object   | Y        | 參數的值                                                     | `[1]`    | 1.2? |
| *Options* | object   | N        | 僅提供 UI 顯示參數輸入，詳細請參照 [套版卡片 Template Option](../../../TemplateCard/TemplatCard.md#-template-option) | **X**    | 1.2? |

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