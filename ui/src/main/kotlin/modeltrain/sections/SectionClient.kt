package modeltrain.sections

import kotlinx.coroutines.await
import kotlin.js.Promise


class SectionClient {
    companion object {
        data class Section(val enabled: Boolean)
    }

    suspend fun getSections(): ArrayList<Int> {
        println("Getting sections...")
        return Promise.resolve(arrayListOf(1, 2, 3, 4))
                .await()
    }

    fun setSection(id: Int, enabled: Boolean) {
        println("Set section $id to ${Section(enabled)}")
    }
}
