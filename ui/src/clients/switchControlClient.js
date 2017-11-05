"use strict";

import qwest from "qwest";

const directions = {
    straight: "straight",
    turn: "turn"
}

const getAllSwitches = () => {
    return qwest.get('/switches')
        .then( (request) => request.response )
        .then( JSON.parse )
}

const setSwitch = (switchId, direction) => {
    const dir = directions[direction];
    return qwest.put(`/switches/${switchId}/${dir}`)
    .then( (request) => request.response )
}

export {getAllSwitches, setSwitch, directions};