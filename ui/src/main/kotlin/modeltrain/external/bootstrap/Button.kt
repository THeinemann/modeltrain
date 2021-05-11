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


external interface ButtonGroupProps : RProps {
    var toggle: Boolean
}

external interface ButtonGroup : RClass<ButtonGroupProps>

external interface ToggleButtonProps : ButtonProps {
    var value: dynamic
    var name: String
}

external interface ToggleButton : RClass<ToggleButtonProps>

external interface ToggleButtonGroupProps : RProps {
    var type: String
    var onChange: (dynamic) -> Unit
    var name: String
}

external interface ToggleButtonGroup : RClass<ToggleButtonGroupProps>