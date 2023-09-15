# pylint: disable=locally-disabled, missing-class-docstring, missing-function-docstring, redefined-outer-name, too-few-public-methods

"""
    Tests room api
"""

import os

import pytest

from jellyfish import RoomApi, RoomConfig
from jellyfish import Room
from jellyfish import ComponentOptionsRTSP, PeerOptionsWebRTC

from jellyfish import ValidationError

from jellyfish import UnauthorizedException, NotFoundException, BadRequestException


HOST = 'jellyfish' if os.getenv('DOCKER_TEST') == 'TRUE' else 'localhost'
SERVER_ADDRESS = f'http://{HOST}:5002'
SERVER_API_TOKEN = "development"

MAX_PEERS = 10
VIDEO_CODEC = "h264"


COMPONENT_HLS = "hls"
COMPONENT_RTSP = "rtsp"

HLS_OPTIONS = None
RTSP_OPTIONS = ComponentOptionsRTSP(
    sourceUri="rtsp://ef36c6dff23ecc5bbe311cc880d95dc8.se:2137/does/not/matter")


class TestAuthentication:
    def test_invalid_token(self):
        room_api = RoomApi(server_address=SERVER_ADDRESS, server_api_token="invalid")

        with pytest.raises(UnauthorizedException):
            room_api.create_room()

    def test_valid_token(self):
        room_api = RoomApi(server_address=SERVER_ADDRESS, server_api_token=SERVER_API_TOKEN)

        _, room = room_api.create_room()

        all_rooms = room_api.get_all_rooms()

        assert room in all_rooms

    def test_default_api_token(self):
        room_api = RoomApi(server_address=SERVER_ADDRESS)

        _, room = room_api.create_room()

        all_rooms = room_api.get_all_rooms()

        assert room in all_rooms


@pytest.fixture
def room_api():
    return RoomApi(server_address=SERVER_ADDRESS, server_api_token=SERVER_API_TOKEN)


class TestCreateRoom:
    def test_no_params(self, room_api):
        _, room = room_api.create_room()

        assert room == Room(components=[], config=RoomConfig(max_peers=None, video_codec=None),
                            id=room.id, peers=[])

        assert room in room_api.get_all_rooms()

    def test_valid_params(self, room_api):
        _, room = room_api.create_room(max_peers=MAX_PEERS, video_codec=VIDEO_CODEC)

        assert room == Room(components=[], config=RoomConfig(
            max_peers=MAX_PEERS, video_codec=VIDEO_CODEC), id=room.id, peers=[])
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

        room_api.delete_room(room.id)
        assert room not in room_api.get_all_rooms()

    def test_invalid(self, room_api):
        with pytest.raises(NotFoundException):
            room_api.delete_room("invalid_id")


class TestGetAllRooms:
    def test_valid(self, room_api):
        _, room = room_api.create_room()

        all_rooms = room_api.get_all_rooms()
        assert isinstance(all_rooms, list)
        assert room in all_rooms


class TestGetRoom:
    def test_valid(self, room_api: RoomApi):
        _, room = room_api.create_room()

        assert Room(components=[], peers=[], id=room.id, config=RoomConfig(
            maxPeers=None, videoCodec=None)) == room_api.get_room(room.id)

    def test_invalid(self, room_api: RoomApi):
        with pytest.raises(NotFoundException):
            room_api.get_room("invalid_id")


class TestAddComponent:
    def test_with_options_hls(self, room_api: RoomApi):
        _, room = room_api.create_room(video_codec="h264")

        room_api.add_component(
            room.id, component_type=COMPONENT_HLS, options=HLS_OPTIONS)

        component = room_api.get_room(room.id).components[0]

        assert component.type == "hls"

    def test_with_options_rtsp(self, room_api: RoomApi):
        _, room = room_api.create_room(video_codec="h264")

        room_api.add_component(
            room.id, component_type=COMPONENT_RTSP, options=RTSP_OPTIONS)
        component = room_api.get_room(room.id).components[0]
        assert component.type == "rtsp"

    def test_without_options_hls(self, room_api: RoomApi):
        _, room = room_api.create_room(video_codec="h264")

        component = room_api.add_component(room.id, component_type=COMPONENT_HLS)
        assert component.type == "hls"

    def test_without_options_rtsp(self, room_api: RoomApi):
        _, room = room_api.create_room(video_codec="h264")

        with pytest.raises(BadRequestException):
            room_api.add_component(room.id, component_type=COMPONENT_RTSP)

    def test_invalid_type(self, room_api: RoomApi):
        _, room = room_api.create_room(video_codec="h264")

        with pytest.raises(BadRequestException):
            room_api.add_component(room.id, component_type="CsmaCd")


class TestDeleteComponent:
    def test_valid_component(self, room_api: RoomApi):
        _, room = room_api.create_room(video_codec="h264")
        component = room_api.add_component(
            room.id, component_type=COMPONENT_HLS)

        room_api.delete_component(room.id, component.id)
        assert [] == room_api.get_room(room.id).components

    def test_invalid_component(self, room_api: RoomApi):
        _, room = room_api.create_room()

        with pytest.raises(NotFoundException):
            room_api.delete_component(room.id, "invalid_id")


class TestAddPeer:
    def test_valid(self, room_api: RoomApi):
        _, room = room_api.create_room()

        _token, peer = room_api.add_peer(room.id, peer_type="webrtc",
                                         options=PeerOptionsWebRTC(enableSimulcast=True))

        assert peer.status == "disconnected"
        assert peer.type == "webrtc"

        room = room_api.get_room(room.id)
        assert peer in room.peers

    def test_invalid(self, room_api: RoomApi):
        _, room = room_api.create_room()

        with pytest.raises(BadRequestException):
            room_api.add_peer(
                room.id, peer_type="invalid_type",
                options=PeerOptionsWebRTC(enableSimulcast=True))


class TestDeletePeer:
    def test_valid(self, room_api: RoomApi):
        _, room = room_api.create_room()
        _, peer = room_api.add_peer(room.id, peer_type="webrtc",
                                    options=PeerOptionsWebRTC(enableSimulcast=True))

        room_api.delete_peer(room.id, peer.id)

        assert [] == room_api.get_room(room.id).peers

    def test_invalid(self, room_api: RoomApi):
        _, room = room_api.create_room()

        with pytest.raises(NotFoundException):
            room_api.delete_peer(room.id, peer_id="invalid_peer_id")
