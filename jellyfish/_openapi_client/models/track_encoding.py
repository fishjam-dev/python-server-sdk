from enum import Enum


class TrackEncoding(str, Enum):
    """None"""

    H264 = "H264"
    OPUS = "OPUS"
    VP8 = "VP8"

    def __str__(self) -> str:
        return str(self.value)
