# request.py handles:
# elevator request object
# source floor, destination floor, direction

from models.enums import Direction
# ElevatorRequest model
class ElevatorRequest:
    request_id: str
    source_floor: int
    destination_floor: int
    direction: Direction
