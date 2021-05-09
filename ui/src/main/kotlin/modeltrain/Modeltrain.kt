package modeltrain

import react.dom.*
import kotlinx.browser.document
import kotlinx.html.js.onClickFunction
import kotlin.js.Date

fun Date.printDate(): String {
    val year = this.getFullYear()
    val month = this.getMonth() + 1
    val day = this.getDate()

    return "$day.$month.$year"
}


fun main() {
    document.bgColor = "blue"
    render(document.getElementById("root")) {
        h1 {
            +"Hello World!"
        }
        p {
            +Date().printDate()
            button {
                attrs.onClickFunction = { println("Button was clicked") }
                +"Click me"
            }
        }
    }
}