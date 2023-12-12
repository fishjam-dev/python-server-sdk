# pylint: disable=locally-disabled, missing-class-docstring, missing-function-docstring, redefined-outer-name, too-few-public-methods, missing-module-docstring

import os

import pytest

from jellyfish import RecordingApi

# from jellyfish import NotFoundException


HOST = "jellyfish" if os.getenv("DOCKER_TEST") == "TRUE" else "localhost"
SERVER_ADDRESS = f"{HOST}:5002"
SERVER_API_TOKEN = "development"


@pytest.fixture
def recording_api():
    return RecordingApi(
        server_address=SERVER_ADDRESS, server_api_token=SERVER_API_TOKEN
    )


class TestGetList:
    def test_valid(self, recording_api: RecordingApi):
        all_rooms = recording_api.get_list()
        assert isinstance(all_rooms, list)


class TestDelete:
    def test_invalid_recording(self, recording_api: RecordingApi):
        with pytest.raises(Exception):
            recording_api.delete("invalid-id")
