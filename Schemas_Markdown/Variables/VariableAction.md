# Custom Variable (自訂參數)

* **自訂變數有以下的操作處理**
  * [Get Value](#-get-value) ─ 取得自訂變數的值
  * [Set Value](#-get-value) ─ 設定自訂變數的值
  * [Remove Variable](#-remove-variable) ─ 移除自訂變數
  * [Remove All Variable](#-remove-all-variable) ─ 移除所有自訂變數

---



## ◆ Get Value

### (1) 透過 Jsonpath 取出變數的值

使用 Jsonpath 取出變數值，請JsonPath的用法請[參考這裡](https://goessner.net/articles/JsonPath/index.html#e2)

* 格式為 `{{$.JsonPath}}` 
    * 變數的值皆會被轉換成字串，使用時需要留意

##### Example

* **變數為一個字串、數字**
    * 可以將`{{$.變數}}`嵌入字串指定位置

```javascript
"{{$.Variable.MyName}}"

"我的名字是 {{$.Variable.MyName}}."
```

* **變數為一個物件 (Object)**
    * 可以將`{{$.變數}}`嵌入字串指定位置
    * 透過 JsonPath 可以取出 Object 的子屬性

```javascript
"{{$.Variable.MyObject.MyId}}"

"我的識別代碼是 {{$.Variable.MyObject.MyId}}."
```

* **變數為一個陣列 (Array)**
    * 可以將`{{$.變數}}`嵌入字串指定位置
    * 透過 JsonPath 可以取出 Array 的第幾個項目

```javascript
"{{$.Variable.MyArray[0]}}"

"第一筆資料是 {{$.Variable.MyArray[0]}}."
```



### (2) 透過 Pre-build Function 取出變數的值

* 詳細請參考 [Inline Expression](InlineExpression.md)



---

## ◆ Set Value

設定變數值

### ■ Schema

| 屬性                                   | 資料型態 | 描述                              | 支援變數 | 版本 |
| -------------------------------------- | -------- | --------------------------------- | -------- | ---- |
| Type                                   | string   | 類型，值為 `variable.set`         | **X**    | 1.0  |
| [TriggerType](#-trigger-type)          | string   | 執行時間點，預設值為 `after_node` | **X**    | 1.0  |
| Variable                               | string   | 變數名稱                          | **X**    | 1.0  |
| [VariableType](#-variable-type)        | string   | 變數存取類型                      | **X**    | 1.2  |
| AssignValue                            | object   | 指派值                            | **O**    | 1.0  |
| [AssignValueType](#-assign-value-type) | string   | 指派類型                          | **X**    | 1.0  |



#### ● Trigger Type

> 變數處理時間點

| 處理時間點     | 描述                                                   |
| -------------- | ------------------------------------------------------ |
| `before_node`  | Node 開始前處理變數的操作                              |
| `retry_prompt` | Prompt Node 觸發 Retry 時處理變數的操作 **`<計畫中>`** |
| `after_node`   | Node 結束後處理變數的操作                              |



#### ● Variable Type

> 變數存取類型

| 類型     | 描述                                                |
| -------- | --------------------------------------------------- |
| `global` | 全域變數 **(預設值)**                               |
| `flow`   | 流程變數，變數存取範圍僅在同一個流程                |
| `node`   | 節點變數，變數存取範圍僅在同一個節點 **`<計畫中>`** |



#### ● Assign Value Type

> 指派資料的型態

| 指派方式/類型                  | 描述                                        |
| ------------------------------ | ------------------------------------------- |
| string                         | 文字                                        |
| string.json                    | JSON文字                                    |
| string.plain                   | 純文字 **`(不處理任何資料綁定)`**           |
| number                         | 數字                                        |
| boolean                        | 布林值                                      |
| object                         | 物件                                        |
| array                          | 陣列                                        |
| variable                       | 指派其他變數的值 **`(不處理任何資料綁定)`** |
| evaluate_expression            | 公式表達式 (C#)                             |
| evaluate_csharp_expression     | 公式表達式 (C#)                             |
| evaluate_javascript_expression | 公式表達式 (JavaScript)                     |



---

### ■ Example

##### (1) 設定固定的值

* **文字**

```json
{
    "Type": "variable.set",
    "TriggerType": "after_node",
    "Variable": "PhoneNumber",
    "VariableType": "global",
    "AssignValue": "0800-092-000",
    "AssignValueType": "string"
}
```

* **純文字**
    * 與 **文字** 和 **Json字串** 的差異就在於指派值不會處理任何的變數綁定

```json
{
    "Type": "variable.set",
    "TriggerType": "after_node",
    "Variable": "PhoneNumber",
    "VariableType": "global",
    "AssignValue": "0800-092-000",
    "AssignValueType": "string.plain"
}
```

* **數字**

```json
{
    "Type": "variable.set",
    "TriggerType": "before_node",
    "Variable": "Radius",
    "VariableType": "global",
    "AssignValue": "5",
    "AssignValueType": "number"
}
```

* **布林值**

```json
{
    "Type": "variable.set",
    "TriggerType": "before_node",
    "Variable": "IsEnable",
    "VariableType": "global",
    "AssignValue": "false",
    "AssignValueType": "number"
}
```

* **物件**

```json
{
    "Type": "variable.set",
    "TriggerType": "after_node",
    "Variable": "ApplyLeaveForm",
    "VariableType": "global",
    "AssignValue": {
        "LeaveDate": "2019-01-01",
        "LeaveHours": 8,
        "LeaveType": "特休假",
        "LeaveSubject": "特休"
    },
    "AssignValueType": "object"
}
```

* **陣列**

```json
{
    "Type": "variable.set",
    "TriggerType": "after_node",
    "Variable": "LevaeType",
    "VariableType": "global",
    "AssignValue": [
        "特休假",
        "病假",
        "事假",
        "公假"
    ],
    "AssignValueType": "array"
}
```

* **Json字串**

```json
{
    "Type": "variable.set",
    "TriggerType": "after_node",
    "Variable": "PhoneNumberMessage",
    "VariableType": "global",
    "AssignValue": "{\"Id\": \"Ace\", \"Name\": \"艾斯\", \"Phone\": \"{{$.Variables.PhoneNumber}}\"}",
    "AssignValueType": "string.json"
}
```



##### (2) 指派另一個變數的值

* **直接指派**

```json
{
    "Type": "variable.set",
    "TriggerType": "after_node",
    "Variable": "UserText",
    "VariableType": "global",
    "AssignValue": "$.Message.Text",
    "AssignValueType": "variable"
}
```

* **將變數的值帶入到字串中**

```json
{
    "Type": "variable.set",
    "TriggerType": "after_node",
    "Variable": "PhoneNumberMessage",
    "VariableType": "global",
    "AssignValue": "Your Phone: {{$.Variable.PhoneNumber}}",
    "AssignValueType": "string"
}
```



##### (4) 設定公式表達式 (C#)

* 透過寫入簡單的 C# 程式碼指派自訂變數的值
  
    * 詳細請參考 [Inline Expression](InlineExpression.md)
* **適用的 Expression**
    * **C#**
        * **JSONPath**
        * **Adaptive Expression** (不建議混用)
    
    * **AssignValueType**
        * `evaluate_expression`
        * `evaluate_csharp_expression`
    
* **數學運算**

```json
{
    "Type": "variable.set",
    "TriggerType": "after_node",
    "Variable": "CircularArea",
    "VariableType": "global",
    "AssignValue": "Math.Pow(3, 2) * Math.PI",
    "AssignValueType": "evaluate_expression"
}
```

* **字串串接**

```json
{
    "Type": "variable.set",
    "TriggerType": "after_node",
    "Variable": "Greeting",
    "VariableType": "global",
    "AssignValue": "\"Hello\" + \" \" + \"world!\"",
    "AssignValueType": "evaluate_expression"
}
```

* **日期時間**

```json
{
    "Type": "variable.set",
    "TriggerType": "after_node",
    "Variable": "Today",
    "VariableType": "global",
    "AssignValue": "DateTime.Now.ToString(\"yyyy-MM-dd\")",
    "AssignValueType": "evaluate_expression"
}
```

* **日期時間計算** 

```json
{
    "Type": "variable.set",
    "TriggerType": "after_node",
    "Variable": "Period",
    "VariableType": "global",
    "AssignValue": "(DateTime.Now - DateTime.Today).TotalHours",
    "AssignValueType": "evaluate_expression"
}
```

* **建立物件**

```json
{
    "Type": "variable.set",
    "TriggerType": "after_node",
    "Variable": "LeaveForm",
    "VariableType": "global",
    "AssignValue": "Json.Create(new { LeaveDate = DateTime.Now.ToString(\"yyyy-MM-dd\"), LeaveHours = 8, LeaveType = \"特休假\", LeaveSubject = \"特休\"  })",
    "AssignValueType": "evaluate_expression"
}
```

* **數學運算式中加入自訂變數**

```json
{
    "Type": "variable.set",
    "TriggerType": "before_node",
    "Variable": "Pi",
    "VariableType": "global",
    "AssignValue": "Math.PI",
    "AssignValueType": "evaluate_expression"
},
{
    "Type": "variable.set",
    "TriggerType": "before_node",
    "Variable": "Radius",
    "VariableType": "global",
    "AssignValue": "5",
    "AssignValueType": "number "
},
{
    "Type": "variable.set",
    "TriggerType": "before_node",
    "Variable": "CircularArea",
    "VariableType": "global",
    "AssignValue": "Math.Pow({{$.Variables.Radius}}, 2) * {{$.Variables.Pi}}",
    "AssignValueType": "evaluate_expression"
}
```





##### (5) 設定公式表達式 (JavaScript)

* 透過寫入簡單的 JavaScript 程式碼指派自訂變數的值
    * 詳細請參考 [Inline Expression](InlineExpression.md)
    * **適用的 Expression**
        * **JavaScript**
        * **JSONPath**
        * **Adaptive Expression** (不建議混用)
    * **AssignValueType**
        * `evaluate_javascript_expression`

* **數學運算**

```json
{
    "Type": "variable.set",
    "TriggerType": "after_node",
    "Variable": "CircularArea",
    "VariableType": "global",
    "AssignValue": "Math.pow(3, 2) * Math.PI",
    "AssignValueType": "evaluate_javascript_expression"
}
```

* **字串串接**

```json
{
    "Type": "variable.set",
    "TriggerType": "after_node",
    "Variable": "Greeting",
    "VariableType": "global",
    "AssignValue": "'Hello' + ' ' + 'world!'",
    "AssignValueType": "evaluate_javascript_expression"
}
```

* **日期時間**

```json
{
    "Type": "variable.set",
    "TriggerType": "after_node",
    "Variable": "Today",
    "VariableType": "global",
    "AssignValue": "new Date()).toISOString()",
    "AssignValueType": "evaluate_javascript_expression"
}
```

* **建立物件**

```json
{
    "Type": "variable.set",
    "TriggerType": "after_node",
    "Variable": "LeaveForm",
    "VariableType": "global",
    "AssignValue": "{ LeaveDate: (new Date()).toISOString(), LeaveHours: 8, LeaveType: '特休假', LeaveSubject: '特休' }",
    "AssignValueType": "evaluate_javascript_expression"
}
```

* **數學運算式中加入自訂變數**

```json
{
    "Type": "variable.set",
    "TriggerType": "before_node",
    "Variable": "Pi",
    "VariableType": "global",
    "AssignValue": "Math.PI",
    "AssignValueType": "evaluate_javascript_expression"
},
{
    "Type": "variable.set",
    "TriggerType": "before_node",
    "Variable": "Radius",
    "VariableType": "global",
    "AssignValue": "5",
    "AssignValueType": "number "
},
{
    "Type": "variable.set",
    "TriggerType": "before_node",
    "Variable": "CircularArea",
    "VariableType": "global",
    "AssignValue": "Math.pow({{$.Variables.Radius}}, 2) * {{$.Variables.Pi}}",
    "AssignValueType": "evaluate_javascript_expression"
}
```



---



## ◆ Remove Variable

> 移除變數，只限自訂變數，自動變數無法移除

### ■ Schema

| 屬性                            | 資料型態 | 描述                              | 支援變數 | 版本 |
| ------------------------------- | -------- | --------------------------------- | -------- | ---- |
| Type                            | string   | 類型，值為 `variable.remove`      | **X**    | 1.0  |
| [TriggerType](#-trigger-type)   | string   | 執行時間點，預設值為 `after_node` | **X**    | 1.0  |
| Variable                        | string   | 變數名稱                          | **X**    | 1.0  |
| [VariableType](#-variable-type) | string   | 變數存取類型                      | **X**    | 1.2  |



---

### ■ Example

```json
{
    "Type": "variable.remove",
    "TriggerType": "after_node",
    "Variable": "PhoneNumber",
    "VariableType": "global"
}
```



---



## ◆ Remove All Variable

> 移除所有變數，只限自訂變數，自動變數無法移除

### ■ Schema

| 屬性                            | 資料型態 | 描述                              | 支援變數 | 版本 |
| ------------------------------- | -------- | --------------------------------- | -------- | ---- |
| Type                            | string   | 類型，值為 `variable.remove.all`  | **X**    | 1.0  |
| [TriggerType](#-trigger-type)   | string   | 執行時間點，預設值為 `after_node` | **X**    | 1.0  |
| [VariableType](#-variable-type) | string   | 變數存取類型                      | **X**    | 1.2  |



---

### ■ Example

```json
{
    "Type": "variable.remove.all",
    "TriggerType": "before_node",
    "VariableType": "global"
}
```

