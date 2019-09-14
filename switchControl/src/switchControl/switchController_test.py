
import unittest
from unittest import skip
from unittest.mock import Mock, patch

from switchControl import Direction
from switchControl.switchController import build_controller

from gpioWrapper import GPIO

from flask import Flask

class SwitchControllerTest(unittest.TestCase):
    @patch('switchControl.SwitchControl')
    def setUp(self, SwitchControl):
        self.app = Flask(__name__)
        self.client = self.app.test_client()

        self.SwitchControl = SwitchControl
        self.switch_dao = Mock()
        self.app.register_blueprint(build_controller(self.switch_dao))
        self.switch_control = SwitchControl.return_value

    def test_should_initialize_sswitch_control_correctly(self):
        self.SwitchControl.assert_called_with(GPIO, self.switch_dao)

    def test_should_set_switch_if_called_with_valid_direction(self):
        rv = self.client.put('/switches/1/straight')
        self.assertEqual(204, rv.status_code)

        self.switch_control.set_switch.assert_called_with(1, Direction.straight)

    def test_should_return_error_if_called_with_invalid_direction(self):
        rv = self.client.put('/switches/2/blue')
        self.assertEqual(400, rv.status_code)

        self.switch_control.set_switch.assert_not_called()

    def test_should_add_switch(self):
        self.switch_control.register_switch.return_value = 3
        rv = self.client.post('/switches/atPin/7')
        self.assertEqual(200, rv.status_code)
        self.assertEqual(b"3\n", rv.data)

        self.switch_control.register_switch.assert_called_with(7)

    def test_should_get_all_switches(self):
        self.switch_control.get_switches.return_value = [1,2,3]
        rv = self.client.get('/switches')
        self.assertEqual(200, rv.status_code)
        self.assertEqual(b'{"data":[1,2,3]}\n', rv.data)

        self.switch_control.get_switches.assert_called_with()
