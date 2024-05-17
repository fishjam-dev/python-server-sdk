from http import HTTPStatus

from fishjam._openapi_client.types import Response


class HTTPError(Exception):
    """"""

    @staticmethod
    def from_response(response: Response):
        """@private"""
        errors = response.parsed.errors
        if response.status_code == HTTPStatus.BAD_REQUEST:
            return BadRequestError(errors)

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            return UnauthorizedError(errors)

        if response.status_code == HTTPStatus.NOT_FOUND:
            return NotFoundError(errors)

        if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
            return ServiceUnavailableError(errors)


class BadRequestError(HTTPError):
    def __init__(self, errors):
        """@private"""
        super().__init__(errors)


class UnauthorizedError(HTTPError):
    def __init__(self, errors):
        """@private"""
        super().__init__(errors)


class NotFoundError(HTTPError):
    def __init__(self, errors):
        """@private"""
        super().__init__(errors)


class ServiceUnavailableError(HTTPError):
    def __init__(self, errors):
        """@private"""
        super().__init__(errors)
