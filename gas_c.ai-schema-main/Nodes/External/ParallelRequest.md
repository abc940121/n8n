# Parallel Request 

* Bot 同時發送多個 Http Request



## ◆ Schema



| 屬性              | 資料型態                                              | 必要屬性 | 描述                                                         | 支援變數 | 版本 |
| ----------------- | ----------------------------------------------------- | -------- | ------------------------------------------------------------ | -------- | ---- |
| *Id*              | string                                                | Y        | Node ID                                                      | **X**    | 1.0  |
| *Name*            | string                                                | N        | Node 名稱                                                    | **X**    | 1.0  |
| *Description*     | string                                                | N        | Node 描述                                                    | **X**    | 1.0  |
| *Type*            | string                                                | Y        | Node 類型，值為 `request.parallel`                           | **X**    | 1.0  |
| **Mode**          | string                                                | N        | 執行的模式<br />● `parallel` ：平行執行，預設值<br />● `sequence `：依序執行，依照陣列順序執行 | **X**    | 1.25 |
| **Requests**      | [HttpRequest](#-http-request)[]                       | Y        | 多個 Http Request，陣列中 Request.Id 不得重複                | **X**    | 1.25 |
| *Actions*         | [NodeAction[]](../../Actions/NodeAction.md)           | N        | Node 轉換行為，即 Transition Condition                       | **X**    | 1.0  |
| *VariableActions* | [VariableAction[]](../../Variables/VariableAction.md) | N        | 處理自訂變數                                                 | **X**    | 1.0  |



### ● Http Request

| 屬性                | 資料型態                  | 必要屬性 | 描述                                 | 支援變數 | 版本 |
| ------------------- | ------------------------- | -------- | ------------------------------------ | -------- | ---- |
| **Id**              | string                    | Y        | Request ID，同一個 Node 不得重複     | **X**    | 1.25 |
| **Method**          | string                    | Y        | GET、POST、PUT、PATCH、DELETE        | **X**    | 1.25 |
| **Url**             | string                    | Y        | Url                                  | **O**    | 1.25 |
| **ContentType**     | string                    | Y        | Content Type                         | **X**    | 1.25 |
| **Headers**         | Dictionary<string,string> | N        | Headers                              | **X**    | 1.25 |
| **RawBody**         | object                    | N        | Raw Body **`[1]`**                   | **O**    | 1.25 |
| **FormBody**        | Dictionary<string,string> | N        | Form Body **`[2]`**                  | **O**    | 1.25 |
| **Timeout**         | int                       | N        | Timeout 時間，預設值：`100` (秒)     | **X**    | 1.25 |
| **ResponseOptions** | ResponseOption            | N        | Http Response 解析設定 **`[3] [4]`** | **X**    | 1.35 |

* **`[1]`** 僅限 **ContentType** 為一個非 Form Data 的類型
    * `text/plain` (純文字)
    * `text/html` (HTML)
    * `text/xml` (XML)
    * `application/json` (JSON 文字)
    * `application/xml` (XML 文字)
    * ...
* **`[2]`** 僅限 **ContentType** 為一個 Form 或 Form Data 的類型
    * `application/x-www-form-urlencoded`
    * `multipart/form-data` **`(尚未支援檔案)`**

### ● Response Options

| 屬性    | 資料型態 | 必要屬性 | 描述                                                        | 支援變數 | 版本 |
| ------- | -------- | -------- | ----------------------------------------------------------- | -------- | ---- |
| Headers | string   | Y        | 拿取的 Http Reponse Header Name `[1]` `[2]`，預設值：空字串 | **O**    | 1.35 |

* **`[1]`** 拿取的 Header Name
    * 空字串：不會拿取任何 Header (預設值)
    * `<Header1>,<Header2>`：指定要拿取的 Header Name，以 `,` 分隔多組 Header Name
    * `*`：拿取全部的 Header
* **`[2]`** 可透過 **`$.Headers.Values.your-header-name`** 或 **`$.NodeOutput.Data.Headers.Values.your-header-name`** 等變數取得 Header 值
    * Header 值為一個字串；但如果有一個以上相同的 Header Name 時，值為是一個字串陣列
    * **Set-Cookie** 可以不需要在這裡設定



---

## ◆ Node Lifecycle

### ■ 輸入

* **使用者訊息 (User Message)**
    * 無

* **節點設定 (Node Setting)**
    * **Mode**  ─ 執行的模式
    * **Requests** ─ 多個 Http Request
    * **Actions** ─ 依據使用者輸入，轉換到對應的 Node
        * **`支援的 Node Action Rule`**
            *  [**JsonPath**](../../Rules/JsonPathRule.md)
            *  [**Evaluate Expression**](../../Rules/EvaluateExpressionRule.md)
            *  [**Composite**](../../Rules/CompositeRule.md)

### ■ 節點運作

> **不會等候使用者輸入**，因此設計時需要留意無窮迴圈

* **OnBeginNode**  `(Turn 1)`
    * **Step.1** 顯示正在處理中
    * **Step.2** 取得呼叫 API 的選項
    * **Step.3** 發送 Http Requests

### ■ 可使用的變數

* **在 Variable Action、Next Node ID 中可使用的變數**
    * [**自動變數**](../../Variables/Variable.md#-自動變數)
    * [**自訂變數**](../../Variables/Variable.md#-自訂變數)
* **在 Node Action Rule 中可使用的變數**
    * **`$.Summary`** ─ 所有的 Request Summary 資訊
        * **IsAllSuccessStatusCode** ─ 所有 Request 都發送成功
        * **IsAllFailStatusCode** ─ 所有 Request 都發送失敗
        * **SuccessRequests** ─ 成功的 Request Id
        * **FailRequests** ─ 失敗的 Request Id
    * **`$.Responses`** ─ 多個 Http Response
        * 為一個 Key-Value 物件，Key 對應 Request Id
    * **`$.Responses.<Request Id>`** ─  為各自的  Http Response，Key 為對應的 Request Id
        * **StatusCode** ─ Status Code
        * **IsSuccessStatusCode** ─ 是否成功
        * **Text** ─ API 回傳的結果，原始文字
        * **Data** ─ API 回傳的結果，Json 物件 (JToken)
        * **Headers**  ─  API 回傳的 Headers 結果
            * **`$.Headers.SetCookies[i].*`**  ─  拿取 `Set-Cookie` 的資料
            * **`$.Headers.Values.your-header-name`**  ─  拿取非標準的 Header 資料
                * 值為字串
                * 如果有一個以上相同的 Header Name 時，值為一個字串陣列

```json
{
    "Summary": {
        "IsAllSuccessStatusCode": true,
        "IsAllFailStatusCode": false,
   		"SuccessRequests": [
            "<Request Id A>",
            "<Request Id C>"
        ],
        "FailRequests": [
            "<Request Id B>"
        ]
    },
    "Responses": {
        "<Request Id A>": {
            "StatusCode": 200,
            "IsSuccessStatusCode": true,
            "Text": "OK",
            "Data": {},
            "Headers": {}
        },
        "<Request Id B>": {
            "StatusCode": 500,
            "IsSuccessStatusCode": false,
            "Text": "Interal Server Error",
            "Data": {},
            "Headers": {}
        },
        "<Request Id C>": {
            "StatusCode": 200,
            "IsSuccessStatusCode": true,
            "Text": "",
            "Data": {},
            "Headers": {
                "SetCookies": [
                    {
                        "Name": "Token",
                        "Value": "123456789d",
                        "Domain": "gss.com.tw",
                        "Expires": "2022-01-01T00:00:00Z",
                        "Path": "/",
                        "Secure": true
                    },
                    {
                        "Name": "User",
                        "Value": "gss",
                        "Domain": "gss.com.tw",
                        "Expires": "2022-01-01T00:00:00Z",
                        "Path": "/",
                        "Secure": true
                    }
                ],
       		 	"Values": {}
            }
        }
    }
}
```

### ■ 輸出

* **Node Output 後可使用的變數**
    * 下一個節點取值
        * **`$.NodeOutput.Data.Summary`** ─ 所有的 Request Summary 資訊
            * **IsAllSuccessStatusCode** ─ 所有 Request 都發送成功
            * **IsAllFailStatusCode** ─ 所有 Request 都發送失敗
            * **SuccessRequests** ─ 成功的 Request Id
            * **FailRequests** ─ 失敗的 Request Id
        * **`$.NodeOutput.Data.Responses`** ─ 多個 Http Response
            * 為一個 Key-Value 物件，Key 對應 Request Id
        * **`$.NodeOutput.Data.Responses.<Request Id>`** ─  為各自的  Http Response
            * **StatusCode** ─ Status Code
            * **IsSuccessStatusCode** ─ 是否成功
            * **Text** ─ API 回傳的結果，原始文字
            * **Data** ─ API 回傳的結果，Json 物件 (JToken)
            * **Headers**  ─  API 回傳的 Headers 結果
                * **`$.NodeOutput.Headers.SetCookies[i].*`**  ─  拿取 `Set-Cookie` 的資料
                * **`$.NodeOutput.Data.Headers.Values.your-header-name`**  ─  拿取非標準的 Header 資料
                    * 值為字串
                    * 如果有一個以上相同的 Header Name 時，值為一個字串陣列

```json
{
    "Type": "ApiResponse",
	"Data": {
        "Summary": {
            "IsAllSuccessStatusCode": true,
            "IsAllFailStatusCode": false,
            "SuccessRequests": [
                "<Request Id A>",
                "<Request Id C>"
            ],
            "FailRequests": [
                "<Request Id B>"
            ]
        },
        "Responses": {
            "<Request Id A>": {
                "StatusCode": 200,
                "IsSuccessStatusCode": true,
                "Text": "OK",
                "Data": {},
                "Headers": {}
            },
            "<Request Id B>": {
                "StatusCode": 200,
                "IsSuccessStatusCode": true,
                "Text": "",
                "Data": {},
                "Headers": {
                    "SetCookies": [
                        {
                            "Name": "Token",
                            "Value": "123456789d",
                            "Domain": "gss.com.tw",
                            "Expires": "2022-01-01T00:00:00Z",
                            "Path": "/",
                            "Secure": true
                        },
                        {
                            "Name": "User",
                            "Value": "gss",
                            "Domain": "gss.com.tw",
                            "Expires": "2022-01-01T00:00:00Z",
                            "Path": "/",
                            "Secure": true
                        }
                    ],
        			"Values": {}
                }
            }
        }
    },
    "From": {
        "BotId": "",
        "FlowId": "",
        "FlowName": "",
        "NodeId": "",
        "NodeName": "",
        "NodeType": "request.formdata",
        "Date": ""
    }
}
```



---

## ◆ Example



```json
{
     "Id": "node_00001",
    "Name": "Parallel Call Http Request",
    "Description": "",
    "Type": "request.parallel",
    "Mode": "parallel",
    "Requests": [
        {
            "Id": "Users",
            "Type": "raw",
            "Method": "POST",
            "Url": "http://localhost:8000/users/",
            "Headers": {
                "Auth": "token"
            },
            "ContentType": "json",
            "RawBody": "{\"userId\": \"1\"}",
            "ResponseOptions": {
                "Headers": ""
            }
        },
        {
            "Id": "BookingRoom",
            "Type": "form",
            "Method": "POST",
            "Url": "http://localhost:8000/books/",
            "Headers": {
                "Auth": "token"
            },
            "FormBody": {
                "bookId": "1"
            },
            "ResponseOptions": {
                "Headers": ""
            }
        }
    ],
    "Actions": [
        {
            "Rules": [],
            "Type": "otherwise",
            "Priority": 50,
            "NextNodeId": "node_00002"
        }
    ],
    "VariableActions": [
        {
            "Type": "variable.set",
            "TriggerType": "after_node",
            "Variable": "GetResult",
            "AssignValue": "$.NodeOutput.Data",
            "AssignValueType": "variable"
        }
    ]
}
```

