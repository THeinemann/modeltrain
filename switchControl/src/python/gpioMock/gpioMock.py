
import logging
from sys import stdout

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(stdout)
logger.addHandler(handler)

BCM = 90
BOARD = 91

IN = 10
OUT = 11

LOW = 0
HIGH = 1

_activePins = {}

class state:
    def __init__(self, direction, state):
        self.direction = direction
        self.state = state

def setmode():
    # Nothing to do here
    pass

def setup(pin, direction):
    if pin in _activePins:
        logger.warning("Pin {} is already active".format(pin))
    _activePins[pin] = state(direction, LOW)

def output(pin, state):
    logger.info("Pin {} is now in state {}".format(pin, state))
    _activePins[pin].state = state

def cleanup(pin=None):
    if pin:
        del _activePins[pin]
    else:
        _activePins.clear()
