"""
RecordingApi used to manage rooms
"""

from jellyfish._openapi_client import AuthenticatedClient
from jellyfish._openapi_client.api.recording import get_recordings, delete_recording
from jellyfish._openapi_client.models import Error


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
        self._client = AuthenticatedClient(
            f"{protocol}://{server_address}", token=server_api_token
        )

    def get_list(self) -> list:
        """Returns a list of available recordings"""

        return self._request(get_recordings).data

    def delete(self, recording_id: str):
        """Deletes recording with given id"""

        return self._request(delete_recording, recording_id=recording_id)

    def _request(self, method, **kwargs):
        resp = method.sync(client=self._client, **kwargs)
        if isinstance(resp, Error):
            raise RuntimeError(resp.errors)

        return resp
