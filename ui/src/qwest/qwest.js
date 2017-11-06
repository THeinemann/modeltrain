
let qwest;
try {
    qwest = require("qwest");
} catch (e) {
    qwest = {
        put: () => {},
        get: () => {}
    }
}

export default qwest;