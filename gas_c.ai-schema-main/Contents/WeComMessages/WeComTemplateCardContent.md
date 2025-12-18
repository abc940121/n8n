# WeCom Template Card

> 企業微信模板卡片

* 自訂 WeCom 模板卡片內容
* **[支援的模板卡片類型](https://developer.work.weixin.qq.com/document/path/90236#%E6%A8%A1%E6%9D%BF%E5%8D%A1%E7%89%87%E6%B6%88%E6%81%AF)**
    * [文字通知型](https://developer.work.weixin.qq.com/document/path/90236#%E6%96%87%E6%9C%AC%E9%80%9A%E7%9F%A5%E5%9E%8B)
    * [圖文通知型](https://developer.work.weixin.qq.com/document/path/90236#%E5%9B%BE%E6%96%87%E5%B1%95%E7%A4%BA%E5%9E%8B)
    * [按鈕互動型](https://developer.work.weixin.qq.com/document/path/90236#%E6%8C%89%E9%92%AE%E4%BA%A4%E4%BA%92%E5%9E%8B)
    * [投票選擇型](https://developer.work.weixin.qq.com/document/path/90236#%E6%8A%95%E7%A5%A8%E9%80%89%E6%8B%A9%E5%9E%8B)
    * [多項選擇型](https://developer.work.weixin.qq.com/document/path/90236#%E5%A4%9A%E9%A1%B9%E9%80%89%E6%8B%A9%E5%9E%8B)



## ◆ Screenshot

![](https://wework.qpic.cn/wwpic/235797_QOJtTyeUTBuAk_G_1632907465/0)

![](https://wework.qpic.cn/wwpic/93182_HHrOrbdjTNW9ieM_1632907497/0)

![](https://wework.qpic.cn/wwpic/102736_wYaFgfHsRIOPzL1_1632907528/0)

![](https://wework.qpic.cn/wwpic/822424_UiGowMtcSD-EyEq_1628758117/0)

![](https://wework.qpic.cn/wwpic/977007_JDisThiPRXam-GG_1628758163/0)



## ◆ Schema

繼承自 [MessageContent](MessageContent.md)

| 屬性        | 資料型態 | 必要屬性 | 描述                                                         | 支援變數 | 版本 |
| ----------- | -------- | -------- | ------------------------------------------------------------ | -------- | ---- |
| *Type*      | string   | Y        | 類型，值為 `wecom.card.template`                             | **X**    | 1.21 |
| **Content** | string   | Y        | 模板卡片內容，JSON 字串，只需要放 `template_card` 的 JSON 內容 | **O**    | 1.21 |



---

## ◆ Example



```json
{
    "Type": "wecom.card.template",
    "Content": "{\"card_type\":\"vote_interaction\",\"main_title\":{\"title\":\"Title\",\"desc\":\"Subtitle\"},\"task_id\":\"655\",\"checkbox\":{\"question_key\":\"key\",\"option_list\":[{\"id\":\"value1\",\"text\":\"Value 1\",\"is_checked\":false},{\"id\":\"value2\",\"text\":\"Value 2\",\"is_checked\":false}],\"mode\":1},\"submit_button\":{\"text\":\"Submit\",\"key\":\"Submit\"}}"
}
```



