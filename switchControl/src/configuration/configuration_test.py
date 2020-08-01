
import unittest
from unittest.mock import call, patch, mock_open

from .configuration import get_configuration_file, load_configuration
from configuration.defaults import defaults

class ConfigurationTest(unittest.TestCase):
    @patch("os.path.exists")
    @patch("configuration.configuration.CONFIG_FILE_NAME", "test.conf")
    @patch("xdg.BaseDirectory.xdg_config_home", "/home/karl-heinz/.config")
    @patch("xdg.BaseDirectory.xdg_config_dirs", ["/etc/xdg", "/opt/myConfig"])
    def test_shouldGetUserConfigFileNameIfItExists(self, exists):
        exists.return_value = True

        result = get_configuration_file()
        self.assertEqual("/home/karl-heinz/.config/test.conf", result)
        exists.assert_called_with(result)

    @patch("os.path.exists")
    @patch("configuration.configuration.CONFIG_FILE_NAME", "test.conf")
    @patch("xdg.BaseDirectory.xdg_config_home", "/home/karl-heinz/.config")
    @patch("xdg.BaseDirectory.xdg_config_dirs", ["/etc/xdg", "/opt/myConfig"])
    def test_shouldGetGlobalConfigFileNameIfItExists(self, exists):
        exists.side_effect = lambda x: x == "/opt/myConfig/test.conf"

        result = get_configuration_file()
        self.assertEqual("/opt/myConfig/test.conf", result)

        exists.assert_has_calls([
            call("/home/karl-heinz/.config/test.conf"),
            call("/etc/xdg/test.conf"),
            call("/opt/myConfig/test.conf")])

    @patch("os.path.exists")
    @patch("configuration.configuration.CONFIG_FILE_NAME", "test.conf")
    @patch("xdg.BaseDirectory.xdg_config_home", "/home/karl-heinz/.config")
    @patch("xdg.BaseDirectory.xdg_config_dirs", ["/etc/xdg", "/opt/myConfig"])
    def test_shouldGetFirstExistingGlobalConfigFileNameIfSeveralExists(self, exists):
        exists.side_effect = lambda x: (x == "/opt/myConfig/test.conf") or (x == "/etc/xdg/test.conf")

        result = get_configuration_file()
        self.assertEqual("/etc/xdg/test.conf", result)

        exists.assert_has_calls([
            call("/home/karl-heinz/.config/test.conf"),
            call("/etc/xdg/test.conf")])

    @patch("os.path.exists")
    @patch("configuration.configuration.CONFIG_FILE_NAME", "test.conf")
    @patch("xdg.BaseDirectory.xdg_config_home", "/home/karl-heinz/.config")
    @patch("xdg.BaseDirectory.xdg_config_dirs", ["/etc/xdg", "/opt/myConfig"])
    def test_shouldReturnNoneIfNoConfigFileExists(self, exists):
        exists.return_value = False

        result = get_configuration_file()
        self.assertEqual(None, result)

        exists.assert_has_calls([
            call("/home/karl-heinz/.config/test.conf"),
            call("/etc/xdg/test.conf"),
            call("/opt/myConfig/test.conf")])

    @patch("configuration.configuration.open")
    @patch("configuration.configuration.get_configuration_file")
    @patch("yaml.load")
    def test_shouldLoadConfiguration(self, mock_yaml_load, mock_get_configuration_file, mock_open2):
        mock_open(mock_open2)
        expected = {"server": {"port": 1234}, "database": "/home/karl-heinz/data.db"}
        mock_get_configuration_file.return_value = "/home/karl-heinz/.config/test.conf"
        mock_yaml_load.return_value = expected

        result = load_configuration()
        self.assertEqual(expected["server"], result["server"])
        self.assertEqual(expected["database"], result["database"])

        mock_get_configuration_file.assert_called_with()
        mock_open2.assert_called_with("/home/karl-heinz/.config/test.conf")
        mock_yaml_load.assert_called_with(mock_open2.return_value)

    @patch("configuration.configuration.open")
    @patch("configuration.configuration.get_configuration_file")
    @patch("yaml.load")
    def test_shouldReturnDefaultConfigurationIfNoFileHasBeenFound(self, mock_yaml_load, mock_get_configuration_file, mock_open2):
        mock_open(mock_open2)
        mock_get_configuration_file.return_value = None

        result = load_configuration()
        self.assertEqual(defaults, result)

        mock_get_configuration_file.assert_called_with()
        mock_open2.assert_not_called()
        mock_yaml_load.assert_not_called()

    @patch("configuration.configuration.open")
    @patch("configuration.configuration.get_configuration_file")
    @patch("yaml.load")
    def test_shouldUseDefaultsForUnsetParameters(self, mock_yaml_load, mock_get_configuration_file, mock_open2):
        mock_open(mock_open2)
        yaml_content = {"database": "/opt/trains.db"}
        mock_get_configuration_file.return_value = "/home/karl-heinz/.config/test.conf"
        mock_yaml_load.return_value = yaml_content

        result = load_configuration()
        self.assertEqual(result["database"], yaml_content["database"])
        self.assertEqual(result['arduino_port'], defaults['arduino_port'])

        mock_get_configuration_file.assert_called_with()
        mock_open2.assert_called_with("/home/karl-heinz/.config/test.conf")
        mock_yaml_load.assert_called_with(mock_open2.return_value)
