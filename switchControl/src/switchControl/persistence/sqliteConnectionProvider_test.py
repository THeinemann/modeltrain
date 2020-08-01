import unittest
from unittest.mock import Mock, call, patch, mock_open

from .sqliteConnectionProvider import get_sqlite_connection

class sqliteConnectionProviderTest(unittest.TestCase):
    @patch("sqlite3.connect")
    def test_shouldGetSqliteConnection(self, mock_connect):
        configuration = {"database": "/tmp/data.db"}

        result = get_sqlite_connection(configuration)
        self.assertEqual(mock_connect.return_value, result)

        mock_connect.assert_called_with("/tmp/data.db", check_same_thread = False)
