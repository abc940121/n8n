# Request Form Data

> 發送 Http Request，其 Request Body 為 Form Data



* **HTTP Request**
    * **Content-Type 支援類型**
        * `application/x-www-form-urlencoded`
        * `multipart/form-data` **`(尚未支援檔案)`**
* **HTTP Response**
    * **Content-Type 支援類型**
        * `text/plain` (純文字)
        * `html` (HTML)
        * `json` (JSON 文字)
        * `xml` (XML 文字)
    * **Content-Encoding 支援類型**
        * `gzip`
        * `deflate`
        * `br`



---

## ◆ Schema

繼承自 [Base Request](BaseRequest.md)

| 屬性                | 資料型態                                              | 必要屬性 | 描述                               | 支援變數 | 版本 |
| ------------------- | ----------------------------------------------------- | -------- | ---------------------------------- | -------- | ---- |
| *Id*                | string                                                | Y        | Node ID                            | **X**    | 1.0  |
| *Name*              | string                                                | N        | Node 名稱                          | **X**    | 1.0  |
| *Description*       | string                                                | N        | Node 描述                          | **X**    | 1.0  |
| *Type*              | string                                                | Y        | Node 類型，值為 `request.formdata` | **X**    | 1.0  |
| **Method**          | string                                                | Y        | GET、POST、PUT、PATCH、DELETE      | **X**    | 1.0  |
| **Url**             | string                                                | Y        | Url                                | **O**    | 1.0  |
| **ContentType**     | string                                                | Y        | Content Type，預設值：`multipart`  | **X**    | 1.6  |
| **Headers**         | Dictionary<string,string>                             | N        | Headers                            | **O**    | 1.0  |
| **Body**            | Dictionary<string,string>                             | N        | Body                               | **O**    | 1.0  |
| **Timeout**         | int                                                   | N        | Timeout 時間，預設值：`100` (秒)   | **X**    | 1.13 |
| **ResponseOptions** | ResponseOption                                        | N        | Http Response 解析設定             | **X**    | 1.35 |
| *Actions*           | [NodeAction[]](../../Actions/NodeAction.md)           | N        | Node 轉換行為                      | **X**    | 1.0  |
| *VariableActions*   | [VariableAction[]](../../Variables/VariableAction.md) | N        | 處理自訂變數                       | **X**    | 1.0  |

### ● Content Type

| 值          | 對應的 HTTP Content Type            | 描述                        |
| ----------- | ----------------------------------- | --------------------------- |
| `multipart` | `multipart/form-data`               | Multipart Form Data，預設值 |
| `form`      | `application/x-www-form-urlencoded` | Form Url Encoded            |

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



## ◆ Node Lifecycle

### ■ 輸入

* **使用者訊息 (User Message)**
    * 無

* **節點設定 (Node Setting)**
    * **Method** ─ HTTP Action，例如：GET、POST、PUT、PATCH、DELETE
    * **Url** ─ URL
    * **Headers** ─ Key 和 Value
    * **Body** ─ Form Data，Key 和 Value
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
    * **Step.3** 發送 Request (Form Data)

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
    * 下一個節點取值
        * **`$.NodeOutput.Data.StatusCode`** ─ Status Code
        * **`$.NodeOutput.Data.IsSuccessStatusCode`** ─ 是否成功
        * **`$.NodeOutput.Data.Text`** ─ API 回傳的結果，原始文字
        * **`$.NodeOutput.Data.Data`** ─ API 回傳的結果，Json 物件 (JToken)
        * **`$.NodeOutput.Data.Headers`**  ─  API 回傳的 Headers 結果
            * **`$.NodeOutput.DataHeaders.SetCookies[i].*`**  ─  拿取 `Set-Cookie` 的資料
            * **`$.NodeOutput.Data.Headers.Values.your-header-name`**  ─  拿取非標準的 Header 資料
                * 值為字串
                * 如果有一個以上相同的 Header Name 時，值為一個字串陣列

```json
{
    "Type": "ApiResponse",
	"Data": {
        "StatusCode": 200,
        "ReasonPhare": "",
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
        "NodeType": "request.formdata",
        "Date": ""
    }
}
```



## ◆ Example

### ● POST Request

```json
{
    "Id": "node_00004",
    "Name": "Call POST Request (Form Data)",
    "Description": "",
    "Type": "request.formdata",
    "Method": "POST",
    "Url": "http://localhost:8000/books/",
    "Headers": {
        "Auth": "token"
    },
    "Body": {
        "bookId": "1"
    },
    "ResponseOptions": {
        "Headers": ""
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
