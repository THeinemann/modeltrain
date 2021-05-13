package modeltrain.sections

import kotlinx.coroutines.*
import modeltrain.external.bootstrap.Variant
import modeltrain.external.bootstrap.bootstrap
import modeltrain.styles.Styles
import react.*
import react.dom.*
import styled.css
import styled.styledDiv
import styled.styledH2
import styled.styledTable

external interface SectionProps : RProps {
    var sectionClient: SectionClient
}

external interface SectionState : RState {
    var sections: List<Int>?
}

class Sections(props: SectionProps) : RComponent<SectionProps, SectionState>(props) {
    val bbutton = bootstrap.button

    override fun RBuilder.render() {
        val scs = state.sections

        styledDiv {
            css(Styles.controlTable)
            styledH2 {
                css(Styles.tableHeader)
                +"Sections"
            }

            if (scs == null) {
                val mainScope = MainScope()
                mainScope.launch {
                    val s = props.sectionClient.getSections()
                    setState {
                        sections = s
                    }
                }
                +"Loading"
            } else {
                styledTable {
                    css(Styles.controlTableBody)
                    tbody {
                        for (section in scs) {
                            tr {
                                td {
                                    +"Section $section"
                                }
                                td {
                                    bbutton {
                                        +"Enable"
                                        attrs {
                                            variant = Variant.SUCCESS
                                            onClickFunction = { props.sectionClient.setSection(section, true) }
                                        }
                                    }
                                }
                                td {
                                    bbutton {
                                        +"Disable"
                                        attrs {
                                            variant = Variant.DANGER
                                            onClickFunction = { props.sectionClient.setSection(section, false) }
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

fun RBuilder.sections(handler: SectionProps.() -> Unit): ReactElement {
    return child(Sections::class) {
        this.attrs(handler)
    }
}