import pytest

from jellyfish import RoomClient

server_address = "localhost:5002"
server_api_token = "development"


def test_create_room_client():
    with pytest.raises(TypeError):
        RoomClient()

    with pytest.raises(TypeError):
        RoomClient(server_address="address")

    with pytest.raises(TypeError):
        RoomClient(server_api_token="api_token")

    room_client = RoomClient(server_address="address", server_api_token="api_token")


def test_authorization():
    pass


@pytest.fixture
def room_client():
    return RoomClient(server_address=server_address, server_api_token=server_api_token)


def test_create_room(room_client):

    room = room_client.create_room(max_peers=10)


def test_delete_room(room_client):
    pass


def test_get_all_rooms(room_client):
    pass


def test_get_room(room_client):
    pass


def test_add_component(room_client):
    pass


def test_delete_component(room_client):
    pass


def test_add_peer(room_client):
    room = room_client.create_room()


def test_remove_peer(room_client):
    pass
