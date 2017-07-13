
from enum import Enum


class Direction(Enum):
    straight = 1
    turn = 2


class SwitchControl:
    def __init__(self, gpio, switch_dao):
        self.switches = {}
        self.nextSwitch = 0
        self.gpio = gpio
        self.switch_dao = switch_dao

    def register_switch(self, pin):
        existing_switch = self.switch_dao.get_switch_for_pin(pin)
        if existing_switch is not None:
            raise RuntimeError("Pin {} already is registered as switch {}".format(pin, existing_switch))
        switch_id = self.switch_dao.insert_switch(pin)
        self.gpio.setup(pin, self.gpio.OUT)
        self.gpio.output(pin, self.gpio.HIGH)
        return switch_id

    def get_output_for_direction(self, direction):
        output_by_direction = {
            Direction.straight: self.gpio.HIGH,
            Direction.turn: self.gpio.LOW
        }
        return output_by_direction[direction]

    def set_switch(self, switch, direction):
        pin = self.switch_dao.get_pin_for_switch(switch)
        if not isinstance(direction, Direction):
            raise ValueError("direction must be a direction value, but is {}".format(direction))
        self.gpio.output(pin, self.get_output_for_direction(direction))
        return "Ok"
