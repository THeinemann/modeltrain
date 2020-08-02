package modeltrain

import kotlin.browser.document
import kotlin.js.Date
import kotlinx.html.*
import kotlinx.html.dom.*

fun Date.printDate(): String {
    val year = this.getFullYear()
    val month = this.getMonth() + 1
    val day = this.getDate()

    return "$day.$month.$year"
}

@JsName("onButtonClick")
fun onButtonClick() {
    println("Button was clicked")
}


fun main() {
    document.bgColor = "blue"
    val root = document.getElementById("root")
    root?.append {
        div {
            h1 {
                +"Hello World"
            }
            p {
                +Date().printDate()
                button {
                    onClick="ui.modeltrain.onButtonClick()"
                    +"Click me"
                }
            }
        }
    }
    println("Hello World!")
}