# Line Flex Message Content

> 靜態的LINE Flex Message Card 訊息，僅適用於 LINE

* **LINE Flex Card Content 衍生類型**
    * **[Fact Carousel Card Content](FlexMessages/LineFlexCarouselCardContent.md)** ─ 明細卡片 (制式 LINE Flex Message Card 訊息)
    * **[Fact Adaptive Card Content](FlexMessages/LineFlexFactCardContent.md)** ─ 明細卡片 (制式 LINE Flex Message Card 訊息)
    * **[List Adaptive Card Content](FlexMessages/LineFlexListCardContent.md)** ─ 清單卡片 (制式 LINE Flex Message Card 訊息)
    * **[Grid Adaptive Card Content](FlexMessages/LineFlexGridCardContent.md)** ─ 表格卡片 (制式 LINE Flex Message Card 訊息)
    * **[Flex Template Card Content](FlexMessages\LineFlexTemplateCardContent.md)** ─ 範本卡片 (套版卡片)



## ◆ Channel Support

> [LINE Flex Message 文件](https://developers.line.biz/en/reference/messaging-api/#message-objects)

| Channel 類型            | 是否支援 | 備註 |
| ----------------------- | -------- | ---- |
| Emulator                | **X**    |      |
| Web Chat、iota Chat Bot | **X**    |      |
| iota                    | **X**    |      |
| LINE                    | **O**    |      |
| Teams                   | **X**    |      |
| Slack                   | **X**    |      |
| Webex                   | **X**    |      |
| Facebook Messenger      | **X**    |      |
| WhatsApp                | **X**    |      |
| Telegram                | **X**    |      |
| M+                      | **X**    |      |
| WeChat (微信個人號)     | **X**    |      |
| WeCom (企業微信)        | **X**    |      |
| DingTalk                | **X**    |      |
| Apple Business Chat     | **X**    |      |





## ◆ Schema

繼承 [MessageContent](MessageContent.md)

| 屬性         | 資料型態                                                 | 必要屬性 | 描述                           | 支援變數 | 版本 |
| ------------ | -------------------------------------------------------- | -------- | ------------------------------ | -------- | ---- |
| *Type*       | string                                                   | Y        | 類型，值為 `line.flex`         | **X**    | 1.0  |
| **AltText**  | string                                                   | Y        | 文字訊息                       | **O**    | 1.0  |
| **Content**  | string                                                   | Y        | LINE Flex Message Json Content | **O**    | 1.0  |
| *QuickReply* | [LineButtonContent[]](FlexMessages/LineActionContent.md) | N        | 快速回覆按鈕                   | **X**    | 1.1  |

### ● Alt Text

> **AltText 必須要給值，值要給有效值字元、不能給空白字元**

* **AltText 在 LINE 上的顯示**

![](FlexMessages/Screenshots/AltText.jpg)



## ◆ Example

### ● 固定內容

* 可以透過 `{{變數名}}` 動態塞入資料

```json
 {
     "Type": "line.flex",
     "AltText": "餐廳資訊",
     "Content": "{\"type\":\"bubble\",\"hero\":{\"url\":\"https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png\",\"size\":\"full\",\"aspectRatio\":\"20:13\",\"aspectMode\":\"cover\",\"flex\":1,\"action\":{\"uri\":\"http://linecorp.com/\",\"type\":\"uri\",\"label\":\" \"},\"type\":\"image\"},\"body\":{\"layout\":\"vertical\",\"contents\":[{\"text\":\"Brown Cafe\",\"contents\":[],\"size\":\"xl\",\"weight\":\"bold\",\"wrap\":false,\"maxLines\":0,\"flex\":1,\"type\":\"text\"},{\"layout\":\"baseline\",\"contents\":[{\"url\":\"https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png\",\"size\":\"sm\",\"type\":\"icon\"},{\"url\":\"https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png\",\"size\":\"sm\",\"type\":\"icon\"},{\"url\":\"https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png\",\"size\":\"sm\",\"type\":\"icon\"},{\"url\":\"https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png\",\"size\":\"sm\",\"type\":\"icon\"},{\"url\":\"https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png\",\"size\":\"sm\",\"type\":\"icon\"},{\"text\":\"4.0\",\"contents\":[],\"color\":\"#999999\",\"size\":\"sm\",\"wrap\":false,\"maxLines\":0,\"flex\":0,\"margin\":\"md\",\"type\":\"text\"}],\"flex\":1,\"margin\":\"md\",\"type\":\"box\"},{\"layout\":\"vertical\",\"contents\":[{\"layout\":\"baseline\",\"contents\":[{\"text\":\"Place\",\"contents\":[],\"color\":\"#AAAAAA\",\"size\":\"sm\",\"wrap\":false,\"maxLines\":0,\"flex\":1,\"type\":\"text\"},{\"text\":\"Miraina Tower, 4-1-6 Shinjuku, Tokyo\",\"contents\":[],\"color\":\"#666666\",\"size\":\"sm\",\"wrap\":true,\"maxLines\":0,\"flex\":5,\"type\":\"text\"}],\"flex\":1,\"spacing\":\"sm\",\"type\":\"box\"},{\"type\":\"box\",\"layout\":\"baseline\",\"contents\":[{\"type\":\"text\",\"text\":\"Date\",\"size\":\"sm\",\"color\":\"#AAAAAA\",\"flex\":1,\"maxLines\":0,\"wrap\":true},{\"type\":\"text\",\"text\":\"{{$.Variables.Today}}\",\"color\":\"#666666\",\"size\":\"sm\",\"flex\":5,\"wrap\":true,\"maxLines\":0}],\"flex\":1,\"spacing\":\"sm\"},{\"layout\":\"baseline\",\"contents\":[{\"text\":\"Time\",\"contents\":[],\"color\":\"#AAAAAA\",\"size\":\"sm\",\"wrap\":false,\"maxLines\":0,\"flex\":1,\"type\":\"text\"},{\"text\":\"10:00 - 23:00\",\"contents\":[],\"color\":\"#666666\",\"size\":\"sm\",\"wrap\":true,\"maxLines\":0,\"flex\":5,\"type\":\"text\"}],\"flex\":1,\"spacing\":\"sm\",\"type\":\"box\"}],\"flex\":1,\"spacing\":\"sm\",\"margin\":\"lg\",\"type\":\"box\"}],\"flex\":1,\"type\":\"box\"},\"footer\":{\"layout\":\"vertical\",\"contents\":[{\"action\":{\"uri\":\"https://linecorp.com\",\"type\":\"uri\",\"label\":\"CALL\"},\"flex\":1,\"height\":\"sm\",\"style\":\"link\",\"type\":\"button\"},{\"action\":{\"uri\":\"https://linecorp.com\",\"type\":\"uri\",\"label\":\"WEBSITE\"},\"flex\":1,\"height\":\"sm\",\"style\":\"link\",\"type\":\"button\"},{\"size\":\"sm\",\"type\":\"spacer\"}],\"flex\":0,\"spacing\":\"sm\",\"type\":\"box\"}}",
     "QuickReply": []
}
```





---

## ◆ 關於 Web Chat 模擬測試

* 如果訊息為 LINE 專用訊息時，LINE 專用訊息專用的訊息會放在 `Attachments` 中
    * 即 ChannelData 會放 LINE 訊息的情況下
* 針對模擬測試而客製的 Web Chat 可以從 `Attachments`
    * 未客製的 Web Chat 則會在 Client 端的 Console 出現無法處理訊息的錯誤
* **Web Chat 收到的 Attachment 格式**
    * **ContentType** ：為 `application/vnd.line.<Line Message Type>`
        * 開頭為 `application/vnd.line`，後面則是放 [LINE 訊息類型](https://developers.line.biz/en/docs/messaging-api/message-types/)，例如：`text`、`template`、`flex`
    * **Contents** ：為 LINE 的訊息內容

```json
{
    "Type": "message",
    "Text": "",
    "Attachments": [
        {
        	"ContentType": "application/vnd.line.flex",
            "Contents": {
                "altText": "卡片訊息",
                "contents": {
                    "footer": {
                        "layout": "vertical",
                        "contents": [
                            {
                                "action": {
                                    "text": "1",
                                    "type": "message",
                                    "label": "Button 01"
                                },
                                "flex": 1,
                                "margin": "md",
                                "height": "sm",
                                "style": "secondary",
                                "type": "button"
                            }
                        ],
                        "flex": 1,
                        "type": "box"
                    },
                    "type": "bubble"
                }
            }
        }
    ],
    "ChannelData": "{\"payload\":{\"message\":{\"altText\":\"卡片訊息\",\"contents\":{\"contents\":[{\"footer\":{\"layout\":\"vertical\",\"contents\":[{\"action\":{\"text\":\"1\",\"type\":\"message\",\"label\":\"Button 01\"},\"flex\":1,\"margin\":\"md\",\"height\":\"sm\",\"style\":\"secondary\",\"type\":\"button\"}],\"flex\":1,\"type\":\"box\"},\"type\":\"bubble\"}],\"type\":\"carousel\"},\"type\":\"flex\"}}}"
}
```

