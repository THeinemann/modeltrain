"use strict";

import React from 'react';
import Reflux from 'reflux';

import {setSection} from '../clients/sectionControlClient'
import {SectionControlStore, sectionControlActions} from "../stores/sectionControlStore" 

function Section({id}) {
    return <tr>
            <td>{id}</td>
            <td>  <button onClick={ () => setSection(id, false) }>Disable</button> </td>
            <td>  <button onClick={ () => setSection(id, true) }>Enable</button> </td>
        </tr>;
}

class SectionsTable extends Reflux.Component {

    constructor(props) {
        super(props);
        this.state = {}
        this.store = SectionControlStore;
    }

    componentDidMount() {
        sectionControlActions.getSections()
    }

    renderLoading() {
        return (<div>Loading sections...</div>)
    }

    render() {
        const switches = this.state.switches
        if (!switches) {
            return this.renderLoading();
        }

        return (
        <div>
            <h3>Sections</h3>
            <table>
                <tbody>
                {(switches.map( (v, i) => <Section key={i} id={v}/>))}
                </tbody>
            </table>
        </div>);
    }
};

export default SectionsTable