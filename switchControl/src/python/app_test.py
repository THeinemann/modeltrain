
from unittest.mock import patch, MagicMock
from switchControl import Direction
import unittest
import json

persistenceModuleMock = MagicMock()
with patch.dict("sys.modules", **{
        "switchControl.persistence": persistenceModuleMock
    }):
    import app

    class SwitchControlTest(unittest.TestCase):
        def setUp(self):
            self.app = app.app.test_client()

        @patch.object(app.switchControl, 'set_switch')
        def test_should_set_switch_if_called_with_valid_direction(self, set_switch_mock):            
            rv = self.app.put('/switches/1/straight')
            self.assertEqual(204, rv.status_code)
            
            set_switch_mock.assert_called_with(1, Direction.straight)

        @patch.object(app.switchControl, 'set_switch')
        def test_should_return_error_if_called_with_invalid_direction(self, set_switch_mock):            
            rv = self.app.put('/switches/2/blue')
            self.assertEqual(400, rv.status_code)
            
            set_switch_mock.assert_not_called()

        @patch.object(app.switchControl, 'register_switch')
        def test_should_add_switch(self, register_switch_mock):
            register_switch_mock.return_value = 3            
            rv = self.app.post('/switches/atPin/7')
            self.assertEqual(200, rv.status_code)
            self.assertEqual(b"3\n", rv.data)

            register_switch_mock.assert_called_with(7)

        @patch.object(app.switchControl, 'get_switches')
        def test_should_get_all_switches(self, get_switches_mock):
            get_switches_mock.return_value = [1,2,3]           
            rv = self.app.get('/switches')
            self.assertEqual(200, rv.status_code)
            self.assertEqual(b'{\n  "data": [\n    1, \n    2, \n    3\n  ]\n}\n', rv.data)
            
            get_switches_mock.assert_called_with()

        @patch.object(app.switchControl, 'register_switch')
        def test_should_add_switch(self, register_switch_mock):
            register_switch_mock.return_value = 3            
            rv = self.app.post('/switches/atPin/7')
            self.assertEqual(200, rv.status_code)
            self.assertEqual(b"3\n", rv.data)

            register_switch_mock.assert_called_with(7)

        @patch.object(app.sectionControl, 'set_section')
        def test_should_set_section(self, set_section_mock): 
            rv = self.app.put('/sections/1', data=json.dumps({"enabled": True}), content_type='application/json')
            self.assertEqual(204, rv.status_code)
            
            set_section_mock.assert_called_with(1, {"enabled": True})

        @patch.object(app.sectionControl, 'set_section')
        def test_should_return_bad_request_if_enabled_field_is_missing(self, set_section_mock): 
            rv = self.app.put('/sections/1', data=json.dumps({}), content_type='application/json')
            self.assertEqual(400, rv.status_code)
            
            set_section_mock.assert_not_called

        @patch.object(app.sectionControl, 'register_section')
        def test_should_add_section(self, register_section_mock): 
            register_section_mock.return_value = 4
            rv = self.app.post('/sections/atPin/18')
            self.assertEqual(200, rv.status_code)
            self.assertEqual(b"4\n", rv.data)
            
            register_section_mock.assert_called_with(18)

        @patch.object(app.sectionControl, 'get_sections')
        def test_should_return_all_sections(self, get_sections_mock): 
            get_sections_mock.return_value = [1,2,3]
            rv = self.app.get('/sections')
            self.assertEqual(200, rv.status_code)
            self.assertEqual(b'{\n  "data": [\n    1, \n    2, \n    3\n  ]\n}\n', rv.data)
            
            get_sections_mock.assert_called_with()