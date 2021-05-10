package modeltrain.sections

import kotlinx.browser.window
import kotlinx.coroutines.await
import modeltrain.common.ArrayWrapper
import modeltrain.common.Headers
import org.w3c.fetch.RequestInit
import kotlin.js.Promise
import kotlin.js.json


class SectionClient {
    companion object {
        data class Section(val enabled: Boolean)
    }

    suspend fun getSections(): List<Int> {
        val data: Array<Int> = window.fetch("/sections")
                .await()
                .json()
                .await()
                .unsafeCast<ArrayWrapper<Int>>()
                .data

        return arrayListOf(*data)
    }

    fun setSection(id: Int, enabled: Boolean) {
        val json = JSON.stringify(Section(enabled))
        val headers = Headers {
            contentType("application/json")
        }

        window.fetch("/sections/$id", RequestInit(
                method = "PUT",
                body = json,
                headers = headers
        ))
    }
}
