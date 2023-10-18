'''
Notifier listening to WebSocket events
'''

import asyncio
from typing import Callable, Any

import betterproto

from websockets import client
from websockets.exceptions import ConnectionClosed

from jellyfish.events import (
    ServerMessage, ServerMessageAuthRequest, ServerMessageAuthenticated,
    ServerMessageSubscribeRequest, ServerMessageEventType, ServerMessageSubscribeResponse,
    ServerMessageMetricsReport)


class Notifier:
    '''
    Allows for receiving WebSocket messages from Jellyfish.
    '''

    def __init__(self,
                 server_address: str = 'localhost:5002',
                 server_api_token: str = 'development',
                 secure: bool = False):
        '''
        Create Notifier instance, providing the jellyfish address and api token.
        Set secure to `True` for `wss` and `False` for `ws` connection (default).
        '''

        protocol = 'wss' if secure else 'ws'
        self._server_address = f'{protocol}://{server_address}/socket/server/websocket'
        self._server_api_token = server_api_token
        self._websocket = None
        self._ready = False

        self._ready_event: asyncio.Event = None

        self._notification_handler: Callable = None
        self._metrics_handler: Callable = None

    def on_server_notification(self, handler: Callable[[Any], None]):
        '''
        Decorator used for defining handler for ServerNotifications
        i.e. all messages other than `ServerMessageMetricsReport`.
        '''
        self._notification_handler = handler
        return handler

    def on_metrics(self, handler: Callable[[ServerMessageMetricsReport], None]):
        '''
        Decorator used for defining handler for `ServerMessageMetricsReport`.
        '''
        self._metrics_handler = handler
        return handler

    async def connect(self):
        '''
        A coroutine which connects Notifier to Jellyfish and listens for all incoming
        messages from the Jellyfish.

        It runs until the connection isn't closed.

        The incoming messages are handled by the functions defined using the
        `on_server_notification` and `on_metrics` decorators.

        The handlers have to be defined before calling `connect`,
        otherwise the messages won't be received.
        '''
        async with client.connect(self._server_address) as websocket:
            try:
                self._websocket = websocket
                await self._authenticate()

                if self._notification_handler:
                    await self._subscribe_event(
                        event=ServerMessageEventType.EVENT_TYPE_SERVER_NOTIFICATION)

                if self._metrics_handler:
                    await self._subscribe_event(event=ServerMessageEventType.EVENT_TYPE_METRICS)

                self._ready = True
                if self._ready_event:
                    self._ready_event.set()

                await self._receive_loop()
            finally:
                self._websocket = None

    async def wait_ready(self) -> True:
        '''
        Waits until the notifier is connected and authenticated to Jellyfish.

        If already connected, returns `True` immediately.
        '''
        if self._ready:
            return True

        if self._ready_event is None:
            self._ready_event = asyncio.Event()

        await self._ready_event.wait()

    async def _authenticate(self):
        msg = ServerMessage(auth_request=ServerMessageAuthRequest(token=self._server_api_token))
        await self._websocket.send(bytes(msg))

        try:
            message = await self._websocket.recv()
        except ConnectionClosed as exception:
            if 'invalid token' in str(exception):
                raise RuntimeError('Invalid server_api_token') from exception
            raise

        message = ServerMessage().parse(message)

        _type, message = betterproto.which_one_of(message, 'content')
        assert isinstance(message, ServerMessageAuthenticated)

    async def _receive_loop(self):
        while True:
            message = await self._websocket.recv()
            message = ServerMessage().parse(message)
            _which, message = betterproto.which_one_of(message, 'content')

            if isinstance(message, ServerMessageMetricsReport):
                self._metrics_handler(message)
            else:
                self._notification_handler(message)

    async def _subscribe_event(self, event: ServerMessageEventType):
        request = ServerMessage(subscribe_request=ServerMessageSubscribeRequest(event))

        await self._websocket.send(bytes(request))
        message = await self._websocket.recv()
        message = ServerMessage().parse(message)
        _which, message = betterproto.which_one_of(message, "content")
        assert isinstance(message, ServerMessageSubscribeResponse)


    @staticmethod
    def handle_json(json):
        msg = json["notification"]
        message = ServerMessage().parse(msg)
        _which, message = betterproto.which_one_of(message, 'content')
        return message
        