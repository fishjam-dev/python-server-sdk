# Jellyfish Python Server SDK

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/jellyfish-dev/python-server-sdk/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/jellyfish-dev/python-server-sdk/tree/main)

Python server SDK for the [Jellyfish Media Server](https://github.com/jellyfish-dev/jellyfish).

Read the docs [here](https://jellyfish-dev.github.io/python-server-sdk/jellyfish.html)

## Installation

```
pip install python-server-sdk
```

## Usage

The SDK exports two main classes for interacting with Jellyfish server:
`RoomApi` and `Notifier`.

`RoomApi` wraps http REST api calls, while `Notifier` is responsible for receiving real-time updates from the server.

#### RoomApi

Create a `RoomApi` instance, providing the jellyfish server address and api token

```python
from jellyfish import RoomApi

room_api = RoomApi(server_address='localhost:5002', server_api_token='development')
```

You can use it to interact with Jellyfish, manage rooms, peers and components

```python
# Create a room
jellyfish_address, room = room_api.create_room(video_codec='h264')
# 'localhost:5002', Room(components=[], config=RoomConfig(max_peers=None, video_codec='h264'), id='5a099a31-0eb2-4c28-84af-a1ec55c228af', peers=[]))

# Add peer to the room
from jellyfish import PeerOptionsWebRTC

peer_token, peer_webrtc = room_api.add_peer(room.id, options=PeerOptionsWebRTC())
# 'AgDYfrCSigFiAA', Peer(id='2869fb5', status=<PeerStatus.DISCONNECTED: 'disconnected'>, type='webrtc')

# Add component to the room
from jellyfish import ComponentOptionsHLS

component_hls = room_api.add_component(room.id, options=ComponentOptionsHLS())
# Component(actual_instance=ComponentHLS(id='c0dfab50-cafd-438d-985e-7b8f97ae55e3', metadata=ComponentMetadataHLS(low_latency=False, playable=False), type='hls'))
```

#### Notifier

Create `Notifier` instance
```python
from jellyfish import Notifier

notifier = Notifier(server_address='localhost:5002', server_api_token='development')
```

Then define handlers for incoming messages
```python
@notifier.on_server_notification
def handle_notification(server_notification):
    print(f'Received a notification: {server_notification}')

@notifier.on_metrics
def handle_metrics(metrics_report):
    print(f'Received WebRTC metrics: {metrics_report}')
```

After that you can start the notifier
```python
async def test_notifier():
    notifier_task = asyncio.create_task(notifier.connect())

    # Wait for notifier to be ready to receive messages
    await notifier.wait_ready()

    # Create a room to trigger a server notification
    room_api = RoomApi()
    room_api.create_room()

    await notifier_task

asyncio.run(test_notifier())

# Received a notification: ServerMessageRoomCreated(room_id='69a3fd1a-6a4d-47bc-ae54-0c72b0d05e29')
# Received WebRTC metrics: ServerMessageMetricsReport(metrics='{}')
```

## Testing

You can test the SDK against a local instance of Jellyfish by running
```console
pytest
```

Make sure to use the default configuration for Jellyfish

Alternatively you can test using Docker
```console
docker-compose -f docker-compose-test.yaml run test
```

## Copyright and License

Copyright 2023, [Software Mansion](https://swmansion.com/?utm_source=git&utm_medium=readme&utm_campaign=jellyfish)

[![Software Mansion](https://logo.swmansion.com/logo?color=white&variant=desktop&width=200&tag=membrane-github)](https://swmansion.com/?utm_source=git&utm_medium=readme&utm_campaign=jellyfish)

Licensed under the [Apache License, Version 2.0](LICENSE)
