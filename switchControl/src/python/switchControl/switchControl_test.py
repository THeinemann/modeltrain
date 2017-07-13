
import unittest
from unittest.mock import Mock
from .switchControl import SwitchControl, Direction
from gpioMock import GpioMock


class SwitchControlTest(unittest.TestCase):
    def test_shouldRegisterSwitch(self):
        GPIO = GpioMock()
        switch_dao_mock = Mock()
        switch_dao_mock.get_switch_for_pin = Mock(return_value=None)
        switch_dao_mock.insert_switch = Mock(side_effect=[1, 2])
        sc = SwitchControl(GPIO, switch_dao_mock)

        sc.register_switch(3)
        self.assertEqual(1, len(GPIO.activePins))
        self.assertEqual(GPIO.OUT, GPIO.activePins[3].direction)
        self.assertEqual(GPIO.HIGH, GPIO.activePins[3].state)
        switch_dao_mock.get_switch_for_pin.assert_called_with(3)
        switch_dao_mock.insert_switch.assert_called_with(3)

    def test_shouldNotRegisterSwitchIfPinIsInUse(self):
        GPIO = GpioMock()
        switch_dao_mock = Mock()
        switch_dao_mock.get_switch_for_pin = Mock(return_value=0)
        switch_dao_mock.insert_switch = Mock(side_effect=[1, 2])
        sc = SwitchControl(GPIO, switch_dao_mock)

        with self.assertRaises(RuntimeError) as cm:
            sc.register_switch(3)
        self.assertEqual(str(cm.exception), "Pin 3 already is registered as switch 0")

    def test_shouldSetSwitch(self):
        GPIO = GpioMock()
        GPIO.setup(3, GPIO.OUT)
        GPIO.output(3, GPIO.HIGH)
        GPIO.setup(4, GPIO.OUT)
        GPIO.output(4, GPIO.HIGH)

        switch_dao = Mock()
        switch_dao.get_pin_for_switch = Mock()

        sc = SwitchControl(GPIO, switch_dao)

        switch1 = 0
        switch2 = 1
        switch_dao.get_pin_for_switch.side_effect = lambda switch: switch == switch1 and 3 or 4

        sc.set_switch(switch1, Direction.straight)
        self.assertEqual(GPIO.HIGH, GPIO.activePins[3].state)
        self.assertEqual(GPIO.HIGH, GPIO.activePins[4].state)
        switch_dao.get_pin_for_switch.assert_called_with(switch1)

        sc.set_switch(switch1, Direction.turn)
        self.assertEqual(GPIO.LOW, GPIO.activePins[3].state)
        self.assertEqual(GPIO.HIGH, GPIO.activePins[4].state)
        switch_dao.get_pin_for_switch.assert_called_with(switch1)

        sc.set_switch(switch2, Direction.turn)
        self.assertEqual(GPIO.LOW, GPIO.activePins[3].state)
        self.assertEqual(GPIO.LOW, GPIO.activePins[4].state)
        switch_dao.get_pin_for_switch.assert_called_with(switch2)
