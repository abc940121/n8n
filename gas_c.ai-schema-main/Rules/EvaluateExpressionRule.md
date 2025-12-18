# Evaluate Expression Rule

> 訂定指定成員的值相關的規則，透過撰寫一小段 C# Script，去驗證目標物件是否符合規則



## ◆ Pre-Condition

無



## ◆ Schema

透過撰寫一小段 C# Script，去驗證目標物件是否符合規則

此驗證規則通常使用在卡片訊息 (Hero Card、Adaptive Card)、API Result、Bot State，繼承自 [Base Rule](BaseRule.md) 

| 屬性               | 資料型態 | 必要屬性 | 描述                                                         | 支援變數        | 版本 |
| ------------------ | -------- | -------- | ------------------------------------------------------------ | --------------- | ---- |
| *Type*             | string   | Y        | 類型，值為 `evaluate_expression`                             | **X**           | 1.0  |
| **ExpressionType** | string   | Y        | 使用的公式類型，預設值：`csharp`                             | **X**           | 1.12 |
| **Expression**     | string   | Y        | 自訂要驗證的公式，透過寫入簡單的 C# 程式碼來驗證，回傳值的資料型態必須為 `bool` | **O ****`[1]`** | 1.0  |

* **`[1]`** **支援變數** 使用指定任意[自動變數、自訂變數](../Variables/Variable.md)

### ■ Expression Type

| 公式類型     | 描述                       |
| ------------ | -------------------------- |
| `csharp`     | Expression 使用 C#，預設值 |
| `javascript` | Expression 使用 JavaScript |



### ■ 注意事項

* **使用前請先看過 [Expression 文件](../Expression.md)**
* **返回值必須為 `bool`**，僅支援 C#
* 目前使用 [Codingseb Expression Evaluator](https://github.com/codingseb/ExpressionEvaluator) 做為 Expression Evaluator 
    * 某些語法可能不支援，[詳細支援表](https://github.com/codingseb/ExpressionEvaluator/wiki/Operators-and-Keywords#standard-operators)，不支援表中的 [Scripts keywords](https://github.com/codingseb/ExpressionEvaluator/wiki/Operators-and-Keywords#scripts-keywords) 列出的項目
    * [Live Demo](https://dotnetfiddle.net/Packages/41132/CodingSeb_ExpressionEvaluator)
* 可以搭配使用 JSON Path 取出變數值，並執行運算，詳細請參考 [Inline Expression](../Variables/InlineExpression)
    * **可以不需要使用 [Inline Expression](../Variables/InlineExpression) 表示方式，即 `{{=> Expression ;}}`**
        * 不用加上 `{{->` 和 `;}}`
    * 使用 JSON Path 取出變數值時，則必須以 `{{JSON Path}}` 的方式表達
* 目前提供的 C# Namespace

```
// 內建
System
System.Math
System.Linq
System.Text
System.Text.RegularExpressions
System.ComponentModel
System.Collections
System.Collections.Generic
System.Collections.Specialized
System.Globalization
System.Security.Cryptography

// 常見套件
Newtonsoft.Json
Newtonsoft.Json.Linq

// 客製函式
GSS.BotBuilder.BotMessageContent.Binders.ExpressionBinders.Evaluators.Functions
```



## ◆ Example

* **判斷輸入的文字訊息 (C#)**

```json
{
    "Type": "evaluate_expression",
    "ExpressionType": "csharp",
    "Expression": "Regex.IsMatch(\"{{$.Text}}\", \"^(yes|no)$\", RegexOptions.IgnoreCase)"
}
```



* **判斷輸入的文字訊息 (JavaScript)**

```json
{
    "Type": "evaluate_expression",
    "ExpressionType": "javascript",
    "Expression": "/^(yes|no)$/i.test('{{$.Text}}')"
}
```



* **判斷輸入的的卡片訊息 (C#)**

```json
{
    "Type": "evaluate_expression",
    "ExpressionType": "csharp",
    "Expression": "\"{{$.Value.Action}}\" == \"Send\" && (DateTime.Parse(\"{{$.Value.StartDate}} {{$.Value.StartTime}}\") < DateTime.Parse(\"{{$.Value.EndDate}} {{$.Value.EndTime}}\"))"
}
```



* **判斷輸入的的卡片訊息 (JavaScript)**

```json
{
    "Type": "evaluate_expression",
    "ExpressionType": "javascript",
    "Expression": "'{{$.Value.Action}}' == 'Send' && (Date.parse('{{$.Value.StartDate}} {{$.Value.StartTime}}') < Date.parse('{{$.Value.EndDate}} {{$.Value.EndTime}}'))"
}
```



