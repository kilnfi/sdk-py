"""Ethereum commands.

This file contains multiple CLI commands showcasing how to use the
KilnConnect SDK to interact with the Ethereum blockchain.

Code here is voluntarily kept simple: it could be refactored with some
levels of abstraction to avoid repetitions, but would imply readers to
understand things unrelated to what their primary goal is: use the
SDK. So let's keep it stupid simple so the integration work is
simpler.
"""

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
def ethereum_network_stats():
    """Show Ethereum Network Stats.
    """
    host = os.getenv('KILN_API_URL')
    access_token = os.getenv('KILN_API_TOKEN')
    kc = kiln_connect.KilnConnect(host, access_token)
    ns = kc.eth.get_eth_network_stats()

    table = Table('Network Gross APY %', 'Supply Staked %')
    table.add_row(
        str(ns.data.network_gross_apy), str(ns.data.supply_staked_percent))
    console.print(table)
