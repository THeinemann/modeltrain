package modeltrain.direction

import modeltrain.external.bootstrap.Variant
import modeltrain.external.bootstrap.bootstrap
import react.*

external interface DirectionsProps : RProps {
    var directionClient: DirectionClient
}
external interface DirectionsState : RState {
    var direction: Direction?
}

class Directions(props: DirectionsProps) : RComponent<DirectionsProps, DirectionsState>(props) {
    val toggleButtonGroup = bootstrap.toggleButtonGroup
    val toggleButton = bootstrap.toggleButton

    override fun RBuilder.render() {

        toggleButtonGroup {
            attrs {
                type = "radio"
                name = "direction"
                onChange = { dir -> props.directionClient.setDirection(dir.unsafeCast<Direction>()) }
            }
            toggleButton {
                +"Forward"
                attrs {
                    name = "forward"
                    value = Direction.Forward
                    variant = Variant.WARNING
                }
            }
            toggleButton {
                +"Backward"
                attrs {
                    name = "backward"
                    value = Direction.Backward
                    variant = Variant.WARNING
                }
            }
        }
    }
}

fun RBuilder.directions(handler: DirectionsProps.() -> Unit): ReactElement {
    return child(Directions::class) {
        this.attrs(handler)
    }
}