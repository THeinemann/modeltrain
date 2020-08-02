import kotlin.test.Test
import kotlin.js.Date

import kotlin.test.assertEquals

class MainTest {
    @Test
    fun shouldPrintDateCorrectly() {
        assertEquals("5.3.2019", Date("2019-03-05").printDate())
    }
}