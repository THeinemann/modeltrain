package modeltrain.external.bootstrap

import org.w3c.dom.events.Event
import react.RClass
import react.RProps

external interface ButtonProps : RProps {
    var variant: String

    @JsName("onClick")
    var onClickFunction: (Event) -> Unit
}

external interface Button : RClass<ButtonProps>