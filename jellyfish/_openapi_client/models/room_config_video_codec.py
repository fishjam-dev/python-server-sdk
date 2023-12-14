from enum import Enum


class RoomConfigVideoCodec(str, Enum):
    """Enforces video codec for each peer in the room"""

    H264 = "h264"
    """RoomConfigVideoCodec: h264"""
    VP8 = "vp8"
    """RoomConfigVideoCodec: vp8"""

    def __str__(self) -> str:
        return str(self.value)
