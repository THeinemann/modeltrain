package modeltrain

import kotlinx.css.*
import react.dom.*
import modeltrain.sections.SectionClient
import modeltrain.sections.sections
import modeltrain.switches.SwitchClient
import modeltrain.switches.switches
import react.*
import styled.css
import styled.styledDiv
import kotlin.js.Date

fun Date.printDate(): String {
    val year = this.getFullYear()
    val month = this.getMonth() + 1
    val day = this.getDate()

    return "$day.$month.$year"
}

val modeltrains = rFunction<RProps>("App") { props ->
    val tableStyle: CSSBuilder.() -> Unit = {
        display = Display.flex
        float = Float.left
        width = LinearDimension("48%")
    }
    val split = 1500

    styledDiv {
        css {
            media("(min-width: ${split + 1}px)") {
                alignContent = Align.center
                width = LinearDimension("30%")
                marginLeft = LinearDimension.auto
                marginRight = LinearDimension.auto
            }

            media("(max-width: ${split}px)") {
                width = LinearDimension("100%")
                marginLeft = LinearDimension("0")
                marginRight = LinearDimension("0")

            }
        }

        h1 {
            +"Model train control"
        }
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

fun RBuilder.App() = modeltrains.invoke {
}