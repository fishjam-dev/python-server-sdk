# pylint: disable=locally-disabled, missing-class-docstring, missing-function-docstring, redefined-outer-name, too-few-public-methods, missing-module-docstring

import asyncio

import betterproto
from websockets import client
from websockets.exceptions import ConnectionClosedOK

from tests.support.protos.jellyfish import (
    PeerMessage,
    PeerMessageAuthenticated,
    PeerMessageAuthRequest,
)


class PeerSocket:
    def __init__(self, server_address):
        self._server_address = server_address

        self._ready = False
        self._ready_event = None

    async def connect(self, token):
        async with client.connect(
            f"ws://{self._server_address}/socket/peer/websocket"
        ) as websocket:
            msg = PeerMessage(auth_request=PeerMessageAuthRequest(token=token))
            await websocket.send(bytes(msg))

            try:
                message = await websocket.recv()
            except ConnectionClosedOK as exception:
                raise RuntimeError from exception

            message = PeerMessage().parse(message)

            _type, message = betterproto.which_one_of(message, "content")
            assert isinstance(message, PeerMessageAuthenticated)

            self._ready = True
            if self._ready_event:
                self._ready_event.set()

            await websocket.wait_closed()

    async def wait_ready(self):
        # pylint: disable=duplicate-code
        if self._ready:
            return

        if self._ready_event is None:
            self._ready_event = asyncio.Event()

        await self._ready_event.wait()
