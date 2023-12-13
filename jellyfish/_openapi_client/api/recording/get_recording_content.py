from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    recording_id: str,
    filename: str,
) -> Dict[str, Any]:
    return {
        "method": "get",
        "url": "/recording/{recording_id}/{filename}".format(
            recording_id=recording_id,
            filename=filename,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, str]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(str, response.json())
        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Error.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    recording_id: str,
    filename: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, str]]:
    """Retrieve Recording (HLS) Content

    Args:
        recording_id (str):
        filename (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, str]]
    """

    kwargs = _get_kwargs(
        recording_id=recording_id,
        filename=filename,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    recording_id: str,
    filename: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, str]]:
    """Retrieve Recording (HLS) Content

    Args:
        recording_id (str):
        filename (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, str]
    """

    return sync_detailed(
        recording_id=recording_id,
        filename=filename,
        client=client,
    ).parsed


async def asyncio_detailed(
    recording_id: str,
    filename: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, str]]:
    """Retrieve Recording (HLS) Content

    Args:
        recording_id (str):
        filename (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, str]]
    """

    kwargs = _get_kwargs(
        recording_id=recording_id,
        filename=filename,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    recording_id: str,
    filename: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, str]]:
    """Retrieve Recording (HLS) Content

    Args:
        recording_id (str):
        filename (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, str]
    """

    return (
        await asyncio_detailed(
            recording_id=recording_id,
            filename=filename,
            client=client,
        )
    ).parsed
