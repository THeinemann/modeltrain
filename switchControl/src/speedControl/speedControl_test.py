
import unittest
from unittest.mock import Mock
from .speedControl import SpeedControl
from .protocol import Command, Direction, StatusCode

class SpeedControlTest(unittest.TestCase):

    def test_shouldSetSpeed(self):
        conn = Mock()
        speedControl = SpeedControl(conn)

        expectedStatus = StatusCode.ok
        conn.read.return_value = expectedStatus.value

        speed = 42
        actualStatus = speedControl.set_speed(speed)

        self.assertEqual(expectedStatus, actualStatus)

        conn.write.assert_called_with(bytes([Command.set_speed.value, 42]))

    def test_shouldSetDirection(self):
        conn = Mock()
        speedControl = SpeedControl(conn)

        direction = Direction.backward
        expectedStatus = StatusCode.internal_error

        conn.read.return_value = expectedStatus.value
        actualStatus = speedControl.set_direction(direction)

        self.assertEqual(expectedStatus, actualStatus)

        conn.write.assert_called_with(bytes([Command.set_direction.value, direction.value]))

