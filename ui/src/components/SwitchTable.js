"use strict";

import React from 'react';
import Reflux from 'reflux';
import {Button} from 'react-bootstrap';
import _ from 'lodash';

import {setSwitch, directions} from '../clients/switchControlClient'
import {switchControlActions, SwitchControlStore} from '../stores/switchControlStore'

function Switch({id}) {
    return <tr>
            <td>{id}</td>
            <td>  <button onClick={ () => setSwitch(id, directions.straight) }>Straight</button> </td>
            <td>  <button onClick={ () => setSwitch(id, directions.turn) }>Turn</button> </td>
        </tr>;
}

class SwitchTable extends Reflux.Component {

    constructor(props) {
        super(props);
        this.state = {}
        this.store = SwitchControlStore;
    }

    componentDidMount() {
        switchControlActions.getSwitches();
    }

    renderLoading() {
        return (<div>Loading data...</div>)
    }

    render() {
        const switches = this.state.switches
        if (!switches) {
            return this.renderLoading();
        }

        return (
        <div>
            <h3>Switches</h3>
            <table>
                <tbody>
                {(switches.map( (v, i) => <Switch key={i} id={v} />))}
                </tbody>
            </table>
        </div>);
    }
};

export default SwitchTable;