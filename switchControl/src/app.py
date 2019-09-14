from flask import Flask, request, jsonify, __version__
import atexit
from gpioWrapper import GPIO
from switchControl.persistence import SwitchDao, sqliteConnectionProvider
from sectionControl import SectionControl
from sectionControl.persistence import SectionDao
from configuration import load_configuration
import logging

from speedControl.speedController import build_controller as build_speed_controller
from sectionControl.sectionController import build_controller as build_section_controller
from switchControl.switchController import build_controller as build_switch_controller


app = Flask(__name__)
GPIO.setmode(GPIO.BCM)

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger("app")

LOGGER.info("Using flask version %s",  __version__)

configuration = load_configuration()
sqlite_connection = sqliteConnectionProvider.get_sqlite_connection(configuration)

switch_dao = SwitchDao(sqlite_connection)
section_dao = SectionDao(sqlite_connection)

atexit.register(GPIO.cleanup)

#app.register_blueprint(build_speed_controller())
app.register_blueprint(build_section_controller(section_dao))
app.register_blueprint(build_switch_controller(switch_dao))
