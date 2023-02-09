import os
import rich
import typer

from rich.console import Console
from rich.table import Table
from typing import Optional

import openapi_client

from openapi_client.apis.tags import eth_api

eth = typer.Typer(
    name='eth', help='Staking utilities for Ethereum', no_args_is_help=True)


console = Console()


@eth.command("network-stats")
def network_stats(accounts: list[str] = None, wallets: list[str] = None, validators: list[str] = None):
    """
    Show status of Ethereum stakes.
    """

    cfg = openapi_client.Configuration()

    cfg.host = os.getenv('KILN_API_URL')
    cfg.access_token = os.getenv('KILN_API_TOKEN')

    with openapi_client.ApiClient(cfg) as api:
        eth = eth_api.ETHApi(api)
        stats = eth.get_ethereum_network_stats()
        print(stats)
