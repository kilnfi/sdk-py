"""Account commands.

This file contains multiple CLI commands showcasing how to use the
KilnConnect SDK to manage Kiln Accounts.

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


accounts_cli = typer.Typer(
    name='accounts', help='Account utilities for Kiln', no_args_is_help=True)


console = Console()
error_console = Console(stderr=True)


def pretty_float(f: float) -> str:
    return str(round(f, 3))


def pretty_description(description: str) -> str:
    if len(description) > 30:
        return f'{description[0:30]}...'
    return description


@accounts_cli.command("list")
def accounts_list():
    """List the Kiln accounts.
    """
    with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kc:
        accounts = kc.accounts.get_accounts().data

        table = Table('Id', 'Name', 'Created At', 'Description')
        for account in accounts:
            table.add_row(
                account.id,
                account.name,
                str(account.created_at),
                pretty_description(account.description),
            )

        console.print(table)


@accounts_cli.command("get")
def accounts_get(id: str):
    """Show the specified Kiln account.
    """
    with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kc:
        account = kc.accounts.get_account(id=id).data

        table = Table('Id', 'Name', 'Created At', 'Description')
        table.add_row(
            account.id,
            account.name,
            str(account.created_at),
            pretty_description(account.description),
        )

        console.print(table)


@accounts_cli.command("create")
def accounts_create(name: str, description: str):
    """Create a Kiln account.
    """
    with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kc:
        payload = kiln_connect.openapi_client.AccountPayload(
            name=name,
            description=description,
        )
        account = kc.accounts.post_account(payload).data

        table = Table('Id', 'Name', 'Created At', 'Description')
        table.add_row(
            account.id,
            account.name,
            str(account.created_at),
            pretty_description(account.description),
        )

        console.print(table)


@accounts_cli.command("update")
def accounts_update(id: str, name: str, description: str):
    """Update a Kiln account.
    """
    with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kc:
        payload = kiln_connect.openapi_client.AccountPayload(
            name=name,
            description=description,
        )
        account = kc.accounts.put_account(id, payload).data

        table = Table('Id', 'Name', 'Created At', 'Description')
        table.add_row(
            account.id,
            account.name,
            str(account.created_at),
            pretty_description(account.description),
        )

        console.print(table)


@accounts_cli.command("portfolio")
def accounts_portfolio(id: str):
    """Show Kiln portfolio of an account.
    """
    with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kc:
        portfolio = kc.accounts.get_account_portfolio(id).data

        table = Table('Token', 'Balance $', 'Balance Token',
                      'Rewards $', 'Rewards Token', 'Active Stakes')

        table.add_row(
            'Global',
            f'{pretty_float(portfolio.total_balance_usd)}$ (100.0%)',
            'n/a',
            f'{pretty_float(portfolio.total_rewards_usd)}$ (100.0%)',
            'n/a',
            f'{portfolio.total_active_stakes}/{portfolio.total_stakes}')

        for p in portfolio.protocols:
            table.add_row(
                p.name,
                f'{pretty_float(p.total_balance.amount_usd)}$ ({pretty_float(p.balance_share_percent) or "0.0"}%)',
                f'{pretty_float(p.total_balance.amount)}{p.token}',
                f'{pretty_float(p.total_rewards.amount_usd)}$ ({pretty_float(p.rewards_share_percent) or "0.0"}%)',
                f'{pretty_float(p.total_rewards.amount)}{p.token}',
                f'{portfolio.total_active_stakes}/{portfolio.total_stakes}',
            )

        console.print(table)
