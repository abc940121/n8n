# M+ InfoPush 訊息

> * 對應 M+ InfoPush 訊息，M+專用訊息
> * 主要用於顯示圖片與連結





## ◆ Screenshot  

![](Screenshots/InfoPush.png)



## ◆ Channel Support

| Channel 類型            | 是否支援 | 備註                                                         |
| ----------------------- | -------- | ------------------------------------------------------------ |
| Emulator                | **O**    |                                                              |
| Web Chat、iota Chat Bot | **O**    |                                                              |
| iota                    | **O**    | 1. 舊版 iota 不支援 Carousel 卡片排版<br />2. 實作上會轉換成 Adaptive Card |
| LINE                    | **O**    | 1. 實作上會轉換成 LINE Flex Message<br />2. 圖片只支援 JPG 和 PNG，檔案上限 1 MB，需要 HTTPS |
| Teams                   | **O**    |                                                              |
| Slack                   | **O**    |                                                              |
| Webex                   | **O**    | 實作上會轉換成 Adaptive Card                                 |
| Facebook Messenger      | **O**    |                                                              |
| WhatsApp                | **O**    | 1. 卡片按鈕皆視為 ImBack<br />2. 按鈕如果同時有 OpenUrl 和 ImBack 會拆成兩個卡片 |
| Telegram                | **O**    |                                                              |
| M+                      | **O**    | 標題文字字數總和不得超過 300個字                             |
| WeChat (微信個人號)     | **X**    |                                                              |
| WeCom (企業微信)        | **X**    |                                                              |
| DingTalk                | **X**    |                                                              |
| Apple Business Chat     | **X**    |                                                              |



## ◆ Schema

繼承 [MessageContent](MessageContent.md)

| 屬性        | 資料型態            | 必要屬性 | 描述                         | 支援變數 | 版本 |
| ----------- | ------------------- | -------- | ---------------------------- | -------- | ---- |
| *Type*      | string              | Y        | 類型，值為 `mplus.infopush`  | **X**    | 1.2? |
| **Items**   | MPlusInfoPushItem[] | Y        | 圖片與連結，至少1個、最多1個 | **X**    | 1.2? |
| **Payload** | MPlusPayload        | N        | 其他選項                     | **X**    | 1.2? |

### ■ M+ InfoPush Item

| 屬性     | 資料型態 | 必要屬性 | 描述                                                         | 支援變數 | 版本 |
| -------- | -------- | -------- | ------------------------------------------------------------ | -------- | ---- |
| Text     | string   | Y        | 標體與文字，最多 300個字                                     | **O**    | 1.2? |
| ImageUrl | string   | Y        | 圖片的連結<br />只支援 JPG 檔案格式，檔案大小不得超過 40 MB<br />不支援 Base64 Image Url | **O**    | 1.2? |
| Url      | string   | Y        | 開啟的連結                                                   | **O**    | 1.2? |

### ■ M+ Payload

| 屬性        | 資料型態 | 必要屬性 | 描述                                                         | 支援變數 | 版本 |
| ----------- | -------- | -------- | ------------------------------------------------------------ | -------- | ---- |
| OpenUrlType | number   | N        | 連結開啟的方式，預設值：`1`<br />‧`1` (內嵌 Webview 開啟，網頁中的連結再透過外部瀏覽器開啟)<br />‧`2` (外部瀏覽器開啟)<br />‧`3` (連結全部都在 Webview 開啟) | **X**    | 1.2? |





---

## ◆ Example



```json
{
    "Type": "mplus.infopush",
    "Items": [
        {
            "Text": "叡揚資訊",
            "Url": "https://gss.com.tw",
            "ImageUrl": "https://gss.com.tw/favorite.jpg"
		},
        {
            "Text": "M+",
            "Url": "https://www.mplusapp.com",
            "ImageUrl": "https://www.mplusapp.com/favorite.jpg"
		}
    ],
    "Payload": {
        "LinkOpenType": 1
    }
}
```





