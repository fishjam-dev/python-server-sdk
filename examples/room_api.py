# Create a room

from jellyfish import ComponentOptionsHLS, PeerOptionsWebRTC, RoomApi


room_api = RoomApi(server_address="localhost:5002", server_api_token="development")

jellyfish_address, room = room_api.create_room(video_codec="h264", webhook_url="http://localhost:5000/webhook")
print((jellyfish_address, room))

# '127.0.0.1:5002', Room(components=[], config=RoomConfig(max_peers=None, video_codec=<RoomConfigVideoCodec.H264: 'h264'>, webhook_url='http://localhost:5000/webhook'), id='1d905478-ccfc-44d6-a6e7-8ccb1b38d955', peers=[])

# Add peer to the room

peer_token, peer_webrtc = room_api.add_peer(room.id, options=PeerOptionsWebRTC())
print((peer_token, peer_webrtc))
# 'M8TUGhj-L11KpyG-2zBPIo', Peer(id='b1232c7e-c969-4450-acdf-ea24f3cdd7f6', status=<PeerStatus.DISCONNECTED: 'disconnected'>, type='webrtc')

# Add component to the room
component_hls = room_api.add_component(room.id, options=ComponentOptionsHLS())
print(component_hls)
# ComponentHLS(id='5f062447-a9f7-45ed-8d1b-511f77dc78ae', properties=ComponentPropertiesHLS(low_latency=False, persistent=False, playable=False, subscribe_mode=<ComponentPropertiesHLSSubscribeMode.AUTO: 'auto'>, target_window_duration=None), type='hls')