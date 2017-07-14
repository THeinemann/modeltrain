from flask import Flask
import sys
import atexit
try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:
    sys.stdout.write("Could not import RPi.GPIO - Will continue with GPIO Mock.\n")
    sys.stdout.write("If you are running this program on a Raspberry Pi, this is probably not what you want.\n")
    sys.stdout.write("The GPIO pins will not actually be changed, i.e. connected devices are not controlled.\n")
    from gpioMock import GPIO
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


@app.route('/switch/<int:switch>/<direction>', methods=['PUT'])
def set_switch(switch, direction):
    return switchControl.set_switch(switch, Direction[direction])


@app.route('/switch/atPin/<int:pin>', methods=['POST'])
def add_switch(pin):
    result = switchControl.register_switch(pin)
    return str(result)
