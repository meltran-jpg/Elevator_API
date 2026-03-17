#hardware_adapter.py handles:
# talks to real elevator hardware
# abstracted away from core logic


from adapters.base_adapter import ElevatorAdapter
from models.elevator import ElevatorState

class HardwareAdapter(ElevatorAdapter):
    """
    adapter for communicating with physical elevator hardware
    """
    def send_state_update(self, state: ElevatorState) -> None:
        """
        translate internal elevator state into hardware commands
        """
        pass
    def receive_state_update(self) -> ElevatorState:
        """
        read sensor data and convert it into ElevatorState
        """
        pass
