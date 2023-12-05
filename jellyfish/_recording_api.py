"""
RecordingApi used to manage rooms
"""

from jellyfish import _openapi_client as jellyfish_api


class RecordingApi:
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

        protocol = "https" if secure else "http"
        self._configuration = jellyfish_api.Configuration(
            host=f"{protocol}://{server_address}", access_token=server_api_token
        )

        self._api_client = jellyfish_api.ApiClient(self._configuration)
        self._recording_api = jellyfish_api.RecordingApi(self._api_client)

    def get_list(self) -> list:
        """Returns a list of available recordings"""

        return self._recording_api.get_recordings().data

    def delete(self, recording_id: str):
        """Deletes recording with given id"""

        return self._recording_api.delete_recording(recording_id)
