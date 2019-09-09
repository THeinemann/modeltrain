
from .protocol import Command, StatusCode

class SpeedControl:
    def __init__(self, serialConnection):
        self.arduino = serialConnection

    def set_speed(self, speed):
        self.arduino.write(bytes([Command.set_speed.value, speed]))
        status = self.arduino.read()
        return StatusCode(status)

    def set_direction(self, direction):
        self.arduino.write(bytes([Command.set_direction.value, direction.value]))
        status = self.arduino.read()
        return StatusCode(status)
