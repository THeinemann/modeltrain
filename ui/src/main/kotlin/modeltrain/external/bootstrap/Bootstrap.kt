package modeltrain.external.bootstrap

external interface Bootstrap {
    @JsName("Dropdown")
    val dropdown: Dropdown
}

@JsModule("react-bootstrap")
@JsNonModule
external val bootstrap: Bootstrap
