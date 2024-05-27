import os

from fishjam import ComponentOptionsHLS, PeerOptionsWebRTC, RoomApi

HOST = "fishjam" if os.getenv("DOCKER_TEST") == "TRUE" else "localhost"
SERVER_ADDRESS = f"{HOST}:5002"

# Create a room
room_api = RoomApi(server_address=SERVER_ADDRESS, server_api_token="development")

fishjam_address, room = room_api.create_room(
    video_codec="h264", webhook_url="http://localhost:5000/webhook"
)
print(f"Fishjam address: {fishjam_address}\nRoom: \n\t{room}\n")

# Add peer to the room
response = room_api.add_peer(room.id, options=PeerOptionsWebRTC())
print(
    f"Websocket URL: {response.peer_websocket_url}\nPeer token: \n\t{response.token}\n"
    f"Peer: \n\t{response.peer}\n"
)

# Add component to the room
component_hls = room_api.add_component(room.id, options=ComponentOptionsHLS())
print(f"Component HLS: \n\t{component_hls}")
