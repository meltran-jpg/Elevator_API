# in_memory_store.py handles:
# stores elevator and request data in memory
# simple data structures for quick access
from typing import Dict
from models.elevator import ElevatorState
from models.request import ElevatorRequest
# in memory storage for elevators and requests
elevators: Dict[str, ElevatorState]
requests: Dict[str, ElevatorRequest]
