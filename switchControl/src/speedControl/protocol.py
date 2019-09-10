
from enum import Enum

BAUD_RATE = 9600

class Command(Enum):
    set_speed = 0
    set_direction = 1

class Direction(Enum):
    forward = 0
    backward = 1

class StatusCode(Enum):
    ok = 20,
    client_error = 40,
    invalid_command = 44,
    internal_error = 50
