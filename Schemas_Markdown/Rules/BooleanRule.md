# Boolean Rule

> 訂定布林相關的規則



## ◆ Pre-Condition

1. **字串不得為空白**
2. **字串必須符合 Boolean 的格式 或是 符合使用者自訂的 Pattern**



## ◆ Schema

繼承自[Base Rule](BaseRule.md) 

| 屬性              | 資料型態 | 必要屬性 | 描述                                     | 支援變數 | 版本 |
| ----------------- | -------- | -------- | ---------------------------------------- | -------- | ---- |
| *Type*            | string   | Y        | 類型，值為 `boolean`                     | **X**    | 1.0  |
| **Condition**     | string   | Y        | [判斷條件 (Condition)](#-condition)      | **X**    | 1.0  |
| **IsNegative**    | boolean  | Y        | 整數判斷是否為反向判斷，預設值為 `false` | **X**    | 1.0  |
| **TruePatterns**  | string[] | N        | 符合 True 的文字，不分大小寫             | **X**    | 1.0  |
| **FalsePatterns** | string[] | N        | 符合 False 的文字，不分大小寫            | **X**    | 1.0  |

### ■ Condition

| 判斷條件                                       | 描述           | 需要的屬性   | 版本 |
| ---------------------------------------------- | -------------- | ------------ | ---- |
| **is_valid**<br />**isvalid**<br />**isValid** | 符合布林的格式 | *IsNegative* | 1.9  |
| **is_true**<br />**istrue**<br />**isTrue**    | 為 true        |              | 1.9  |
| **is_false**<br />**isfalse**<br />**isFalse** | 為 false       |              | 1.9  |



## ◆ Example



### ● 預設

```json
{
    "Type": "boolean",
    "Condition": "istrue",
    "IsNegative": false,
    "TruePatterns": [],
    "FalsePatterns": []
}
```

* **Input Message -----> Rule Result**
    * `"true"` -----> `pass`
    * `"false"` -----> `fail`
        * 不符合 Condition 設定的條件
    * `"hello"` -----> `fail`
        * 不符合 Default Condition



### ● 加入自訂 Pattern

```json
{
    "Type": "boolean",
    "Condition": "istrue",
    "IsNegative": false,
    "TruePatterns": [ 
        "yes",
        "ok",
        "sure"
    ],
    "FalsePatterns": [
        "no"
    ]
}
```

* **Input Message -----> Rule Result**
    * `"true"` -----> `pass`
    * `"false"` -----> `fail`
        * 不符合 Condition 設定的條件
    * `"Yes"` -----> `pass`
        * 符合 FalsePatterns
    * `"No"`-----> `fail`
        * 符合 FalsePatterns，但是不符合 Condition 設定的條件
    * `"ok"`-----> `pass`
        * 符合 FalsePatterns
    * `"Hi"`-----> `fail`
        * 不符合 Default Condition




