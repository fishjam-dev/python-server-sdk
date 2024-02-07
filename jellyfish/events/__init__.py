"""
.. include:: ../../docs/server_notifications.md
"""

# Exported messages
from jellyfish.events._protos.jellyfish import (
    ServerMessageComponentCrashed,
    ServerMessageHlsPlayable,
    ServerMessageMetricsReport,
    ServerMessagePeerConnected,
    ServerMessagePeerCrashed,
    ServerMessagePeerDisconnected,
    ServerMessageRoomCrashed,
    ServerMessageRoomCreated,
    ServerMessageRoomDeleted,
    ServerMessageTrack,
    ServerMessageTrackAdded,
    ServerMessageTrackMetadataUpdated,
    ServerMessageTrackRemoved,
    ServerMessageTrackType,
)

__all__ = [
    "ServerMessageRoomCreated",
    "ServerMessageRoomDeleted",
    "ServerMessageRoomCrashed",
    "ServerMessagePeerConnected",
    "ServerMessagePeerDisconnected",
    "ServerMessagePeerCrashed",
    "ServerMessageComponentCrashed",
    "ServerMessageTrack",
    "ServerMessageTrackType",
    "ServerMessageTrackAdded",
    "ServerMessageTrackMetadataUpdated",
    "ServerMessageTrackRemoved",
    "ServerMessageHlsPlayable",
    "ServerMessageMetricsReport",
]
