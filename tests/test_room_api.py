# pylint: disable=locally-disabled, missing-class-docstring, missing-function-docstring

import pytest

import jellyfish

from jellyfish import RoomApi, RoomConfig
from jellyfish import Room, Peer, Component


SERVER_ADDRESS = "http://localhost:5002"
SERVER_API_TOKEN = "development"

MAX_PEERS = 10
VIDEO_CODEC = "h264"


def test_create_room_client():
    with pytest.raises(TypeError):
        RoomApi()

    with pytest.raises(TypeError):
        RoomApi(server_address="address")

    with pytest.raises(TypeError):
        RoomApi(server_api_token="api_token")

    RoomApi(server_address="address", server_api_token="api_token")


class Authentication:
    def test_invalid_token():
        room_api = RoomApi(server_address=SERVER_ADDRESS, server_api_token="invalid")

        with pytest.raises(TypeError):
            room_api.create_room()

    def test_valid_token():
        room_api = RoomApi(server_address=SERVER_ADDRESS, server_api_token=SERVER_API_TOKEN)

        room = room_api.create_room()

        all_rooms = room_api.get_all_rooms()

        assert room in all_rooms


@pytest.fixture
def room_api():
    return jellyfish.RoomApi(server_address=SERVER_ADDRESS, server_api_token=SERVER_API_TOKEN)


class CreateRoom:
    def __init__(self) -> None:
        self.room_api = room_api()

    def test_no_params(self):
        _, room = self.room_api.create_room()

        assert room == Room(components=[], config=RoomConfig(max_peers=None, video_codec=None),
                            id=room.id, peers=[])

        assert room in self.room_api.get_all_rooms()

    def test_valid_params(self):
        _, room = self.room_api.create_room(max_peers=MAX_PEERS, video_codec=VIDEO_CODEC)

        assert room == Room(components=[], config=RoomConfig(max_peers=None, video_codec=None),
                            id=room.id, peers=[])
        assert room in self.room_api.get_all_rooms()

    def test_invalid_max_peers(self):
        with pytest.raises(TypeError):
            self.room_api.create_room(max_peers="10", video_codec=VIDEO_CODEC)

    def test_invalid_video_codec(self):
        with pytest.raises(TypeError):
            self.room_api.create_room(max_peers=MAX_PEERS, video_codec="h420")


class DeleteRoom:
    def __init__(self) -> None:
        self.room_api = room_api()

    def test_valid(self):
        _, room = self.room_api.create_room()

        room_api.delete(room.id)
        assert room not in self.room_api.get_all_rooms()

    def test_invalid(self):
        with pytest.raises(TypeError):
            self.room_api.delete_room("invalid_id")


class GetAllRooms:
    # def __init__(self) -> None:
    #     self.room_api = room_api()

    def test_valid(self, room_api):
        assert room_api.get_all_rooms() is list


def test_get_all_rooms(room_api):
    pass


def test_get_room(room_api):
    pass


def test_add_component(room_api):
    pass


def test_delete_component(room_api):
    pass


def test_add_peer(room_api):
    # room = room_client.create_room()
    pass


def test_remove_peer(room_api):
    pass
