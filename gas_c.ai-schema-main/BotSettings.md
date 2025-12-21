# Bot Settings

> **Bot 系統設定，無法被對話流程使用**



| Setting Name                           | Description                | Version    |
| -------------------------------------- | -------------------------- | ---------- |
| **BotPluginSetting**                   | Bot Plugin (擴充套件) 設定 | 1.26       |
| **InfiniteDialogLoopDetectionSetting** | 無窮對話迴圈偵測設定       | 1.14       |
| **HttpClientSetting**                  | Http Client 相關設定       | 1.17       |
| **AdaptiveCardRenderSetting**          | Adaptive Card 版本參數     | **計畫中** |
| **MessageRenderSetting**               | 變數綁定相關參數           | **計畫中** |
| **LineMessageRenderSetting**           | Line Message 參數          | **計畫中** |



```json
{
    "BotSettings": [
        {
            "Name": "BotPluginSetting"
        },
        {
            "Name": "InfiniteDialogLoopDetectionSetting"
        },
        {
            "Name": "HttpClientSetting"
        }
    ]
}
```



---

## ◆ Bot Plugin Setting

> * **Bot Plugin 設定，Plugin 的啟用和停用由 [appsettings.json 上的 擴充套件 (Plugins)](../AppSetting.md#7-擴充套件-plugins) 搬移到這裡**
>     * Plugin 的啟用和停用完全由各個 Bot 自己管理
>     * 對於舊版的相容：未設定這個設定 (值為 Null) 時仍會使用 [appsettings.json 上的 擴充套件 (Plugins)](../AppSetting.md#7-擴充套件-plugins) 

* **Name** ： Bot Setting 名稱，值為：`BotPluginSetting`
* **Plugins** ： 引用的 Bot Plugin 與其啟用狀態，**`appsettings.json` 仍需設定的 Plugin 目錄，且該目錄下指定的 Plugin 也必須存在**
    * **Id** ─ Plugin ID，而 Key 提供 [Custom Dialog Node](Schema/Nodes/Custom/CustomDialog.md) 使用
    * **IsEnabled** ─ 是否啟用

```json
{
    "BotSettings": [
        {
            "Name": "BotPluginSetting",
            "Plugins": [
                {
                    "Id": "DemoDialog",
                    "IsEnabled": true
                },
                {
                    "Id": "GssCaiDialog",
                    "IsEnabled": true
                }
            ]
        }
    ]
}
```

* **Plugin 引用/啟用真值表**
    * **Plugin A** ─ 有安裝在 Plugin 目錄下
    * **Plugin B** ─ 沒有安裝在 Plugin 目錄下

| Bot Plugin Setting 設定 | Plugin A           | Plugin B |
| ----------------------- | ------------------ | -------- |
| **未引用 (沒有設定)**   | :x:                | :x:      |
| **已引用、啟用**        | :heavy_check_mark: | :x:      |
| **已引用、停用**        | :x:                | :x:      |



---

## ◆ Infinite Dialog Loop Detection Setting

> **無窮迴圈設定，會覆寫掉 [appsettings.json 上的無窮迴圈設定](../AppSetting.md#9-無窮對話迴圈偵測設定)**



* **Name** ： Bot Setting 名稱，值為：`InfiniteDialogLoopDetectionSetting`
* **MaxNodeAccessCountPerTurn**
    * 在1個 Bot 與 User 對話回合中，每個節點最大訪問次數
    * **`設定值必須大於或等於 1`**，大於這個數值即被認定為無窮對話迴圈
    * 對話節點的訪問次數計算會在特定條件下重置 (歸零)：
        * 當 Bot 等待 User 輸入，會重置每個節點的訪問次數
        * 當某個對話流程結束時，會重置該對話流程的每個節點的訪問次數
    * 這一個設定僅適用於這一個 Bot (Bot Script)
        * 與 appsettings.json 上的設定差別是 appsettings.json 上的設定適用於所有的 Bot (Bot Script)
* **SpecialOptions**
    * 為特例的對對象個別設定最大訪問次數
    * **Node** ：為指定的 Node 設定最大訪問次數
    * **Flow** ：為指定的 Flow 底下的 Node 設定最大訪問次數

> 覆寫順序： **appsettings.json** > **Bot** > **Flow** > **Node**



```json
{
    "BotSettings": [
        {
            "Name": "InfiniteDialogLoopDetectionBotSetting",
            "MaxNodeAccessCountPerTurn": 1,
            "NodeSettings": [
                {
                    "Items": [ "node_A0002" ],
                    "MaxNodeAccessCountPerTurn": 3
                }
            ],
            "FlowSettings": [
                {
                    "Items": [ "flow_00004A", "flow_00004B" ],
                    "MaxNodeAccessCountPerTurn": 2
                }
            ]
        }
    ]
}
```



---

## ◆ Http Client Setting

> **Http Client 相關設定**

* **Name** ： Bot Setting 名稱，值為：`HttpClientSetting`
* **CertificateValidation** ： 是否啟用憑證檢查，預設值：`true` (啟用)
    * `true` : 啟用憑證檢查
    * `false` : 停用憑證檢查

```json
{
    "BotSettings": [
        {
            "Name": "HttpClientSetting",
            "CertificateValidation": true
        }
    ]
}
```





---

## ◆ Adaptive Card Render Setting

> **計畫中...**



## ◆ Message Data Render Setting

> **計畫中...**



## ◆ Line Message Render Setting

> **尚無任何計畫**



