# Button Content

> 按鈕設定



* **使用 LINE Channel 請查看 [Line Action Content](../FlexMessages/LineActionContent.md)**



## ◆ Schema

| 屬性    | 資料型態                           | 必要屬性 | 描述                | 支援變數    | 版本 |
| ------- | ---------------------------------- | -------- | ------------------- | ----------- | ---- |
| Type    | string                             | Y        | 類型，值為 `imBack` | **X**       | 1.0  |
| Title   | string                             | Y        | 按鈕標題            | **O**       | 1.0  |
| IconUrl | string                             | N        | 按鈕圖示 URL        | **O**       |      |
| Value   | string \| int \| double \| boolean | N        | 按鈕值              | **O **`[1]` | 1.0  |
| Options | object                             | N        | 按鈕選項  `[2]`     | **O**       | 1.23 |

* `[1]` **如果資料型態不是上述的 4個，則不會啟用將變數的值動態帶入**
* `[2]` 不同的 Channel 有不同的內容格式
    * **LINE** ─ **詳細查看 [Line Action Content](../FlexMessages/LineActionContent.md)**



### ● Button Type

同 Bot Framework 的 Action Type，請 [參考這裡](<https://docs.microsoft.com/en-us/azure/bot-service/dotnet/bot-builder-dotnet-add-rich-card-attachments?view=azure-bot-service-3.0#process-events-within-rich-cards>)

| 按鈕類型   | 描述                    | 版本 |
| ---------- | ----------------------- | ---- |
| `imBack`   | 回覆訊息 (顯示回覆內容) | 1.0  |
| `postBack` | 回覆訊息 (隱藏回覆內容) | 1.0  |
| `openUrl`  | 開啟連結                | 1.0  |

* **LINE 專用的 Button Type** ─ **詳細查看 [Line Action Content](../FlexMessages/LineActionContent.md)**



## ◆ Example



```json
{
    "Type": "imBack",
    "Title": "Button 01",
    "Value": "1"
}
```

