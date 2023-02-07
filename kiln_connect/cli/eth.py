import rich
import typer

from rich.console import Console
from rich.table import Table
from typing import Optional

from ..sdk import Kiln
from .config import get_current_config_or_die


eth = typer.Typer(
    name='eth', help='Staking utilities for Ethereum', no_args_is_help=True)


console = Console()


@eth.command("stakes")
def stakes(accounts: list[str] = None, wallets: list[str] = None, validators: list[str] = None):
    """
    Show status of Ethereum stakes.
    """
    cfg = get_current_config_or_die()

    if not accounts and not wallets and not validators:
        accounts = [cfg.get("kiln-account")]

    k = Kiln(env=cfg.get("kiln-env"), api_token=cfg.get("kiln-api-token"))

    table = Table("Stake", "Status", "Rewards")

    stakes = []
    if accounts:
        stakes += k.eth.get_stakes_by_accounts(accounts)
    if validators:
        stakes += k.eth.get_stakes_by_validators(validators)
    if wallets:
        stakes += k.eth.get_stakes_by_wallets(wallets)

    for stake in stakes:
        table.add_row(
            stake.get('validator_address'), stake.get('state'), stake.get('rewards'))

    console.print(table)
