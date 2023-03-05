"""Accounts wrapper class.

This Accounts class is meant to accessed via KilnConnect.accounts. It
contains helpers around accounts management.
"""

from kiln_connect.integrations import Integrations
from kiln_connect.openapi_client import (
    ApiClient,
)
from kiln_connect.openapi_client import (
    AccountsApi,
)


class Accounts(AccountsApi):
    """Wrapper for the Accounts API.
    """

    def __init__(self, api: ApiClient, integrations: Integrations):
        super().__init__(api)
        self.integrations = integrations
