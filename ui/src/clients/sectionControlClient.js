"use strict";

import qwest from "../qwest/qwest";


const getAllSections = () => {
    return qwest.get('/sections')
        .then( (request) => request.response )
        .then( JSON.parse )
}

const setSection = (switchId, enabled) => {
    const options = {
        dataType: "json",
        responseType: "json"
    }
    return qwest.put(`/sections/${switchId}`, {enabled}, options )
    .then( (request) => request.response )
}

export {getAllSections, setSection};