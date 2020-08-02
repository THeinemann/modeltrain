import kotlin.browser.document
import kotlin.js.Date

fun Date.printDate(): String {
    val year = this.getFullYear()
    val month = this.getMonth() + 1
    val day = this.getDate()

    return "$day.$month.$year"
}

fun main() {
    document.bgColor = "blue"
    val root = document.getElementById("root")
    if (root != null) {
        root.innerHTML = "<h1>Hello World!</h1> <div>" + (Date()).printDate() + "</div>"
    }
    println("Hello World!")
}