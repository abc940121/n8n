# DateTime Rule

> 訂定日期時間文字的規則



## ◆ Pre-Condition

1. **字串不得為空白**
2. **字串必須符合日期時間的格式 或是 符合使用者自訂的 Pattern**
3. **Rule 判斷有包含日期和時間**



## ◆ Schema

日期時間文字判斷規則，繼承自[Base Rule](BaseRule.md) 

| 屬性           | 資料型態 | 必要屬性 | 描述                                                         | 支援變數        | 版本 |
| -------------- | -------- | -------- | ------------------------------------------------------------ | --------------- | ---- |
| *Type*         | string   | Y        | 類型，值為 `datetime`                                        | **X**           | 1.0  |
| **Condition**  | string   | Y        | [判斷條件 (Condition)](#■-condition)，預設值：`is_valid`     | **X**           | 1.0  |
| **Patterns**   | string[] | N        | 自訂日期時間格式，未設定時會使用 C# 預設的 Parse Pattern，[詳細格式請參考這裡](https://docs.microsoft.com/zh-tw/dotnet/standard/base-types/custom-date-and-time-format-strings) | **X**           | 1.0  |
| **Value**      | string   | N        | [期望的日期時間](#-期望的日期時間格式)                       | **O** **`[1]`** | 1.0  |
| **Value2**     | string   | N        | [期望的日期時間](#-期望的日期時間格式)，僅 Condition 為 between 時使用 | **O** **`[1]`** | 1.0  |
| **Expression** | string   | N        | 時間是否滿足 [Cron Expression](http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html)，僅 Condition 為 cron 時使用 | **X**           | 1.0  |
| **IsNegative** | boolean  | Y        | 文字判斷是否為反向判斷，預設值為 `false`                     | **X**           | 1.0  |

* **`[1]`** **支援變數** 使用指定任意[自動變數、自訂變數](../Variables/Variable.md)

### ■ Condition

| 判斷條件                                                 | 描述                                            | 需要的屬性                  | 版本 |
| -------------------------------------------------------- | ----------------------------------------------- | --------------------------- | ---- |
| **is_valid**<br />**isvalid**<br />**isValid**           | 為有效的日期時間                                |                             | 1.9  |
| **is_today**<br />**istoday**<br />**isToday**           | 日期時間為今天                                  | *IsNegative*                | 1.9  |
| **is_same_date**<br />**issamedate**<br />**isSameDate** | 日期時間在 Value 那天，**比較的時間單位只到日** | Value, *IsNegative*         | 1.9  |
| **before**                                               | 日期時間在 Value 之前，**比較的時間單位為秒**   | Value, *IsNegative*         | 1.0  |
| **after**                                                | 日期時間在 Value 之後，**比較的時間單位為秒**   | Value, *IsNegative*         | 1.0  |
| **between**                                              | 日期時間介於 Value與 Value2 區間範圍            | Value, Value2, *IsNegative* | 1.0  |
| **cron**                                                 | 日期時間滿足 Expression (Cron Expression)       | Expression, *IsNegative*    | 1.0  |

### ■ 期望的日期時間格式

* **Value**、**Value2**
    * **now、today**
    * **指定日期時間**
        * 格式須符合 C# DateTime 的表示格式或是 自訂日期時間格式，[詳細格式請參考這裡](https://docs.microsoft.com/zh-tw/dotnet/standard/base-types/custom-date-and-time-format-strings)
        * 例如：`2019-01-01`、`2019-01-01 15:00`...
* **Expression**
    * 需符合 Cron Expression 格式，[詳細格式請參考這裡]( http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html )
    * Cron Expression 範例
        * **`* * * ? * MON-FRI`** ─ 日期時間為工作天
        * **`* * * 1 * ? *`** ─ 日期時間為每個月第一天

> 如果 Exception Value 不符合上述的格式要求，Rule 的判斷一律不通過



## ◆ Example

* **輸入的值是否為合法的日期時間 (使用C# 預設 Pattern)**

```json
{
    "Type": "datetime",
    "Condition": "is_valid",
    "Patterns": [],
    "Value": "",
    "Value2": "",
    "Expression": "",
    "IsNegative": false,
    "IgnoreCase": true
}
```



* **輸入的值是否為合法的日期時間 (使用自訂 Pattern)**

```json
{
    "Type": "datetime",
    "Condition": "is_valid",
    "Patterns": [
        "yyyy年MM月dd日",
        "yyyy-MM-dd"
    ],
    "Value": "",
    "Value2": "",
    "Expression": "",
    "IsNegative": false,
    "IgnoreCase": true
}
```



* **日期時間值是否符合 2019-12-31 之前**

```json
{
    "Type": "datetime",
    "Condition": "before",
    "Patterns": [
        "yyyy年MM月dd日",
        "yyyy-MM-dd"
    ],
    "Value": "2019-12-31",
    "Value2": "",
    "Expression": "",
    "IsNegative": false,
    "IgnoreCase": true
}
```

* **日期時間值是否符合介於 2019-01-01 與 2019-12-31 之間**

```json
{
    "Type": "datetime",
    "Condition": "before",
    "Patterns": [
        "yyyy年MM月dd日",
        "yyyy-MM-dd"
    ],
    "Value": "2019-01-01",
    "Value2": "2019-12-31",
    "Expression": "",
    "IsNegative": false,
    "IgnoreCase": true
}
```


* **日期時間值是否為上班日**

```json
{
    "Type": "datetime",
    "Condition": "cron",
    "Patterns": [
        "dd-MM-yyyy"
    ],
    "Value": "",
    "Value2": "",
    "Expression": "* * * ? * MON-FRI",
    "IsNegative": false,
    "IgnoreCase": true
}
```



