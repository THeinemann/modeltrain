import unittest
from unittest.mock import Mock

from .switchDao import SwitchDao


class SwitchDaoTest(unittest.TestCase):
    def __init__(self, name):
        super(SwitchDaoTest, self).__init__(name)
        self.conn = None
        self.cursor = None
        self.switch_dao = None

    def setUp(self):
        self.conn = Mock()
        self.conn.cursor = Mock()

        self.cursor = Mock()
        self.cursor.execute = Mock()
        self.cursor.fetchone = Mock()
        self.cursor.fetchall = Mock()
        self.conn.cursor.return_value = self.cursor

        self.switch_dao = SwitchDao(self.conn)

    def test_shouldGetSwitchForPin(self):
        self.cursor.fetchone.return_value = (42,)
        actual = self.switch_dao.get_switch_for_pin(3)

        self.assertEqual(actual, 42)
        self.cursor.execute.assert_called_with(SwitchDao.getSwitchForPinStatement, (3,))

    def test_shouldReturnNoneIfPinIsNotUsed(self):
        self.cursor.fetchone.return_value = None
        actual = self.switch_dao.get_switch_for_pin(3)

        self.assertEqual(actual, None)
        self.cursor.execute.assert_called_with(SwitchDao.getSwitchForPinStatement, (3,))

    def test_shouldGetPinForSwitch(self):
        self.cursor.fetchone.return_value = (42,)
        actual = self.switch_dao.get_pin_for_switch(3)

        self.assertEqual(actual, 42)
        self.cursor.execute.assert_called_with(SwitchDao.getPinForSwitchStatement, (3,))

    def test_shouldThrowIfSwitchDoesNotExist(self):
        self.cursor.fetchone.return_value = None
        with self.assertRaises(ValueError) as cm:
            self.switch_dao.get_pin_for_switch(3)
        self.cursor.execute.assert_called_with(SwitchDao.getPinForSwitchStatement, (3,))
        self.assertEqual(str(cm.exception), "3 is not a valid switch ID")

    def test_shouldInsertSwitch(self):
        self.cursor.lastrowid = 11
        self.conn.commit = Mock()

        actual = self.switch_dao.insert_switch(4)
        self.assertEqual(actual, 11)

        self.cursor.execute.assert_called_with(SwitchDao.insertStatement, (4,))
        self.conn.commit.assert_called()

    def test_shouldGetAllSwitches(self):
        self.cursor.fetchall.return_value = [(1,),(2,),(3,)]
        
        actual = self.switch_dao.get_all_switches()
        self.assertEqual(actual, [1,2,3])

        self.cursor.execute.assert_called_with(SwitchDao.getSwitchesStatement)
        self.cursor.fetchall.assert_called_with()
