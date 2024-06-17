from enum import Enum


class NodeStatusStatus(str, Enum):
    """Informs about the status of Fishjam or a specific service"""

    DOWN = "DOWN"
    UP = "UP"

    def __str__(self) -> str:
        return str(self.value)
