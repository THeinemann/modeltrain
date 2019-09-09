import unittest
from unittest.mock import Mock, call, patch, mock_open

from .sqliteConnectionProvider import get_database_file, get_sqlite_connection

class sqliteConnectionProviderTest(unittest.TestCase):
    def test_shouldGetDatabaseFileFromConfiguration(self):
        configuration = {"database": "/tmp/data.db"}

        result = get_database_file(configuration)
        self.assertEqual("/tmp/data.db", result)

    @patch("xdg.BaseDirectory.xdg_data_home", "/home/karl-heinz")
    @patch("switchControl.persistence.sqliteConnectionProvider.DEFAULT_DB_FILE", "data42.db")
    def test_shouldGetDefaultDatabaseFile(self):

        result = get_database_file({})
        self.assertEqual("/home/karl-heinz/data42.db", result)
    
    @patch("switchControl.persistence.sqliteConnectionProvider.get_database_file")
    @patch("sqlite3.connect")
    def test_shouldGetSqliteConnection(self, mock_connect, mock_get_database_file):
        mock_get_database_file.return_value = "/tmp/data.db"
        configuration = Mock()

        result = get_sqlite_connection(configuration)
        self.assertEqual(mock_connect.return_value, result)

        mock_get_database_file.assert_called_with(configuration)
        mock_connect.assert_called_with("/tmp/data.db")