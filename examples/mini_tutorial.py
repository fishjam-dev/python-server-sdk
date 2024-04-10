import asyncio
import os

from jellyfish import (
    ComponentOptionsFile,
    ComponentOptionsHLS,
    ComponentOptionsHLSSubscribeMode,
    Notifier,
    RoomApi,
)
from jellyfish.events import (
    ServerMessageHlsPlayable,
    ServerMessageTrackAdded,
    ServerMessageTrackType,
)

HOST = "jellyfish" if os.getenv("DOCKER_TEST") == "TRUE" else "localhost"
SERVER_ADDRESS = f"{HOST}:5002"


notifier = Notifier(server_address=SERVER_ADDRESS, server_api_token="development")

notifier_task = None


@notifier.on_server_notification
def handle_notification(server_notification):
    print(f"Received a notification: {server_notification}")

    if isinstance(server_notification, ServerMessageTrackAdded):
        if server_notification.track.type == ServerMessageTrackType.TRACK_TYPE_AUDIO:
            print("New audio track has been added")
        elif server_notification.track.type == ServerMessageTrackType.TRACK_TYPE_VIDEO:
            print("New video track has been added")
    elif isinstance(server_notification, ServerMessageHlsPlayable):
        print("HLS stream is playable")
        notifier_task.cancel()


@notifier.on_metrics
def handle_metrics(metrics_report):
    pass


async def test_notifier():
    global notifier_task
    notifier_task = asyncio.create_task(notifier.connect())

    # Wait for notifier to be ready to receive messages
    await notifier.wait_ready()

    room_api = RoomApi(server_address=SERVER_ADDRESS)

    # Create a room to trigger a server notification with h264 as a codec,
    # that allow to use HLS.
    address, room = room_api.create_room(video_codec="h264")

    # Create new room api with returned jellyfish address as a room could be
    # created on a different jellyfish instance
    # (if you communicate with a cluster of jellyfishes)
    room_api = RoomApi(server_address=address)

    # Add HLS component with manual subscribe mode
    hls_component = room_api.add_component(
        room.id,
        ComponentOptionsHLS(subscribe_mode=ComponentOptionsHLSSubscribeMode.MANUAL),
    )

    # Add File Component
    file_component = room_api.add_component(room.id, ComponentOptionsFile("video.h264"))

    # Subscribe on specific component
    room_api.subscribe(room.id, hls_component.id, [file_component.id])

    try:
        await notifier_task
    except asyncio.CancelledError:
        print("Notifier task canceled, exiting")


asyncio.run(test_notifier())
