package modeltrain.styles

import kotlinx.css.*

typealias CssStyle = CSSBuilder.() -> Unit

object Styles {
    val tableHeader: CssStyle = {
        backgroundRepeat = BackgroundRepeat.noRepeat
        backgroundImage = Image("linear-gradient(transparent, transparent),linear-gradient(transparent, transparent),linear-gradient(to right, blue, white)")
        backgroundPosition = "120%, 122%, 0 130%"
        backgroundSize = "100% 10px"
    }

    val controlTable: CssStyle = {
        width = LinearDimension("40%")
        minWidth = LinearDimension("250px")
        marginLeft = LinearDimension.auto
        marginRight = LinearDimension.auto
    }
}