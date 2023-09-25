# pylint: disable=locally-disabled, missing-class-docstring, missing-function-docstring, redefined-outer-name, too-few-public-methods, missing-module-docstring

import os
import asyncio

import pytest

from jellyfish import Notifier, RoomApi, PeerOptionsWebRTC
from jellyfish import (ServerMessageRoomCreated, ServerMessageRoomDeleted,
                       ServerMessagePeerConnected, ServerMessagePeerDisconnected,
                       ServerMessageMetricsReport)

from tests.support.peer_socket import PeerSocket
from tests.support.asyncio_utils import assert_events, assert_metrics, cancel


HOST = 'jellyfish' if os.getenv('DOCKER_TEST') == 'TRUE' else 'localhost'
SERVER_ADDRESS = f'{HOST}:5002'
SERVER_API_TOKEN = 'development'


class TestConnectingToServer:
    @pytest.mark.asyncio
    async def test_valid_credentials(self):
        notifier = Notifier(server_address=SERVER_ADDRESS,
                            server_api_token=SERVER_API_TOKEN)

        notifier_task = asyncio.create_task(notifier.connect())
        await notifier.wait_ready()
        # pylint: disable=protected-access
        assert notifier._websocket.open

        await cancel(notifier_task)

    @pytest.mark.asyncio
    async def test_invalid_credentials(self):
        notifier = Notifier(server_address=SERVER_ADDRESS,
                            server_api_token='server_crappy_token')

        task = asyncio.create_task(notifier.connect())

        with pytest.raises(RuntimeError):
            await task


@pytest.fixture
def room_api():
    return RoomApi(server_address=SERVER_ADDRESS, server_api_token=SERVER_API_TOKEN)


@pytest.fixture
def notifier():
    return Notifier(server_address=SERVER_ADDRESS, server_api_token=SERVER_API_TOKEN)


class TestReceivingNotifications:
    @pytest.mark.asyncio
    async def test_room_created_deleted(self, room_api: RoomApi, notifier: Notifier):
        event_checks = [
            ServerMessageRoomCreated,
            ServerMessageRoomDeleted
        ]
        assert_task = asyncio.create_task(assert_events(notifier, event_checks))

        notifier_task = asyncio.create_task(notifier.connect())
        await notifier.wait_ready()

        _, room = room_api.create_room()
        room_api.delete_room(room.id)

        await assert_task
        await cancel(notifier_task)

    @pytest.mark.asyncio
    async def test_peer_connected_disconnected(self, room_api: RoomApi, notifier: Notifier):
        event_checks = [
            ServerMessagePeerConnected,
            ServerMessagePeerDisconnected
        ]
        assert_task = asyncio.create_task(assert_events(notifier, event_checks))

        notifier_task = asyncio.create_task(notifier.connect())
        await notifier.wait_ready()

        _, room = room_api.create_room()
        peer_token, _peer = room_api.add_peer(room.id, options=PeerOptionsWebRTC())

        peer_socket = PeerSocket(server_address=SERVER_ADDRESS)
        peer_task = asyncio.create_task(peer_socket.connect(peer_token))

        await peer_socket.wait_ready()

        room_api.delete_room(room.id)

        await assert_task
        await cancel(peer_task)
        await cancel(notifier_task)


class TestReceivingMetrics:
    @pytest.mark.asyncio
    async def test_metrics_with_one_peer(self, room_api: RoomApi, notifier: Notifier):
        _, room = room_api.create_room()
        peer_token, _peer = room_api.add_peer(room.id, PeerOptionsWebRTC())

        peer_socket = PeerSocket(server_address=SERVER_ADDRESS)
        peer_task = asyncio.create_task(peer_socket.connect(peer_token))

        await peer_socket.wait_ready()

        assert_task = asyncio.create_task(assert_metrics(notifier, [ServerMessageMetricsReport]))
        notifier_task = asyncio.create_task(notifier.connect())

        await assert_task
        await cancel(peer_task)
        await cancel(notifier_task)
