
from enum import Enum
import sys
try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:
    sys.stdout.write("Could not import RPi.GPIO - Will continue with GPIO Mock.\n")
    sys.stdout.write("If you are running this program on a Raspberry Pi, this is probably not what you want.\n")
    sys.stdout.write("The GPIO pins will not actually be changed, i.e. connected devices are not controlled.\n")
    from gpioMock import GPIO

class Direction(Enum):
    straight = 1
    turn = 2

class SwitchControl:
    def __init__(self):
        self.switches = {}
        self.nextSwitch = 0

    def registerSwitch(self, pin):
        if pin in self.switches.values():
            switch = list(self.switches.keys())[list(self.switches.values()).index(pin)]
            raise RuntimeError("Pin {} already is registered as switch {}".format(pin, switch))
        switchId = self.nextSwitch
        self.switches[switchId] = pin
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
        self.nextSwitch = switchId + 1
        return switchId
