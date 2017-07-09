
from enum import Enum


class SwitchControl:
    _switches = {}
    _nextSwitch = 0
    _directions = {
        'straight': GPIO.HIGH,
        'turn': GPIO.LOW
    }
