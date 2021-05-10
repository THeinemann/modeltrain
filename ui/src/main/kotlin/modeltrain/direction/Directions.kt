package modeltrain.direction

import modeltrain.external.bootstrap.bootstrap
import react.*

external interface DirectionsProps : RProps {
    var directionClient: DirectionClient
}
external interface DirectionsState : RState {
    var direction: Direction?
}

class Directions(props: DirectionsProps) : RComponent<DirectionsProps, DirectionsState>(props) {
    val dropdown = bootstrap.dropdown
    override fun RBuilder.render() {
        dropdown {
            attrs {
                onSelect = { direction, _ -> props.directionClient.setDirection(direction) }
            }
            dropdown.toggle {
                if (state.direction == null) {
                    +"Direction"
                } else {
                    +"${state.direction}"
                }
            }

            dropdown.menu {
                dropdown.item {
                    attrs {
                        eventKey = Direction.Forward
                    }
                    +"Forward"
                }
                dropdown.item {
                    attrs {
                        eventKey = Direction.Backward
                    }
                    +"Backward"
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