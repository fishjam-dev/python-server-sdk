# coding: utf-8

"""
    Python API wrapper for Jellyfish Media Server

    The version of the OpenAPI document: 0.2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictStr, conint

from typing import Optional

from jellyfish._openapi_client.models.hls_skip import HlsSkip

from jellyfish._openapi_client.api_client import ApiClient
from jellyfish._openapi_client.api_response import ApiResponse
from jellyfish._openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError,
)


class DefaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def jellyfish_web_hls_controller_index(
        self,
        room_id: Annotated[StrictStr, Field(..., description="Room id")],
        filename: Annotated[StrictStr, Field(..., description="Name of the file")],
        range: Annotated[
            Optional[StrictStr], Field(description="Byte range of partial segment")
        ] = None,
        hls_msn: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="Segment sequence number"),
        ] = None,
        hls_part: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="Partial segment sequence number"),
        ] = None,
        hls_skip: Annotated[
            Optional[HlsSkip], Field(description="Is delta manifest requested")
        ] = None,
        **kwargs
    ) -> str:  # noqa: E501
        """Send file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.jellyfish_web_hls_controller_index(room_id, filename, range, hls_msn, hls_part, hls_skip, async_req=True)
        >>> result = thread.get()

        :param room_id: Room id (required)
        :type room_id: str
        :param filename: Name of the file (required)
        :type filename: str
        :param range: Byte range of partial segment
        :type range: str
        :param hls_msn: Segment sequence number
        :type hls_msn: int
        :param hls_part: Partial segment sequence number
        :type hls_part: int
        :param hls_skip: Is delta manifest requested
        :type hls_skip: HlsSkip
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: str
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            raise ValueError(
                "Error! Please call the jellyfish_web_hls_controller_index_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            )
        return self.jellyfish_web_hls_controller_index_with_http_info(
            room_id, filename, range, hls_msn, hls_part, hls_skip, **kwargs
        )  # noqa: E501

    @validate_arguments
    def jellyfish_web_hls_controller_index_with_http_info(
        self,
        room_id: Annotated[StrictStr, Field(..., description="Room id")],
        filename: Annotated[StrictStr, Field(..., description="Name of the file")],
        range: Annotated[
            Optional[StrictStr], Field(description="Byte range of partial segment")
        ] = None,
        hls_msn: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="Segment sequence number"),
        ] = None,
        hls_part: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="Partial segment sequence number"),
        ] = None,
        hls_skip: Annotated[
            Optional[HlsSkip], Field(description="Is delta manifest requested")
        ] = None,
        **kwargs
    ) -> ApiResponse:  # noqa: E501
        """Send file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.jellyfish_web_hls_controller_index_with_http_info(room_id, filename, range, hls_msn, hls_part, hls_skip, async_req=True)
        >>> result = thread.get()

        :param room_id: Room id (required)
        :type room_id: str
        :param filename: Name of the file (required)
        :type filename: str
        :param range: Byte range of partial segment
        :type range: str
        :param hls_msn: Segment sequence number
        :type hls_msn: int
        :param hls_part: Partial segment sequence number
        :type hls_part: int
        :param hls_skip: Is delta manifest requested
        :type hls_skip: HlsSkip
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(str, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            "room_id",
            "filename",
            "range",
            "hls_msn",
            "hls_part",
            "hls_skip",
        ]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method jellyfish_web_hls_controller_index" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["room_id"]:
            _path_params["room_id"] = _params["room_id"]

        if _params["filename"]:
            _path_params["filename"] = _params["filename"]

        # process the query parameters
        _query_params = []
        if _params.get("hls_msn") is not None:  # noqa: E501
            _query_params.append(("_HLS_msn", _params["hls_msn"]))

        if _params.get("hls_part") is not None:  # noqa: E501
            _query_params.append(("_HLS_part", _params["hls_part"]))

        if _params.get("hls_skip") is not None:  # noqa: E501
            _query_params.append(("_HLS_skip", _params["hls_skip"].value))

        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        if _params["range"]:
            _header_params["range"] = _params["range"]

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings = ["authorization"]  # noqa: E501

        _response_types_map = {
            "200": "str",
            "404": "Error",
        }

        return self.api_client.call_api(
            "/hls/{room_id}/{filename}",
            "GET",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )