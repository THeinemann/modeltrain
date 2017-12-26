"use strict";

import qwest from "../qwest/qwest";

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
    if ( dir ) {
        return qwest.put(`/switches/${switchId}/${dir}`)
        .then( (request) => request.response )
    } else {
        return Promise.reject(`Direction ${direction} is invalid.`)
    }
}

export {getAllSwitches, setSwitch, directions};