import asyncio
import os

from jellyfish import Notifier, RoomApi
from jellyfish.events import ServerMessageTrackAdded, ServerMessageTrackType

notifier = Notifier(server_address="localhost:5002", server_api_token="development")

notifier_task = None

LIMIT = os.getenv("CI_LIMIT", None)
print(f"LIMIT: {LIMIT}")

if LIMIT is not None:
    LIMIT = int(LIMIT)


counter = 0


@notifier.on_server_notification
def handle_notification(server_notification):
    print(f"Received a notification: {server_notification}")

    if isinstance(server_notification, ServerMessageTrackAdded):
        if server_notification.track.type == ServerMessageTrackType.TRACK_TYPE_AUDIO:
            print("New audio track has been added")
        elif server_notification.track.type == ServerMessageTrackType.TRACK_TYPE_VIDEO:
            print("New video track has been added")


@notifier.on_metrics
def handle_metrics(metrics_report):
    print(f"Received WebRTC metrics: {metrics_report}")
    global counter
    if LIMIT and counter > LIMIT:
        notifier_task.cancel()
    counter += 1


async def test_notifier():
    global notifier_task
    notifier_task = asyncio.create_task(notifier.connect())

    # Wait for notifier to be ready to receive messages
    await notifier.wait_ready()

    # Create a room to trigger a server notification
    room_api = RoomApi()
    room_api.create_room()

    try:
        await notifier_task
    except asyncio.CancelledError:
        print("Notifier task canceled, exiting")


asyncio.run(test_notifier())
