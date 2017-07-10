
from enum import Enum
import sys

class Direction(Enum):
    straight = 1
    turn = 2

class SwitchControl:
    def __init__(self, gpio):
        self.switches = {}
        self.nextSwitch = 0
        self.gpio = gpio

    def registerSwitch(self, pin):
        if pin in self.switches.values():
            switch = list(self.switches.keys())[list(self.switches.values()).index(pin)]
            raise RuntimeError("Pin {} already is registered as switch {}".format(pin, switch))
        switchId = self.nextSwitch
        self.switches[switchId] = pin
        self.gpio.setup(pin, self.gpio.OUT)
        self.gpio.output(pin, self.gpio.HIGH)
        self.nextSwitch = switchId + 1
        return switchId

    def getOutputForDirection(self, direction):
        outputByDirection = {
        Direction.straight: self.gpio.HIGH,
            Direction.turn: self.gpio.LOW
        }
        return outputByDirection[direction]

    def setSwitch(self, switch, direction):
        if not switch in self.switches:
            raise ValueError("{} is not a valid switch ID".format(switch))
        if not isinstance(direction, Direction):
            raise ValueError("direction must be a direction value, but is {}".format(direction))
        self.gpio.output(self.switches[switch], self.getOutputForDirection(direction))
        return "Ok"
