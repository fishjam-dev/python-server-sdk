'''
Notifier
'''

import logging
import asyncio

from typing import Callable, Any


import betterproto

from websockets import client
from websockets.exceptions import ConnectionClosedOK

from jellyfish._protos.jellyfish import (
    ServerMessage, ServerMessageAuthRequest, ServerMessageAuthenticated,
    ServerMessageSubscribeRequest, ServerMessageEventType, ServerMessageSubscribeResponse,
    ServerMessageMetricsReport)


class Notifier:
    '''
    Allows for receiving websocket notifications from Jellyfish.
    '''

    def __init__(self, server_address: str = 'localhost:5002', server_api_token: str = 'development'):
        self._server_address = server_address
        self._server_api_token = server_api_token
        self._websocket = None
        self._ready = False

        self._ready_event: asyncio.Event = None

        self._notification_handler: Callable = None
        self._metrics_handler: Callable = None

    def on_server_notification(self, handler: Callable[[Any], None]):
        '''
        Decorator used for defining handler for ServerNotifications.
        '''
        self._notification_handler = handler
        return handler

    def on_metrics(self, handler: Callable[[ServerMessageMetricsReport], None]):
        '''
        Decorator used for defining handler for MetricsReport.
        '''
        self._metrics_handler = handler
        return handler

    async def connect(self):
        '''
        Connects Notifier to Jellyfish
        '''
        async with client.connect(f'ws://{self._server_address}/socket/server/websocket') \
                as websocket:
            self._websocket = websocket

            msg = ServerMessage(auth_request=ServerMessageAuthRequest(token=self._server_api_token))
            await websocket.send(bytes(msg))

            try:
                message = await websocket.recv()
            except ConnectionClosedOK as exception:
                raise RuntimeError from exception

            message = ServerMessage().parse(message)

            _type, message = betterproto.which_one_of(message, 'content')
            assert isinstance(message, ServerMessageAuthenticated)

            if self._notification_handler:
                await self._subscribe_event(
                    event=ServerMessageEventType.EVENT_TYPE_SERVER_NOTIFICATION)

            if self._metrics_handler:
                await self._subscribe_event(event=ServerMessageEventType.EVENT_TYPE_METRICS)

            self._ready = True

            if self._ready_event:
                self._ready_event.set()

            receive_task = asyncio.create_task(self._receive_loop())

            await receive_task

        self._websocket = None

    async def wait_ready(self):
        '''
        Waits ready
        '''
        if self._ready:
            return

        if self._ready_event is None:
            self._ready_event = asyncio.Event()

        await self._ready_event.wait()

    async def _receive_loop(self):
        while True:
            message = await self._websocket.recv()
            message = ServerMessage().parse(message)
            _which, message = betterproto.which_one_of(message, "content")

            logging.info('Received message from server: %s', message)

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

        logging.info('Successfully subscribed to %s', event)
