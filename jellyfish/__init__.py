"""
    .. include:: ../README.md
"""

# pylint: disable=locally-disabled, no-name-in-module, import-error

from pydantic.error_wrappers import ValidationError

# API
from jellyfish._room_api import RoomApi
from jellyfish._ws_notifier import Notifier
from jellyfish._webhook_notifier import receive_json

# Models
from jellyfish._openapi_client import (
    Room,
    RoomConfig,
    Peer,
    Component,
    ComponentHLS,
    ComponentRTSP,
    ComponentOptions,
    ComponentOptionsRTSP,
    ComponentOptionsHLS,
    PeerOptionsWebRTC,
)

# Server Messages
from jellyfish import events

# Exceptions
from jellyfish._openapi_client.exceptions import (
    UnauthorizedException,
    NotFoundException,
    BadRequestException,
)


__all__ = [
    "RoomApi",
    "Notifier",
    "receive_json",
    "Room",
    "Peer",
    "Component",
    "ComponentHLS",
    "ComponentRTSP",
    "ComponentOptionsHLS",
    "RoomConfig",
    "ComponentOptions",
    "ComponentOptionsRTSP",
    "PeerOptionsWebRTC",
    "events",
    "UnauthorizedException",
    "NotFoundException",
    "BadRequestException",
]

__docformat__ = "restructuredtext"
