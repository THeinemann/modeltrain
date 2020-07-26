
from flask import Blueprint, request
from .protocol import Direction, StatusCode
import speedControl.speedControl

def build_controller(configuration):
    controller = Blueprint('speed_controller', __name__)

    speed_control = speedControl.SpeedControl(configuration['arduino_port'])

    @controller.route('/direction', methods=['PUT'])
    def set_direction():
        payload = request.get_json()

        direction = None
        try:
            direction = Direction[payload]
        except KeyError:
            return 'Invalid direction', 400

        status = speed_control.set_direction(direction)

        if status == StatusCode.ok:
            return '', 204
        else:
            return 'An unexpected error occurred', 500

    @controller.route('/speed', methods=['PUT'])
    def set_speed():
        speed = request.get_json()

        if type(speed) != int:
            return 'Speed must be a number', 400
        if speed < 0 or speed > 255:
            return 'Speed must be a in range [0..255]', 400
        status = speed_control.set_speed(speed)

        if status == StatusCode.ok:
            return '', 204
        else:
            return 'An unexpected error occurred', 500

    return controller
