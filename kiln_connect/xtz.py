"""Tezos wrapper class.

This XTZ class is meant to accessed via KilnConnect.xtz. It
contains helpers around tezos management.
"""

from kiln_connect.integrations import Integrations
from kiln_connect.openapi_client import (
    ApiClient,
)
from kiln_connect.openapi_client import (
    XtzApi,
)


class XTZ(XtzApi):
    """Wrapper for the Tezos API.
    """

    def __init__(self, api: ApiClient, integrations: Integrations):
        super().__init__(api)
        self.integrations = integrations
