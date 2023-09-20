from jellyfish.protos.jellyfish.jellyfish import ServerMessage

msg = server_notifications_pb2.ServerMessage.HlsPlayable()
msg.room_id = "dupsko"

print('msg:', msg)