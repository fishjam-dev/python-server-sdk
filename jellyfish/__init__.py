"""
    .. include:: ../README.md
"""

# pylint: disable=locally-disabled, no-name-in-module, import-error

from pydantic.error_wrappers import ValidationError

# API
from jellyfish._room_api import RoomApi
from jellyfish._notifier import Notifier

# Models
from jellyfish._openapi_client import (
    Room, RoomConfig, Peer, Component, ComponentHLS, ComponentRTSP, ComponentOptions,
    ComponentOptionsRTSP, ComponentOptionsHLS, PeerOptionsWebRTC)

# Server Messages
from jellyfish._protos.jellyfish import *

# Exceptions
from jellyfish._openapi_client.exceptions import (
    UnauthorizedException, NotFoundException, BadRequestException)


__all__ = [
    'RoomApi', 'Notifier', 'Room', 'Peer', 'Component', 'ComponentHLS', 'ComponentRTSP',
    'ComponentOptionsHLS', 'RoomConfig', 'ComponentOptions', 'ComponentOptionsRTSP',
    'PeerOptionsWebRTC', 'ServerMessageAuthRequest', 'ServerMessageAuthenticated',
    'ServerMessageSubscribeRequest', 'ServerMessageEventType', 'ServerMessageSubscribeResponse',
    'ServerMessageMetricsReport', 'ServerMessageRoomCreated', 'ServerMessageRoomDeleted',
    'ServerMessageComponentCrashed', 'ServerMessageHlsPlayable', 'ServerMessagePeerConnected',
    'ServerMessagePeerCrashed', 'ServerMessagePeerDisconnected', 'ServerMessageRoomCrashed',
    'UnauthorizedException', 'NotFoundException', 'BadRequestException']

__docformat__ = "restructuredtext"
