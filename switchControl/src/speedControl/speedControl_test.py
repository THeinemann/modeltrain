
import unittest
from unittest.mock import Mock, patch
from .speedControl import SpeedControl
from .protocol import Command, Direction, StatusCode, BAUD_RATE
import serial

class SpeedControlTest(unittest.TestCase):
    port = '/dev/ttyATM0'

    @patch('serial.Serial')
    def test_shouldInitializeSerialPortInConstructor(self, serial_mock):
        conn = serial_mock.return_value

        speedControl = SpeedControl(self.port)

        self.assertEqual(conn, speedControl.arduino)
        serial_mock.assert_called_with(self.port, BAUD_RATE, timeout=1)

    @patch('serial.Serial')
    def test_shouldSetSpeed(self, serial_mock):
        conn = serial_mock.return_value
        speedControl = SpeedControl(self.port)

        expectedStatus = StatusCode.ok
        conn.read.return_value = bytes([expectedStatus.value])

        speed = 42
        actualStatus = speedControl.set_speed(speed)

        self.assertEqual(expectedStatus, actualStatus)

        conn.write.assert_called_with(bytes([Command.set_speed.value, 42]))


    @patch('serial.Serial')
    def test_shouldSetDirection(self, serial_mock):
        conn = serial_mock.return_value
        speedControl = SpeedControl(self.port)

        direction = Direction.backward
        expectedStatus = StatusCode.internal_error

        conn.read.return_value = bytes([expectedStatus.value])
        actualStatus = speedControl.set_direction(direction)

        self.assertEqual(expectedStatus, actualStatus)

        conn.write.assert_called_with(bytes([Command.set_direction.value, direction.value]))

