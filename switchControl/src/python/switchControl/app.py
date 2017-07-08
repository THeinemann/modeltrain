from flask import Flask
import sys
try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:
    sys.stdout.write("Could not import RPi.GPIO - Will continue with GPIO Mock.\n")
    sys.stdout.write("If you are running this program on a Raspberry Pi, this is probably not what you want.\n")
    sys.stdout.write("The GPIO pins will not actually be changed, i.e. connected devices are not controlled.\n")
    import gpioMock as GPIO


app = Flask(__name__)
GPIO.setmode(GPIO.BCM)

# TODO Save state outside of program
_switches = {}
_nextSwitch = 0
_directions = {
    'straight': GPIO.HIGH,
    'turn': GPIO.LOW
}

@app.route('/switch/<int:switch>/<direction>', methods=['PUT'])
def setSwitch(switch, direction):
    if not switch in _switches:
        raise ValueError("{} is not a valid switch ID".format(switch))
    if not direction in _directions:
        raise ValueError("direction must be either straight or turn, but is {}".format(direction))
    GPIO.output(_switches[switch], _directions[direction])
    return "Hello, World!"

@app.route('/switch/<int:pin>', methods=['POST'])
def addSwitch(pin):
    global _nextSwitch
    if pin in _switches:
        raise RuntimeError("Pin {} already is registered as switch {}".format(pin, _switches[pin]))
    switchId = _nextSwitch
    _switches[switchId] = pin
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    _nextSwitch = switchId + 1
    return str(switchId)
