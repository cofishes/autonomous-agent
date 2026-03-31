class AutonomousAgentException(Exception):
    """Base class for all exceptions related to the Autonomous Agent."""
    pass


class InitializationError(AutonomousAgentException):
    """Raised when the agent fails to initialize properly."""
    pass


class NavigationError(AutonomousAgentException):
    """Raised when there is an error in the navigation process."""
    pass


class TaskExecutionError(AutonomousAgentException):
    """Raised when the agent fails to execute a task."""
    pass


class CommunicationError(AutonomousAgentException):
    """Raised for issues related to communication with other systems or agents."""
    pass
