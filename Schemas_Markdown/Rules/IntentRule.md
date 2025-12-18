# Intent Rule

>  訂定意圖相關的規則，此 Rule 為 [QA類對話節點](../Nodes/QA/BaseQA.md)專用



## ◆ Pre-Condition

1. **必須要在 [QA類對話節點](../Nodes/QA/BaseQA.md) 中使用**



## ◆ Schema

判斷意圖，繼承自 [Base Rule](BaseRule.md)

| 屬性       | 資料型態 | 必要屬性 | 描述                   | 支援變數 | 版本 |
| ---------- | -------- | -------- | ---------------------- | -------- | ---- |
| *Type*     | string   | Y        | 類型，值為 `intent`    | **X**    | 1.0  |
| **Intent** | string   | Y        | 意圖的類型             | **X**    | 1.0  |
| **Score**  | double   | Y        | 信心指數，預設值:`0.8` | **X**    | 1.0  |

### ■ Condition

1. **符合指定 Inteent**
2. **信心度需大於 Score**



## ◆ Example



```json
{
    "Type": "intent",
    "Intent": "FAQ",
    "Score": 0.8
}
```




