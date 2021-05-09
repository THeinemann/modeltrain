package modeltrain.switches

import kotlinx.coroutines.MainScope
import kotlinx.coroutines.launch
import kotlinx.html.js.onClickFunction
import modeltrain.styles.Styles
import react.*
import react.dom.*
import styled.css
import styled.styledH2

external interface SwitchProps: RProps {
    var switchClient: SwitchClient
}

external interface SwitchState: RState {
    var switches: List<Int>?
}

class Switches(props: SwitchProps) : RComponent<SwitchProps, SwitchState>(props) {
    override fun RBuilder.render() {
        val sws = state.switches
        if (sws == null) {
            val mainScope = MainScope()
            mainScope.launch {
                val s = props.switchClient.getSwitches()
                setState {
                    switches = s
                }
            }
            +"Loading"
        } else {
            span {
                styledH2 {
                    css(Styles.tableHeader)
                    +"Switches"
                }
                table {
                    tbody {
                        for (switch in sws) {
                            tr {
                                td {
                                    +"Switch $switch"
                                }
                                td {
                                    button {
                                        +"Straight"
                                        attrs.onClickFunction = { props.switchClient.setSwitch(switch, Direction.Straight) }
                                    }
                                }
                                td {
                                    button {
                                        +"Turn"
                                        attrs.onClickFunction = { props.switchClient.setSwitch(switch, Direction.Turn) }
                                    }
                                }
                            }
                        }
                    }

                }
            }
        }
    }
}


fun RBuilder.switches(handler: SwitchProps.() -> Unit): ReactElement {
    return child(Switches::class) {
        this.attrs(handler)
    }
}