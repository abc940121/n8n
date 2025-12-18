# MediaSourceContent

>  按鈕設定

## ◆ Schema

| 屬性         | 資料型態 | 必要屬性 | 描述                          | 支援變數 | 版本 |
| ------------ | -------- | -------- | ----------------------------- | -------- | ---- |
| Url          | string   | Y        | 影片或音樂連結                | **O**    | 1.0  |
| ThumbnailUrl | string   | `[1]`    | 預覽圖片                      | **O**    | 1.0  |
| AutoStart    | boolean  | N        | 是否自動播放，預設值為`false` | **X**    | 1.0  |

* `[1]` 部分支援影片的 Channel  可能需要預覽圖片



## ◆ Example

* **音樂，建議格式：mp3、wav**

```json
{
    "Url": "https://www.gss.com.tw/audio.mp3"
}
```

* **影片，建議格式：mp4、wmv、YouTube**

```json
{
    "Url": "https://www.youtube.com/watch?v=8UsaBBrrL7c"
}
```

