"use strict";

import Reflux from "reflux";
import {getAllSections} from "../clients/sectionControlClient"

const sectionControlActions = Reflux.createActions([
    "getSections",
]);

class SectionControlStore extends Reflux.Store {
    constructor() {
        super();
        this.state = {switches: null, error: null};
        this.listenTo(sectionControlActions.getSections, this.onGetSections);
    }

    onGetSections() {
        getAllSections()
            .then( (switches) => { this.setState({switches: switches.data})} )
            .catch( (error) => { this.setState({error})} );
    }
}

export {SectionControlStore, sectionControlActions};