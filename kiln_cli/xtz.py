"""Tezos commands.

This file contains multiple CLI commands showcasing how to use the
KilnConnect SDK to interact with the Tezos blockchain.

Code here is voluntarily kept simple: it could be refactored with some
levels of abstraction to avoid repetitions, but would imply readers to
understand things unrelated to what their primary goal is: use the
SDK. So let's keep it stupid simple so the integration work is
simpler.
"""
from enum import Enum

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

xtz_cli = typer.Typer(
    name='xtz', help='Staking utilities for Tezos', no_args_is_help=True)

console = Console()
error_console = Console(stderr=True)


class RewardsFormat(str, Enum):
    daily = "daily"
    cycle = "cycle"


def sort_identifiers(identifiers: list[str]) -> Tuple[list[str], list[str]]:
    """Sorts XTZ filtering identifiers in corresponding buckets.

    The Kiln XTZ API supports filtering by:

    - Tezos wallet address
    - Kiln Account ID (UUID)

    This functions returns the identifiers sorted in their corresponding bucket.
    """

    accounts = []
    wallets = []

    for identifier in identifiers:
        identifier = identifier[2:] if '0x' in identifier else identifier

        # Kiln Account UUIDs
        if re.match('^[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12}$', identifier):
            accounts.append(identifier)
            continue

        # Wallet addresses start with tz or KT1
        if re.match('^(tz|KT1)[a-zA-Z0-9]*$', identifier):
            wallets.append(identifier)
            continue

        raise click.UsageError(
            "Unknown identifier (should be a BLS validator address, an ETH wallet address or a Kiln account UUID)")

    # This is a current limit of the Kiln API, we only support one
    # filter type at a time. This removes confusion when a staked is
    # matched by multiple filters.
    if accounts and wallets:
        raise click.UsageError(
            "Identifiers should be of the same type"
        )

    return accounts or None, wallets or None


def pretty_mutez_to_tez(mutez: str) -> str:
    """Quick helper to pretty print MUTEZ to TEZ.
    """
    if not mutez:
        return 'n/a'
    tez = str(round(int(mutez) / 1e6, 6))
    return f"{tez}XTZ"


@xtz_cli.command("network-stats")
def xtz_network_stats():
    """Show Tezos Network Stats.
    """
    with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kc:
        ns = kc.xtz.get_xtz_network_stats()

        table = Table('Network Gross APY %', 'Nb Validator', 'Supply Percentage Stake', 'Updated At')
        table.add_row(
            str(round(ns.data.network_gross_apy, 3)),
            str(ns.data.nb_validators),
            str(round(ns.data.supply_staked_percent, 3)),
            str(ns.data.updated_at)
        )

        console.print(table)


@xtz_cli.command("stakes")
def xtz_stakes(identifiers: list[str]):
    """List Tezos Stake status.
    """
    with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kc:
        accounts, wallets = sort_identifiers(identifiers)

        stakes = kc.xtz.get_xtz_stakes(accounts=accounts, wallets=wallets)

        table = Table('Stake(s)', 'Baker', 'Status', 'Delegated at Block', 'Delegated Cycle', 'Activated Cycle',
                      'Balance', 'Rewards')
        for stake in stakes.data:
            table.add_row(
                stake.stake_address,
                stake.baker_address,
                stake.state,
                str(stake.delegated_block),
                str(stake.delegated_cycle),
                str(stake.activated_cycle),
                pretty_mutez_to_tez(stake.balance),
                pretty_mutez_to_tez(stake.rewards))

        console.print(table)


@xtz_cli.command("rewards")
def xtz_rewards(
        identifiers: list[str],
        response_format: RewardsFormat = typer.Option(RewardsFormat.daily, '--format')):
    """View Tezos rewards.
    """
    with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kc:
        accounts, wallets = sort_identifiers(identifiers)

        rewards = kc.xtz.get_xtz_rewards(accounts=accounts, wallets=wallets, format=response_format.value)

        if response_format == RewardsFormat.daily:
            table = Table('Date', 'Active Balance', 'Rewards', 'Gross APY')
            for reward in rewards.data:
                table.add_row(
                    str(reward.actual_instance.var_date),
                    pretty_mutez_to_tez(reward.actual_instance.active_balance),
                    pretty_mutez_to_tez(reward.actual_instance.rewards),
                    str(round(reward.actual_instance.gross_apy, 3))
                )
            console.print(table)
        elif response_format == RewardsFormat.cycle:
            table = Table('Cycle', 'Cycle Begins At', 'Active Balance', 'Rewards', 'Gross APY')
            for reward in rewards.data:
                table.add_row(
                    str(reward.actual_instance.cycle),
                    str(reward.actual_instance.cycle_begins_at),
                    pretty_mutez_to_tez(reward.actual_instance.active_balance),
                    pretty_mutez_to_tez(reward.actual_instance.rewards),
                    str(round(reward.actual_instance.gross_apy, 3)))
            console.print(table)


