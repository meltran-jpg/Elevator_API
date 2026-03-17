# enums.py handles:
# direction --> up, down, idle
# door status --> open, closed
# elevator status --> moving, stopped

from enum import Enum

# direction --> up, down, idle
class Direction(Enum):
    UP = "up"
    DOWN = "down"
    IDLE = "idle"
# door status --> open or closed
class DoorState(Enum):
    OPEN = "open"
    CLOSED = "closed"

# elevator status --> operational, out_of_service, emergency_stop
class ElevatorStatus(Enum):
    OPERATIONAL = "operational"
    OUT_OF_SERVICE = "out_of_service"
    EMERGENCY_STOP = "emergency_stop"
