# elevator.py handles 
# elevatorstate object
# current floor
# target floor
# movement between floors

from typing import List
from models.enums import Direction, DoorState, ElevatorStatus

class ElevatorState:
    elevator_id: str
    current_floor: int
    direction: Direction
    door_state: DoorState
    target_floors: List[int]
    status: ElevatorStatus
    load_percentage: float
