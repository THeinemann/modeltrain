
from .protocol import Command, StatusCode, BAUD_RATE
import serial

class SpeedControl:
    def __init__(self, port):
        self.arduino = serial.Serial(port, BAUD_RATE, timeout=1)

    def set_speed(self, speed):
        self.arduino.write(bytes([Command.set_speed.value, speed]))
        status = self.arduino.read()[0]
        return StatusCode(status)

    def set_direction(self, direction):
        self.arduino.write(bytes([Command.set_direction.value, direction.value]))
        status = self.arduino.read()[0]
        return StatusCode(int(status))
