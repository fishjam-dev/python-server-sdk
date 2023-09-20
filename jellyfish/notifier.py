import logging

import asyncio
import betterproto

from websockets import client

from jellyfish import (
    ServerMessage, ServerMessageAuthRequest, ServerMessageAuthenticated,
    ServerMessageSubscribeRequest, ServerMessageEventType, ServerMessageSubscribeResponse)

URI = 'http://localhost:5002/socket/server/websocket'
API_TOKEN = 'development'


class Notifier:
    def __init__(self, on_message, server_address, server_api_token):
        self._on_message = on_message
        self._server_address = server_address
        self._server_api_token = server_api_token
        self._websocket = None
        self._subscribtion_response_event = None

    async def connect(self):
        async with client.connect(f'ws://{self._server_address}/socket/server/websocket') as websocket:
            self._websocket = websocket

            msg = ServerMessage(auth_request=ServerMessageAuthRequest(token=self._server_api_token))
            await websocket.send(bytes(msg))

            message = await websocket.recv()
            message = ServerMessage().parse(message)

            _type, message = betterproto.which_one_of(message, 'content')
            assert isinstance(message, ServerMessageAuthenticated)

            receive_task = asyncio.create_task(self._receive_loop())

            await receive_task

        self._websocket = None

    async def subscribe_server_notification(self):
        await self._subscribe_event(ServerMessageEventType.EVENT_TYPE_SERVER_NOTIFICATION)

    async def _receive_loop(self):
        while True:
            message = await self._websocket.recv()
            message = ServerMessage().parse(message)
            _which, message = betterproto.which_one_of(message, "content")

            logging.info('Received message from server: %s', message)

            if isinstance(message, ServerMessageSubscribeResponse):
                self._subscribtion_response_event.set()

            self._on_message(message)

    async def _subscribe_event(self, event: ServerMessageEventType):
        request = ServerMessage(subscribe_request=ServerMessageSubscribeRequest(event))

        self._subscribtion_response_event = asyncio.Event()
        response_task = asyncio.create_task(self._subscribtion_response_event.wait())

        await self._websocket.send(bytes(request))

        await response_task
        self._subscribtion_response_event = None
        logging.info('Successfully subscribed to %s', event)
