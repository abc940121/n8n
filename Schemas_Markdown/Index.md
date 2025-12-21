# Schema 文件目錄



## 1. Dialog Flow & Node

* [**Bot**](Bot.md)
    * [**Dialog Flows**](Flows/DialogFlow.md) ─ 對話流程
        * [**Dialog Node**](Nodes/BaseDialogNode.md) ─ 對話節點
    * [**Bot Event Hook**](Events/BaseEvent.md) ─ 對話訊息與事件訊息



## 2. Message Content

* [**Message**](Contents/MessageContent.md)



## 3. Rule

* [**Rules**](Rules/BaseRule.md)  ─ 規則條件
* Rule 相依的項目：
    * [**Node Action**](Actions/NodeAction.md) ─ 對話切換動作，Rule 在這裡當作對話切換的條件
    * [**Prompt Validator**](Nodes/Prompt/PromptValidator.md)  ─ [**Prompt Dialog**](Nodes/Prompt/BasePrompt.md) 的訊息驗證，Rule 在這裡當作 Prompt 的驗證規則



## 4. Variable

* [**Variable**](Variables/Variable.md) ─ 變數
* [**Variable Action**](Variables/VariableAction.md) ─ 變數操作
* **[Inline Expression](Variables/InlineExpression.md)** ─ 單行公式運算處理



## 5. App Settings

* **[AppSettings](../AppSetting.md)**  ─ Bot 應用程式設定



## 6. Plugins

* **[Custom Plugin](https://git.gss.com.tw/fpsbu/gssbotdialogflowengineplugins)**
    * **[GssCaiDialog](https://git.gss.com.tw/fpsbu/gssbotdialogflowengineplugins/blob/master/Plugins/GssCaiDialogPlugin/Readme.md)**
        * 提供 GSS C.AI 服務處理，功能有自然語言解析 (NLU)、智慧問答服務 (QA)







