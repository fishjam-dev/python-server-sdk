from enum import Enum


class PeerStatus(str, Enum):
    """Informs about the peer status"""

    CONNECTED = "connected"
    DISCONNECTED = "disconnected"

    def __str__(self) -> str:
        return str(self.value)
