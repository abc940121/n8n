# Composite Rule

> 複合規則



## ◆ Pre-Condition

1. **需要至少一個以上的 Rule**



## ◆ Schema

複合多組判斷規則，繼承自 [Base Rule](BaseRule.md) 

| 屬性           | 資料型態               | 必要屬性 | 描述                                                | 支援變數 | 版本 |
| -------------- | ---------------------- | -------- | --------------------------------------------------- | -------- | ---- |
| *Type*         | string                 | Y        | 類型，值為 `composite`                              | **X**    | 1.0  |
| **Condition**  | string                 | Y        | [判斷條件 (Condition)](#-condition)，預設值為 `and` | **X**    | 1.0  |
| **Rules**      | [Rules[]](BaseRule.md) | Y        | 子規則                                              | **X**    | 1.0  |
| **IsNegative** | boolean                | Y        | 反向判斷，預設值為 `false`                          | **X**    | 1.0  |

### ■ Condition

| 判斷條件 | 描述                      | 需要的屬性 | 版本 |
| :------- | ------------------------- | ---------- | ---- |
| **and**  | 所有的條件都須符合 (交集) | Rules      | 1.1  |
| **or**   | 只要有一個條件符合 (聯集) | Rules      | 1.1  |



## ◆ Example

* **單層，使用 `and`**

```javascript
(value > 0) && (value <= 100)
```



```json
{
    "Type": "composite",
    "Condition": "and",
    "Rules": [
        {
            "Type": "integer",
            "Condition": ">",
            "Value": 0,
            "Value2": 0,
            "IsNegative": false
        },
        {
            "Type": "integer",
            "Condition": "<=",
            "Value": 100,
            "Value2": 0,
            "IsNegative": false
        }
    ],
    "IsNegative": false
}
```

* **單層，使用 `or`**

```javascript
(value == "help") || (value == "quit") || (value == "menu")
```



```json
{
    "Type": "composite",
    "Condition": "or",
    "Rules": [
        {
            "Type": "text",
            "Condition": "exactly",
            "Value": "help",
            "IsNegative": false,
            "IgnoreCase": true
        },
        {
            "Type": "text",
            "Condition": "exactly",
            "Value": "quit",
            "IsNegative": false,
            "IgnoreCase": true
        },
        {
            "Type": "text",
            "Condition": "exactly",
            "Value": "menu",
            "IsNegative": false,
            "IgnoreCase": true
        }
    ],
    "IsNegative": false
}
```

* **多層 **
    * 使用多層 Rule 表示下面的邏輯判斷

```javascript
($.Value.Action == 'Send' && $.Value.Price !== 0) || ($.Value.Action == 'Cancel')
```



```json
{
    "Type": "composite",
    "Condition": "or",
    "Rules": [
        {
            "Type": "composite",
            "Condition": "and",
            "Rules": [
                {
                    "Type": "jsonpath",
                    "Rule": {
                        "Type": "text",
                        "Condition": "exactly",
                        "Value": "Send",
                        "IsNegative": false,
                        "IgnoreCase": true
                    },
                    "JsonPath": "$.Value.Action"
                },
                {
                    "Type": "jsonpath",
                    "Rule": {
                        "Type": "integer",
                        "Condition": "iszero",
                        "Value": 0,
                        "Value2": 0,
                        "IsNegative": true
                    },
                    "JsonPath": "$.Value.Price"
                }
            ],
            "IsNegative": false
        },
        {
            "Type": "composite",
            "Condition": "and",
            "Rules": [
                {
                    "Type": "jsonpath",
                    "Rule": {
                        "Type": "text",
                        "Condition": "exactly",
                        "Value": "Cancel",
                        "IsNegative": false,
                        "IgnoreCase": true
                    },
                    "JsonPath": "$.Value.Action"
                }
            ],
            "IsNegative": false
        }
    ],
    "IsNegative": false
}
```













