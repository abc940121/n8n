# Regular Expression Rule

> 訂定文字的規則，文字判斷規則



## ◆ Pre-Condition

1. **字串不得為空白**



## ◆ Schema

繼承自 [Base Rule](BaseRule.md) 

| 屬性           | 資料型態 | 必要屬性 | 描述                                     | 支援變數 | 版本 |
| -------------- | -------- | -------- | ---------------------------------------- | -------- | ---- |
| *Type*         | string   | Y        | 類型，值為 `regex`                       | **X**    | 1.0  |
| **Pattern**    | string   | N        | 期望的輸入，Regex Pattern                | **X**    | 1.0  |
| **IsNegative** | boolean  | Y        | 文字判斷是否為反向判斷，預設值為 `false` | **X**    | 1.0  |
| **IgnoreCase** | boolean  | Y        | 是否忽略大小寫，預設值為 `false`         | **X**    | 1.0  |

> 需滿足 Regular Expression Pattern



## ◆ Example



```json
{
    "Type": "regex",
    "Pattern": "^(help)$",
    "IsNegative": false,
    "IgnoreCase": false
}
```

