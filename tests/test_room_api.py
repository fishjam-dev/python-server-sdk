# pylint: disable=locally-disabled, missing-class-docstring, missing-function-docstring

import random
import pytest

import jellyfish
import pydantic

from jellyfish import RoomApi, RoomConfig
from jellyfish import Room, Peer, Component
from jellyfish import ComponentOptionsRTSP, PeerOptionsWebRTC

from jellyfish import ValidationError

SERVER_ADDRESS = "http://localhost:5002"
SERVER_API_TOKEN = "development"

MAX_PEERS = 10
VIDEO_CODEC = "h264"


COMPONENT_HLS = "hls"
COMPONENT_RTSP = "rtsp"

HLS_OPTIONS = None
RTSP_OPTIONS = ComponentOptionsRTSP(sourceUri="rtsp://ef36c6dff23ecc5bbe311cc880d95dc8.se:2137/does/not/matter")


def test_create_room_client():
    with pytest.raises(TypeError):
        RoomApi()

    with pytest.raises(TypeError):
        RoomApi(server_address="address")

    with pytest.raises(TypeError):
        RoomApi(server_api_token="api_token")

    RoomApi(server_address="address", server_api_token="api_token")


class TestAuthentication:
    def test_invalid_token(self, room_api):
        room_api = RoomApi(server_address=SERVER_ADDRESS, server_api_token="invalid")

        with pytest.raises(NotImplementedError):
            room_api.create_room()

    def test_valid_token(self, room_api):
        room_api = RoomApi(server_address=SERVER_ADDRESS, server_api_token=SERVER_API_TOKEN)

        room = room_api.create_room()

        all_rooms = room_api.get_all_rooms()

        assert room in all_rooms


@pytest.fixture
def room_api():
    return jellyfish.RoomApi(server_address=SERVER_ADDRESS, server_api_token=SERVER_API_TOKEN)


class TestCreateRoom:
    def test_no_params(self, room_api):
        _, room = room_api.create_room()

        assert room == Room(components=[], config=RoomConfig(max_peers=None, video_codec=None),
                            id=room.id, peers=[])

        assert room in room_api.get_all_rooms()

    def test_valid_params(self, room_api):
        _, room = room_api.create_room(max_peers=MAX_PEERS, video_codec=VIDEO_CODEC)

        assert room == Room(components=[], config=RoomConfig(max_peers=MAX_PEERS, video_codec=VIDEO_CODEC),
                            id=room.id, peers=[])
        assert room in room_api.get_all_rooms()

    def test_invalid_max_peers(self, room_api):
        with pytest.raises(ValidationError):
            room_api.create_room(max_peers="10", video_codec=VIDEO_CODEC)

    def test_invalid_video_codec(self, room_api):
        with pytest.raises(ValidationError):
            room_api.create_room(max_peers=MAX_PEERS, video_codec="h420")


class TestDeleteRoom:
    def test_valid(self, room_api):
        _, room = room_api.create_room()

        room_api.delete(room.id)
        assert room not in room_api.get_all_rooms()

    def test_invalid(self, room_api):
        with pytest.raises(RuntimeError):
            room_api.delete_room("invalid_id")


class TestGetAllRooms:
    def test_valid(self, room_api):
        room = room_api.create_room()

        all_rooms = room_api.get_all_rooms()
        assert all_rooms is list
        assert room in all_rooms


class TestGetRoom:
    def test_valid(self, room_api: RoomApi):
        room = room_api.create_room()

        assert Room(components=[], peers=[], id=room.id, config=RoomConfig(
            maxPeers=None, videoCodec=None)) == room_api.get_room(room.id)

    def test_invalid(self, room_api: RoomApi):
        with pytest.raises(NotImplementedError):
            room_api.get_room("invalid_id")


class TestAddComponent:
    def test_with_options(self, room_api: RoomApi):
        room_id = room_api.create_room().id

        component = room_api.add_component(room_id, type=COMPONENT_HLS, options=HLS_OPTIONS)
        assert component == Component(id=component.id, type=COMPONENT_HLS)

        component = room_api.add_component(room_id, type=COMPONENT_RTSP, options=RTSP_OPTIONS)
        assert component == Component(id=component.id, type=COMPONENT_RTSP)

    def test_without_options(self, room_api: RoomApi):
        room_id = room_api.create_room().id

        component = room_api.add_component(room_id, type=COMPONENT_HLS)
        assert component == Component(id=component.id, type=COMPONENT_HLS)

        with pytest.raises(NotImplementedError):
            room_api.add_component(room_id, type=COMPONENT_RTSP)

    def test_invalid_type(self, room_api: RoomApi):
        room_id = room_api.create_room().id

        with pytest.raises(NotImplementedError):
            room_api.add_component(room_id, type="CsmaCd")


class TestDeleteComponent:
    def test_valid_component(self, room_api: RoomApi):
        room_id = room_api.create_room().id
        component = room_api.add_component(room_id, type=COMPONENT_HLS, options=HLS_OPTIONS)

        room_api.delete_component(room_id, component.id)
        assert [] == room_api.get_room(room_id).components

    def test_invalid_component(self, room_api: RoomApi):
        room_id = room_api.create_room().id

        with pytest.raises(TypeError):
            room_api.delete_component(room_id, "invalid_id")


class TestAddPeer:
    def test_valid(self, room_api: RoomApi):
        room_id = room_api.create_room().id

        peer = room_api.add_peer(room_id, type="webrtc", options=PeerOptionsWebRTC(enableSimulcast=True))

        assert peer.status == "disconnected"
        assert peer.type == "webrtc"

        room = room_api.get_room(room_id)
        assert peer in room.peers

    def test_invalid(self, room_api: RoomApi):
        room_id = room_api.create_room().id

        with pytest.raises(NotImplementedError):
            room_api.add_peer(room_id, type="invalid_type")


class TestDeletePeer:
    def test_valid(self, room_api: RoomApi):
        room_id = room_api.create_room().id
        peer = room_api.add_peer(room_id, type="webrtc", options=PeerOptionsWebRTC(enableSimulcast=True))

        room_api.delete_peer(peer.id)

        assert [] == room_api.get_room(room_id).peers

    def test_invalid(self, room_api: RoomApi):
        room_id = room_api.create_room().id

        with pytest.raises(NotImplementedError):
            room_api.delete_peer("invalid_peer_id")
