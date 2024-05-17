from enum import Enum


class ComponentPropertiesRecordingSubscribeMode(str, Enum):
    """Whether the Recording component should subscribe to tracks automatically or manually"""

    AUTO = "auto"
    MANUAL = "manual"

    def __str__(self) -> str:
        return str(self.value)
