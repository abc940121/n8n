# Channel Data Payload

* **注意事項**
    * **Channel Data Payload 必須是一個有效的值或是指定變數**
    * **指定變數的值也必須是一個有效的值**
    * **Channel Data Payload的值會放到 Channel Data 的 `data` 之下**



## ◆ 有效的 Channel Data Payload

### ● 物件

* **Schema**

```json
{
    "Type": "",
    "QuickReply": [],
    "ChannelDataPayload": {
        "Name": "ShowSatisfaction",
        "Data": {
            "Name": "Show Satisfaction Button"
        }
    }
}
```

* **實際產生的 Channel Data 內容**

```json
{
    "ChannelData": {
        "data": {
            "Name": "ShowSatisfaction",
            "Data": {
                "Name": "Show Satisfaction Button"
            }
        }
    }
}
```



### ● 陣列

* **Schema**

```json
{
    "Type": "",
    "QuickReply": [],
    "ChannelDataPayload": [
        "Apple",
        "Pen",
        "Pineapple"
    ]
}
```

* **實際產生的 Channel Data 內容**

```json
{
    "ChannelData": {
        "data":  [
            "Apple",
            "Pen",
            "Pineapple"
        ]
    }
}
```



### ● 字串

* **Schema**

```json
{
    "Type": "",
    "QuickReply": [],
    "ChannelDataPayload": "Hello World"
}
```

* **實際產生的 Channel Data 內容**

```json
{
    "ChannelData": {
        "data": "Hello World"
    }
}
```



### ● 數字

* **Schema**

```json
{
    "Type": "",
    "QuickReply": [],
    "ChannelDataPayload": 655
}
```

* **實際產生的 Channel Data 內容**

```json
{
    "ChannelData": {
        "data":  655
    }
}
```



### ● 指定的變數

* **變數名稱** ─ `$.Variables.LeaveInfo`

```json
{
    "Applicant": "張三",
    "LeaveType": "特休假",
    "StartDate": "2019-12-11 09:00",
    "LeaveHours": "8",
    "Subject": "特休"
}
```

* **Example**

```json
{
    "Type": "",
    "QuickReply": [],
    "ChannelDataPayload": "$.Variables.LeaveInfo"
}
```

* **實際產生的 Channel Data 內容**

```json
{
    "ChannelData": {
        "data": {
            "Applicant": "張三",
            "LeaveType": "特休假",
            "StartDate": "2019-12-11 09:00",
            "LeaveHours": "8",
            "Subject": "特休"
        }
    }
}
```



---

## ◆ 無效的 Channel Data Payload

### ● 空物件、空陣列、空字串

* **Schema**

```json
{
    "Type": "",
    "QuickReply": [],
    "ChannelDataPayload": {}
}
```

```json
{
    "Type": "",
    "QuickReply": [],
    "ChannelDataPayload": null
}
```

```json
{
    "Type": "",
    "QuickReply": [],
    "ChannelDataPayload": []
}
```

```json
{
    "Type": "",
    "QuickReply": [],
    "ChannelDataPayload": ""
}
```

* **實際產生的 Channel Data 內容**

```json
{
    "ChannelData": {
        "data": null
    }
}
```



---

### ● 無效的變數值

> * 變數值為 Null
> * 變數值為空物件
> * 變數值為空陣列
> * 變數值為空字串
> * 變數不存在



* **變數名稱** ─ `$.Variables.UserProfile`

```json
{}
```

* **變數名稱** ─ `$.Variables.Items`

```json
[]
```

* **變數名稱** ─ `$.Variables.GreetingText`

```json
""
```



* **Invalid Schema**

```json
{
    "Type": "",
    "QuickReply": [],
    "ChannelDataPayload": "$.Variables.UserProfile"
}
```

```json
{
    "Type": "",
    "QuickReply": [],
    "ChannelDataPayload": "$.Variables.Items"
}
```

```json
{
    "Type": "",
    "QuickReply": [],
    "ChannelDataPayload": "$.Variables.GreetingText"
}
```

```json
{
    "Type": "",
    "QuickReply": [],
    "ChannelDataPayload": "$.Variables.Wft"
}
```

* **實際產生的 Channel Data 內容**

```json
{
    "ChannelData": {
        "data": null
    }
}
```



