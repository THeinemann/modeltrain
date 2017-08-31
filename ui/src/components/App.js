import React from 'react';

class App extends React.Component {
    basicFunction(i) {
        return i + 2;
    };

    render() {
        const i = 7;
        return (
        <div style={{textAlign: 'center'}}>
            <h1>Hello World</h1>
            This is the test screen. Content will follow soon!<br/>
            By the way, did you know that {i} + 2 equals {this.basicFunction(i)}?
        </div>);
    }
};

export default App;