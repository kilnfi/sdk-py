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


def pretty_wei_to_eth(wei: str) -> str:
    """Quick helper to pretty print WEI to ETH.
    """
    eth = str(round(int(wei) / 1e18, 3))
    return f"{eth}Ξ"


@eth.command("stakes")
def ethereum_stakes(validators: list[str]):
    """Show Ethereum Stake status.
    """
    host = os.getenv('KILN_API_URL')
    access_token = os.getenv('KILN_API_TOKEN')
    kc = kiln_connect.KilnConnect(host, access_token)

    stakes = kc.eth.get_eth_stakes(validators=validators).data

    table = Table('Stake(s)', 'Status', 'Balance', 'Rewards')
    for stake in stakes:
        table.add_row(
            stake.validator_address,
            stake.state,
            pretty_wei_to_eth(stake.balance),
            pretty_wei_to_eth(stake.rewards))

    console.print(table)


@eth.command("rewards")
def ethereum_rewards(validators: list[str]):
    """Show Ethereum rewards.
    """
    host = os.getenv('KILN_API_URL')
    access_token = os.getenv('KILN_API_TOKEN')
    kc = kiln_connect.KilnConnect(host, access_token)

    rewards = kc.eth.get_eth_rewards(validators=validators).data

    table = Table(
        'Time', 'Stake Balance', 'Consensus', 'Execution', 'Rewards', 'Gross APY')
    for reward in rewards:
        table.add_row(
            str(reward.var_date),
            pretty_wei_to_eth(reward.stake_balance),
            pretty_wei_to_eth(reward.consensus_rewards),
            pretty_wei_to_eth(reward.execution_rewards),
            pretty_wei_to_eth(reward.rewards),
            str(round(reward.gross_apy, 3)))
    console.print(table)


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
        str(round(ns.data.network_gross_apy, 3)),
        str(round(ns.data.supply_staked_percent, 3)))
    console.print(table)
