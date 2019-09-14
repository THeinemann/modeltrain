
from flask import Blueprint, jsonify, request
import sectionControl
import logging
from gpioWrapper import GPIO

LOGGER = logging.getLogger("section_controller")

def build_controller(section_dao):
    controller = Blueprint('section_controller', __name__, url_prefix='/sections')

    section_control = sectionControl.SectionControl(GPIO, section_dao)

    @controller.route('/<int:section>', methods=['PUT'])
    def set_section(section):
        data = request.get_json()
        if "enabled" not in data:
            return jsonify('Request body must contain field "enabled"'), 400
        section_control.set_section(section, data)
        return jsonify(""), 204

    @controller.route('/atPin/<int:pin>', methods=['POST'])
    def add_section(pin):
        result = section_control.register_section(pin)
        return jsonify(result)

    @controller.route('')
    def get_sesctions():
        result = section_control.get_sections()
        LOGGER.info("Found the following sections: %s", result)
        return jsonify({"data": result})

    return controller
