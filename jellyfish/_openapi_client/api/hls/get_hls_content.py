from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    room_id: str,
    filename: str,
    *,
    field_hls_msn: Union[Unset, None, int] = UNSET,
    field_hls_part: Union[Unset, None, int] = UNSET,
    field_hls_skip: Union[Unset, None, str] = UNSET,
    range_: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(range_, Unset):
        headers["range"] = range_

    params: Dict[str, Any] = {}
    params["_HLS_msn"] = field_hls_msn

    params["_HLS_part"] = field_hls_part

    params["_HLS_skip"] = field_hls_skip

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/hls/{room_id}/{filename}".format(
            room_id=room_id,
            filename=filename,
        ),
        "params": params,
        "headers": headers,
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
    room_id: str,
    filename: str,
    *,
    client: Union[AuthenticatedClient, Client],
    field_hls_msn: Union[Unset, None, int] = UNSET,
    field_hls_part: Union[Unset, None, int] = UNSET,
    field_hls_skip: Union[Unset, None, str] = UNSET,
    range_: Union[Unset, str] = UNSET,
) -> Response[Union[Error, str]]:
    """Retrieve HLS Content

    Args:
        room_id (str):
        filename (str):
        field_hls_msn (Union[Unset, None, int]): Segment sequence number Example: 10.
        field_hls_part (Union[Unset, None, int]): Partial segment sequence number Example: 10.
        field_hls_skip (Union[Unset, None, str]): Is delta manifest requested Example: True.
        range_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, str]]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        filename=filename,
        field_hls_msn=field_hls_msn,
        field_hls_part=field_hls_part,
        field_hls_skip=field_hls_skip,
        range_=range_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    room_id: str,
    filename: str,
    *,
    client: Union[AuthenticatedClient, Client],
    field_hls_msn: Union[Unset, None, int] = UNSET,
    field_hls_part: Union[Unset, None, int] = UNSET,
    field_hls_skip: Union[Unset, None, str] = UNSET,
    range_: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, str]]:
    """Retrieve HLS Content

    Args:
        room_id (str):
        filename (str):
        field_hls_msn (Union[Unset, None, int]): Segment sequence number Example: 10.
        field_hls_part (Union[Unset, None, int]): Partial segment sequence number Example: 10.
        field_hls_skip (Union[Unset, None, str]): Is delta manifest requested Example: True.
        range_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, str]
    """

    return sync_detailed(
        room_id=room_id,
        filename=filename,
        client=client,
        field_hls_msn=field_hls_msn,
        field_hls_part=field_hls_part,
        field_hls_skip=field_hls_skip,
        range_=range_,
    ).parsed


async def asyncio_detailed(
    room_id: str,
    filename: str,
    *,
    client: Union[AuthenticatedClient, Client],
    field_hls_msn: Union[Unset, None, int] = UNSET,
    field_hls_part: Union[Unset, None, int] = UNSET,
    field_hls_skip: Union[Unset, None, str] = UNSET,
    range_: Union[Unset, str] = UNSET,
) -> Response[Union[Error, str]]:
    """Retrieve HLS Content

    Args:
        room_id (str):
        filename (str):
        field_hls_msn (Union[Unset, None, int]): Segment sequence number Example: 10.
        field_hls_part (Union[Unset, None, int]): Partial segment sequence number Example: 10.
        field_hls_skip (Union[Unset, None, str]): Is delta manifest requested Example: True.
        range_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, str]]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        filename=filename,
        field_hls_msn=field_hls_msn,
        field_hls_part=field_hls_part,
        field_hls_skip=field_hls_skip,
        range_=range_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    room_id: str,
    filename: str,
    *,
    client: Union[AuthenticatedClient, Client],
    field_hls_msn: Union[Unset, None, int] = UNSET,
    field_hls_part: Union[Unset, None, int] = UNSET,
    field_hls_skip: Union[Unset, None, str] = UNSET,
    range_: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, str]]:
    """Retrieve HLS Content

    Args:
        room_id (str):
        filename (str):
        field_hls_msn (Union[Unset, None, int]): Segment sequence number Example: 10.
        field_hls_part (Union[Unset, None, int]): Partial segment sequence number Example: 10.
        field_hls_skip (Union[Unset, None, str]): Is delta manifest requested Example: True.
        range_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, str]
    """

    return (
        await asyncio_detailed(
            room_id=room_id,
            filename=filename,
            client=client,
            field_hls_msn=field_hls_msn,
            field_hls_part=field_hls_part,
            field_hls_skip=field_hls_skip,
            range_=range_,
        )
    ).parsed
