import kotlinx.browser.document
import modeltrain.App
import react.dom.render

fun main() {
    document.bgColor = "blue"
    render(document.getElementById("root")) {
        App()
    }
}