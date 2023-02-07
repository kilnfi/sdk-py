"""
Kiln Connect Ethereum.
"""

import requests

from dataclasses import dataclass
from typing import Optional

from .helpers import check_http_response


class Ethereum:
    """Wrapper around the Kiln Ethereum API.
    """

    def __init__(self, config):
        self._config = config

    def _query_for(self, resource: str) -> tuple[str, dict]:
        """
        Returns the API URL and headers for the query to perform against resource.
        """
        return f"{self._config.api_url}/v1/eth/{resource}", {"Authorization": f"Bearer {self._config.api_token}"}

    def get_stakes_by_accounts(self, accounts: list[str]) -> list[dict]:
        """
        List Ethereum stakes by Kiln account.
        """
        endpoint, headers = self._query_for('stakes')
        response = requests.get(
            endpoint, params={"accounts": ",".join(accounts)}, headers=headers)
        check_http_response(response)
        return response.json().get('data')

    def get_stakes_by_validators(self, validators: list[str]) -> list[dict]:
        """
        List Ethereum stakes by validator public key.
        """
        endpoint, headers = self._query_for('stakes')
        response = requests.get(
            endpoint, params={"validators": ",".join(validators)}, headers=headers)
        check_http_response(response)
        return response.json().get('data')

    def get_stakes_by_wallets(self, wallets: list[str]) -> list[dict]:
        """
        List Ethereum stakes by wallet.
        """
        endpoint, headers = self._query_for('stakes')
        response = requests.get(
            endpoint, params={"wallets": ",".join(wallets)}, headers=headers)
        check_http_response(response)
        return response.json().get('data')
