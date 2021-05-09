package modeltrain.switches

import kotlinx.browser.window
import kotlinx.coroutines.await
import org.w3c.fetch.RequestInit
import kotlin.js.Promise
import kotlin.js.json

enum class Direction(private val value: String) {
    Straight("straight"), Turn("turn");

    override fun toString(): String {
        return value
    }
}

class SwitchClient {
    suspend fun getSwitches(): List<Int> {
        val data: Array<Int> = window.fetch("/switches")
                .await()
                .json()
                .await()
                .asDynamic().data as Array<Int>


        return arrayListOf(*data)
    }

    fun setSwitch(id: Int, direction: Direction) {
        window.fetch("/switches/$id/$direction", RequestInit(
                method = "PUT"
        ))
    }
}