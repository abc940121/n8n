# WeCom (企業微信) Message Content

> WeCom (企業微信) 專用的訊息



## ◆ 相容的訊息



| 訊息內容 (Content)                  | 類型 ID       | 描述         | 版本 |
| ----------------------------------- | ------------- | ------------ | ---- |
| [Text](TextContent.md)              | `text`        | 文字內容     | 1.0  |
| [Random Text](RandomText.md)        | `text.random` | 隨機文字內容 | 1.2  |
| [SignIn Card](SignInCardContent.md) | `signin.card` | 登入卡片     | 1.0  |



## ◆ 專用的訊息



| 訊息內容 (Content)                                           | 類型 ID                   | 描述                   | 版本 |
| ------------------------------------------------------------ | ------------------------- | ---------------------- | ---- |
| [WeCom Text](WeComMessages/WeComTextContent.md)              | `wecom.text`              | 文字內容               | 1.20 |
| [WeCom Fact Card](WeComMessages/WeComFactCardContent.md)     | `wecom.card.fact`         | 明細卡片               | 1.20 |
| [WeCom Button Card](WeComMessages/WeComButtonCardContent.md) | `wecom.card.button`       | 按鈕卡片               | 1.20 |
| [WeCom Image Card](WeComMessages/WeComImageCardContent.md)   | `wecom.card.image`        | 圖文卡片 (無按鈕)      | 1.20 |
| [WeCom Choice Card](WeComMessages/WeComChoiceCardContent.md) | `wecom.card.choice`       | 勾選卡片               | 1.20 |
| [WeCom Dropdown List Card](WeComMessages/WeComDropdownListCardContent.md) | `wecom.card.dropdownlist` | 多組下拉選單卡片       | 1.20 |
| [WeCom Template Card](WeComMessages/WeComTemplateCardContent.md) | `wecom.card.template`     | 企業微信 Template Card | 1.20 |







---

## ◆ 關於 Web Chat 模擬測試

* 如果訊息為 WeCom 專用訊息時，LINE 專用訊息專用的訊息會放在 `Attachments` 中
    * 即 ChannelData 會放 WeCom 訊息的情況下
* 針對模擬測試而客製的 Web Chat 可以從 `Attachments`
    * 未客製的 Web Chat 則會在 Client 端的 Console 出現無法處理訊息的錯誤
* **Web Chat 收到的 Attachment 格式**
    * **ContentType** ：為 `application/vnd.tencent.wecom.<WeCom Message Type>`
        * 開頭為 `application/vnd.tencent.wecom`，後面則是放 [企業微信訊息類型](https://developer.work.weixin.qq.com/document/path/90236)，例如：`text`、`markdown`、`template_card`
    * **Contents** ：為 WeCom 的訊息內容

```json
{
    "Type": "message",
    "Text": "",
    "Attachments": [
        {
        	"ContentType": "application/vnd.tencent.wecom.template_card",
            "Contents": {
                "msgtype": "template_card"
                "template_card": {
                    "card_type": "vote_interaction",
                    "main_title": {
                        "title": "Title",
                        "desc": "Subtitle"
                    },
                    "task_id": "655",
                    "checkbox": {
                        "question_key": "key",
                        "option_list": [
                            {
                                "id": "value1",
                                "text": "Value 1",
                                "is_checked": false
                            },
                            {
                                "id": "value2",
                                "text": "Value 2",
                                "is_checked": false
                            }
                        ],
                        "mode": 1
                    },
                    "submit_button": {
                        "text": "Submit",
                        "key": "Submit"
                    }
                }
            }
        }
    ],
    "ChannelData": "{\"type\":\"template_card\"\"message\":{\"card_type\":\"vote_interaction\",\"main_title\":{\"title\":\"Title\",\"desc\":\"Subtitle\"},\"task_id\":\"655\",\"checkbox\":{\"question_key\":\"key\",\"option_list\":[{\"id\":\"value1\",\"text\":\"Value 1\",\"is_checked\":false},{\"id\":\"value2\",\"text\":\"Value 2\",\"is_checked\":false}],\"mode\":1},\"submit_button\":{\"text\":\"Submit\",\"key\":\"Submit\"}}}"
}
```

