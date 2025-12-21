# Custom Dialog

> 如果現有的 Node 無法滿足需求時，可以透過自訂對話來達成目標，但是需要建置 Dll 檔案，實作[自訂對話文件可參考這裡](https://git.gss.com.tw/fpsbu/gssbotdialogflowengineplugins/)



## ◆ Schema

繼承自 [Base Node](../BaseDialogNode.md)

| 屬性               | 資料型態                                              | 必要屬性 | 描述                                                         | 支援變數  | 版本    |
| ------------------ | ----------------------------------------------------- | -------- | ------------------------------------------------------------ | --------- | ------- |
| Id                 | string                                                | Y        | Node ID                                                      | **X**     | 1.2     |
| Name               | string                                                | N        | Node 名稱                                                    | **X**     | 1.2     |
| Description        | string                                                | N        | Node 描述                                                    | **X**     | 1.2     |
| Type               | string                                                | Y        | Node 類型，值為 `custom`                                     | **X**     | 1.2     |
| ~~**AssemblyId**~~ | ~~string~~                                            | ~~Y~~    | ~~自訂對話的 DLL檔 ID **`(不得重複)`**~~                     | ~~**O**~~ | ~~1.2~~ |
| **PluginId**       | string                                                | Y        | 自訂對話的 Plugin ID **`(不得重複)`**                        | **O**     | 1.3     |
| **DialogName**     | string                                                | Y        | 執行 DLL檔所需的 Dialog 類別名稱                             | **O**     | 1.2     |
| **Parameters**     | Dictionary<string, [Parameter](#-parameter)>          | N        | 執行自訂對話所需的參數<br />**v1.14 以上的 Value 由 object 調整為 [Paremeter](#-parremeter)** | **X**     | 1.14    |
| *Actions*          | [NodeAction[]](../../Actions/NodeAction.md)           | Y        | Node 轉換行為                                                | **X**     | 1.2     |
| *VariableActions*  | [VariableAction[]](../../Variables/VariableAction.md) | N        | 處理自訂變數                                                 | **X**     | 1.2     |

* ~~**AssemblyId** 需要再 [appsetting.json](../../../AppSetting.md#5-擴充套件-plugins) 中設定對應的 DLL 檔案~~ **`1.3版以上不在提供支援`**
* **PluginId** 指定的 Plugin ID

### ● Parameter

| 屬性   | 資料型態 | 必要屬性 | 描述                                 | 支援變數 | 版本 |
| ------ | -------- | -------- | ------------------------------------ | -------- | ---- |
| $Type  | string   | Y        | 參數的類型，預設值：`use_expression` | **X**    | 1.14 |
| $Value | object   | Y        | 參數的值                             | `[1]`    | 1.14 |

* `[1]` 是否支援變數會以 **$Type** 的值而定
    * **$Type** 為 `use_expression` 時，支援變數
    * **$Type** 為 `plain` 和 `message_content` 時，不支援變數
    * **$Type** 為 `variable` 時，直接使用指定變數的值，不處理任何運算
        * 如果設定多組變數時，只會使用第一個變數
        * 例如："`{{$.Variables.Var1}} {{$.Variables.Var2}}`"，只會取出變數 `$.Variables.Var1` 的值

#### ● Argument Type

| 指派方式/類型     | 描述                                                         |
| ----------------- | ------------------------------------------------------------ |
| `use_expression`  | 參數的值會處理任何資料綁定                                   |
| `plain`           | 參數的值不處理任何資料綁定 **`(不處理任何變數運算)`**        |
| `variable`        | 指派指定變數，不處理任何資料綁定，只處理1個變數 **`(不處理任何變數運算)`** |
| `message_content` | 參數的值為 Message Content，不處理任何資料綁定 **`(不處理任何變數運算)`** |

* **v1.14 之前的 Parameters Schema**

```json
{
    "Type": "custom",
    "PluginId": "MyPlugin",
    "DialogName": "PluginDialog",
    "Parameters": {
        "MyData": "{{$.FlowVariables.Data}}",
        "Title": "Hello World",
        "MessageContent": {
            "Type": "text",
            "Text": "Hello World! ${User}",
            "QuickReply": []
        }
    }
}
```

* **v1.14 之後的 Parameters Schema**

```json
{
    "Type": "custom",
    "PluginId": "MyPlugin",
    "DialogName": "PluginDialog",
    "Parameters": {
        "MyData": {
            "$Type": "use_expression",
            "$Value": "{{$.FlowVariables.Data}}"
        },
        "Title": {
            "$Type": "use_expression",
            "$Value": "Hello World"
        },
        "MessageContent": {
            "$Type": "message_content",
            "$Value":  {
                "Type": "text",
                "Text": "Hello World! ${User}",
                "QuickReply": []
            }
        }
    }
}
```



## ◆ Node Lifecycle

### ■ 輸入

* **使用者訊息 (User Message)**
    * 無
* **節點設定 (Node Setting)**
    * **AssemblyFile** ─ 自訂對話的 DLL檔路徑，[實作自訂對話文件](https://git.gss.com.tw/fpsbu/gssbotdialogflowengineplugins/)
    * **DialogName** ─ 執行 DLL檔所需的 Dialog 類別名稱，[實作自訂對話文件](https://git.gss.com.tw/fpsbu/gssbotdialogflowengineplugins/)
    * **Parameters** ─ 執行自訂對話所需的參數
    * **Actions** ─ 依據使用者輸入，轉換到對應的 Node

### ■ 節點運作

> **不會等候使用者輸入**，因此設計時需要留意無窮迴圈

* **BeginCustomDialog**  `(Turn 1)`
    * **Step.1** 讀取 DLL檔，執行 DLL檔指定對話
* **EndCustomDialog** `(Turn 2)`
    * **Step.1** 取得指定對話的輸出、後續動作
    * **Step.2a** 如果後續動作是呼叫指定對話流程 (`Begin Flow`)、切換指定對話流程 (`Switch Flow`)
        * **Step.2a-1** 執行後續動作，並進入 `Turn 3`
    * **Step.2b** 如果後續動作是預設、指定下一個節點 (Node)
        * **Step.2b-1** 如果指定對話有指定下一個節點 (Node) 或流程 (Flow)，否則取出下一個預設節點 (Node)
        * **Step.2b-2** 結束目前節點，進到下一個節點
* **EndCustomFlowAction** `(Turn 3)`
    * **Step.1** 後續動作執行完畢後，依據後續動作決定進到下一個節點

### ■ 可使用的變數

* **在 Variable Action、Next Node ID 中可使用的變數**
    * [**自動變數**](../../Variables/Variable.md#-自動變數)
    * [**自訂變數**](../../Variables/Variable.md#-自訂變數)
* **在 Node Action Rules 中可使用的變數**
    * **Custom Output Data**
        * 內容依據指定對話的輸出而定

* **在 Node Action** `(當指定對話有指定後續呼叫子流程時)`
    * **Subflow Output Data**
        * 內容依據子流程輸入的內容而定

### ■ 輸出

* **Node Output 後可使用的變數**
    * 內容依據指定對話的輸出而定
    * 內容依據子流程輸入的內容而定



## ◆ Plugins

* **[GssCaiDialog](https://git.gss.com.tw/fpsbu/gssbotdialogflowengineplugins/blob/master/Plugins/GssCaiDialogPlugin/Readme.md)**
    * 提供 GSS C.AI 服務處理，功能有自然語言解析 (NLU)、智慧問答服務 (QA)



## ◆ Example

- **Node Action 可以使用自動變數和自訂變數作為判斷條件**

```json
{
    "Id": "node_00001",
    "Name": "Check Input",
    "Description": "",
    "Type": "custom",
    "PluginId": "GssCaiDialog",
    "DialogName": "GssCaiDialog",
    "Parameters": {},
    "Actions": [
        {
            "Rules": [
                {
                    "Type": "jsonpath",
                    "Rule": {
                        "Type": "text",
                        "Condition": "exactly",
                        "Value": "faq",
                        "IsNegative": false,
                        "IgnoreCase": true
                    },
                    "JsonPath": "$.TopIntent.Type"
                }
            ],
            "Type": "and",
            "Priority": 50,
            "NextNodeId": "node_00001"
        },
        {
            "Rules": [],
            "Type": "none",
            "Priority": 50,
            "NextNodeId": ""
        }
    ],
    "VariableActions": []
}
```