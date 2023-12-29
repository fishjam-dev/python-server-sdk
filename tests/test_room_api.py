# pylint: disable=locally-disabled, missing-class-docstring, missing-function-docstring, redefined-outer-name, too-few-public-methods, missing-module-docstring


import os
import uuid
from dataclasses import dataclass

import pytest

from jellyfish import (
    ComponentFile,
    ComponentHLS,
    ComponentOptionsFile,
    ComponentOptionsHLS,
    ComponentOptionsHLSSubscribeMode,
    ComponentOptionsRTSP,
    ComponentPropertiesFile,
    ComponentPropertiesHLS,
    ComponentPropertiesHLSSubscribeMode,
    ComponentPropertiesRTSP,
    ComponentRTSP,
    Peer,
    PeerOptionsWebRTC,
    PeerStatus,
    Room,
    RoomApi,
    RoomConfig,
    RoomConfigVideoCodec,
)
from jellyfish.errors import (
    BadRequestError,
    NotFoundError,
    ServiceUnavailableError,
    UnauthorizedError,
)

HOST = "jellyfish" if os.getenv("DOCKER_TEST") == "TRUE" else "localhost"
SERVER_ADDRESS = f"{HOST}:5002"
SERVER_API_TOKEN = "development"

MAX_PEERS = 10
CODEC_H264 = "h264"

HLS_OPTIONS = ComponentOptionsHLS()
HLS_PROPERTIES = ComponentPropertiesHLS(
    low_latency=False,
    persistent=False,
    playable=False,
    subscribe_mode=ComponentPropertiesHLSSubscribeMode("auto"),
    target_window_duration=None,
)
HLS_PROPERTIES.additional_properties = {"s3": None}

RTSP_OPTIONS = ComponentOptionsRTSP(
    source_uri="rtsp://ef36c6dff23ecc5bbe311cc880d95dc8.se:2137/does/not/matter"
)
RTSP_PROPERTIES = ComponentPropertiesRTSP(
    source_uri=RTSP_OPTIONS.source_uri,
    keep_alive_interval=15000,
    reconnect_delay=15000,
    rtp_port=20000,
    pierce_nat=True,
)

FILE_OPTIONS = ComponentOptionsFile(file_path="video.h264")
FILE_PROPERTIES = ComponentPropertiesFile(file_path=FILE_OPTIONS.file_path)


class TestAuthentication:
    def test_invalid_token(self):
        room_api = RoomApi(server_address=SERVER_ADDRESS, server_api_token="invalid")

        with pytest.raises(UnauthorizedError):
            room_api.create_room()

    def test_valid_token(self):
        room_api = RoomApi(
            server_address=SERVER_ADDRESS, server_api_token=SERVER_API_TOKEN
        )

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

        assert room == Room(
            components=[],
            config=RoomConfig(
                room_id=room.id, max_peers=None, video_codec=None, webhook_url=None
            ),
            id=room.id,
            peers=[],
        )

        assert room in room_api.get_all_rooms()

    def test_valid_params(self, room_api):
        _, room = room_api.create_room(
            max_peers=MAX_PEERS, video_codec=RoomConfigVideoCodec(CODEC_H264)
        )

        assert room == Room(
            components=[],
            config=RoomConfig(
                room_id=room.id,
                max_peers=MAX_PEERS,
                video_codec=RoomConfigVideoCodec(CODEC_H264),
                webhook_url=None,
            ),
            id=room.id,
            peers=[],
        )
        assert room in room_api.get_all_rooms()

    def test_invalid_max_peers(self, room_api):
        with pytest.raises(BadRequestError):
            room_api.create_room(
                max_peers="10", video_codec=CODEC_H264, webhook_url=None
            )

    def test_invalid_video_codec(self, room_api):
        with pytest.raises(ValueError):
            room_api.create_room(max_peers=MAX_PEERS, video_codec="h420")

    def test_valid_room_id(self, room_api):
        room_id = str(uuid.uuid4())
        _, room = room_api.create_room(room_id=room_id)

        assert room == Room(
            components=[],
            config=RoomConfig(
                room_id=room.id,
                max_peers=None,
                video_codec=None,
                webhook_url=None,
            ),
            id=room_id,
            peers=[],
        )
        assert room in room_api.get_all_rooms()

    def test_duplicated_room_id(self, room_api):
        room_id = str(uuid.uuid4())
        _, room = room_api.create_room(room_id=room_id)

        with pytest.raises(BadRequestError) as exception_info:
            _, room = room_api.create_room(room_id=room_id)

        assert (
            str(exception_info.value)
            == f'Cannot add room with id "{room_id}" - room already exists'
        )


class TestDeleteRoom:
    def test_valid(self, room_api):
        _, room = room_api.create_room()

        room_api.delete_room(room.id)
        assert room not in room_api.get_all_rooms()

    def test_invalid(self, room_api):
        with pytest.raises(NotFoundError):
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

        assert Room(
            components=[],
            peers=[],
            id=room.id,
            config=RoomConfig(
                room_id=room.id, max_peers=None, video_codec=None, webhook_url=None
            ),
        ) == room_api.get_room(room.id)

    def test_invalid(self, room_api: RoomApi):
        with pytest.raises(NotFoundError):
            room_api.get_room("invalid_id")


@dataclass
class ComponentTestData:
    component: any
    type: str
    options: any
    properties: any


class TestAddComponent:
    def test_with_options_hls(self, room_api):
        data = ComponentTestData(ComponentHLS, "hls", HLS_OPTIONS, HLS_PROPERTIES)
        self._test_component(room_api, data)

    def test_with_options_rtsp(self, room_api):
        data = ComponentTestData(ComponentRTSP, "rtsp", RTSP_OPTIONS, RTSP_PROPERTIES)
        self._test_component(room_api, data)

    @pytest.mark.file_component_sources
    def test_with_options_file(self, room_api):
        data = ComponentTestData(ComponentFile, "file", FILE_OPTIONS, FILE_PROPERTIES)
        self._test_component(room_api, data)

    def test_invalid_type(self, room_api: RoomApi):
        _, room = room_api.create_room(video_codec=CODEC_H264)

        with pytest.raises(ValueError):
            room_api.add_component(room.id, options=PeerOptionsWebRTC())

    def _test_component(self, room_api: RoomApi, test_data: ComponentTestData):
        _, room = room_api.create_room(video_codec=CODEC_H264)

        response = room_api.add_component(room.id, options=test_data.options)
        component = room_api.get_room(room.id).components[0]

        component = test_data.component(
            id=component.id,
            type=test_data.type,
            properties=test_data.properties,
        )

        assert response == component
        assert component == component


class TestDeleteComponent:
    def test_valid_component(self, room_api: RoomApi):
        _, room = room_api.create_room(video_codec=CODEC_H264)
        component = room_api.add_component(room.id, options=HLS_OPTIONS)

        room_api.delete_component(room.id, component.id)
        assert [] == room_api.get_room(room.id).components

    def test_invalid_component(self, room_api: RoomApi):
        _, room = room_api.create_room()

        with pytest.raises(NotFoundError):
            room_api.delete_component(room.id, "invalid_id")


class TestHLSSubscribe:
    def test_valid_subscription(self, room_api: RoomApi):
        _, room = room_api.create_room(video_codec=CODEC_H264)
        _ = room_api.add_component(
            room.id,
            options=ComponentOptionsHLS(
                subscribe_mode=ComponentOptionsHLSSubscribeMode("manual")
            ),
        )
        assert room_api.hls_subscribe(room.id, ["peer-id"]) is None

    def test_invalid_subscription_in_auto_mode(self, room_api: RoomApi):
        _, room = room_api.create_room(video_codec=CODEC_H264)
        _ = room_api.add_component(room.id, options=HLS_OPTIONS)
        with pytest.raises(BadRequestError) as exception_info:
            room_api.hls_subscribe(room.id, ["component-id"])

        assert (
            str(exception_info.value)
            == "HLS component option `subscribe_mode` is set to :auto"
        )


class TestAddPeer:
    def _assert_peer_created(self, room_api, webrtc_peer, room_id):
        peer = Peer(id=webrtc_peer.id, type="webrtc", status=PeerStatus("disconnected"))

        room = room_api.get_room(room_id)
        assert peer in room.peers

    def test_with_specified_options(self, room_api: RoomApi):
        _, room = room_api.create_room()

        _token, peer = room_api.add_peer(
            room.id, options=PeerOptionsWebRTC(enable_simulcast=True)
        )

        self._assert_peer_created(room_api, peer, room.id)

    def test_default_options(self, room_api: RoomApi):
        _, room = room_api.create_room()

        _token, peer = room_api.add_peer(room.id, options=PeerOptionsWebRTC())

        self._assert_peer_created(room_api, peer, room.id)

    def test_peer_limit_reached(self, room_api: RoomApi):
        _, room = room_api.create_room(max_peers=1)

        _token, peer = room_api.add_peer(room.id, options=PeerOptionsWebRTC())

        self._assert_peer_created(room_api, peer, room.id)

        with pytest.raises(ServiceUnavailableError):
            room_api.add_peer(room.id, options=PeerOptionsWebRTC())


class TestDeletePeer:
    def test_valid(self, room_api: RoomApi):
        _, room = room_api.create_room()
        _, peer = room_api.add_peer(
            room.id, options=PeerOptionsWebRTC(enable_simulcast=True)
        )

        room_api.delete_peer(room.id, peer.id)

        assert [] == room_api.get_room(room.id).peers

    def test_invalid(self, room_api: RoomApi):
        _, room = room_api.create_room()

        with pytest.raises(NotFoundError):
            room_api.delete_peer(room.id, peer_id="invalid_peer_id")
