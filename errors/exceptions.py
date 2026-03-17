# exceptions.py handles:
# custom exception classes
# maps errors to api responses


class ElevatorError(Exception):
    error_code: str
    message: str
class InvalidFloorError(ElevatorError):
    error_code = "INVALID_FLOOR"
class ElevatorNotFoundError(ElevatorError):
    error_code = "ELEVATOR_NOT_FOUND"
class ElevatorOutOfServiceError(ElevatorError):
    error_code = "ELEVATOR_OUT_OF_SERVICE"
