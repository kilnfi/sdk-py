"""
Kiln Connect Helpers.
"""

from .errors import *


def check_http_response(response: object) -> None:
    """
    Check response verifies the HTTP response succeeded.
    """
    if response.status_code >= 400 and response.status_code < 500:
        raise KilnInvalidRequestError
    if response.status_code >= 500 and response.status_code < 600:
        raise KilnInternalError
