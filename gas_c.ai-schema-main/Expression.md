# Expression

為了滿足一些各種需要，在各個訊息、節點、變數指派、判斷規則上允許寫一小段程式碼



## ◆ 使用的地方

* **[Evaluate Expression Rule](Rules/EvaluateExpressionRule.md)**
    * 用於判斷規則
* **[Inline Expression](Variables/InlineExpression.md)**
    * 用於訊息、節點部分參數處理
* **[Assign Variable with Evaluate Expression](Variables/VariableAction)**
    * 用於指派自訂變數處理
* **Data Source**
    * 用於取出變數，並指派到特定節點或特定訊息的 Data Source 
* **[Custom Function Node](Nodes/Custom/CustomFunction.md)**
    * 用於資料整理



---

## ◆ 使用的 Expression 處理的作法

* **Expression** 處理的作法有3種，這3種皆會搭配使用
    * **JSON Path**
    * **C# Expression**
    * **JavaScript Expression**
        * 目前僅用在 Custom Function Node
    * **Adaptive Expression**



---

### ■ JSON Path

* 主要用於取出變數的值
* JSON Path的用法請[參考這裡](https://goessner.net/articles/JsonPath/index.html#e2)
    * [JSON Path Online Evaluator](https://jsonpath.com/)
* 使用的格式為 `$.JsonPath` 
    * JSON Path 的表示式
    * 變數的值皆會被轉換成字串，使用時需要留意



---

### ■ C# Expressions

* 主要用於取出邏輯判斷
* 目前使用 [Codingseb Expression Evaluator](https://github.com/codingseb/ExpressionEvaluator) 做為 Expression Evaluator 
    * 某些語法可能不支援，[詳細支援表](https://github.com/codingseb/ExpressionEvaluator/wiki/Operators-and-Keywords#standard-operators)
    * 除了 **Custom Function Node** 以外，皆不支援支援表中的 [Scripts keywords](https://github.com/codingseb/ExpressionEvaluator/wiki/Operators-and-Keywords#scripts-keywords) 列出的項目
    * [Live Demo](https://dotnetfiddle.net/Packages/41132/CodingSeb_ExpressionEvaluator)



#### ● 目前提供的 Namespace

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

// 自訂函式 (實驗中)
GSS.BotBuilder.BotMessageContent.Binders.ExpressionBinders.Evaluators.Functions
```





---

### ■ JavaScript Expression

* 主要用於 Custom Function Node 資料整理處理
* 目前使用  [NiL.JS](https://github.com/nilproject/NiL.JS) 做為 Expression Evaluator
    * 支援 ES 6 的語法



#### ● 提供的套件 `(計畫中)`

* **[Luxon](https://moment.github.io/luxon/)** 或 **[Moment.JS](https://momentjs.com/)**
    * 日期時間實用工具
* **[Lodash](https://lodash.com/)**
    * 字串、陣列、物件、Linq 實用工具
* **[axios](https://github.com/axios/axios)**
    * Http 相關的處理



---

### ■ Adaptive Expression

* 主要用於 Adaptive Card 訊息處理、取出變數的值
* 使用 Microsoft 提供的 Adaptive Expression 做為 Expression Evaluator 
    * Adaptive Card 內建已經支援 Adaptive Expression
    * [官方文件](https://docs.microsoft.com/zh-tw/azure/bot-service/bot-builder-concept-adaptive-expressions?view=azure-bot-service-4.0)
    * 官方也提供一些基本函式的運算，[Pre-Build Function](https://docs.microsoft.com/zh-tw/azure/bot-service/adaptive-expressions/adaptive-expressions-prebuilt-functions?view=azure-bot-service-4.0)
* 使用的格式為 `${Adaptive Expression}` 
    * 開頭 `${`、結尾 `}`
    * **<font color=red>由於這樣的格式容易會和 JSON Path、其他 Expression 在字串解析上發生衝突，因此建議不要混合使用</font>**







