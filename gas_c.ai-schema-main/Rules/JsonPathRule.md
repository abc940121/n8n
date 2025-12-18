# JsonPath Rule

> 訂定指定成員的值相關的規則



## ◆ Variable Rule 與 JsonPath Rule 的差異

> 兩種 Rule 雖然有差異，但是功能並不重疊

* **[Variable Rule](VariableRule.md)**
    * 可以指定任意[自動變數、自訂變數](../Variables/Variable.md)
    * 無法指定 Node 輸出的資料
        * 因為在執行 Rule 條件判斷時，尚未儲存Node 輸出的資料到 NodeOuptut (自動變數) 中
* **JsonPath Rule (第一層)**
    * 只能指定 Node 輸出的資料
    * **第二層之後的 Rule**
        * 使用指定任意[自動變數、自訂變數](../Variables/Variable.md)




## ◆ Pre-Condition

1. **指定目標不得為 Null**



## ◆ Schema

判斷物件，透過 [JsonPath](https://goessner.net/articles/JsonPath/ ) 取得指定目標，然後驗證指定目標的值。另外，指定目標是否為 NULL也會影響結果。

此驗證規則通常使用在卡片訊息 (Hero Card、Adaptive Card)、API Result、Bot State。繼承自 [Base Rule](BaseRule.md) 

| 屬性 | 資料型態                           | 必要屬性 | 描述                                                | 支援變數                                        | 版本                                         |
| -------- | ---------------------------------- | -------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| *Type*   | string                             | Y        | 類型，值為 `jsonpath`                                        | **X**                                   | 1.0                                     |
| **Rule** | [BaseRule](../Rules/BaseRule.md) | Y        | 指定要驗證的目標的驗證規則                               | **`[1]`**               | 1.0                            |
| **JsonPath** | string                             | Y        | JsonPath，指定要驗證的目標，詳細語法請參考[這裡](<https://github.com/json-path/JsonPath>) | **O `[2]`** | 1.0 |

* **`[1]`** 第二層之後的 Rule 的 **支援變數** 使用指定任意[自動變數、自訂變數](../Variables/Variable.md)
* **`[2]`** JsonPath **支援變數** 使用指定 Node 輸出的資料



## ◆ Example

* **卡片回傳訊息 (Activity.Text)**

```json
{
    "Type": "jsonpath",
    "Rule": {
        "Type": "text",
        "Condition": "exactly",
        "Value": "1",
        "IsNegative": false,
        "IgnoreCase": true
    },
    "JsonPath": "$.Text"
}
```



* **卡片回傳訊息 (Activity.Value)**

```json
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
}
```
