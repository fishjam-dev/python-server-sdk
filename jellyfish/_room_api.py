"""
RoomApi used to manage rooms
"""

from typing import Literal, Union

from jellyfish._openapi_client import AuthenticatedClient
from jellyfish._openapi_client.api.hls import subscribe_tracks
from jellyfish._openapi_client.api.room import (
    add_component,
    add_peer,
    create_room,
    delete_component,
    delete_peer,
    delete_room,
    get_all_rooms,
    get_room,
)
from jellyfish._openapi_client.models import (
    AddComponentJsonBody,
    AddPeerJsonBody,
    ComponentHLS,
    ComponentOptionsHLS,
    ComponentOptionsRTSP,
    ComponentRTSP,
    Error,
    Peer,
    PeerOptionsWebRTC,
    Room,
    RoomConfig,
    RoomConfigVideoCodec,
    SubscriptionConfig,
)


class RoomApi:
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

        protocol = "https" if secure else "http"

        self._client = AuthenticatedClient(f"{protocol}://{server_address}", token=server_api_token)

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

        resp = self._request(create_room, json_body=room_config)
        return (resp.data.jellyfish_address, resp.data.room)

    def delete_room(self, room_id: str) -> None:
        """Deletes a room"""

        return self._request(delete_room, room_id=room_id)

    def get_all_rooms(self) -> list:
        """Returns list of all rooms"""

        return self._request(get_all_rooms).data

    def get_room(self, room_id: str) -> Room:
        """Returns room with the given id"""

        return self._request(get_room, room_id=room_id).data

    def add_peer(self, room_id: str, options: PeerOptionsWebRTC) -> (str, Peer):
        """
        Creates peer in the room

        Currently only `webrtc` peer is supported

        Returns a tuple (`peer_token`, `Peer`) - the token needed by Peer to authenticate
        to Jellyfish and the new `Peer`
        """

        peer_type = "webrtc"
        json_body = AddPeerJsonBody(type=peer_type, options=options)

        resp = self._request(add_peer, room_id=room_id, json_body=json_body)
        return (resp.data.token, resp.data.peer)

    def delete_peer(self, room_id: str, peer_id: str) -> None:
        """Deletes peer"""

        return self._request(delete_peer, id=peer_id, room_id=room_id)

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

        return self._request(add_component, room_id=room_id, json_body=json_body).data

    def delete_component(self, room_id: str, component_id: str) -> None:
        """Deletes component"""

        return self._request(delete_component, id=component_id, room_id=room_id)

    def hls_subscribe(self, room_id: str, tracks: list):
        """subscribes hls component for tracks"""

        subscription_config = SubscriptionConfig(tracks=tracks)

        return self._request(subscribe_tracks, room_id=room_id, json_body=subscription_config)

    def _request(self, method, **kwargs):
        resp = method.sync(client=self._client, **kwargs)
        if isinstance(resp, Error):
            raise RuntimeError(resp.errors)

        return resp
