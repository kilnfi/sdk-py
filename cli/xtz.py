"""Tezos commands.

This file contains multiple CLI commands showcasing how to use the
KilnConnect SDK to interact with the Tezos blockchain.

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


xtz_cli = typer.Typer(
    name='xtz', help='Staking utilities for Tezos', no_args_is_help=True)


console = Console()
error_console = Console(stderr=True)


@xtz_cli.command("network-stats")
def xtz_network_stats():
    """Show Tezos Network Stats.
    """
    with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kc:
        ns = kc.xtz.get_xtz_network_stats()

        table = Table('Network Gross APY %')
        table.add_row(
            str(round(ns.data.network_gross_apy, 3)))

        console.print(table)
