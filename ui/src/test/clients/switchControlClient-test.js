
import { expect } from "chai";
import Sinon from "sinon";
import qwest from "../../qwest/qwest"

import { getAllSwitches } from "../../clients/switchControlClient";

describe("SwitchControlClient", () => {
    let sandbox;
    let qwest_getstub;

    beforeEach(() => {
        sandbox = Sinon.createSandbox()
        qwest_getstub = sandbox.stub(qwest, "get")
    })

    afterEach(() => {
        sandbox.restore();
    })

    it("should get switches", () => {
        qwest_getstub.resolves({
            "response": "{\"data\": [1,2,3] }" 
        })

        return getAllSwitches().then((response) => {
            expect(response.data).to.eql([1,2,3])
        })
    })

})