package modeltrain.common

import kotlin.js.Json
import kotlin.test.Test
import kotlin.test.assertEquals

class HeaderBuilderTest {

    @Test
    fun shouldBuildHeaders() {

        val headers: Json = Headers {
            contentType("application/json")
            this["blah"] = "blubb"
        }

        assertEquals("blubb", headers["blah"])
        assertEquals("application/json", headers["Content-Type"])
    }
}