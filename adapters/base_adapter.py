from abc import ABC, abstractmethod
from models.elevator import ElevatorState




class ElevatorAdapter(ABC):
    """
    abstract adapter defining how the system communicates with external elevator systems
    """

    @abstractmethod
    def send_state_update(self, state: ElevatorState) -> None:
        """
        send the desired elevator state to an external system
        """
        pass

    @abstractmethod
    def receive_state_update(self) -> ElevatorState:
        """
        receive the latest elevator state from an external system
        
        """
        pass
