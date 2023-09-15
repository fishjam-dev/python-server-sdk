# Jellyfish Python Server SDK

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/jellyfish-dev/python-server-sdk/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/jellyfish-dev/python-server-sdk/tree/main)

Python server SDK for [Jellyfish](https://github.com/jellyfish-dev/jellyfish) media server.

Read the docs [here](https://jellyfish-dev.github.io/python-server-sdk/jellyfish.html)

## Installation

You can install the latest version of the package from github:
```
pip install git+https://github.com/jellyfish-dev/python-server-sdk
```

## Usage

First create a `RoomApi` instance, providing the jellyfish server address and api token

```python
from jellyfish import RoomApi

room_api = RoomApi(server_address='localhost:5002', server_api_token='development')
```

You can use it to interact with Jellyfish managing rooms, peers and components

```python
# Create a room
jellyfish_address, room = room_api.create_room()
# 'localhost:5002', Room(components=[], id='f7cc2eac-f699-4609-ac8f-92f1ad6bea0c', peers=[])

# Add peer to the room
from jellyfish import PeerOptionsWebRTC

peer_token, peer_webrtc = room_api.add_peer(room.id, peer_type='webrtc', options=PeerOptionsWebRTC())
# 'AgDYfrCSigFiAA', Peer(id='2869fb5', status=<PeerStatus.DISCONNECTED: 'disconnected'>, type='webrtc')

# Add component to the room
component_hls = room_api.add_component(room.id, component_type='hls')
# Component(id='4c028a86', metadata=ComponentMetadata(playable=False), type='hls')
```

## Copyright and License

Copyright 2023, [Software Mansion](https://swmansion.com/?utm_source=git&utm_medium=readme&utm_campaign=jellyfish)

[![Software Mansion](https://logo.swmansion.com/logo?color=white&variant=desktop&width=200&tag=membrane-github)](https://swmansion.com/?utm_source=git&utm_medium=readme&utm_campaign=jellyfish)

Licensed under the [Apache License, Version 2.0](LICENSE)