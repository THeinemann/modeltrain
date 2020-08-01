
import unittest
from unittest.mock import Mock, patch

from flask import Flask
import speedControl.speedControl

from .protocol import StatusCode, Direction

from .speedController import build_controller

DEFAULT_CONFIG = {
    "arduino_port": "/dev/someSerialPort"
}

class SpeedControllerTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()

    @patch.object(speedControl, 'SpeedControl')
    def test_shouldSetDirection(self, SpeedControl):
        service = SpeedControl.return_value
        service.set_direction.return_value = StatusCode.ok
        self.app.register_blueprint(build_controller(DEFAULT_CONFIG))
        rv = self.client.put('/direction', data = '"forward"', content_type='application/json')

        self.assertEqual(204, rv.status_code)
        service.set_direction.assert_called_with(Direction.forward)

    @patch.object(speedControl, 'SpeedControl')
    def test_shouldReturnBadRequestIfDirectionIsInvalid(self, SpeedControl):
        service = SpeedControl.return_value
        service.set_direction.return_value = StatusCode.ok
        self.app.register_blueprint(build_controller(DEFAULT_CONFIG))
        rv = self.client.put('/direction', data = '"north"', content_type='application/json')

        self.assertEqual(400, rv.status_code)
        service.set_direction.assert_not_called()

    @patch.object(speedControl, 'SpeedControl')
    def test_shouldReturn500IfStatusCodeIsInternalError(self, SpeedControl):
        service = SpeedControl.return_value
        service.set_direction.return_value = StatusCode.internal_error
        self.app.register_blueprint(build_controller(DEFAULT_CONFIG))
        rv = self.client.put('/direction', data = '"forward"', content_type='application/json')

        self.assertEqual(500, rv.status_code)
        service.set_direction.assert_called_with(Direction.forward)

    @patch.object(speedControl, 'SpeedControl')
    def test_shouldSetSpeed(self, SpeedControl):
        service = SpeedControl.return_value
        service.set_speed.return_value = StatusCode.ok
        self.app.register_blueprint(build_controller(DEFAULT_CONFIG))
        rv = self.client.put('/speed', data = '255', content_type='application/json')

        self.assertEqual(204, rv.status_code)
        service.set_speed.assert_called_with(255)

    @patch.object(speedControl, 'SpeedControl')
    def test_shouldReturnBadRequestIfSpeedIsOutOfRange(self, SpeedControl):
        service = SpeedControl.return_value
        service.set_speed.return_value = StatusCode.ok
        self.app.register_blueprint(build_controller(DEFAULT_CONFIG))
        rv = self.client.put('/speed', data = '256', content_type='application/json')

        self.assertEqual(400, rv.status_code)
        service.set_speed.assert_not_called()

    @patch.object(speedControl, 'SpeedControl')
    def test_shouldReturnBadRequestIfSpeedIsNotANumber(self, SpeedControl):
        service = SpeedControl.return_value
        self.app.register_blueprint(build_controller(DEFAULT_CONFIG))

        rv = self.client.put('/speed', data = '[]', content_type='application/json')

        self.assertEqual(400, rv.status_code)
        service.set_speed.assert_not_called()

    @patch.object(speedControl, 'SpeedControl')
    def test_shouldReturn500IfSpeedStatusIsInternalError(self, SpeedControl):
        service = SpeedControl.return_value
        service.set_speed.return_value = StatusCode.internal_error
        self.app.register_blueprint(build_controller(DEFAULT_CONFIG))
        rv = self.client.put('/speed', data = '255', content_type='application/json')

        self.assertEqual(500, rv.status_code)
