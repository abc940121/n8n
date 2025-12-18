# Adaptive Card Release Note

## v1.0 Changelog

* Initialize



---

## v1.1 Changelog

* **Cards**
    * AdaptiveCard
        * selectAction
* **Card Elements**
    * Image
        * backgroundColor
        * height
        * selectAction
        * width
        * style
            * person
        * url.data
    * Media `(new)`
    * MediaSource `(new)`
* **Containers**
    * Container
        * selectAction
        * verticalContentAlignment
    * ColumnSet 
        * selectAction
    * Column
        * selectAction
* **Actions**
    * Action.OpenUrl
        * iconUrl
    * Action.Submit
        * iconUrl
    * Action.ShowCard
        * iconUrl

## v1.2 Changelog

* **Cards**
    * Adaptive Card
        * fillMode
        * minHeight
* **Card Elements**
    * TextBlock
        * fontType
    * RichTextBlock `(new)`
* **Containers**
    * Container
        * style
        * minHeight
        * bleed
    * ColumnSet
        * style
        * minHeight
        * bleed
    * Column
        * minHeight
        * bleed
    * ActionSet `(new)`
    * ActionFallback `(new)`
* **Actions**
    * Action.OpenUrl
        * style
    * Action.Submit
        * style
    * Action.ShowCard
        * style
    * Action.ToggleVisibility `(new)`
* **Inputs**
    * Input.Text
        * inlineAction



## v1.3 Changelog

> **主要著重在 Input 的資料檢查**

* **AdaptiveCard**
    * ~~style~~ `(remove)`
* **Actions**
    * Action.Submit
        * ignoreInputValidation `(new)`
* **Inputs**
    * label `(new)`
    * isRequired `(new)`
    * errorMessage `(new)`
    * Input.Text 
        * regex `(new)`



## v1.4 Changelog

* **Actions**
    * Action.Execute