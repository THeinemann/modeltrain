package modeltrain.switches

import kotlinx.coroutines.await
import kotlin.js.Promise

enum class Direction(private val value: String) {
    Straight("straight"), Turn("turn");

    override fun toString(): String {
        return value
    }
}

class SwitchClient {
    suspend fun getSwitches(): List<Int> {
        return Promise.resolve(arrayListOf(1, 2, 3, 4, 5))
                .await()
    }

    fun setSwitch(id: Int, direction: Direction) {
        println("Set switch $id to $direction")
    }
}