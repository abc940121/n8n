# Request Raw Data Or Binary

>  發送 Http Request，其 Request Body，當 Response 是一個 Binary 檔案時自動上傳到 File Server



* **HTTP Request**
    * **Content-Type 支援類型**
        * `text/plain` (純文字)
        * `text/html` (HTML)
        * `text/xml` (XML)
        * `application/json` (JSON 文字)
        * `application/xml` (XML 文字)
* **HTTP Response**
    * **Content-Type 支援類型**
        * `text/plain` (純文字)
        * `text/html` (HTML)
        * `text/xml` (XML)
        * `application/json` (JSON 文字)
        * `application/xml` (XML 文字)
        * 非上述的 Content-Type 才會上傳到 C.ai File Server
    * **Content-Encoding 支援類型**
        * `gzip`
        * `deflate`
        * `br`



---

## ◆ Schema

繼承自 [Base Request](BaseRequest.md)

| 屬性                        | 資料型態                                              | 必要屬性 | 描述                                                         | 支援變數 | 版本 |
| --------------------------- | ----------------------------------------------------- | -------- | ------------------------------------------------------------ | -------- | ---- |
| *Id*                        | string                                                | Y        | Node ID                                                      | **X**    | 1.6  |
| *Name*                      | string                                                | N        | Node 名稱                                                    | **X**    | 1.6  |
| *Description*               | string                                                | N        | Node 描述                                                    | **X**    | 1.6  |
| *Type*                      | string                                                | Y        | Node 類型，值為 `request.raw.binary`                         | **X**    | 1.6  |
| **Method**                  | string                                                | Y        | GET、POST、PUT、PATCH、DELETE                                | **X**    | 1.6  |
| **Url**                     | string                                                | Y        | Url                                                          | **O**    | 1.6  |
| **ContentType**             | string                                                | Y        | Content Type，預設值：`text`                                 | **X**    | 1.6  |
| **Headers**                 | Dictionary<string,string>                             | N        | Headers                                                      | **O**    | 1.6  |
| **Body**                    | string                                                | N        | Body                                                         | **O**    | 1.6  |
| **Timeout**                 | int                                                   | N        | Timeout 時間，預設值：`100` (秒)                             | **O**    | 1.13 |
| **ResponseOptions**         | ResponseOption                                        | N        | Http Response 解析設定                                       | **X**    | 1.35 |
| **AutoUploadBinaryOptions** | AutoUploadBinaryOption                                | N        | 自動將 Http Response Binary 檔案上傳到 File Server 的參數設定 | **X**    | 2.x  |
| *Actions*                   | [NodeAction[]](../../Actions/NodeAction.md)           | N        | Node 轉換行為                                                | **X**    | 1.6  |
| *VariableActions*           | [VariableAction[]](../../Variables/VariableAction.md) | N        | 處理自訂變數                                                 | **X**    | 1.6  |

### ● Content Type

| 值                 | 對應的 HTTP Content Type | 描述                             |
| ------------------ | ------------------------ | -------------------------------- |
| `text`             | `text/plain`             | **[縮寫]** 純文字 (預設值)       |
| `text/plain`       | `text/plain`             | 純文字                           |
| `html`             | `text/html`              | **[縮寫]** HTML 字串             |
| `text/html`        | `text/html`              | HTML 字串                        |
| `json`             | `application/json`       | **[縮寫]**  JSON 字串            |
| `application/json` | `application/json`       | JSON 字串                        |
| `xml`              | `application/xml`        | **[縮寫]**  XML 字串             |
| `application/xml`  | `application/xml`        | XML 字串                         |
| `text/xml`         | `text/xml`               | XML 字串                         |
| 其他 Content Type  |                          | 允許自己設定自己要的 ontent Type |

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

### ● Auto Upload Binary Options

* 自動將 Http Response Binary 檔案上傳到 File Server 的參數
* Binary 檔案的定義
    * 非純文字 (`text/plain`)、HTML (`text/html`)、JSON 文字 (`application/json`)、XML 文字 (`text/xml`、`application/xml`)

| 屬性           | 資料型態 | 必要屬性 | 描述                                                         | 支援變數 | 版本 |
| -------------- | -------- | -------- | ------------------------------------------------------------ | -------- | ---- |
| IsEnable       | bool     | N        | 如果為 true 代表啟用此功能，預設值：`false`                  | **X**    | 2.x  |
| ExpirationTime | string   | N        | 設定檔案多久過期，格式 `[dd.]hh:mm:ss`，預設值：`1.00:00:00` (一天) | **O**    | 2.x  |



## ◆ Node Lifecycle

### ■ 輸入

* **使用者訊息 (User Message)**
    * 無

* **節點設定 (Node Setting)**
    * **Method** ─ HTTP Action，例如：GET、POST、PUT、PATCH、DELETE
    * **Url** ─ URL
    * **Headers** ─ Key 和 Value
    * **ContentType ─ ** Content Type
    * **Body** ─ Raw Content
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
    * **Step.3** 發送 Request (Json Raw)

### ■ 可使用的變數

* **在 Variable Action、Next Node ID 中可使用的變數**
    * [**自動變數**](../../Variables/Variable.md#-自動變數)
    * [**自訂變數**](../../Variables/Variable.md#-自訂變數)
* **在 Node Action Rule 中可使用的變數**
    * **`$.StatusCode`** ─ Status Code
    * **`$.IsSuccessStatusCode`** ─ 是否成功
    * **`$.Text`** ─ API 回傳的結果，原始文字
    * **`$.Data`** ─ API 回傳的結果，Json 物件 (JToken)
    * **`$.Headers`**  ─  API 回傳的 Headers 結果
        * **`$.Headers.SetCookies[i].*`**  ─  拿取 `Set-Cookie` 的資料
        * **`$.Headers.Values.your-header-name`**  ─  拿取非標準的 Header 資料
            * 值為字串
            * 如果有一個以上相同的 Header Name 時，值為一個字串陣列

```json
{
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
```

### ■ 輸出

* **Node Output 後可使用的變數**
    * 當 **AutoUploadBinaryOptions.IsEnable = true** 且 appsettings.json 的 FileServerOptions 有設定時，Node Output 為 File Server 的 Response
        * 上述條件不成立時，Node Output 則此節點 Request 的 Response
    * 下一個節點取值
        * **`$.NodeOutput.Data.StatusCode`** ─ Status Code
        * **`$.NodeOutput.Data.IsSuccessStatusCode`** ─ 是否成功
        * **`$.NodeOutput.Data.Text`** ─ API 回傳的結果，原始文字
        * **`$.NodeOutput.Data.Data`** ─ API 回傳的結果，Json 物件 (JToken)
        * **`$.NodeOutput.Data.Headers`**  ─  API 回傳的 Headers 結果
            * **`$.NodeOutput.Data.Headers.SetCookies[i].*`**  ─  拿取 `Set-Cookie` 的資料
            * **`$.NodeOutput.Data.Headers.Values.your-header-name`**  ─  拿取非標準的 Header 資料
                * 值為字串
                * 如果有一個以上相同的 Header Name 時，值為一個字串陣列

```json
{
    "Type": "ApiResponse",
	"Data": {
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
    },
    "From": {
        "BotId": "",
        "FlowId": "",
        "FlowName": "",
        "NodeId": "",
        "NodeName": "",
        "NodeType": "request.raw.binary",
        "Date": ""
    }
}
```



## ◆ Example

### ● GET Request (JSON Response)

```json
{
    "Id": "node_00002",
    "Name": "Call GET Request (Json)",
    "Description": "",
    "Type": "request.raw.binary",
    "Method": "GET",
    "Url": "http://localhost:8000/users/1",
    "Headers": {
        "Auth": "token"
    },
    "ContentType": "json",
    "Body": "",
    "ResponseOptions": {
        "Headers": ""
    },
    "AutoUploadBinaryOptions": {
        "IsEnable": true,
        "ExpirationTime": "1.00:00:00"
    },
    "Actions": [
        {
            "Rules": [
                {
                    "Type": "jsonpath",
                    "Rule": {
                        "Type": "text",
                        "Condition": "exactly",
                        "Value": "true",
                        "IsNegative": false,
                        "IgnoreCase": true
                    },
                    "JsonPath": "$.IsSuccessStatusCode"
                }
            ],
            "Type": "intersection",
            "Priority": 50,
            "NextNodeId": "node_00005"
        },
        {
            "Rules": [],
            "Type": "otherwise",
            "Priority": 50,
            "NextNodeId": "node_00008"
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



### ● GET Request (Binary Response)

```json
{
    "Id": "node_00008",
    "Name": "Call GET Request (Binary)",
    "Description": "",
    "Type": "request.raw.binary",
    "Method": "GET",
    "Url": "https://www.gss.com.tw/templates/bevel/images/gss-logo.png",
    "ContentType": "",
    "Headers": {},
    "Body": "",
    "ResponseOptions": {
        "Headers": "*"
    },
    "AutoUploadBinaryOptions": {
        "IsEnable": true,
        "ExpirationTime": "1.00:00:00"
    },
    "Actions": [
        {
            "Rules": [
                {
                    "Type": "jsonpath",
                    "Rule": {
                        "Type": "text",
                        "Condition": "exactly",
                        "Value": "true",
                        "IsNegative": false,
                        "IgnoreCase": true
                    },
                    "JsonPath": "$.IsSuccessStatusCode"
                }
            ],
            "Type": "and",
            "Priority": 50,
            "NextNodeId": "node_10006"
        },
        {
            "Rules": [],
            "Type": "otherwise",
            "Priority": 50,
            "NextNodeId": "node_10009"
        }
    ],
    "VariableActions": [
        {
            "Type": "variable.set",
            "TriggerType": "after_node",
            "Variable": "GetResult",
            "VariableType": "global",
            "AssignValue": "$.NodeOutput.Data",
            "AssignValueType": "variable"
        }
    ]
}
```



### ● POST Request (JSON Response)

```json
{
    "Id": "node_00003",
    "Name": "Call POST Request (Json)",
    "Description": "",
    "Type": "request.raw.binary",
    "Method": "POST",
    "Url": "http://localhost:8000/users/",
    "Headers": {
        "Auth": "token"
    },
    "ContentType": "json",
    "Body": "{\"userId\": \"1\"}",
    "ResponseOptions": {
        "Headers": "",
    },
    "AutoUploadBinaryOptions": {
        "IsEnable": true,
        "ExpirationTime": "1.00:00:00"
    },
    "Actions": [
        {
            "Rules": [
                {
                    "Type": "jsonpath",
                    "Rule": {
                        "Type": "text",
                        "Condition": "exactly",
                        "Value": "true",
                        "IsNegative": false,
                        "IgnoreCase": true
                    },
                    "JsonPath": "$.IsSuccessStatusCode"
                }
            ],
            "Type": "intersection",
            "Priority": 50,
            "NextNodeId": "node_00005"
        },
        {
            "Rules": [],
            "Type": "otherwise",
            "Priority": 50,
            "NextNodeId": "node_00008"
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



### ● POST Request (Binary Response)

* 範例為介接 [Azure Text to Speech](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/rest-text-to-speech?tabs=nonstreaming#convert-text-to-speech)

```json
{
    "Id": "node_00008",
    "Name": "Call POST Request (Binary)",
    "Description": "",
    "Type": "request.raw.binary",
    "Method": "POST",
    "Url": "https://eastasia.tts.speech.microsoft.com/cognitiveservices/v1",
    "Headers": {
        "X-Microsoft-OutputFormat": "riff-24khz-16bit-mono-pcm",
        "Ocp-Apim-Subscription-Key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "User-Agent": "BotFlowEngine"
    },
    "ContentType": "application/ssml+xml",
    "Body": "<speak version=\"1.0\" xml:lang=\"en-US\"><voice xml:lang=\"en-US\" xml:gender=\"Male\" name=\"en-US-ChristopherNeural\">I'm excited to try text to speech!</voice></speak>",
    "ResponseOptions": {},
    "AutoUploadBinaryOptions": {
         "IsEnable": true,
         "ExpirationTime": "1.00:00:00"
     },
     "Actions": [
         {
             "Rules": [
                 {
                     "Type": "jsonpath",
                     "Rule": {
                         "Type": "text",
                         "Condition": "exactly",
                         "Value": "true",
                         "IsNegative": false,
                         "IgnoreCase": true
                     },
                     "JsonPath": "$.IsSuccessStatusCode"
                 }
             ],
             "Type": "and",
             "Priority": 50,
             "NextNodeId": "node_10006"
         },
         {
             "Rules": [],
             "Type": "otherwise",
             "Priority": 50,
             "NextNodeId": "node_10009"
         }
     ],
     "VariableActions": [
         {
             "Type": "variable.set",
             "TriggerType": "after_node",
             "Variable": "GetResult",
             "VariableType": "global",
             "AssignValue": "$.NodeOutput.Data",
             "AssignValueType": "variable"
         }
     ]
}
```

