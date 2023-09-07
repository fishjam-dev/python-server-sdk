"""
    RoomApi used to manage rooms
"""

import openapi_client as jellyfish_api

from openapi_client import AddPeerRequest, AddComponentRequest, PeerOptions, ComponentOptions
from openapi_client import Room, RoomConfig


class RoomApi:
    """Allows for managing rooms"""

    def __init__(self, server_address, server_api_token):
        self._configuration = jellyfish_api.Configuration(
            host=server_address,
            access_token=server_api_token
        )

        self._api_client = jellyfish_api.ApiClient(self._configuration)
        self._room_api = jellyfish_api.RoomApi(self._api_client)

    def create_room(self, max_peers: int = None, video_codec: str = None) -> (str, Room):
        """Creates a room"""

        room_config = RoomConfig(maxPeers=max_peers, videoCodec=video_codec)
        resp = self._room_api.create_room(room_config)

        return (resp.data.jellyfish_address, resp.data.room)

    def delete_room(self, room_id: str) -> None:
        """Deletes a room"""

        return self._room_api.delete_room(room_id)

    def get_all_rooms(self) -> list:
        """Returns list of all rooms"""

        return self._room_api.get_all_rooms().data

    def get_room(self, room_id: str) -> Room:
        """Returns room with the given id"""

        return self._room_api.get_room(room_id).data

    def add_peer(self, room_id: str, peer_type: str, options: PeerOptions):
        """Creates peer in the room"""

        options = PeerOptions(options)
        request = AddPeerRequest(type=peer_type, options=options)

        resp = self._room_api.add_peer(room_id, request)
        return (resp.data.token, resp.data.peer)

    def delete_peer(self, room_id, peer_id):
        """Deletes peer"""

        return self._room_api.delete_peer(room_id, peer_id)

    def add_component(self, room_id, component_type, options=None):
        """Creates component in the room"""

        if options:
            options = ComponentOptions(options)

        request = AddComponentRequest(type=component_type, options=options)

        return self._room_api.add_component(room_id, request).data

    def delete_component(self, room_id, component_id):
        """Deletes component"""

        return self._room_api.delete_component(room_id, component_id)
