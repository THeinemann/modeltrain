package modeltrain.external.bootstrap

import org.w3c.dom.events.Event
import react.*

external interface DropdownProps : RProps {
    var onSelect: (dynamic, Event) -> Unit
}
external interface DropdownToggleProps : RProps
external interface DropdownMenuProps : RProps
external interface DropdownItemProps : RProps {
    var eventKey: dynamic
}

external interface Dropdown : RClass<DropdownProps> {
    @JsName("Toggle")
    val toggle: RClass<DropdownToggleProps>

    @JsName("Menu")
    val menu: RClass<DropdownMenuProps>

    @JsName("Item")
    val item: RClass<DropdownItemProps>
}