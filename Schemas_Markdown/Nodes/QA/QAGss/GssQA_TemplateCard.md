# GSS.QA 範本卡片設定

> 定義 GSS QA 答案卡片的樣式



## ◆ 架構

* **Name** ─ 名稱，值為：`GssQaCard`
* **Class** ─ 類別，值為：`GssQaCard`
* **Type** ─ 訊息內容類型，建議為：`AdaptiveCard`
* **MasterContent** ─ [主要答案卡片的內容](#-主要卡片內容)，建議以 Adaptive Card 的格式呈現
    * 可以透過 [Adaptive Card Designer]( https://adaptivecards.io/designer/ ) 設計完後，可以放到這裡
* **Components** ─ [答案卡片的相關元件 (控制項)](#-卡片內容控制項)，建議以 Adaptive Card Contianer 的格式

```json
{
    "Name": "GssQaCard",
    "Class": "GssQaCard",
    "Type": "AdaptiveCard",
    "MasterContent": {},
    "Components": []
}
```



## ◆ 主要卡片內容

設計答案卡片的排版，並預留可以動態塞入 **最佳答案** 和 **相關問題** 區塊

* **預留的區塊**
    * **TopAnswerLabel**
        * 最佳答案的的標題
    * **TopAnswerBlock**
        * 最佳答案預留的區塊
    * **OtherAnswersLabel**
        * 相關答案的標題
    * **OtherAnswersBlock**
        * 相關答案預留的區塊

```json
 {
     "type": "AdaptiveCard",
     "version": "1.0",
     "body": [
         {
             "type": "Container",
             "id": "TopAnswerLabel",
             "items": [
                 {
                     "type": "TextBlock",
                     "text": "我覺得最接近的答案AA",
                     "weight": "Bolder",
                     "size": "Medium"
                 }
             ]
         },
         {
             "type": "Container",
             "id": "TopAnswerBlock",
             "items": []
         },
         {
             "type": "Container",
             "id": "OtherAnswersLabel",
             "items": [
                 {
                     "type": "TextBlock",
                     "text": "推薦主題",
                     "weight": "Bolder",
                     "size": "Medium"
                 }
             ],
             "separator": true
         },
         {
             "type": "Container",
             "id": "OtherAnswersBlock",
             "items": []
         }
     ]
 }
```



##  ◆ 卡片內容控制項

### ■ 最佳答案 (TopAnswerBlock)

* **Id** ─ 控制項 ID
* **ContainerId** ─ 主要卡片內容預留區塊 (Adaptive Container) 的 ID
* **ContentCondition** ─ Content 選用條件
    * 這裡會依據 GSS QA 答案的類型 `{{$.Type}}`，判斷要從 **ContentCases** 中選用哪一種呈現內容 (Content) 顯示答案
    * 預設支援[變數](../../../Variables/VariableAction.md#-get-value)的替換
* **ContentCases** ─ 依據 `ContentCondition` 的值，選用哪一種呈現內容 (Content) 顯示答案
    * 內容以 Adaptive Container 為容器
    * 目前已知的答案樣式
        * **`text`** ─ 純文字
        * **`link`** ─ 連結
        * **`flow`** ─ 切換到其他流程
        * **`none`** ─ 找不到答案
* **DefaultCase** ─ 預設使用的 Content，預設值為 `none`

> 由於答案類型的不同，會有不同的 UI 呈現，因此需要特別為各種答案設計各自的 UI

```json
{
    "Id": "TopAnswer",
    "ContainerId": "TopAnswerBlock",
    "ContentCondition": "{{$.Type}}",
    "DefaultCase": "none",
    "ContentCases": {
        "text": {
            "type": "Container",
            "items": []
        },
        "link": {
            "type": "Container",
            "items": [],
            "selectAction": {}
        },
        "flow": {
            "type": "Container",
            "items": [],
            "selectAction": {}
        },
        "none": {
            "type": "Container",
            "items": []
        }
    }
}
```



### ■ 相關答案 (OtherAnswersBlock)


* **Id** ─ 控制項 ID
* **ContainerId** ─ 主要卡片內容預留區塊 (Adaptive Container) 的 ID
* **ContentCondition** ─ Content 選用條件
    * 這裡會依據 GSS QA 答案的類型 `{{$.Type}}`，判斷要從 **ContentCases** 中選用哪一種呈現內容 (Content) 顯示答案
    * 預設支援[變數](../../../Variables/VariableAction.md#-get-value)的替換
* **ContentCases** ─ 依據 `ContentCondition` 的值，選用哪一種呈現內容 (Content) 顯示答案
    * 內容以 Adaptive Container 為容器
    * 目前已知的答案樣式
        * **`text`** ─ 純文字
        * **`link`** ─ 連結
        * **`flow`** ─ 切換到其他流程
* **DefaultCase** ─ 預設使用的 Content，預設值為 `text`

> 由於答案類型的不同，會有不同的 UI 呈現，因此需要特別為各種答案設計各自的 UI

```json
{
    "Id": "OtherAnswer",
    "ContainerId": "OtherAnswersBlock",
    "ContentCondition": "{{$.Type}}",
    "DefaultCase": "text",
    "ContentCases": {
        "text": {
            "type": "Container",
            "items": [],
            "selectAction": {}
        },
        "link": {
            "type": "Container",
            "items": [],
            "selectAction": {}
        },
        "flow": {
            "type": "Container",
            "items": [],
            "selectAction": {},
        }
    }
}
```




## ◆ 預設範本

* [預設範本](../../../../../Source/BotFlowRunner/BotFlowRunner/TemplateMessages/GssQaCard.json)


