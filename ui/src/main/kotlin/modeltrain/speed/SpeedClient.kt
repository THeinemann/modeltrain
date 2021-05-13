package modeltrain.speed

import kotlinx.browser.window
import modeltrain.common.Headers
import org.w3c.fetch.RequestInit

class SpeedClient {
    @ExperimentalUnsignedTypes
    fun setSpeed(speed: UByte) {
        val json = speed.toString()
        val headers = Headers {
            contentType("application/json")
        }

        window.fetch("/speed", RequestInit(
                method = "PUT",
                body = json,
                headers = headers
        ))
    }
}