# elevator_controller.py handels:
# getting elevator status
# open/ close doors
# emergency stop

from models.elevator import ElevatorState
from models.enums import DoorState

def get_elevator_status(elevator_id: str) -> ElevatorState:
    """return current state of an elevator"""
    pass

def set_door_state(elevator_id: str, door_state: DoorState) -> None:
    """open or close elevator doors  """
    pass

def emergency_stop(elevator_id: str, reason: str | None = None) -> None:
    """immediately stop elevator operation """
    pass
def restore_service(elevator_id: str) -> None:
    """restore elevator to operational state"""
    pass
