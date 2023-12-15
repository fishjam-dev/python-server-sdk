"""
RoomApi used to manage rooms
"""

from typing import Literal, Union

from jellyfish._openapi_client.api.hls import subscribe_tracks as hls_subscribe_tracks
from jellyfish._openapi_client.api.room import add_component as room_add_component
from jellyfish._openapi_client.api.room import add_peer as room_add_peer
from jellyfish._openapi_client.api.room import create_room as room_create_room
from jellyfish._openapi_client.api.room import delete_component as room_delete_component
from jellyfish._openapi_client.api.room import delete_peer as room_delete_peer
from jellyfish._openapi_client.api.room import delete_room as room_delete_room
from jellyfish._openapi_client.api.room import get_all_rooms as room_get_all_rooms
from jellyfish._openapi_client.api.room import get_room as room_get_room
from jellyfish._openapi_client.models import (
    AddComponentJsonBody,
    AddPeerJsonBody,
    ComponentHLS,
    ComponentOptionsHLS,
    ComponentOptionsRTSP,
    ComponentRTSP,
    Peer,
    PeerOptionsWebRTC,
    Room,
    RoomConfig,
    RoomConfigVideoCodec,
    SubscriptionConfig,
)
from jellyfish.api._base_api import BaseApi


class RoomApi(BaseApi):
    """Allows for managing rooms"""

    def __init__(
        self,
        server_address: str = "localhost:5002",
        server_api_token: str = "development",
        secure: bool = False,
    ):
        """
        Create RoomApi instance, providing the jellyfish address and api token.
        Set secure to `True` for `https` and `False` for `http` connection (default).
        """
        super().__init__(
            server_address=server_address, server_api_token=server_api_token, secure=secure
        )

    def create_room(
        self,
        max_peers: int = None,
        video_codec: Literal["h264", "vp8"] = None,
        webhook_url: str = None,
    ) -> (str, Room):
        """
        Creates a new room

        Returns a tuple (`jellyfish_address`, `Room`) - the address of the Jellyfish
        in which the room has been created and the created `Room`

        The returned address may be different from the current `RoomApi` instance.
        In such case, a new `RoomApi` instance has to be created using the returned address
        in order to interact with the room.
        """

        if video_codec is not None:
            video_codec = RoomConfigVideoCodec(video_codec)
        else:
            video_codec = None

        room_config = RoomConfig(
            max_peers=max_peers, video_codec=video_codec, webhook_url=webhook_url
        )

        resp = self._request(room_create_room, json_body=room_config)
        return (resp.data.jellyfish_address, resp.data.room)

    def delete_room(self, room_id: str) -> None:
        """Deletes a room"""

        return self._request(room_delete_room, room_id=room_id)

    def get_all_rooms(self) -> list:
        """Returns list of all rooms"""

        return self._request(room_get_all_rooms).data

    def get_room(self, room_id: str) -> Room:
        """Returns room with the given id"""

        return self._request(room_get_room, room_id=room_id).data

    def add_peer(self, room_id: str, options: PeerOptionsWebRTC) -> (str, Peer):
        """
        Creates peer in the room

        Currently only `webrtc` peer is supported

        Returns a tuple (`peer_token`, `Peer`) - the token needed by Peer to authenticate
        to Jellyfish and the new `Peer`
        """

        peer_type = "webrtc"
        json_body = AddPeerJsonBody(type=peer_type, options=options)

        resp = self._request(room_add_peer, room_id=room_id, json_body=json_body)
        return (resp.data.token, resp.data.peer)

    def delete_peer(self, room_id: str, peer_id: str) -> None:
        """Deletes peer"""

        return self._request(room_delete_peer, id=peer_id, room_id=room_id)

    def add_component(
        self, room_id: str, options: Union[ComponentOptionsHLS, ComponentOptionsRTSP]
    ) -> Union[ComponentHLS, ComponentRTSP]:
        """Creates component in the room"""

        if isinstance(options, ComponentOptionsHLS):
            component_type = "hls"
        elif isinstance(options, ComponentOptionsRTSP):
            component_type = "rtsp"
        else:
            raise ValueError("options must be either ComponentOptionsHLS or ComponentOptionsRTSP")

        json_body = AddComponentJsonBody(type=component_type, options=options)

        return self._request(room_add_component, room_id=room_id, json_body=json_body).data

    def delete_component(self, room_id: str, component_id: str) -> None:
        """Deletes component"""

        return self._request(room_delete_component, id=component_id, room_id=room_id)

    def hls_subscribe(self, room_id: str, tracks: list):
        """subscribes hls component for tracks"""

        subscription_config = SubscriptionConfig(tracks=tracks)

        return self._request(hls_subscribe_tracks, room_id=room_id, json_body=subscription_config)
