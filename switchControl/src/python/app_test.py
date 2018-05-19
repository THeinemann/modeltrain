
from unittest.mock import patch, MagicMock
from switchControl import Direction
import unittest

persistenceModuleMock = MagicMock()
with patch.dict("sys.modules", **{
        "switchControl.persistence": persistenceModuleMock
    }):
    import app

    class SwitchControlTest(unittest.TestCase):
        def setUp(self):
            self.app = app.app.test_client()

        @patch.object(app.switchControl, 'set_switch')
        def test_should_set_switch_if_called_with_valid_direction(self, switchControlMock):            
            rv = self.app.put('/switches/1/straight')
            self.assertEqual(204, rv.status_code)
            
            switchControlMock.assert_called_with(1, Direction.straight)

        @patch.object(app.switchControl, 'set_switch')
        def test_should_return_error_if_called_with_invalid_direction(self, switchControlMock):            
            rv = self.app.put('/switches/2/blue')
            self.assertEqual(400, rv.status_code)
            
            switchControlMock.assert_not_called()

        @patch.object(app.switchControl, 'register_switch')
        def test_should_add_switch(self, switchControlMock):
            switchControlMock.return_value = 3            
            rv = self.app.post('/switches/atPin/7')
            self.assertEqual(200, rv.status_code)
            self.assertEqual(b"3\n", rv.data)
            
            switchControlMock.assert_called_with(7)

        