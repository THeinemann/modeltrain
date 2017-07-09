
import unittest
from switchControl.switchControl import SwitchControl
from gpioMock import GPIO

class SwitchControlTest(unittest.TestCase):
    def test_registerSwitch(self):
        sc = SwitchControl()
        sc.registerSwitch(3)
        self.assertEqual(1, len(sc.switches))
        self.assertTrue(0 in sc.switches)
        self.assertEqual(3, sc.switches[0])
        self.assertEqual(1, sc.nextSwitch)

        self.assertEqual(1, len(GPIO.activePins))
        self.assertEqual(GPIO.OUT, GPIO.activePins[3].direction)
        self.assertEqual(GPIO.HIGH, GPIO.activePins[3].state)

        with self.assertRaises(RuntimeError):
            sc.registerSwitch(3)

        sc.registerSwitch(4)
        self.assertEqual(2, len(sc.switches))
        self.assertTrue(0 in sc.switches)
        self.assertTrue(1 in sc.switches)
        self.assertEqual(3, sc.switches[0])
        self.assertEqual(4, sc.switches[1])
        self.assertEqual(2, sc.nextSwitch)

        self.assertEqual(2, len(GPIO.activePins))
        self.assertEqual(GPIO.OUT, GPIO.activePins[3].direction)
        self.assertEqual(GPIO.HIGH, GPIO.activePins[3].state)
        self.assertEqual(GPIO.OUT, GPIO.activePins[4].direction)
        self.assertEqual(GPIO.HIGH, GPIO.activePins[4].state)
