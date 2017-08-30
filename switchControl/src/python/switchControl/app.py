from flask import Flask
import atexit
from gpioWrapper import GPIO
from switchControl.switchControl import SwitchControl, Direction
from switchControl.persistence import SwitchDao, sqliteConnectionProvider

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)

switchControl = None


@app.before_first_request
def init():
    print("Running init")
    global switchControl
    sqlite_connection = sqliteConnectionProvider.get_sqlite_connection()
    switch_dao = SwitchDao(sqlite_connection)
    switchControl = SwitchControl(GPIO, switch_dao)
    atexit.register(GPIO.cleanup)


@app.route('/switches/<int:switch>/<direction>', methods=['PUT'])
def set_switch(switch, direction):
    return switchControl.set_switch(switch, Direction[direction])


@app.route('/switches/atPin/<int:pin>', methods=['POST'])
def add_switch(pin):
    result = switchControl.register_switch(pin)
    return str(result)


@app.route('/switches')
def get_switches(pin):
    result = switchControl.get_switches()
    return str(result)
