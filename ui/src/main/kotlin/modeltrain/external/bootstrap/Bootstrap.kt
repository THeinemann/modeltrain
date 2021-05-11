package modeltrain.external.bootstrap

external interface Bootstrap {
    @JsName("Dropdown")
    val dropdown: Dropdown

    @JsName("Button")
    val button: Button
}

@JsModule("react-bootstrap")
@JsNonModule
external val bootstrap: Bootstrap
