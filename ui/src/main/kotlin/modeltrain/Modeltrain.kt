package modeltrain

import react.dom.*
import kotlinx.browser.document
import kotlinx.html.js.onClickFunction
import modeltrain.sections.SectionClient
import modeltrain.sections.sections
import react.*
import kotlin.js.Date

fun Date.printDate(): String {
    val year = this.getFullYear()
    val month = this.getMonth() + 1
    val day = this.getDate()

    return "$day.$month.$year"
}

val modeltrains = rFunction<RProps>("App") { props ->
    h1 {
        +"Hello World!"
    }
    p {
        sections {
            sectionClient = SectionClient()
        }
    }
}

fun RBuilder.App() = modeltrains.invoke {
}