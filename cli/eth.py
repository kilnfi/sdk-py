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
import click

from rich.console import Console
from rich.table import Table
from typing import Optional

import kiln_connect


eth = typer.Typer(
    name='eth', help='Staking utilities for Ethereum', no_args_is_help=True)


console = Console()
error_console = Console(stderr=True)


def wei_to_eth(wei: str) -> str:
    """Quick helper to pretty print WEI to ETH.
    """
    eth = str(round(int(wei) / 1e18, 3))
    return f"{eth}Ξ"


@ eth.command("stakes")
def ethereum_stakes(
        validators: Optional[list[str]] = None,
        wallets: Optional[list[str]] = None,
        accounts: Optional[list[str]] = None):
    """Show Ethereum Stake status.
    """
    if not validators and not wallets and not accounts:
        raise typer.BadParameter(
            'need at least one of --validators, --wallets, --accounts')

    host = os.getenv('KILN_API_URL')
    access_token = os.getenv('KILN_API_TOKEN')
    kc = kiln_connect.KilnConnect(host, access_token)

    stakes = []
    if validators:
        stakes.extend(kc.eth.get_eth_stakes(validators=validators).data)
    if wallets:
        stakes.extend(kc.eth.get_eth_stakes(wallets=wallets).data)
    if accounts:
        stakes.extend(kc.eth.get_eth_stakes(accounts=accounts).data)

    table = Table('Stake', 'Status', 'Balance', 'Rewards')
    for stake in stakes:
        table.add_row(
            stake.validator_address, stake.state, wei_to_eth(stake.balance), wei_to_eth(stake.rewards))
    console.print(table)


@ eth.command("network-stats")
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
