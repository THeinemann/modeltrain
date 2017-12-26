
import { expect } from "chai";
import Sinon from "sinon";
import qwest from "../../qwest/qwest"

import { getAllSwitches, setSwitch } from "../../clients/switchControlClient";

describe("SwitchControlClient", () => {
    let sandbox;
    let qwest_getstub;
    let qwest_putstub;

    beforeEach(() => {
        sandbox = Sinon.createSandbox()
        qwest_getstub = sandbox.stub(qwest, "get")
        qwest_putstub = sandbox.stub(qwest, "put")
    })

    afterEach(() => {
        sandbox.restore();
    })

    it("should get switches", () => {
        qwest_getstub.resolves({
            "response": "{\"data\": [1,2,3] }" 
        })

        return getAllSwitches().then((response) => {
            expect(qwest_getstub.called).to.be.true;
            expect(response.data).to.eql([1,2,3])
        })
    })

    it("should set switch", () => {
        qwest_putstub.resolves({})

        return setSwitch(42, "turn").then((response) => {
            expect(response).to.be.undefined
        })
    })

    it("should not set switch if direction is invalid", () => {
        qwest_putstub.resolves({})

        return setSwitch(42, "upstairs").then(
            (response) => {
                expect.fail("Should have recognized direction as invalid.")
            }, (error) => {
                expect(error).to.equal("Direction upstairs is invalid.")
            }
        )
    })

})