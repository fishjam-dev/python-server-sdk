from jellyfish.protos.jellyfish import server_notifications_pb2

msg = server_notifications_pb2.ServerMessage.HlsPlayable()
msg.room_id = "dupsko"

print('msg:', msg)