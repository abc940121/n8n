# Node Action

> 定義對話節點切換的動作與條件



## ◆ Schema

| 屬性 | 資料型態                          | 必要屬性 | 描述                   | 支援變數 | 版本            |
| ---------- | --------------------------------- | -------- | ------------------------------- | ------------------------------- | ------------------------------- |
| Name | string | N | Action 的名稱或敘述 | **X** | 1.0 |
| Rules      | [BaseRule[]](../Rules/BaseRule.md) | Y      | Node 轉換規則                   | **X** | 1.0                |
| Type     | string                            | Y      | 多組規則的判斷，預設值為 `none` | **X** | 1.0 |
| Priority   | number                            | Y      | Action的優先順序，範圍 0 ~ 100  | **X** | 1.0 |
| NextNodeId | string                            | Y      | 符合條件時，轉換到下一個 Node   | **O** | 1.0 |

### ■ Type

| Type             | Description              | Version       |
| :--------------- | ------------------------ | ------------------------ |
| **and** | 所有的條件都須符合 | 1.0 |
| **or** | 只要有一個條件符合 | 1.0 |
| ~~**intersection**~~ | ~~所有的條件都須符合 (交集)~~ | 1.0 |
| ~~**union**~~    | ~~只要有一個條件符合 (聯集)~~ | 1.0 |
| **none** |   無需符合任何條件            |   1.0         |
| **otherwise** | 無需符合任何條件，在 Node Action 決策順序會放在最後 | 1.0 |

### ■ Priority

* **Action 處理的先後順序：**
  1. **Priority 分數**
     * 分數高優先處理
  2. **Node Action Array 的順序**
     * Priority 分數同分時，會優先處理Action Array 最前面的 Action



## ◆ Example



```json
{
    "Name": "",
    "Rules": [
        {
            "Type": "text",
            "Condition": "exactly",
            "Value": "help",
            "IsNegative": false,
            "IgnoreCase": true
        }
    ],
    "Type": "and",
    "NextNodeId": "node_0002"
}
```

