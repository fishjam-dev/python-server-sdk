import asyncio

from jellyfish.notifier import Notifier

URI = 'ws://localhost:5002/socket/server/websocket'
API_TOKEN = 'development'

SERVER_ADDRESS = 'localhost:5002'
SERVER_API_TOKEN = 'development'


def on_message(message):
    print('new message from handler', message)


notifier = Notifier(on_message=on_message, server_address=SERVER_ADDRESS,
                    server_api_token=SERVER_API_TOKEN)


async def main():
    task = asyncio.create_task(notifier.connect())

    await asyncio.sleep(0.2)
    await notifier.subscribe_server_notification()

    await task


asyncio.run(main())
