# pylint: disable=locally-disabled, missing-class-docstring, missing-function-docstring, redefined-outer-name, too-few-public-methods, missing-module-docstring

import asyncio
import os
import socket
import time
from multiprocessing import Process, Queue

import pytest
import requests

from jellyfish import Notifier, PeerOptionsWebRTC, RoomApi
from jellyfish.events import (
    ServerMessageMetricsReport,
    ServerMessagePeerConnected,
    ServerMessagePeerDisconnected,
    ServerMessageRoomCreated,
    ServerMessageRoomDeleted,
)
from tests.support.asyncio_utils import assert_events, assert_metrics, cancel
from tests.support.peer_socket import PeerSocket
from tests.support.webhook_notifier import run_server

HOST = "jellyfish" if os.getenv("DOCKER_TEST") == "TRUE" else "localhost"
SERVER_ADDRESS = f"{HOST}:5002"
SERVER_API_TOKEN = "development"
WEBHOOK_ADDRESS = "test" if os.getenv("DOCKER_TEST") == "TRUE" else "localhost"
WEBHOOK_URL = f"http://{WEBHOOK_ADDRESS}:5000/webhook"
queue = Queue()


@pytest.fixture(scope="session", autouse=True)
def start_server():
    flask_process = Process(target=run_server, args=(queue,))
    flask_process.start()

    timeout = 60  # wait maximum of 60 seconds
    while True:
        try:
            response = requests.get(f"http://{WEBHOOK_ADDRESS}:5000/", timeout=1_000)
            if response.status_code == 200:  # Or another condition
                break
        except (requests.ConnectionError, socket.error):
            time.sleep(1)  # wait for 1 second before trying again
            timeout -= 1
            if timeout == 0:
                pytest.fail("Server did not start in the expected time")

    yield  # This is where the testing happens.

    flask_process.terminate()


class TestConnectingToServer:
    @pytest.mark.asyncio
    async def test_valid_credentials(self):
        notifier = Notifier(server_address=SERVER_ADDRESS, server_api_token=SERVER_API_TOKEN)

        notifier_task = asyncio.create_task(notifier.connect())
        await notifier.wait_ready()
        # pylint: disable=protected-access
        assert notifier._websocket.open

        await cancel(notifier_task)

    @pytest.mark.asyncio
    async def test_invalid_credentials(self):
        notifier = Notifier(server_address=SERVER_ADDRESS, server_api_token="wrong_token")

        task = asyncio.create_task(notifier.connect())

        with pytest.raises(RuntimeError):
            await task


@pytest.fixture
def room_api():
    return RoomApi(server_address=SERVER_ADDRESS, server_api_token=SERVER_API_TOKEN)


@pytest.fixture
def notifier():
    notifier = Notifier(server_address=SERVER_ADDRESS, server_api_token=SERVER_API_TOKEN)

    @notifier.on_server_notification
    def handle_notification(_server_notification):
        pass

    @notifier.on_metrics
    def handle_metrics(_metrics_report):
        pass

    return notifier


class TestReceivingNotifications:
    @pytest.mark.asyncio
    async def test_room_created_deleted(self, room_api: RoomApi, notifier: Notifier):
        event_checks = [ServerMessageRoomCreated, ServerMessageRoomDeleted]
        assert_task = asyncio.create_task(assert_events(notifier, event_checks.copy()))

        notifier_task = asyncio.create_task(notifier.connect())
        await notifier.wait_ready()

        _, room = room_api.create_room(webhook_url=WEBHOOK_URL)

        room_api.delete_room(room.id)

        await assert_task
        await cancel(notifier_task)

        for event in event_checks:
            self.assert_event(event)

    @pytest.mark.asyncio
    async def test_peer_connected_disconnected(self, room_api: RoomApi, notifier: Notifier):
        event_checks = [
            ServerMessageRoomCreated,
            ServerMessagePeerConnected,
            ServerMessagePeerDisconnected,
            ServerMessageRoomDeleted,
        ]
        assert_task = asyncio.create_task(assert_events(notifier, event_checks.copy()))

        notifier_task = asyncio.create_task(notifier.connect())
        await notifier.wait_ready()

        _, room = room_api.create_room(webhook_url=WEBHOOK_URL)

        peer_token, peer = room_api.add_peer(room.id, options=PeerOptionsWebRTC())

        peer_socket = PeerSocket(server_address=SERVER_ADDRESS)
        peer_task = asyncio.create_task(peer_socket.connect(peer_token))

        await peer_socket.wait_ready()

        room_api.delete_peer(room.id, peer.id)

        room_api.delete_room(room.id)

        await assert_task
        await cancel(peer_task)
        await cancel(notifier_task)

        for event in event_checks:
            self.assert_event(event)

    @pytest.mark.asyncio
    async def test_peer_connected_room_deleted(self, room_api: RoomApi, notifier: Notifier):
        event_checks = [
            ServerMessageRoomCreated,
            ServerMessagePeerConnected,
            ServerMessageRoomDeleted,
        ]
        assert_task = asyncio.create_task(assert_events(notifier, event_checks.copy()))

        notifier_task = asyncio.create_task(notifier.connect())
        await notifier.wait_ready()

        _, room = room_api.create_room(webhook_url=WEBHOOK_URL)
        peer_token, _peer = room_api.add_peer(room.id, options=PeerOptionsWebRTC())

        peer_socket = PeerSocket(server_address=SERVER_ADDRESS)
        peer_task = asyncio.create_task(peer_socket.connect(peer_token))

        await peer_socket.wait_ready()

        room_api.delete_room(room.id)

        await assert_task
        await cancel(peer_task)
        await cancel(notifier_task)

        for event in event_checks:
            self.assert_event(event)

    def assert_event(self, event):
        data = queue.get(timeout=2.5)
        assert data == event or isinstance(data, event)


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
