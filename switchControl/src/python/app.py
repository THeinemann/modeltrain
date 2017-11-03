from flask import Flask, jsonify
import atexit
from gpioWrapper import GPIO
from switchControl import SwitchControl, Direction
from switchControl.persistence import SwitchDao, sqliteConnectionProvider
from configuration import load_configuration
import logging

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)

switchControl = None

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger("app")

@app.before_first_request
def init():
    global switchControl
    LOGGER.info("Running init")
    configuration = load_configuration()
    sqlite_connection = sqliteConnectionProvider.get_sqlite_connection(configuration)
    switch_dao = SwitchDao(sqlite_connection)
    switchControl = SwitchControl(GPIO, switch_dao)
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
    return jsonify(result)
