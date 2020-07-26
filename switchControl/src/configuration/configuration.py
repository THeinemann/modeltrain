import yaml
from pathlib import Path

import yaml
import logging
from xdg import BaseDirectory
from os import path

from configuration.defaults import defaults

CONFIG_FILE_NAME = "modeltrains.yml"

LOGGER = logging.getLogger("configuration")

def get_configuration_file():
    user_config_file = "{}/{}".format(BaseDirectory.xdg_config_home, CONFIG_FILE_NAME)

    if path.exists(user_config_file):
        return user_config_file

    for dir in BaseDirectory.xdg_config_dirs:
        global_config_file = "{}/{}".format(dir, CONFIG_FILE_NAME)
        if path.exists(global_config_file):
            return global_config_file

    return None

def load_configuration():
    file_name = get_configuration_file()
    LOGGER.info("Reading configuration from file %s", file_name)

    if file_name:
        with open(file_name) as file:
            set_parameters = yaml.load(file)
            return dict(defaults, **set_parameters)

    return defaults
