
import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@dataclass
class state:
    direction: int
    state: int


class GpioMock:
    BCM = 90
    BOARD = 91

    IN = 10
    OUT = 11

    LOW = 0
    HIGH = 1

    RISING = 20
    FALLING = 21
    BOTH = 22

    VERSION = "GPIO Mock"

    def __init__(self):
        self.activePins = {}

    def setmode(self, mode):
        # Nothing to do here
        pass

    def setup(self, pin, direction, initial=None):
        if pin in self.activePins:
            logger.warning("Pin {} is already active".format(pin))
        self.activePins[pin] = state(direction, initial or self.LOW)

    def output(self, pin, state):
        logger.info("Pin {} is now in state {}".format(pin, state))
        self.activePins[pin].state = state

    def cleanup(self, pin=None):
        if pin:
            logger.info("Cleaning up pin {}".format(pin))
            del self.activePins[pin]
        else:
            logger.info("Cleaning up all pins")
            self.activePins.clear()

GPIO = GpioMock()
