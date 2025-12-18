# 各個 Channel 支援的 Message Content



## ◆ Quick Reply

> 下方一次性快速回覆的按鈕

| Channel 類型            | 是否支援 | 備註                                               |
| ----------------------- | -------- | -------------------------------------------------- |
| Emulator                | **O**    |                                                    |
| Web Chat、iota Chat Bot | **O**    |                                                    |
| iota                    | **X**    |                                                    |
| LINE                    | **▲**    | 僅在手機版支援<br />只支援訊息回覆，不支援開啟連結 |
| Teams                   | **X**    | 整個訊息物件上限 28 KB                             |
| Slack                   | **X**    |                                                    |
| Webex                   | **X**    |                                                    |
| Facebook Messenger      | **▲**    | 只支援訊息回覆，不支援開啟連結                     |
| WhatsApp                | **X**    |                                                    |
| Telegram                | **?**    |                                                    |
| M+                      | **X**    |                                                    |
| WeChat (微信個人號)     | **X**    |                                                    |
| WeCom (企業微信)        | **X**    |                                                    |
| DingTalk                | **X**    |                                                    |
| Apple Business Chat     | **X**    | 目前暫不支援<br />(Apple Business Chat 有支援)     |



## ◆ Channel Data

> Channel Data 內容

| Channel 類型        | 是否支援 | 備註                     |
| ------------------- | -------- | ------------------------ |
| Emulator            | **O**    |                          |
| Web Chat            | **O**    |                          |
| iota                | **X**    |                          |
| LINE                | **▲**    | 僅拿來放 Flex Message    |
| Teams               | **X**    |                          |
| Slack               | **▲**    | 僅拿來放 Block Kit 訊息  |
| Webex               | **▲**    | 僅拿來放訊息推送對象     |
| Facebook Messenger  | **X**    |                          |
| Telegram            | **X**    |                          |
| M+                  | **X**    |                          |
| WeChat (微信個人號) | **X**    |                          |
| WeCom (企業微信)    | **▲**    | 僅拿來放企業微信模板卡片 |
| DingTalk            | **X**    |                          |
| Apple Business Chat | **X**    |                          |



---

## ◆ [Text](TextContent.md)

> 文字內容

| Channel 類型        | 是否支援 | 備註                                                   |
| ------------------- | -------- | ------------------------------------------------------ |
| Emulator            | **O**    | 支援 Markdown 語法                                     |
| Web Chat            | **O**    | 支援 Markdown 語法                                     |
| iota                | **O**    |                                                        |
| LINE                | **O**    | 文字長度上限 2000 字                                   |
| Teams               | **O**    | 1. 支援 Markdown 語法<br />2. 整個訊息物件上限 28 KB   |
| Slack               | **▲**    | 支援 Slack Markdown 語法，非標準的 Markdown 語法       |
| Webex               | **O**    | 支援 Markdown 語法                                     |
| Facebook Messenger  | **O**    | 文字長度上限 2000 字                                   |
| Telegram            | **O**    | 1. 部分支援 Markdown 語法<br />2. 文字長度上限 4096 字 |
| M+                  | **O**    |                                                        |
| WeChat (微信個人號) | **O**    |                                                        |
| WeCom (企業微信)    | **O**    | 支援部分 Markdown 語法                                 |
| DingTalk            | **O**    | 支援部分 Markdown 語法                                 |
| Apple Business Chat | **O**    |                                                        |



---

## ◆ [Random Text](RandomText.md)

> 隨機文字內容

| Channel 類型        | 是否支援 | 備註                                                   |
| ------------------- | -------- | ------------------------------------------------------ |
| Emulator            | **O**    | 支援 Markdown 語法                                     |
| Web Chat            | **O**    | 支援 Markdown 語法                                     |
| iota                | **O**    |                                                        |
| LINE                | **O**    | 文字長度上限 2000 字                                   |
| Teams               | **O**    | 1. 支援 Markdown 語法<br />2. 整個訊息物件上限 28 KB   |
| Slack               | **O**    | Slack Markdown 語法，非標準的 Markdown 語法            |
| Webex               | **O**    | 支援 Markdown 語法                                     |
| Facebook Messenger  | **O**    | 文字長度上限 2000 字                                   |
| Telegram            | **O**    | 1. 部分支援 Markdown 語法<br />2. 文字長度上限 4096 字 |
| M+                  | **O**    |                                                        |
| WeChat (微信個人號) | **O**    |                                                        |
| WeCom (企業微信)    | **O**    | 支援部分 Markdown 語法                                 |
| DingTalk            | **O**    | 支援部分 Markdown 語法                                 |
| Apple Business Chat | **O**    |                                                        |



---

## ◆ [Hero Card](HeroCardContent.md)

> 一般卡片 (圖文卡片)

| Channel 類型        | 是否支援 | 備註                                                         |
| ------------------- | -------- | ------------------------------------------------------------ |
| Emulator            | **O**    |                                                              |
| Web Chat            | **O**    |                                                              |
| iota                | **O**    | 1. 舊版 iota 不支援 Carousel 卡片排版<br />2. 實作上會轉換成 Adaptive Card |
| LINE                | **O**    | 1. 實作上會轉換成 LINE Flex Message<br />2. ~~卡片 PostBack 按鈕回覆的值是放在 Activity.Text~~<br />3. 圖片只支援 JPG 和 PNG，檔案上限 1 MB，需要 HTTPS |
| Teams               | **O**    | 卡片按鈕皆視為 ImBack                                        |
| Slack               | **O**    | 1. 實作上會轉換成 Slack Block Kit 訊息<br />2. 回覆的內容為專用格式 |
| Webex               | **O**    | 1. 實作上會轉換成 Adaptive Card<br />2. 按鈕數量最多5個      |
| Facebook Messenger  | **O**    | 卡片按鈕皆視為 ImBack                                        |
| Telegram            | **O**    | 卡片按鈕皆視為 PostBack                                      |
| M+                  | **▲**    | 1. 按鈕不支援開啟連結<br />2. 按鈕標題 = 點擊後回覆文字，卡片按鈕皆視為 ImBack<br />3. 標題與文字字數總和不得超過 500個字 |
| WeChat (微信個人號) | **X**    |                                                              |
| WeCom (企業微信)    | **▲**    | 1. 不支援 Carousel 卡片排版<br />2. 不支援圖片顯示<br />3. 不支援群組對話 |
| DingTalk            | **▲**    | 不支援圖片、標題 (Title)、按鈕、Carousel 卡片排版            |
| Apple Business Chat | **X**    | 目前暫不提供支援<br />(Apple Business Chat 有提供類似卡片的訊息) |



---

## ◆ [SignIn Card](SignInCardContent.md)

> 登入卡片 (文字卡片)

| Channel 類型        | 是否支援 | 備註                                                         |
| ------------------- | -------- | ------------------------------------------------------------ |
| Emulator            | **O**    |                                                              |
| Web Chat            | **O**    |                                                              |
| iota                | **O**    | 1. 舊版 iota 不支援 Carousel 卡片排版<br />2. 實作上會轉換成 Adaptive Card |
| LINE                | **O**    | 1. 實作上會轉換成 LINE Flex Message<br />2. ~~卡片 PostBack 按鈕回覆的值是放在 Activity.Text~~ |
| Teams               | **O**    | 卡片按鈕皆視為 ImBack                                        |
| Slack               | **O**    | 1. 實作上會轉換成 Slack Block Kit 訊息<br />2. 回覆的內容為專用格式 |
| Webex               | **O**    | 1. 實作上會轉換成 Adaptive Card<br />2. 按鈕數量最多5個      |
| Facebook Messenger  | **O**    | 卡片按鈕皆視為 ImBack                                        |
| Telegram            | **O**    | 卡片按鈕皆視為 PostBack                                      |
| M+                  | **▲**    | 1. 按鈕不支援開啟連結<br />2. 按鈕標題 = 點擊後回覆文字，卡片按鈕皆視為 ImBack<br />3. 標題字數不得超過 500個字 |
| WeChat (微信個人號) | **X**    |                                                              |
| WeCom (企業微信)    | **O**    | 1. 不支援 Carousel 卡片排版<br />2. 不支援群組對話           |
| DingTalk            | **O**    | 不支援按鈕、Carousel 卡片排版                                |
| Apple Business Chat | **X**    | 目前暫不提供支援<br />(Apple Business Chat 有提供類似卡片的訊息) |



---

## ◆ [Animation Card](AnimationCardContent.md)

> 圖片卡片 (JPG、PNG、GIF)

| Channel 類型        | 是否支援 | 備註                                                         |
| ------------------- | -------- | ------------------------------------------------------------ |
| Emulator            | **O**    |                                                              |
| Web Chat            | **O**    |                                                              |
| iota                | **O**    | 1. 舊版 iota 不支援 Carousel 卡片排版<br />2. 實作上會轉換成 Adaptive Card |
| LINE                | **O**    | 1. 實作上會轉換成 LINE Flex Message<br />2. 卡片 PostBack 按鈕回覆的值是放在 Activity.Text<br />3. 圖片只支援 JPG 和 PNG，檔案上限 1 MB，需要 HTTPS |
| Teams               | **X**    |                                                              |
| Slack               | **O**    | 1. 實作上會轉換成 Slack Block Kit 訊息<br />2. 回覆的內容為專用格式 |
| Webex               | **O**    | 1. 實作上會轉換成 Adaptive Card<br />2. 按鈕數量最多5個      |
| Facebook Messenger  | **X**    |                                                              |
| Telegram            | **O**    | 卡片按鈕皆視為 PostBack                                      |
| M+                  | **X**    |                                                              |
| WeChat (微信個人號) | **X**    |                                                              |
| WeCom (企業微信)    | **X**    |                                                              |
| DingTalk            | **X**    |                                                              |
| Apple Business Chat | **X**    |                                                              |



---

## ◆ [Receipt Card](ReceiptCardContent.md)

> 收據卡片、明細卡片

| Channel 類型        | 是否支援 | 備註                                                         |
| ------------------- | -------- | ------------------------------------------------------------ |
| Emulator            | **O**    |                                                              |
| Web Chat            | **O**    |                                                              |
| iota                | **O**    | 1. 舊版 iota不支援 Carousel 卡片排版<br />2. 實作上會轉換成 Adaptive Card |
| LINE                | **O**    | 1. 實作上會轉換成 LINE Flex Message<br />2. ~~卡片 PostBack 按鈕回覆的值是放在 Activity.Text~~<br />3. 圖片只支援 JPG 和 PNG，檔案上限 1 MB，需要 HTTPS |
| Teams               | **O**    | 卡片按鈕皆視為 ImBack                                        |
| Slack               | **X**    |                                                              |
| Webex               | **O**    | 1. 實作上會轉換成 Adaptive Card<br />2. 按鈕數量最多5個      |
| Facebook Messenger  | **X**    |                                                              |
| Telegram            | **X**    |                                                              |
| M+                  | **X**    |                                                              |
| WeChat (微信個人號) | **X**    |                                                              |
| WeCom (企業微信)    | **X**    |                                                              |
| DingTalk            | **X**    |                                                              |
| Apple Business Chat | **X**    |                                                              |



---

## ◆ [Audio Card](AudioCardContent.md)

> 音訊卡片 (MP3、WAV)

| Channel 類型        | 是否支援 | 備註                                                         |
| ------------------- | -------- | ------------------------------------------------------------ |
| Emulator            | **O**    |                                                              |
| Web Chat            | **O**    |                                                              |
| iota                | **O**    | 1. 舊版 iota不支援 Carousel 卡片排版<br />2. 實作上會轉換成 Adaptive Card |
| LINE                | **▲**    | 1. 實作上會轉換成 2則訊息 Audio Message + LINE Flex Message<br />2. ~~卡片 PostBack 按鈕回覆的值是放在 Activity.Text~~<br />3. 檔案只支援 MP3，檔案上限 10 MB，需要 HTTPS |
| Teams               | **X**    |                                                              |
| Slack               | **X**    |                                                              |
| Webex               | **O**    | 1. 實作上會轉換成 Adaptive Card<br />2. 按鈕數量最多5個      |
| Facebook Messenger  | **X**    |                                                              |
| Telegram            | **X**    |                                                              |
| M+                  | **X**    |                                                              |
| WeChat (微信個人號) | **X**    |                                                              |
| WeCom (企業微信)    | **X**    |                                                              |
| DingTalk            | **X**    |                                                              |
| Apple Business Chat | **X**    |                                                              |



---

## ◆ Video Card

> 影片卡片 (Youtube、MP4)

| Channel 類型        | 是否支援 | 備註                                                         |
| ------------------- | -------- | ------------------------------------------------------------ |
| Emulator            | **O**    |                                                              |
| Web Chat            | **O**    |                                                              |
| iota                | **O**    | 1. 舊版 iota不支援 Carousel 卡片排版<br />2. 實作上會轉換成 Adaptive Card |
| LINE                | **▲**    | 1. 實作上會轉換成 2則訊息 Video Message + LINE Flex Message<br />2. ~~卡片 PostBack 按鈕回覆的值是放在 Activity.Text~~<br />3. 檔案只支援 MP4，檔案上限 10 MB，且需要 HTTPS |
| Teams               | **X**    |                                                              |
| Slack               | **O**    | 1. 需影片截圖<br />2. 影片連結限可嵌入 iFrame 的連結，例如：YouTube Embed |
| Webex               | **O**    | 1. 實作上會轉換成 Adaptive Card<br />2. 按鈕數量最多5個      |
| Facebook Messenger  | **X**    |                                                              |
| Telegram            | **X**    |                                                              |
| M+                  | **X**    |                                                              |
| WeChat (微信個人號) | **X**    |                                                              |
| WeCom (企業微信)    | **X**    |                                                              |
| DingTalk            | **X**    |                                                              |
| Apple Business Chat | **X**    |                                                              |



## ◆ [Attachment](Attachment.md)

> 附件檔案

| Channel 類型        | 是否支援 | 備註                                                         |
| ------------------- | -------- | ------------------------------------------------------------ |
| Emulator            | **O**    |                                                              |
| Web Chat            | **O**    |                                                              |
| iota                | **X**    |                                                              |
| LINE                | **O**    | 1. 圖片僅限 JPG、PNG，檔案上限 1 MB、需要 HTTPS<br />2. 聲音檔僅限 MP3，檔案上限 10 MB、需要 HTTPS<br />3. 影片檔僅限 MP4，檔案上限 10 MB、需要 HTTPS |
| Teams               | **O**    | 檔案上限 4MB                                                 |
| Slack               | **X**    |                                                              |
| Webex               | **X**    |                                                              |
| Facebook Messenger  | **O**    | 檔案上限 25 MB                                               |
| Telegram            | **O**    | 檔案上限未知                                                 |
| M+                  | **O**    | 圖片僅限 JPG、PNG，檔案上限 40 MB                            |
| WeChat (微信個人號) | **X**    |                                                              |
| WeCom (企業微信)    | **X**    |                                                              |
| DingTalk            | **X**    |                                                              |
| Apple Business Chat | **X**    |                                                              |



---

## ◆ [Adaptive Card](AdaptiveCardContent.md)、[Adaptive Template Card](AdaptiveCards/TemplateCardContent.md)

> 自訂卡片 (Adaptive Card)、範本卡片 (Adaptive Template Card)

> [Adaptive Card 文件](https://adaptivecards.io/explorer/)

| Channel 類型        | 是否支援 | 備註                                                         |
| ------------------- | -------- | ------------------------------------------------------------ |
| Emulator            | **O**    | Adaptive Card 支援的版本為 **1.3**                           |
| Web Chat            | **O**    | Adaptive Card 支援的版本為 **1.4**                           |
| iota                | **O**    | Adaptive Card 支援的版本為 **1.5**                           |
| LINE                | **X**    |                                                              |
| Teams               | **O**    | 1. Adaptive Card 支援的版本為 **1.1**<br />2. 不支援 Audio 和 Video 等元件 |
| Slack               | **X**    |                                                              |
| Webex               | **O**    | 1. Adaptive Card 支援的版本為 **1.3**<br />2. 按鈕數量最多5個 |
| Facebook Messenger  | **X**    |                                                              |
| Telegram            | **X**    |                                                              |
| M+                  | **X**    |                                                              |
| WeChat (微信個人號) | **X**    |                                                              |
| WeCom (企業微信)    | **X**    |                                                              |
| DingTalk            | **X**    |                                                              |
| Apple Business Chat | **X**    |                                                              |



---

## ◆ [Adaptive Fact Card](AdaptiveCards/FactCardContent.md)

> 明細卡片 (Adaptive Card)

> [Adaptive Card 文件](https://adaptivecards.io/explorer/)

| Channel 類型        | 是否支援 | 備註                                                         |
| ------------------- | -------- | ------------------------------------------------------------ |
| Emulator            | **O**    | Adaptive Card 支援的版本為 **1.3**                           |
| Web Chat            | **O**    | Adaptive Card 支援的版本為 **1.4**                           |
| iota                | **O**    | Adaptive Card 支援的版本為 **1.5**                           |
| LINE                | **O**    | 實作上會的轉成 LINE Flex Message                             |
| Teams               | **O**    | 1. Adaptive Card 支援的版本為 **1.1**<br />2. 不支援 Audio 和 Video 等元件 |
| Slack               | **X**    | 計畫中...                                                    |
| Webex               | **O**    | 1. Adaptive Card 支援的版本為 **1.3**<br />2. 按鈕數量最多5個 |
| Facebook Messenger  | **X**    |                                                              |
| Telegram            | **X**    |                                                              |
| M+                  | **X**    |                                                              |
| WeChat(微信個人號)  | **X**    |                                                              |
| WeCom (企業微信)    | **X**    |                                                              |
| DingTalk            | **X**    |                                                              |
| Apple Business Chat | **X**    |                                                              |



---

## ◆ [Adaptive List Card](AdaptiveCards/ListCardContent.md)

> 清單卡片 (Adaptive Card)

> [Adaptive Card 文件](https://adaptivecards.io/explorer/)

| Channel 類型        | 是否支援 | 備註                                                         |
| ------------------- | -------- | ------------------------------------------------------------ |
| Emulator            | **O**    | Adaptive Card 支援的版本為 **1.3**                           |
| Web Chat            | **O**    | Adaptive Card 支援的版本為 **1.4**                           |
| iota                | **O**    | Adaptive Card 支援的版本為 **1.5**                           |
| LINE                | **O**    | 實作上會的轉成 LINE Flex Message                             |
| Teams               | **O**    | 1. Adaptive Card 支援的版本為 **1.1**<br />2. 不支援 Audio 和 Video 等元件 |
| Slack               | **X**    | 計畫中...                                                    |
| Webex               | **O**    | 1. Adaptive Card 支援的版本為 **1.3**<br />2. 按鈕數量最多5個 |
| Facebook Messenger  | **X**    |                                                              |
| Telegram            | **X**    |                                                              |
| M+                  | **X**    |                                                              |
| WeChat(微信個人號)  | **X**    |                                                              |
| WeCom (企業微信)    | **X**    |                                                              |
| DingTalk            | **X**    |                                                              |
| Apple Business Chat | **X**    |                                                              |



---

## ◆ [Adaptive Grid Card](AdaptiveCards/GridCardContent.md)

> 表格卡片 (Adaptive Card)

> [Adaptive Card 文件](https://adaptivecards.io/explorer/)

| Channel 類型        | 是否支援 | 備註                                                         |
| ------------------- | -------- | ------------------------------------------------------------ |
| Emulator            | **O**    | Adaptive Card 支援的版本為 **1.3**                           |
| Web Chat            | **O**    | Adaptive Card 支援的版本為 **1.4**                           |
| iota                | **O**    | Adaptive Card 支援的版本為 **1.5**                           |
| LINE                | **O**    | 實作上會的轉成 LINE Flex Message                             |
| Teams               | **O**    | 1. Adaptive Card 支援的版本為 **1.1**<br />2. 不支援 Audio 和 Video 等元件 |
| Slack               | **X**    |                                                              |
| Webex               | **O**    | 1. Adaptive Card 支援的版本為 **1.3**<br />2. 按鈕數量最多5個 |
| Facebook Messenger  | **X**    |                                                              |
| Telegram            | **X**    |                                                              |
| M+                  | **X**    |                                                              |
| WeChat(微信個人號)  | **X**    |                                                              |
| WeCom (企業微信)    | **X**    |                                                              |
| DingTalk            | **X**    |                                                              |
| Apple Business Chat | **X**    |                                                              |



---

## ◆ [Adaptive Form Card](AdaptiveCards/FormCardContent,md)

> 表單卡片、問卷卡片 (Adaptive Card)

> [Adaptive Card 文件](https://adaptivecards.io/explorer/)

| Channel 類型        | 是否支援 | 備註                                                         |
| ------------------- | -------- | ------------------------------------------------------------ |
| Emulator            | **O**    | Adaptive Card 支援的版本為 **1.3**                           |
| Web Chat            | **O**    | Adaptive Card 支援的版本為 **1.4**                           |
| iota                | **O**    | Adaptive Card 支援的版本為 **1.5**                           |
| LINE                | **X**    |                                                              |
| Teams               | **O**    | 1. Adaptive Card 支援的版本為 **1.1**<br />2. 不支援 Audio 和 Video 等元件 |
| Slack               | **X**    |                                                              |
| Webex               | **O**    | 1. Adaptive Card 支援的版本為 **1.3**<br />2. 按鈕數量最多5個 |
| Facebook Messenger  | **X**    |                                                              |
| Telegram            | **X**    |                                                              |
| M+                  | **X**    |                                                              |
| WeChat (微信個人號) | **X**    |                                                              |
| WeCom (企業微信)    | **X**    |                                                              |
| DingTalk            | **X**    |                                                              |
| Apple Business Chat | **X**    |                                                              |



---

## ◆ [LINE Flex Message](LineFlexMessageContent.md)、[LINE Template Flex Message](FlexMessages/LineFlexTemplateCardContent.md)

> 自訂卡片 (LINE Flex Message)、範本卡片 (LINE Template Flex Message)

> [LINE Flex Message 文件](https://developers.line.biz/en/reference/messaging-api/#message-objects)

| Channel 類型        | 是否支援 | 備註 |
| ------------------- | -------- | ---- |
| Emulator            | **X**    |      |
| Web Chat            | **X**    |      |
| iota                | **X**    |      |
| LINE                | **O**    |      |
| Teams               | **X**    |      |
| Slack               | **X**    |      |
| Webex               | **X**    |      |
| Facebook Messenger  | **X**    |      |
| Telegram            | **X**    |      |
| M+                  | **X**    |      |
| WeChat (微信個人號) | **X**    |      |
| WeCom (企業微信)    | **X**    |      |
| DingTalk            | **X**    |      |
| Apple Business Chat | **X**    |      |



---

## ◆ [LINE Flex Fact Card](FlexMessages/LineFlexFactCardContent.md)

> 明細卡片 (LINE Flex Message)

> [LINE Flex Message 文件](https://developers.line.biz/en/reference/messaging-api/#message-objects)

| Channel 類型        | 是否支援 | 備註                                                  |
| ------------------- | -------- | ----------------------------------------------------- |
| Emulator            | **O**    | 實作上會轉成 Adaptive Card                            |
| Web Chat            | **O**    | 實作上會轉成 Adaptive Card                            |
| iota                | **O**    | 實作上會轉成 Adaptive Card                            |
| LINE                | **O**    |                                                       |
| Teams               | **O**    | 實作上會轉成 Adaptive Card                            |
| Slack               | **X**    | 計畫中...                                             |
| Webex               | **O**    | 1. 實作上會轉成 Adaptive Card<br />2. 按鈕數量最多5個 |
| Facebook Messenger  | **X**    |                                                       |
| Telegram            | **X**    |                                                       |
| M+                  | **X**    |                                                       |
| WeChat (微信個人號) | **X**    |                                                       |
| WeCom (企業微信)    | **X**    |                                                       |
| DingTalk            | **X**    |                                                       |
| Apple Business Chat | **X**    |                                                       |



---

## ◆ [LINE Flex List Card](LineFlexListCardContent)

> 清單卡片 (LINE Flex Message)

> [LINE Flex Message 文件](https://developers.line.biz/en/reference/messaging-api/#message-objects)

| Channel 類型        | 是否支援 | 備註                                                  |
| ------------------- | -------- | ----------------------------------------------------- |
| Emulator            | **O**    | 實作上會轉成 Adaptive Card                            |
| Web Chat            | **O**    | 實作上會轉成 Adaptive Card                            |
| iota                | **O**    | 實作上會轉成 Adaptive Card                            |
| LINE                | **O**    |                                                       |
| Teams               | **O**    | 實作上會轉成 Adaptive Card                            |
| Slack               | **X**    | 計畫中...                                             |
| Webex               | **O**    | 1. 實作上會轉成 Adaptive Card<br />2. 按鈕數量最多5個 |
| Facebook Messenger  | **X**    |                                                       |
| Telegram            | **X**    |                                                       |
| M+                  | **X**    |                                                       |
| WeChat (微信個人號) | **X**    |                                                       |
| WeCom (企業微信)    | **X**    |                                                       |
| DingTalk            | **X**    |                                                       |
| Apple Business Chat | **X**    |                                                       |



---

## ◆ [LINE Flex Grid Card](FlexMessages/LineFlexGridCardContent.md)

> 表格卡片 (LINE Flex Message)

> [LINE Flex Message 文件](https://developers.line.biz/en/reference/messaging-api/#message-objects)

| Channel 類型        | 是否支援 | 備註                                                  |
| ------------------- | -------- | ----------------------------------------------------- |
| Emulator            | **O**    | 實作上會轉成 Adaptive Card                            |
| Web Chat            | **O**    | 實作上會轉成 Adaptive Card                            |
| iota                | **O**    | 實作上會轉成 Adaptive Card                            |
| LINE                | **O**    |                                                       |
| Teams               | **O**    | 實作上會轉成 Adaptive Card                            |
| Slack               | **X**    |                                                       |
| Webex               | **O**    | 1. 實作上會轉成 Adaptive Card<br />2. 按鈕數量最多5個 |
| Facebook Messenger  | **X**    |                                                       |
| Telegram            | **X**    |                                                       |
| M+                  | **X**    |                                                       |
| WeChat (微信個人號) | **X**    |                                                       |
| WeCom (企業微信)    | **X**    |                                                       |
| DingTalk            | **X**    |                                                       |
| Apple Business Chat | **X**    |                                                       |



---

## ◆ [Event](EventContent.md)

> 互動事件

| Channel 類型        | 是否支援 | 備註 |
| ------------------- | -------- | ---- |
| Emulator            | **X**    |      |
| Web Chat            | **O**    |      |
| iota                | **X**    |      |
| LINE                | **X**    |      |
| Teams               | **X**    |      |
| Slack               | **X**    |      |
| Webex               | **X**    |      |
| Facebook Messenger  | **X**    |      |
| Telegram            | **X**    |      |
| M+                  | **X**    |      |
| WeChat (微信個人號) | **X**    |      |
| WeCom (企業微信)    | **X**    |      |
| DingTalk            | **X**    |      |
| Apple Business Chat | **X**    |      |



---

## ◆ [Carousel Card](CarouselContent.md)

> Carousel 卡片排版

| Channel 類型        | 是否支援 | 備註            |
| ------------------- | -------- | --------------- |
| Emulator            | **O**    |                 |
| Web Chat            | **O**    |                 |
| iota                | **O**    | 舊版 iota不支援 |
| LINE                | **O**    |                 |
| Teams               | **O**    |                 |
| Slack               | **X**    |                 |
| Webex               | **X**    |                 |
| Facebook Messenger  | **O**    |                 |
| Telegram            | **X**    |                 |
| M+                  | **X**    |                 |
| WeChat (微信個人號) | **X**    |                 |
| WeCom (企業微信)    | **X**    |                 |
| DingTalk            | **X**    |                 |
| Apple Business Chat | **X**    |                 |

