package modeltrain.switches

import kotlinx.coroutines.MainScope
import kotlinx.coroutines.launch
import modeltrain.external.bootstrap.Variant
import modeltrain.external.bootstrap.bootstrap
import modeltrain.styles.Styles
import react.*
import react.dom.*
import styled.css
import styled.styledDiv
import styled.styledH2
import styled.styledTable

external interface SwitchProps : RProps {
    var switchClient: SwitchClient
}

external interface SwitchState : RState {
    var switches: List<Int>?
}

class Switches(props: SwitchProps) : RComponent<SwitchProps, SwitchState>(props) {
    val bbutton = bootstrap.button

    override fun RBuilder.render() {
        val sws = state.switches

        styledDiv {
            css(Styles.controlTable)
            styledH2 {
                css(Styles.tableHeader)
                +"Switches"
            }

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
                styledTable {
                    css(Styles.controlTableBody)
                    tbody {
                        for (switch in sws) {
                            tr {
                                td {
                                    +"Switch $switch"
                                }
                                td {
                                    bbutton {
                                        +"Straight"
                                        attrs {
                                            variant = Variant.PRIMARY
                                            onClickFunction = { props.switchClient.setSwitch(switch, Direction.Straight) }
                                        }
                                    }
                                }
                                td {
                                    bbutton {
                                        +"Turn"
                                        attrs {
                                            variant = Variant.SECONDARY
                                            onClickFunction = { props.switchClient.setSwitch(switch, Direction.Turn) }
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
}


fun RBuilder.switches(handler: SwitchProps.() -> Unit): ReactElement {
    return child(Switches::class) {
        this.attrs(handler)
    }
}