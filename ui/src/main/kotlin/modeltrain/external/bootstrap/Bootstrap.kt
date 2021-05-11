package modeltrain.external.bootstrap

external interface Bootstrap {
    @JsName("Dropdown")
    val dropdown: Dropdown

    @JsName("Button")
    val button: Button

    @JsName("ToggleButton")
    val toggleButton: ToggleButton

    @JsName("ButtonGroup")
    val buttonGroup: ButtonGroup

    @JsName("ToggleButtonGroup")
    val toggleButtonGroup: ToggleButtonGroup
}

@JsModule("react-bootstrap")
@JsNonModule
external val bootstrap: Bootstrap
