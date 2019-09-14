
from unittest.mock import patch, MagicMock
from switchControl import Direction
import unittest
from unittest import skip
from unittest.mock import Mock
from flask import Flask
import json
from gpioWrapper import GPIO

from sectionControl.sectionController import build_controller

class AppTest(unittest.TestCase):
    @patch('sectionControl.SectionControl')
    def setUp(self, SectionControl):
        self.SectionControl = SectionControl
        self.section_control = SectionControl.return_value
        self.app = Flask(__name__)
        self.client = self.app.test_client()

        self.section_dao = Mock()

        self.app.register_blueprint(build_controller(self.section_dao))

    def test_should_initialize_section_control(self):
        self.SectionControl.assert_called_with(GPIO, self.section_dao)

    def test_should_set_section(self): 
        rv = self.client.put('/sections/1', data=json.dumps({"enabled": True}), content_type='application/json')

        self.assertEqual(204, rv.status_code)

        self.section_control.set_section.assert_called_with(1, {"enabled": True})

    def test_should_return_bad_request_if_enabled_field_is_missing(self):
        rv = self.client.put('/sections/1', data=json.dumps({}), content_type='application/json')
        self.assertEqual(400, rv.status_code)

        self.section_control.set_section.assert_not_called

    def test_should_add_section(self):
        self.section_control.register_section.return_value = 4
        rv = self.client.post('/sections/atPin/18')
        self.assertEqual(200, rv.status_code)
        self.assertEqual(b"4\n", rv.data)

        self.section_control.register_section.assert_called_with(18)

    def test_should_return_all_sections(self):
        self.section_control.get_sections.return_value = [1,2,3]
        rv = self.client.get('/sections')
        self.assertEqual(200, rv.status_code)
        self.assertEqual(b'{"data":[1,2,3]}\n', rv.data)

        self.section_control.get_sections.assert_called_with()
