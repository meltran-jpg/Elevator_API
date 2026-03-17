# simulator_adapter.py handles:
# simulates elevator movement
# used for testing and demos


from adapters.base_adapter import ElevatorAdapter
from models.elevator import ElevatorState

class SimulatorAdapter(ElevatorAdapter):
    """
    adapter for simulated elevator behavior
    """


    def send_state_update(self, state: ElevatorState) -> None:
        """
        update simulated elevator state
        """
        pass
    def receive_state_update(self) -> ElevatorState:
        """
        return simulated elevator state
        """
        pass
