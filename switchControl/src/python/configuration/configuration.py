import yaml
from pathlib import Path

import yaml
from xdg import BaseDirectory
from os import path

CONFIG_FILE_NAME = "modeltrains.yml"

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

    if file_name:
        with open(file_name) as file:
            return yaml.load(file)

    return {}
