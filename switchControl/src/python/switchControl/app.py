from flask import Flask
import sys
try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:
    sys.stdout.write("Could not import RPi.GPIO - Will continue with GPIO Mock.\n")
    sys.stdout.write("If you are running this program on a Raspberry Pi, this is probably not what you want.\n")
    sys.stdout.write("The GPIO pins will not actually be changed, i.e. connected devices are not controlled.\n")
    from gpioMock import GPIO
from switchControl.switchControl import SwitchControl, Direction

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)

switchControl = SwitchControl(GPIO)

@app.route('/switch/<int:switch>/<direction>', methods=['PUT'])
def setSwitch(switch, direction):
    return switchControl.setSwitch(switch, Direction[direction])

@app.route('/switch/atPin/<int:pin>', methods=['POST'])
def addSwitch(pin):
    result = switchControl.registerSwitch(pin)
    return str(result)
