import asyncio

from jellyfish._notifier import Notifier

URI = 'ws://localhost:5002/socket/server/websocket'
API_TOKEN = 'development'

SERVER_ADDRESS = 'localhost:5002'
SERVER_API_TOKEN = 'development'


notifier = Notifier(server_address=SERVER_ADDRESS,
                    server_api_token=SERVER_API_TOKEN)


@notifier.on_server_notification
def handler(server_notification):
    print('new message from handler', server_notification)


asyncio.run(notifier.connect())

print('after asyncio.run')
