package modeltrain.switches

import kotlinx.coroutines.MainScope
import kotlinx.coroutines.launch
import kotlinx.html.js.onClickFunction
import react.*
import react.dom.*

external interface SwitchProps: RProps {
    var switchClient: SwitchClient
}

external interface SwitchState: RState {
    var switches: List<Int>?
}

class Switches(props: SwitchProps) : RComponent<SwitchProps, SwitchState>(props) {
    override fun RBuilder.render() {
        val scs = state.switches
        if (scs == null) {
            val mainScope = MainScope()
            mainScope.launch {
                val s = props.switchClient.getSwitches()
                setState {
                    switches = s
                }
            }
            +"Loading"
        } else {
            table {
                tbody {
                    for (section in scs) {
                        tr {
                            td {
                                +"Section $section"
                            }
                            td {
                                button {
                                    +"Straight"
                                    attrs.onClickFunction = { props.switchClient.setSwitch(section, Direction.Straight) }
                                }
                            }
                            td {
                                button {
                                    +"Turn"
                                    attrs.onClickFunction = { props.switchClient.setSwitch(section, Direction.Turn) }
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