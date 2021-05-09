package modeltrain.styles

import kotlinx.css.*

object Styles {
    val tableHeader: CSSBuilder.() -> Unit = {
        backgroundRepeat = BackgroundRepeat.noRepeat
        backgroundImage = Image("linear-gradient(transparent, transparent),linear-gradient(transparent, transparent),linear-gradient(to right, blue, white)")
        backgroundPosition = "120%, 122%, 0 130%"
        backgroundSize = "100% 10px"
    }
}