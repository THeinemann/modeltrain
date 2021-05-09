import kotlinx.browser.document
import modeltrain.App
import react.dom.render

fun main() {
    render(document.getElementById("root")) {
        App()
    }
}