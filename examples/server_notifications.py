import asyncio

from jellyfish import Notifier, RoomApi

notifier = Notifier(server_address='localhost:5002', server_api_token='development')

@notifier.on_server_notification
def handle_notification(server_notification):
    print(f'Received a notification: {server_notification}')

@notifier.on_metrics
def handle_metrics(metrics_report):
    print(f'Received WebRTC metrics: {metrics_report}')

async def test_notifier():
    notifier_task = asyncio.create_task(notifier.connect())

    # Wait for notifier to be ready to receive messages
    await notifier.wait_ready()

    # Create a room to trigger a server notification
    room_api = RoomApi()
    room_api.create_room()

    await notifier_task

asyncio.run(test_notifier())