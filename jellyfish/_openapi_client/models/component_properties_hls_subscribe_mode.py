from enum import Enum


class ComponentPropertiesHLSSubscribeMode(str, Enum):
    """Whether the HLS component should subscribe to tracks automatically or manually"""

    AUTO = "auto"
    MANUAL = "manual"

    def __str__(self) -> str:
        return str(self.value)
