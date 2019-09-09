
import unittest
from unittest.mock import Mock
from .sectionControl import SectionControl
from gpioMock import GpioMock


class SectionControlTest(unittest.TestCase):
    def test_shouldRegisterSection(self):
        GPIO = GpioMock()
        section_dao_mock = Mock()
        section_dao_mock.get_section_for_pin = Mock(return_value=None)
        section_dao_mock.insert_section = Mock(side_effect=[1, 2])
        sc = SectionControl(GPIO, section_dao_mock)

        sc.register_section(3)
        self.assertEqual(1, len(GPIO.activePins))
        self.assertEqual(GPIO.OUT, GPIO.activePins[3].direction)
        self.assertEqual(GPIO.HIGH, GPIO.activePins[3].state)
        section_dao_mock.get_section_for_pin.assert_called_with(3)
        section_dao_mock.insert_section.assert_called_with(3)

    def test_shouldNotRegisterSectionIfPinIsInUse(self):
        GPIO = GpioMock()
        section_dao_mock = Mock()
        section_dao_mock.get_section_for_pin = Mock(return_value=0)
        section_dao_mock.insert_section = Mock(side_effect=[1, 2])
        sc = SectionControl(GPIO, section_dao_mock)

        with self.assertRaises(RuntimeError) as cm:
            sc.register_section(3)
        self.assertEqual(str(cm.exception), "Pin 3 already is registered as section 0")

    def test_shouldSetSection(self):
        GPIO = GpioMock()
        GPIO.setup(3, GPIO.OUT)
        GPIO.output(3, GPIO.HIGH)
        GPIO.setup(4, GPIO.OUT)
        GPIO.output(4, GPIO.HIGH)

        section_dao = Mock()

        sc = SectionControl(GPIO, section_dao)

        section1 = 0
        section2 = 1
        section_dao.get_pin_for_section.side_effect = lambda section: section == section1 and 3 or 4

        sc.set_section(section1, {"enabled": True})
        self.assertEqual(GPIO.LOW, GPIO.activePins[3].state)
        self.assertEqual(GPIO.HIGH, GPIO.activePins[4].state)
        section_dao.get_pin_for_section.assert_called_with(section1)

        sc.set_section(section1, {"enabled": False})
        self.assertEqual(GPIO.HIGH, GPIO.activePins[3].state)
        self.assertEqual(GPIO.HIGH, GPIO.activePins[4].state)
        section_dao.get_pin_for_section.assert_called_with(section1)


        sc.set_section(section2, {"enabled": True})
        self.assertEqual(GPIO.HIGH, GPIO.activePins[3].state)
        self.assertEqual(GPIO.LOW, GPIO.activePins[4].state)
        section_dao.get_pin_for_section.assert_called_with(section2)


    def test_shouldGetAllSections(self):
        GPIO = GpioMock()
        
        section_dao = Mock()
        section_dao.get_all_sections.return_value = [1,2,3,4,5]

        sc = SectionControl(GPIO, section_dao)

        actual = sc.get_sections()

        self.assertEqual(actual, [1,2,3,4,5])
        section_dao.get_all_sections.assert_called()