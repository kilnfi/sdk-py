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
import rich
import typer
import time

import fireblocks_sdk
from rich.console import Console
from rich.table import Table
from typing import Optional

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


@eth_cli.command("stakes")
def ethereum_stakes(identifiers: list[str], by: str = typer.Option('validator')):
    """List Ethereum Stake status.
    """
    with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kc:
        stakes = None

        if by == 'validator':
            stakes = kc.eth.get_eth_stakes(validators=identifiers).data
        elif by == 'account':
            stakes = kc.eth.get_eth_stakes(accounts=identifiers).data
        elif by == 'wallet':
            stakes = kc.eth.get_eth_stakes(wallets=identifiers).data
        else:
            raise click.UsageError(
                "Argument --by should be one of 'validator', 'account', 'wallet'")

        table = Table('Stake(s)', 'Status', 'Balance', 'Rewards')
        for stake in stakes:
            table.add_row(
                stake.validator_address,
                stake.state,
                pretty_wei_to_eth(stake.balance),
                pretty_wei_to_eth(stake.rewards))

        console.print(table)


@eth_cli.command("rewards")
def ethereum_rewards(identifiers: list[str], by: str = typer.Option('validator')):
    """View Ethereum rewards.
    """
    with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kc:
        rewards = None

        if by == 'validator':
            rewards = kc.eth.get_eth_rewards(validators=identifiers).data
        elif by == 'account':
            rewards = kc.eth.get_eth_rewards(accounts=identifiers).data
        elif by == 'wallet':
            rewards = kc.eth.get_eth_rewards(wallets=identifiers).data
        else:
            raise click.UsageError(
                "Argument --by should be one of 'validator', 'account', 'wallet'")

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
def ethereum_operations(identifiers: list[str], by: str = typer.Option('validator')):
    """List Ethereum operations.
    """
    with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kc:
        operations = None

        if by == 'validator':
            operations = kc.eth.get_eth_operations(validators=identifiers).data
        elif by == 'account':
            operations = kc.eth.get_eth_operations(accounts=identifiers).data
        elif by == 'wallet':
            operations = kc.eth.get_eth_operations(wallets=identifiers).data
        else:
            raise click.UsageError(
                "Argument --by should be one of 'validator', 'account', 'wallet'")

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
