
import { expect } from "chai"

import App from "../components/App"

describe("Some example test", () => {
    it("should pass", () => {
        expect(1 > 0).to.equal(true)
    })
    
    it("should increase number by two", () => {
        const app = new App;
        expect(app.basicFunction(1)).to.equal(3)
        expect(app.basicFunction(4)).to.equal(6)
    })
})