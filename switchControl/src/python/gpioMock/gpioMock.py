
import logging
from sys import stdout

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(stdout)
logger.addHandler(handler)

class state:
    def __init__(self, direction, state):
        self.direction = direction
        self.state = state

class gpioMock:
    BCM = 90
    BOARD = 91

    IN = 10
    OUT = 11

    LOW = 0
    HIGH = 1

    activePins = {}

    def setmode(self, mode):
        # Nothing to do here
        pass

    def setup(self, pin, direction):
        if pin in self.activePins:
            logger.warning("Pin {} is already active".format(pin))
        self.activePins[pin] = state(direction, self.LOW)

    def output(self, pin, state):
        logger.info("Pin {} is now in state {}".format(pin, state))
        self.activePins[pin].state = state

    def cleanup(self, pin=None):
        if pin:
            del self.activePins[pin]
        else:
            self.activePins.clear()

GPIO = gpioMock()
