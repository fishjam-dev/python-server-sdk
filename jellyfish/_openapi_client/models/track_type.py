from enum import Enum


class TrackType(str, Enum):
    """None"""

    AUDIO = "audio"
    VIDEO = "video"

    def __str__(self) -> str:
        return str(self.value)
