# Adaptive Action Content



## ◆ Schema

| 屬性  | 資料型態 | 必要屬性 | 描述                                   | 支援變數 | 版本 |
| ----- | -------- | -------- | -------------------------------------- | -------- | ---- |
| Type  | string   | Y        | 類型                                   | **X**    | 1.1  |
| Title | string   | Y        | 按鈕標題                               | **O**    | 1.1  |
| Value | string   | N        | 按鈕值                                 | **O**    | 1.1  |
| Verb  | string   | N        | 按鈕動作，僅限 Type = `execute.action` | **O**    | 1.22 |
| Style | string   | N        | 按鈕樣式，預設值：`default`            | **O**    | 1.7  |

### ● Button Type

| 按鈕類型         | 描述                | 版本 |
| ---------------- | ------------------- | ---- |
| `submit.text`    | 回覆訊息 (文字)     | 1.1  |
| `submit.data`    | 回覆訊息 (JSON物件) | 1.1  |
| `open.url`       | 開啟連結            | 1.1  |
| `show.card`      | 顯示子卡片          | 1.1  |
| `execute.action` | 執行動作            | 1.22 |

### ● Button Style

| 按鈕類型      | 描述     | 版本 |
| ------------- | -------- | ---- |
| `default`     | 預設樣式 | 1.7  |
| `positive`    | 藍色按鈕 | 1.7  |
| `destructive` | 紅色按鈕 | 1.7  |

## ◆ Example

```json
{
    "Type": "submit.text",
    "Title": "Button 01",
    "Value": "1",
    "Style": "default"
}
```



---

# Adaptive Select Action Content



## ◆ Schema

| 屬性  | 資料型態 | 必要屬性 | 描述                                   | 支援變數 | 版本 |
| ----- | -------- | -------- | -------------------------------------- | -------- | ---- |
| Type  | string   | Y        | 類型，`這裡破例允許透過變數處理`       | **O**    | 1.1  |
| Verb  | string   | N        | 按鈕動作，僅限 Type = `execute.action` | **O**    | 1.22 |
| Value | string   | N        | 按鈕值                                 | **O**    | 1.1  |

### ● Button Type

| 按鈕類型         | 描述                | 版本 |
| ---------------- | ------------------- | ---- |
| `submit.text`    | 回覆訊息 (文字))    | 1.1  |
| `submit.data`    | 回覆訊息 (JSON物件) | 1.1  |
| `open.url`       | 開啟連結            | 1.1  |
| `execute.action` | 執行動作            | 1.22 |

## ◆ Example

```json
{
    "Type": "submit.text",
    "Value": "1"
}
```

