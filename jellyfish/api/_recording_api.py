"""
RecordingApi used to manage rooms
"""

from jellyfish._openapi_client.api.recording import delete_recording, get_recordings
from jellyfish.api._base_api import BaseApi


class RecordingApi(BaseApi):
    """Allows for managing recordings"""

    def __init__(
        self,
        server_address: str = "localhost:5002",
        server_api_token: str = "development",
        secure: bool = False,
    ):
        """
        Create RecordingApi instance, providing the jellyfish address and api token.
        Set secure to `True` for `https` and `False` for `http` connection (default).
        """

        super().__init__(
            server_address=server_address, server_api_token=server_api_token, secure=secure
        )

    def get_list(self) -> list:
        """Returns a list of available recordings"""

        return self._request(get_recordings).data

    def delete(self, recording_id: str):
        """Deletes recording with given id"""

        return self._request(delete_recording, recording_id=recording_id)
