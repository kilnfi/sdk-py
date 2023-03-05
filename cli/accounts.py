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


@accounts_cli.command("list")
def accounts_list():
    """Show Kiln accounts.
    """
    with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kc:
        accounts = kc.accounts.get_accounts().data

        table = Table('Id', 'Name', 'Created At', 'Description')
        for account in accounts:
            table.add_row(
                account.id,
                account.name,
                account.created_at,
                account.description)

        console.print(table)
