from jellyfish._openapi_client.client import AuthenticatedClient
from jellyfish._openapi_client.models import Error
from jellyfish._openapi_client.types import Response
from jellyfish.errors import HTTPError


class BaseApi:
    def __init__(
        self,
        server_address: str = "localhost:5002",
        server_api_token: str = "development",
        secure: bool = False,
    ):
        protocol = "https" if secure else "http"

        self.client = AuthenticatedClient(
            f"{protocol}://{server_address}", token=server_api_token
        )

    def _request(self, method, **kwargs):
        response: Response = method.sync_detailed(client=self.client, **kwargs)

        if isinstance(response.parsed, Error):
            raise HTTPError.from_response(response)

        return response.parsed
