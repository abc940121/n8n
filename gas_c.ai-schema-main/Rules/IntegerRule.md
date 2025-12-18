# Integer Rule

> 訂定整數相關的規則



## ◆ Pre-Condition

1. **字串不得為空白**
2. **字串必須符合整數的格式**



## ◆ Schema

整數判斷規則，這個規則有基本的判斷，輸入的值必須要為整數。繼承自 [Base Rule](BaseRule.md) 

| 屬性           | 資料型態 | 必要屬性 | 描述                                      | 支援變數 | 版本 |
| -------------- | -------- | -------- | ----------------------------------------- | -------- | ---- |
| *Type*         | string   | Y        | 類型，值為 `integer`                      | **X**    | 1.0  |
| **Condition**  | string   | Y        | [判斷條件 (Condition)](#-condition)       | **X**    | 1.0  |
| **Value**      | long     | N        | 期望的輸入                                | **O**    | 1.0  |
| **Value2**     | long     | N        | 期望的輸入，僅 Condition為 between 時使用 | **O**    | 1.0  |
| **IsNegative** | boolean  | Y        | 整數判斷是否為反向判斷，預設值為 `false`  | **X**    | 1.0  |

* **`[1]`** **支援變數** 使用指定任意[自動變數、自訂變數](../Variables/Variable.md)

### ■ Condition

| 判斷條件                                    | 描述                             | 需要的屬性                  | 版本 |
| ------------------------------------------- | -------------------------------- | --------------------------- | ---- |
| **IsInteger**                               | 是否為整數                       | *IsNegative*                | 1.12 |
| **is_zero**<br />**iszero**<br />**isZero** | 數字為 0                         | *IsNegative*                | 1.9  |
| **==**                                      | 數字等於 Value                   | Value                       | 1.0  |
| **!=**                                      | 數字不等於 Value                 | Value                       | 1.0  |
| **>**                                       | 數字大於 Value                   | Value, *IsNegative*         | 1.0  |
| **>=**                                      | 數字大於或等於 Value             | Value, *IsNegative*         | 1.0  |
| **<**                                       | 數字小於 Value                   | Value, *IsNegative*         | 1.0  |
| **<=**                                      | 數字小於或等於 Value             | Value, *IsNegative*         | 1.0  |
| **max**                                     | 數字不得高於 Value               | Value                       | 1.0  |
| **min**                                     | 數字不得低於 Value               | Value                       | 1.0  |
| **between**                                 | 數字介於 Value與 Value2 區間範圍 | Value, Value2, *IsNegative* | 1.0  |



## ◆ Example

* **判斷數字相等**

```json
{
    "Type": "integer",
    "Condition": "==",
    "Value": 655,
    "Value2": 0,
    "IsNegative": false
}
```

> 註：上面Example，value2 未使用



* **判斷數字區間**

```json
{
    "Type": "integer",
    "Condition": "between",
    "Value": 5,
    "Value2": 10,
    "IsNegative": false
}
```

