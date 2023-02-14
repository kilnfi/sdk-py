import os
import rich
import typer

from rich.console import Console
from rich.table import Table
from typing import Optional

import kiln_connect


eth = typer.Typer(
    name='eth', help='Staking utilities for Ethereum', no_args_is_help=True)


console = Console()


@eth.command("network-stats")
def network_stats(accounts: list[str] = None, wallets: list[str] = None, validators: list[str] = None):
    """
    Show status of Ethereum stakes.
    """

    host = os.getenv('KILN_API_URL')
    access_token = os.getenv('KILN_API_TOKEN')

    kc = kiln_connect.KilnConnect(host, access_token)

    table = Table('Network Gross APY %', 'Supply Staked %')

    r = kc.eth.get_ethereum_network_stats()
    if r.response.status == 200:
        d = r.body.get('data')

        network_gross_apy = str(round(d['network_gross_apy'], 3))
        supply_staked_percent = str(round(d['supply_staked_percent'], 3))

        table.add_row(str(network_gross_apy), str(supply_staked_percent))
        console.print(table)
