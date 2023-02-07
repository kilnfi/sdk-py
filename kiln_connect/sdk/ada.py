"""
Kiln Connect Cardano.
"""

import requests

from dataclasses import dataclass
from typing import Optional

from .helpers import check_http_response


class Cardano:
    """Wrapper around the Kiln Cardano API.
    """

    def __init__(self, config):
        self._config = config

    def _query_for(self, resource: str) -> tuple[str, dict]:
        """
        Returns the API URL and headers for the query to perform against an Cardano resource.
        """
        return f"{self._config.api_url}/v1/ada/{resource}", {"Authorization": f"Bearer {self._config.api_token}"}

    def get_stakes_by_accounts(self, accounts: list[str]) -> list[dict]:
        """
        List Cardano stakes by Kiln account.
        """
        endpoint, headers = self._query_for('stakes')
        response = requests.get(
            endpoint, params={"accounts": ",".join(accounts)}, headers=headers)
        check_http_response(response)
        return response.json().get('data')

    def get_stakes_by_stake_addresses(self, stake_addresses: list[str]) -> list[dict]:
        """
        List Cardano stakes by stake addresses.
        """
        endpoint, headers = self._query_for('stakes')
        response = requests.get(
            endpoint, params={"stake_addresses": ",".join(stake_addresses)}, headers=headers)
        check_http_response(response)
        return response.json().get('data')

    def get_stakes_by_wallets(self, wallets: list[str]) -> list[dict]:
        """
        List Cardano stakes by wallet.
        """
        endpoint, headers = self._query_for('stakes')
        response = requests.get(
            endpoint, params={"wallets": ",".join(wallets)}, headers=headers)
        check_http_response(response)
        return response.json().get('data')

    def get_rewards_by_accounts(self, accounts: list[str]) -> list[dict]:
        """
        List Cardano rewards by Kiln account.
        """
        endpoint, headers = self._query_for('rewards')
        response = requests.get(
            endpoint, params={"accounts": ",".join(accounts)}, headers=headers)
        check_http_response(response)
        return response.json().get('data')

    def get_rewards_by_stake_addresses(self, stake_addresses: list[str]) -> list[dict]:
        """
        List Cardano rewards by stake addresses.
        """
        endpoint, headers = self._query_for('rewards')
        response = requests.get(
            endpoint, params={"stake_addresses": ",".join(stake_addresses)}, headers=headers)
        check_http_response(response)
        return response.json().get('data')

    def get_rewards_by_wallets(self, wallets: list[str]) -> list[dict]:
        """
        List Cardano rewards by wallet.
        """
        endpoint, headers = self._query_for('rewards')
        response = requests.get(
            endpoint, params={"wallets": ",".join(wallets)}, headers=headers)
        check_http_response(response)
        return response.json().get('data')
