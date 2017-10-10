import unittest
from unittest.mock import Mock

from .sectionDao import SectionDao


class SectionDaoTest(unittest.TestCase):
    def __init__(self, name):
        super(SectionDaoTest, self).__init__(name)
        self.conn = None
        self.cursor = None
        self.section_dao = None

    def setUp(self):
        self.conn = Mock()
        self.conn.cursor = Mock()

        self.cursor = Mock()
        self.cursor.execute = Mock()
        self.cursor.fetchone = Mock()
        self.cursor.fetchall = Mock()
        self.conn.cursor.return_value = self.cursor

        self.section_dao = SectionDao(self.conn)

    def test_shouldGetSectionForPin(self):
        self.cursor.fetchone.return_value = (42,)
        actual = self.section_dao.get_section_for_pin(3)

        self.assertEqual(actual, 42)
        self.cursor.execute.assert_called_with(SectionDao.getSectionForPinStatement, (3,))

    def test_shouldReturnNoneIfPinIsNotUsed(self):
        self.cursor.fetchone.return_value = None
        actual = self.section_dao.get_section_for_pin(3)

        self.assertEqual(actual, None)
        self.cursor.execute.assert_called_with(SectionDao.getSectionForPinStatement, (3,))

    def test_shouldGetPinForSection(self):
        self.cursor.fetchone.return_value = (42,)
        actual = self.section_dao.get_pin_for_section(3)

        self.assertEqual(actual, 42)
        self.cursor.execute.assert_called_with(SectionDao.getPinForSectionStatement, (3,))

    def test_shouldThrowIfSectionDoesNotExist(self):
        self.cursor.fetchone.return_value = None
        with self.assertRaises(ValueError) as cm:
            self.section_dao.get_pin_for_section(3)
        self.cursor.execute.assert_called_with(SectionDao.getPinForSectionStatement, (3,))
        self.assertEqual(str(cm.exception), "3 is not a valid section ID")

    def test_shouldInsertSection(self):
        self.cursor.lastrowid = 11
        self.conn.commit = Mock()

        actual = self.section_dao.insert_section(4)
        self.assertEqual(actual, 11)

        self.cursor.execute.assert_called_with(SectionDao.insertStatement, (4,))
        self.conn.commit.assert_called()

    def test_shouldGetAllSections(self):
        self.cursor.fetchall.return_value = [(1,),(2,),(3,)]
        
        actual = self.section_dao.get_all_sections()
        self.assertEqual(actual, [1,2,3])

        self.cursor.execute.assert_called_with(SectionDao.getSectionsStatement)
        self.cursor.fetchall.assert_called_with()
