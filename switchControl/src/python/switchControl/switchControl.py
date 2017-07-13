
from enum import Enum


class Direction(Enum):
    straight = 1
    turn = 2


class SwitchControl:
    def __init__(self, gpio):
        self.switches = {}
        self.nextSwitch = 0
        self.gpio = gpio

    def register_switch(self, pin):
        if pin in self.switches.values():
            switch = list(self.switches.keys())[list(self.switches.values()).index(pin)]
            raise RuntimeError("Pin {} already is registered as switch {}".format(pin, switch))
        switch_id = self.nextSwitch
        self.switches[switch_id] = pin
        self.gpio.setup(pin, self.gpio.OUT)
        self.gpio.output(pin, self.gpio.HIGH)
        self.nextSwitch = switch_id + 1
        return switch_id

    def get_output_for_direction(self, direction):
        output_by_direction = {
            Direction.straight: self.gpio.HIGH,
            Direction.turn: self.gpio.LOW
        }
        return output_by_direction[direction]

    def set_switch(self, switch, direction):
        if switch not in self.switches:
            raise ValueError("{} is not a valid switch ID".format(switch))
        if not isinstance(direction, Direction):
            raise ValueError("direction must be a direction value, but is {}".format(direction))
        self.gpio.output(self.switches[switch], self.get_output_for_direction(direction))
        return "Ok"
