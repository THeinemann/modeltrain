from flask import Blueprint, jsonify

import switchControl
from switchControl import Direction
import logging

from gpioWrapper import GPIO

LOGGER = logging.getLogger("switch_controller")

def build_controller(switch_dao):
    controller = Blueprint('switch_controller', __name__, url_prefix='/switches')

    switch_control = switchControl.SwitchControl(GPIO, switch_dao)

    @controller.route('/<int:switch>/<direction>', methods=['PUT'])
    def set_switch(switch, direction):
        d = None
        try:
            d = Direction[direction]
        except KeyError:
            return jsonify("{} is not a valid direction".format(direction)), 400
        switch_control.set_switch(switch, d)
        return jsonify(""), 204

    @controller.route('/atPin/<int:pin>', methods=['POST'])
    def add_switch(pin):
        result = switch_control.register_switch(pin)
        return jsonify(result)

    @controller.route('')
    def get_switches():
        result = switch_control.get_switches()
        LOGGER.info("Found the following switches: %s", result)
        return jsonify({"data": result})

    return controller
