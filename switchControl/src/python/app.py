from flask import Flask, request, jsonify, __version__
import atexit
from gpioWrapper import GPIO
from switchControl import SwitchControl, Direction
from switchControl.persistence import SwitchDao, sqliteConnectionProvider
from sectionControl import SectionControl
from sectionControl.persistence import SectionDao
from configuration import load_configuration
import logging

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)

switchControl = None
sectionControl = None

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger("app")

LOGGER.info("Using flask version %s",  __version__)

@app.before_first_request
def init():
    global switchControl
    global sectionControl
    LOGGER.info("Running init")
    configuration = load_configuration()
    sqlite_connection = sqliteConnectionProvider.get_sqlite_connection(configuration)
    
    switch_dao = SwitchDao(sqlite_connection)
    switchControl = SwitchControl(GPIO, switch_dao)

    section_dao = SectionDao(sqlite_connection)
    sectionControl = SectionControl(GPIO, section_dao)
    atexit.register(GPIO.cleanup)


@app.route('/switches/<int:switch>/<direction>', methods=['PUT'])
def set_switch(switch, direction):
    d = None
    try:
        d = Direction[direction]
    except KeyError:
        return jsonify("{} is not a valid direction".format(direction)), 400
    switchControl.set_switch(switch, d)
    return jsonify(""), 204

@app.route('/switches/atPin/<int:pin>', methods=['POST'])
def add_switch(pin):
    result = switchControl.register_switch(pin)
    return jsonify(result)

@app.route('/switches')
def get_switches():
    result = switchControl.get_switches()
    LOGGER.info("Found the following switches: %s", result)
    return jsonify({"data": result})


@app.route('/sections/<int:section>', methods=['PUT'])
def set_section(section):
    data = request.json
    if "enabled" not in data:
        return jsonify('Request body must contain field "enabled"'), 400
    sectionControl.set_section(section, data)
    return jsonify(""), 204

@app.route('/sections/atPin/<int:pin>', methods=['POST'])
def add_section(pin):
    result = sectionControl.register_section(pin)
    return jsonify(result)

@app.route('/sections')
def get_sesctions():
    result = sectionControl.get_sections()
    LOGGER.info("Found the following sections: %s", result)
    return jsonify({"data": result})
