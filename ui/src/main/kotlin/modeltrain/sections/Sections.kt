package modeltrain.sections

import kotlinx.coroutines.*
import kotlinx.html.js.onClickFunction
import react.*
import react.dom.*

external interface SectionProps: RProps {
    var sectionClient: SectionClient
}

external interface SectionState: RState {
    var sections: List<Int>?
}

class Sections(props: SectionProps) : RComponent<SectionProps, SectionState>(props) {
    override fun RBuilder.render() {
        val scs = state.sections
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
            table {
                tbody {
                    for (section in scs) {
                        tr {
                            td {
                                +"Section $section"
                            }
                            td {
                                button {
                                    +"Enable"
                                    attrs.onClickFunction = { props.sectionClient.setSection(section, true) }
                                }
                            }
                            td {
                                button {
                                    +"Disable"
                                    attrs.onClickFunction = { props.sectionClient.setSection(section, false) }
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