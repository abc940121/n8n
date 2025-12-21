# Slack Content

> 靜態的 Slack Block Card 訊息，僅適用於 Slack

* **LINE Flex Card Content 衍生類型**
    * **Slack List Content** ─ 清單卡片 (制式 Slack Card 訊息) `(計畫中)`
    * **Slack Form Card Content** ─ 表單卡片 (制式 Slack Card 訊息) `(計畫中)`
    * **Slack Template Card Content** ─ 範本卡片



## ◆ Channel Support

> [Slack Block Kit 文件](https://api.slack.com/reference/block-kit/blocks)

| Channel 類型            | 是否支援 | 備註 |
| ----------------------- | -------- | ---- |
| Emulator                | **X**    |      |
| Web Chat、iota Chat Bot | **X**    |      |
| iota                    | **X**    |      |
| LINE                    | **X**    |      |
| Teams                   | **X**    |      |
| Slack                   | **O**    |      |
| Webex                   | **X**    |      |
| Telegram                | **X**    |      |
| Facebook Messenger      | **X**    |      |
| WhatsApp                | **X**    |      |
| M+                      | **X**    |      |
| WeChat (微信個人號)     | **X**    |      |
| WeCom (企業微信)        | **X**    |      |
| DingTalk                | **X**    |      |
| Apple Business Chat     | **X**    |      |



## ◆ Schema

繼承 [MessageContent](MessageContent.md)

| 屬性        | 資料型態 | 必要屬性 | 描述                         | 支援變數 | 版本 |
| ----------- | -------- | -------- | ---------------------------- | -------- | ---- |
| *Type*      | string   | Y        | 類型，值為 `slack.blocks`    | **X**    | 1.0  |
| **Content** | string   | Y        | Slack Block Kit Json Content | **O**    | 1.2? |









