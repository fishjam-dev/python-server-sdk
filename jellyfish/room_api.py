import time
import jellyfish_openapi_client as jellyfish_api
from jellyfish_openapi_client.rest import ApiException

from jellyfish_openapi_client import Room, RoomConfig


class RoomApi:
    def __init__(self, server_address, server_api_token):
        self._configuration = jellyfish_api.Configuration(
            host=server_address,
            access_token=server_api_token
        )

        self._api_client = jellyfish_api.ApiClient(self._configuration)
        self._room_api = jellyfish_api.RoomApi(self._api_client)

    def create_room(self, max_peers: int = None, video_codec: str = None) -> Room:
        """Creates a room"""

        room_config = RoomConfig(maxPeers=max_peers, videoCodec=video_codec)
        room = self._room_api.create_room(room_config)

        return (room.data.jellyfish_address, room.data.room)

    def delete_room(self):
        pass

    def get_all_rooms(self):
        pass

    def get_room(self):
        pass

    def add_peer():
        pass

    def delete_peer():
        pass

    def add_component():
        pass

    def delete_component():
        pass
