package modeltrain.common

import kotlin.js.Json
import kotlin.js.json

object Headers {
    class HeaderBuilder {
        private val values: MutableMap<String, String> = HashMap()

        fun contentType(ct: String) {
            values["Content-Type"] = ct
        }

        operator fun set(key: String, value: Any) {
            values[key] = value.toString()
        }


        fun build(): Json {
            val headerValues: Array<Pair<String, String>> = values
                    .map { entry -> Pair(entry.key, entry.value) }
                    .toTypedArray()

            return json(*headerValues)
        }
    }

    operator fun invoke(handler: HeaderBuilder.() -> Unit): Json {
        val hb = HeaderBuilder()
        hb.handler()
        return hb.build()
    }
}