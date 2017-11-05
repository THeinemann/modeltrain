"use strict";

import React from 'react';
import SwitchTable from './SwitchTable'
import SectionsTable from './SectionsTable'

const App = function() {
    return <table className="app-table">
                <tbody>
                    <tr>
                        <td className='app-table-cell'><SwitchTable/></td>
                        <td className='app-table-cell'><SectionsTable/></td>
                    </tr>
                </tbody>
            </table>;
};

export default App;