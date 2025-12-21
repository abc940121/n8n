# Base Request

* **Request** ─ Bot 發送 Http Request
* 發送 Http Request 有以下的類型
  * **[Request Raw Data](RequestRawData.json)** - 發送 Raw Data 的 Request
      * 支援 JSON、XML、Plain Text、HTML
  * **[Request Raw Json](RequestRawJson.md)** - 發送 Raw Data (JSON) 的 Request
      * **1.6 版之後的版本，建議改用 [Request Raw Data](RequestRawData.md)**
  * **[Request Form Data](RequestFormData.md)** - 發送 Form Data 的 Request
  * **[Request Raw Data Or Binary](RequestRawDataOrBinary.md)** - 發送 Raw Data 的 Request 或取得檔案的 Request
      * 支援 JSON、XML、Plain Text、HTML
      * 支援 Binary，並自動上傳到 C.ai File Server
  * **[Parallel Request ](ParallelRequest.md)** - 發送 Raw Data 的 Request (平行發送)
  * **[Multicast Request](BatchRequest.md)** - 發送 Raw Data 的 Request (批示發送)



## ◆ Schema

繼承自 [Base Node](../BaseDialogNode.md)

| 屬性                | 資料型態                                              | 必要屬性 | 描述                                   | 支援變數 | 版本 |
| ------------------- | ----------------------------------------------------- | -------- | -------------------------------------- | -------- | ---- |
| *Id*                | string                                                | Y        | Node ID                                | **X**    | 1.0  |
| *Name*              | string                                                | N        | Node 名稱                              | **X**    | 1.0  |
| *Description*       | string                                                | N        | Node 描述                              | **X**    | 1.0  |
| *Type*              | string                                                | Y        | Node 類型，值為 `request`              | **X**    | 1.0  |
| **Method**          | string                                                | Y        | GET、POST、PUT、PATCH、DELETE          | **X**    | 1.0  |
| **Url**             | string                                                | Y        | Url                                    | **O**    | 1.0  |
| **Headers**         | Dictionary<string,string>                             | N        | Headers                                | **X**    | 1.0  |
| **Body**            | object                                                | N        | Body                                   | **O**    | 1.0  |
| **Timeout**         | int                                                   | N        | Timeout 時間，預設值：`100` (秒)       | **X**    | 1.13 |
| **ResponseOptions** | ResponseOption                                        | N        | Http Response 解析設定                 | **X**    | 1.35 |
| *Actions*           | [NodeAction[]](../../Actions/NodeAction.md)           | N        | Node 轉換行為，即 Transition Condition | **X**    | 1.0  |
| *VariableActions*   | [VariableAction[]](../../Variables/VariableAction.md) | N        | 處理自訂變數                           | **X**    | 1.0  |

### ● Response Options

| 屬性   | 資料型態 | 必要屬性 | 描述                                                        | 支援變數 | 版本 |
| ------ | -------- | -------- | ----------------------------------------------------------- | -------- | ---- |
| Header | string   | Y        | 拿取的 Http Reponse Header Name `[1]` `[2]`，預設值：空字串 | **O**    | 1.35 |

* `[1]` 拿取的 Header Name
    * 空字串：不會拿取任何 Header (預設值)
    * `<Header1>,<Header2>`：指定要拿取的 Header Name，以 `,` 分隔多組 Header Name
    * `*`：拿取全部的 Header
* `[2]` 可透過 **`$.Headers.Values["HeaderName"]`** 或 **`$.NodeOutput.Data.Headers.Values["HeaderName"]`** 等變數取得 Header 值
    * Header 值為一個字串；但如果有一個以上相同的 Header Name 時，值為是一個字串陣列
    * **Set-Cookie** 可以不需要在這裡設定



