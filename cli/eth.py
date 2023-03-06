"""Ethereum commands.

This file contains multiple CLI commands showcasing how to use the
KilnConnect SDK to interact with the Ethereum blockchain.

Code here is voluntarily kept simple: it could be refactored with some
levels of abstraction to avoid repetitions, but would imply readers to
understand things unrelated to what their primary goal is: use the
SDK. So let's keep it stupid simple so the integration work is
simpler.
"""

import click
import os
import re
import rich
import typer
import time

import fireblocks_sdk
from rich.console import Console
from rich.table import Table
from typing import Optional, Tuple

import kiln_connect


eth_cli = typer.Typer(
    name='eth', help='Staking utilities for Ethereum', no_args_is_help=True)


console = Console()
error_console = Console(stderr=True)


def pretty_wei_to_eth(wei: str) -> str:
    """Quick helper to pretty print WEI to ETH.
    """
    if not wei:
        return 'n/a'
    eth = str(round(int(wei) / 1e18, 3))
    return f"{eth}Ξ"


def sort_identifiers(identifiers: list[str]) -> Tuple[list[str], list[str], list[str]]:
    """Sorts ETH filtering identifiers in corresponding buckets.

    The Kiln ETH API supports filtering by:

    - ETH2 BLS validator address (consensus address)
    - ETH1 wallet address (execution address)
    - Kiln Account ID (UUID)

    This functions returns the identifiers sorted in their corresponding bucket.
    """

    validators = []
    accounts = []
    wallets = []

    for identifier in identifiers:
        identifier = identifier[2:] if '0x' in identifier else identifier

        # Validator addresses are 96 bytes
        if re.match('^[0-9a-zA-Z]{96}$', identifier):
            validators.append(identifier)
            continue

        # Kiln Account UUIDs
        if re.match('^[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12}$', identifier):
            accounts.append(identifier)
            continue

        # Wallet addresses are 40 bytes
        if re.match('^[0-9a-zA-Z]{40}$', identifier):
            wallets.append(identifier)
            continue

        raise click.UsageError(
            "Unknown identifier (should be a BLS validator address, an ETH wallet address or a Kiln account UUID)")

    # This is a current limit of the Kiln API, we only support one
    # filter type at a time. This removes confusion when a staked is
    # matched by multiple filters.
    if (validators and accounts) or (validators and wallets) or (accounts and wallets):
        raise click.UsageError(
            "Identifiers should be of the same type"
        )

    return validators or None, accounts or None, wallets or None


@eth_cli.command("stakes")
def ethereum_stakes(identifiers: list[str]):
    """List Ethereum Stake status.
    """
    with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kc:
        validators, accounts, wallets = sort_identifiers(identifiers)

        stakes = kc.eth.get_eth_stakes(
            validators=validators, accounts=accounts, wallets=wallets).data

        table = Table('Stake(s)', 'Status', 'Balance', 'Rewards')
        for stake in stakes:
            table.add_row(
                stake.validator_address,
                stake.state,
                pretty_wei_to_eth(stake.balance),
                pretty_wei_to_eth(stake.rewards))

        console.print(table)


@eth_cli.command("rewards")
def ethereum_rewards(identifiers: list[str]):
    """View Ethereum rewards.
    """
    with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kc:
        validators, accounts, wallets = sort_identifiers(identifiers)
        rewards = kc.eth.get_eth_rewards(
            validators=validators, accounts=accounts, wallets=wallets).data

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


@eth_cli.command("operations")
def ethereum_operations(identifiers: list[str]):
    """List Ethereum operations.
    """
    with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kc:
        validators, accounts, wallets = sort_identifiers(identifiers)
        operations = kc.eth.get_eth_operations(
            validators=validators, accounts=accounts, wallets=wallets).data

        table = Table('Stake', 'Time', 'Type')
        for op in operations:
            op = op.actual_instance
            table.add_row(
                op.validator_address,
                str(op.time),
                op.type)

        console.print(table)


@eth_cli.command("network-stats")
def ethereum_network_stats():
    """Show Ethereum Network Stats.
    """
    with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kc:
        ns = kc.eth.get_eth_network_stats()

        table = Table('Network Gross APY %', 'Supply Staked %')
        table.add_row(
            str(round(ns.data.network_gross_apy, 3)),
            str(round(ns.data.supply_staked_percent, 3)))

        console.print(table)


@eth_cli.command("stake-via-fireblocks")
def ethereum_stake_via_fireblocks(account_id: str, wallet: str):
    """Stake ETH via fireblocks.
    """
    with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kc:
        kc.eth.stake('fireblocks', account_id, wallet, 32000000000000000000)
