from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_peer_json_body import AddPeerJsonBody
from ...models.error import Error
from ...models.peer_details_response import PeerDetailsResponse
from ...types import Response


def _get_kwargs(
    room_id: str,
    *,
    json_body: AddPeerJsonBody,
) -> Dict[str, Any]:
    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/room/{room_id}/peer".format(
            room_id=room_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, PeerDetailsResponse]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = PeerDetailsResponse.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Error.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = Error.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, PeerDetailsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    room_id: str,
    *,
    client: AuthenticatedClient,
    json_body: AddPeerJsonBody,
) -> Response[Union[Error, PeerDetailsResponse]]:
    """Create peer

    Args:
        room_id (str):
        json_body (AddPeerJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PeerDetailsResponse]]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    room_id: str,
    *,
    client: AuthenticatedClient,
    json_body: AddPeerJsonBody,
) -> Optional[Union[Error, PeerDetailsResponse]]:
    """Create peer

    Args:
        room_id (str):
        json_body (AddPeerJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PeerDetailsResponse]
    """

    return sync_detailed(
        room_id=room_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    room_id: str,
    *,
    client: AuthenticatedClient,
    json_body: AddPeerJsonBody,
) -> Response[Union[Error, PeerDetailsResponse]]:
    """Create peer

    Args:
        room_id (str):
        json_body (AddPeerJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PeerDetailsResponse]]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    room_id: str,
    *,
    client: AuthenticatedClient,
    json_body: AddPeerJsonBody,
) -> Optional[Union[Error, PeerDetailsResponse]]:
    """Create peer

    Args:
        room_id (str):
        json_body (AddPeerJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PeerDetailsResponse]
    """

    return (
        await asyncio_detailed(
            room_id=room_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
