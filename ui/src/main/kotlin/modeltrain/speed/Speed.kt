package modeltrain.speed

import modeltrain.direction.Directions
import modeltrain.direction.DirectionsProps
import modeltrain.external.bootstrap.bootstrap
import react.*

external interface SpeedProps : RProps {
    var speedClient: SpeedClient
}

class Speed(props: SpeedProps) : RComponent<SpeedProps, RState>(props) {

    val steps: List<UByte> = (0..255 step 10).toList().map(Int::toUByte)

    override fun RBuilder.render() {
        val dropdown = bootstrap.dropdown

        dropdown {
            attrs {
                onSelect = { speed, _ ->
                    println(speed)
                    props.speedClient.setSpeed(speed.unsafeCast<UByte>())
                }
            }
            dropdown.toggle {
                +"Speed"
            }

            dropdown.menu {
                steps.map { speed ->
                    dropdown.item {
                        attrs { eventKey = speed }
                        +"$speed"
                    }
                }
            }
        }
    }
}

fun RBuilder.speed(handler: SpeedProps.() -> Unit): ReactElement {
    return child(Speed::class) {
        this.attrs(handler)
    }
}