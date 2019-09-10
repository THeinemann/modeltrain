
import unittest
from unittest.mock import Mock, patch
import serial

from app import app
import flask

from .protocol import StatusCode, Direction

with patch('serial.Serial') as Serial:
    from .speedController import set_direction, speed_control

    class SpeedControllerTest(unittest.TestCase):
        def setUp(self):
            self.client = app.test_client()

        def tearDown(self):
            Serial.reset_mock()

        @patch.object(speed_control, 'set_direction')
        def test_shouldSetDirection(self, set_direction):
            set_direction.return_value = StatusCode.ok
            rv = self.client.put('/direction', data = '"forward"', content_type='application/json')

            self.assertEqual(204, rv.status_code)
            set_direction.assert_called_with(Direction.forward)

        @patch.object(speed_control, 'set_direction')
        def test_shouldReturnBadRequestIfDirectionIsInvalid(self, set_direction):
            rv = self.client.put('/direction', data = '"north"', content_type='application/json')

            self.assertEqual(400, rv.status_code)
            set_direction.assert_not_called()

        @patch.object(speed_control, 'set_direction')
        def test_shouldReturn500IfStatusCodeIsInternalError(self, set_direction):
            set_direction.return_value = StatusCode.internal_error
            rv = self.client.put('/direction', data = '"forward"', content_type='application/json')

            self.assertEqual(500, rv.status_code)
            set_direction.assert_called_with(Direction.forward)

        @patch.object(speed_control, 'set_speed')
        def test_shouldSetSpeed(self, set_speed):
            set_speed.return_value = StatusCode.ok
            rv = self.client.put('/speed', data = '255', content_type='application/json')

            self.assertEqual(204, rv.status_code)
            set_speed.assert_called_with(255)

        @patch.object(speed_control, 'set_speed')
        def test_shouldReturnBadRequestIfSpeedIsOutOfRange(self, set_speed):
            set_speed.return_value = StatusCode.ok
            rv = self.client.put('/speed', data = '256', content_type='application/json')

            self.assertEqual(400, rv.status_code)
            set_speed.assert_not_called()

        @patch.object(speed_control, 'set_speed')
        def test_shouldReturnBadRequestIfSpeedIsNotANumber(self, set_speed):
            set_speed.return_value = StatusCode.ok
            rv = self.client.put('/speed', data = '[]', content_type='application/json')

            self.assertEqual(400, rv.status_code)
            set_speed.assert_not_called()

        @patch.object(speed_control, 'set_speed')
        def test_shouldReturn500IfSpeedStatusIsInternalError(self, set_speed):
            set_speed.return_value = StatusCode.internal_error
            rv = self.client.put('/speed', data = '255', content_type='application/json')

            self.assertEqual(500, rv.status_code)
