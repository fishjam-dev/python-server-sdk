# pylint: disable=locally-disabled, missing-class-docstring, missing-function-docstring, redefined-outer-name, too-few-public-methods

"""
    Tests room api
"""

import os

import pytest

from jellyfish import RoomApi, RoomConfig
from jellyfish import Room
from jellyfish import ComponentOptionsRTSP, ComponentOptionsHLS, PeerOptionsWebRTC

from jellyfish import ValidationError

from jellyfish import UnauthorizedException, NotFoundException


HOST = 'jellyfish' if os.getenv('DOCKER_TEST') == 'TRUE' else 'localhost'
SERVER_ADDRESS = f'http://{HOST}:5002'
SERVER_API_TOKEN = 'development'

MAX_PEERS = 10
CODEC_H264 = 'h264'
PEER_WEBRTC = 'webrtc'

COMPONENT_HLS = 'hls'
COMPONENT_RTSP = 'rtsp'

HLS_OPTIONS = ComponentOptionsHLS()
RTSP_OPTIONS = ComponentOptionsRTSP(
    sourceUri='rtsp://ef36c6dff23ecc5bbe311cc880d95dc8.se:2137/does/not/matter')


class TestAuthentication:
    def test_invalid_token(self):
        room_api = RoomApi(server_address=SERVER_ADDRESS, server_api_token='invalid')

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
        _, room = room_api.create_room(max_peers=MAX_PEERS, video_codec=CODEC_H264)

        assert room == Room(components=[], config=RoomConfig(
            max_peers=MAX_PEERS, video_codec=CODEC_H264), id=room.id, peers=[])
        assert room in room_api.get_all_rooms()

    def test_invalid_max_peers(self, room_api):
        with pytest.raises(ValidationError):
            room_api.create_room(max_peers="10", video_codec=CODEC_H264)

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
        _, room = room_api.create_room(video_codec=CODEC_H264)

        room_api.add_component(room.id, options=HLS_OPTIONS)

        component = room_api.get_room(room.id).components[0].actual_instance
        print(component)

        assert component.type == COMPONENT_HLS

    def test_with_options_rtsp(self, room_api: RoomApi):
        _, room = room_api.create_room(video_codec=CODEC_H264)

        room_api.add_component(room.id, options=RTSP_OPTIONS)
        component = room_api.get_room(room.id).components[0].actual_instance
        assert component.type == COMPONENT_RTSP

    def test_invalid_type(self, room_api: RoomApi):
        _, room = room_api.create_room(video_codec=CODEC_H264)

        with pytest.raises(ValueError):
            room_api.add_component(room.id, options=PeerOptionsWebRTC())


class TestDeleteComponent:
    def test_valid_component(self, room_api: RoomApi):
        _, room = room_api.create_room(video_codec=CODEC_H264)
        component = room_api.add_component(room.id, options=HLS_OPTIONS).actual_instance

        room_api.delete_component(room.id, component.id)
        assert [] == room_api.get_room(room.id).components

    def test_invalid_component(self, room_api: RoomApi):
        _, room = room_api.create_room()

        with pytest.raises(NotFoundException):
            room_api.delete_component(room.id, 'invalid_id')


class TestAddPeer:
    def _assert_peer_created(self, room_api, peer, room_id):
        assert peer.status == 'disconnected'
        assert peer.type == PEER_WEBRTC

        room = room_api.get_room(room_id)
        assert peer in room.peers

    def test_with_specified_options(self, room_api: RoomApi):
        _, room = room_api.create_room()

        _token, peer = room_api.add_peer(room.id, options=PeerOptionsWebRTC(enableSimulcast=True))

        self._assert_peer_created(room_api, peer, room.id)

    def test_default_options(self, room_api: RoomApi):
        _, room = room_api.create_room()

        _token, peer = room_api.add_peer(room.id, options=PeerOptionsWebRTC())

        self._assert_peer_created(room_api, peer, room.id)


class TestDeletePeer:
    def test_valid(self, room_api: RoomApi):
        _, room = room_api.create_room()
        _, peer = room_api.add_peer(room.id, options=PeerOptionsWebRTC(enableSimulcast=True))

        room_api.delete_peer(room.id, peer.id)

        assert [] == room_api.get_room(room.id).peers

    def test_invalid(self, room_api: RoomApi):
        _, room = room_api.create_room()

        with pytest.raises(NotFoundException):
            room_api.delete_peer(room.id, peer_id='invalid_peer_id')
