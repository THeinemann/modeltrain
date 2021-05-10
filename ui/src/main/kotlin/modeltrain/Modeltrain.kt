package modeltrain

import kotlinx.css.*
import modeltrain.direction.DirectionClient
import modeltrain.direction.directions
import modeltrain.sections.SectionClient
import modeltrain.sections.sections
import modeltrain.switches.SwitchClient
import modeltrain.switches.switches
import react.*
import styled.css
import styled.styledDiv
import styled.styledH1
import kotlin.js.Date

fun Date.printDate(): String {
    val year = this.getFullYear()
    val month = this.getMonth() + 1
    val day = this.getDate()

    return "$day.$month.$year"
}

val modeltrains = rFunction<RProps>("App") {
    val tableStyle: CSSBuilder.() -> Unit = {
        display = Display.flex
        float = Float.left
        width = LinearDimension("48%")
    }

    styledDiv {
        styledH1 {
            css {
                textAlign = TextAlign.center
            }
            +"Model train control"
        }
        styledDiv {
            css {
                textAlign = TextAlign.center
            }
            directions {
                directionClient = DirectionClient()
            }
        }
        styledDiv {
            styledDiv {
                css(tableStyle)
                switches {
                    switchClient = SwitchClient()
                }
            }
            styledDiv {
                css(tableStyle)
                sections {
                    sectionClient = SectionClient()
                }
            }
        }


    }
}

fun RBuilder.App() = modeltrains.invoke {
}