# Text Rule

> 訂定文字的規則



## ◆ Pre-Condition

無



## ◆ Schema

文字判斷規則，繼承自 [Base Rule](BaseRule.md) 

| 屬性           | 資料型態 | 必要屬性 | 描述                                   | 支援變數        | 版本 |
| -------------- | -------- | -------- | -------------------------------------- | --------------- | ---- |
| *Type*         | string   | Y        | 類型，值為 `text`                      | **X**           | 1.0  |
| **Condition**  | string   | Y        | [判斷條件 (Condition)](#-condition)    | **X**           | 1.0  |
| **Value**      | string   | N        | 期望的輸入                             | **O** **`[1]`** | 1.0  |
| **IsNegative** | boolean  | Y        | 文字判斷是否為反向判斷，預設為 `false` | **X**           | 1.0  |
| **IgnoreCase** | boolean  | Y        | 是否忽略大小寫，預設為 `false`         | **X**           | 1.0  |

* **`[1]`** **支援變數** 使用指定任意[自動變數、自訂變數](../Variables/Variable.md)



### ■ Condition

| 判斷條件                                                     | 描述             | 需要的屬性          | 版本 |
| ------------------------------------------------------------ | ---------------- | ------------------- | ---- |
| **startwith**<br />**startWith**<br />**start_with**         | 字串開頭為 Value | Value, *IsNegative* | 1.9  |
| **endwith**<br />**endWith**<br />**end_with**               | 字串結尾為 Value | Value, *IsNegative* | 1.9  |
| **contain**                                                  | 字串包含 Value   | Value, *IsNegative* | 1.0  |
| **exactly**<br />**equal**<br />**==**                       | 字串為 Value     | Value, *IsNegative* | 1.9  |
| **is_null**<br />**is_null_or_empty**<br />**isnull**<br />**isnullorempty**<br />**isNull**<br />**isNullOrEmpty** | 字串為空         | *IsNegative*        | 1.9  |



## ◆ Example



```json
{
    "Type": "text",
    "Condition": "contain",
    "Value": "app",
    "IsNegative": false,
    "IgnoreCase": true
}
```



