package modeltrain.direction

import kotlinx.browser.window
import modeltrain.common.Headers
import org.w3c.fetch.RequestInit

enum class Direction(private val value: String) {
    Forward("forward"), Backward("backward");

    override fun toString(): String {
        return value
    }
}

class DirectionClient {
    fun setDirection(direction: Direction) {
        val json = JSON.stringify(direction.toString())
        val headers = Headers {
            contentType("application/json")
        }

        window.fetch("/direction", RequestInit(
                method = "PUT",
                body = json,
                headers = headers
        ))
    }
}