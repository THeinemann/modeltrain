"use strict";

import Reflux from "reflux";
import {getAllSwitches} from "../clients/switchControlClient"

const switchControlActions = Reflux.createActions([
    "getSwitches",
    "setSwitch"
]);

class SwitchControlStore extends Reflux.Store {
    constructor() {
        super();
        this.state = {switches: null, error: null};
        this.listenTo(switchControlActions.getSwitches, this.onGetSwitches);
    }

    onGetSwitches() {
        getAllSwitches()
            .then( (switches) => { this.setState({switches: switches.data})} )
            .catch( (error) => { this.setState({error})} );
    }
}

export {SwitchControlStore, switchControlActions};