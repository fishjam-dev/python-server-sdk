# pylint: disable=locally-disabled, missing-class-docstring, missing-function-docstring, redefined-outer-name, too-few-public-methods

import os
import pytest

import asyncio

from jellyfish._notifier import Notifier

HOST = 'jellyfish' if os.getenv('DOCKER_TEST') == 'TRUE' else 'localhost'
SERVER_ADDRESS = f'{HOST}:5002'
SERVER_API_TOKEN = 'development'


class TestConnectingToServer:
    @pytest.mark.asyncio
    async def test_valid_credentials(self):
        notifier = Notifier(server_address=SERVER_ADDRESS,
                            server_api_token=SERVER_API_TOKEN)

        task = asyncio.create_task(notifier.connect())

        await asyncio.sleep(0.1)
        assert notifier._websocket.open

        task.cancel()
        await asyncio.sleep(0.1)

    @pytest.mark.asyncio
    async def test_invalid_credentials(self):
        notifier = Notifier(server_address=SERVER_ADDRESS,
                            server_api_token='server_crappy_token')

        task = asyncio.create_task(notifier.connect())

        with pytest.raises(RuntimeError):
            await task


@pytest.fixture
def notifier():
    return Notifier(server_address=SERVER_ADDRESS, server_api_token=SERVER_API_TOKEN)


class TestReceivingNotifications:
    @pytest.mark.asyncio


class TestReceivingMetrics:
    @pytest.mark.asyncio
