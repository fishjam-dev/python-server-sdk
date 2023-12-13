from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_component_json_body import AddComponentJsonBody
from ...models.component_details_response import ComponentDetailsResponse
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    room_id: str,
    *,
    json_body: AddComponentJsonBody,
) -> Dict[str, Any]:
    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/room/{room_id}/component".format(
            room_id=room_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ComponentDetailsResponse, Error]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = ComponentDetailsResponse.from_dict(response.json())

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
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ComponentDetailsResponse, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    room_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: AddComponentJsonBody,
) -> Response[Union[ComponentDetailsResponse, Error]]:
    """Creates the component and adds it to the room

    Args:
        room_id (str):
        json_body (AddComponentJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ComponentDetailsResponse, Error]]
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
    client: Union[AuthenticatedClient, Client],
    json_body: AddComponentJsonBody,
) -> Optional[Union[ComponentDetailsResponse, Error]]:
    """Creates the component and adds it to the room

    Args:
        room_id (str):
        json_body (AddComponentJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ComponentDetailsResponse, Error]
    """

    return sync_detailed(
        room_id=room_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    room_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: AddComponentJsonBody,
) -> Response[Union[ComponentDetailsResponse, Error]]:
    """Creates the component and adds it to the room

    Args:
        room_id (str):
        json_body (AddComponentJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ComponentDetailsResponse, Error]]
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
    client: Union[AuthenticatedClient, Client],
    json_body: AddComponentJsonBody,
) -> Optional[Union[ComponentDetailsResponse, Error]]:
    """Creates the component and adds it to the room

    Args:
        room_id (str):
        json_body (AddComponentJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ComponentDetailsResponse, Error]
    """

    return (
        await asyncio_detailed(
            room_id=room_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
