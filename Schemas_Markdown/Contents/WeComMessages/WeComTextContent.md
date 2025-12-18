# WeCom Text Content

> 靜態的文字訊息、Markdown 訊息



## ◆ Screenshot  

* **純文字**

![](https://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_msg$5bc63c26.png)

* **Markdown 文字**

![](http://p.qpic.cn/pic_wework/1114461239/dddbcdd097e5f308248cd7f99e0ebb336975267b9348c4ec/0)



---

## ◆ Schema

繼承自 [MessageContent](MessageContent.md)

| 屬性           | 資料型態 | 必要屬性 | 描述                                 | 支援變數 | 版本 |
| -------------- | -------- | -------- | ------------------------------------ | -------- | ---- |
| *Type*         | string   | Y        | 類型，值為 `wecom.text`              | **X**    | 1.21 |
| **Text**       | string   | Y        | 文字內容，字數最多 **2048** 個字     | **O**    | 1.21 |
| **IsMarkdown** | boolean  | N        | 是否為 Markdown 格式，預設值：`true` | **X**    | 1.21 |



---

## ◆ Example

### ● 靜態文字

* **純文字**
    * 支援 HTML 連結的語法
    * 支援換行符號 `\n`

```json
{
    "Type": "wecom.text",
    "Text": "Hello Word\n<a href=\"https://www.gss.com.tw\">詳細</a>",
    "IsMarkdown": false
}
```

* **Markdown文字**

```json
{
    "Type": "wecom.text",
    "Text": "**Hello Word**\n> [詳細](https://www.gss.com.tw)",
    "IsMarkdown": true
}
```

* **Markdown 支援的語法**

```markdown
# 一級標題
## 二級標題
### 三級標題
#### 四級標題
##### 五級標題
###### 六級標題

**粗體**

[超連結](http://yoururl)

`等寬字型`

> 引文

<font color="info">綠色</font>
<font color="comment">灰色</font>
<font color="warning">橙色</font>
```



### ●  動態文字 (使用變數)

* 透過輸入 `{{變數名稱}}` 將變數的值帶入
* 變數可以[參考這裡](../Variables/Variable.md) 

```json
{
    "Type": "text",
    "Text": "Hello {{$.Conversation.UserName}}\n<a href=\"https://www.gss.com.tw\">詳細</a>",
    "IsMarkdown": false
}
```

```json
{
    "Type": "text",
    "Text": "Hello {{$.Conversation.UserName}}\n> [詳細](https://www.gss.com.tw)</a>",
    "IsMarkdown": true
}
```





