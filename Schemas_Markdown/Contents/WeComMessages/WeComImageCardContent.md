# WeCom 圖文卡片

> 圖文卡片



## ◆ Screenshot  

![](https://p.qpic.cn/pic_wework/3478722865/7a7c92760b2bd396e3b856a660f43c8b7db11271bddb3f34/0)



## ◆ Schema

繼承自 [MessageContent](MessageContent.md)

| 屬性              | 資料型態                                      | 必要屬性 | 描述                                                     | 支援變數 | 版本 |
| ----------------- | --------------------------------------------- | -------- | -------------------------------------------------------- | -------- | ---- |
| *Type*            | string                                        | Y        | 類型，值為 `wecom.card.image`                            | **X**    | 1.21 |
| **Title**         | string                                        | Y        | 標題，字數最多 **128** 個字                              | **O**    | 1.21 |
| **Text**          | string                                        | N        | 內文，字數最多 **512** 個字                              | **O**    | 1.21 |
| **ImageUrl**      | string                                        | Y        | 圖片連結，支援 JPG、PNG 檔案                             | **O**    | 1.21 |
| **AspectRatio**   | double                                        | N        | 圖片長寬比例，預設值：`1.3`，最大值 `2.25`，最小值 `1.3` | **X**    | 1.21 |
| **CardTapAction** | [WeComCardTapAction](#-wecom-card-tap-action) | Y        | 卡片點擊事件                                             | **O**    | 1.21 |
| **LinkButton**    | [WeComLinkAction](#-wecom-link-action)[]      | N        | 連結按鈕                                                 | **X**    | 1.21 |

### ● WeCom Card Tap Action

| 屬性        | 資料型態 | 必要屬性              | 描述             | 支援變數 | 版本 |
| ----------- | -------- | --------------------- | ---------------- | -------- | ---- |
| Type        | string   | Y                     | 類型             | **X**    | 1.21 |
| Url         | string   | **Type** = `open_url` | 網址             | **O**    | 1.21 |
| AppId       | string   | **Type** = `open_app` | 小程式 Id        | **O**    | 1.21 |
| AppPagePath | string   | **Type** = `open_app` | 小程式 Page Path | **O**    | 1.21 |

* **WeCom Card Tap Type**

| 按鈕類型   | 描述       | 版本 |
| ---------- | ---------- | ---- |
| `open_url` | 開啟連結   | 1.21 |
| `open_app` | 開啟小程式 | 1.21 |

### ● WeCom Link Action

| 屬性        | 資料型態 | 必要屬性              | 描述             | 支援變數 | 版本 |
| ----------- | -------- | --------------------- | ---------------- | -------- | ---- |
| Type        | string   | Y                     | 類型             | **X**    | 1.21 |
| Title       | string   | Y                     | 按鈕標題         | **O**    | 1.21 |
| Url         | string   | **Type** = `open_url` | 網址             | **O**    | 1.21 |
| AppId       | string   | **Type** = `open_app` | 小程式 Id        | **O**    | 1.21 |
| AppPagePath | string   | **Type** = `open_app` | 小程式 Page Path | **O**    | 1.21 |

* **WeCom Link Action Type**

| 按鈕類型   | 描述       | 版本 |
| ---------- | ---------- | ---- |
| `nonoe`    | 無任何動作 | 1.21 |
| `open_url` | 開啟連結   | 1.21 |
| `open_app` | 開啟小程式 | 1.21 |



---

## ◆ Example

* **卡片點擊事件為開啟網頁**

```json
{
    "Type": "wecom.card.image",
    "Title": "Title",
    "Text": "Text",
    "ImageUrl": "https://yourhost/image.jpg",
    "CardTapAction": {
        "Type": "open_url",
        "Url": "https://www.gss.com.tw"
    }
}
```

* **卡片點擊事件為開啟小程式**

```json
{
    "Type": "wecom.card.image",
    "Title": "Title",
    "Text": "Text",
    "ImageUrl": "https://yourhost/image.jpg",
    "CardTapAction": {
        "Type": "open_app",
        "AppId": "GSS",
        "AppPagePath": "/index.html"
    }
}
```

