import rich
import typer

from rich.console import Console
from rich.table import Table
from typing import Optional

from ..sdk import Kiln
from .config import get_current_config_or_die


ada = typer.Typer(
    name='ada', help='Staking utilities for Cardano', no_args_is_help=True)


console = Console()


@ada.command("stakes")
def stakes(accounts: list[str] = None, wallets: list[str] = None, stake_addresses: list[str] = None):
    """
    Show status of Cardano stakes.
    """
    cfg = get_current_config_or_die()

    # Use the default configured account if no option specified.
    if not accounts and not wallets and not stake_addresses:
        accounts = [cfg.get("kiln-account")]

    k = Kiln(env=cfg.get("kiln-env"), api_token=cfg.get("kiln-api-token"))

    table = Table("Stake Address", "State", "Balance", "Rewards")

    stakes = []
    if accounts:
        stakes = k.ada.get_stakes_by_accounts(accounts)
    elif stake_addresses:
        stakes = k.ada.get_stakes_by_stake_addresses(stake_addresses)
    elif wallets:
        stakes = k.ada.get_stakes_by_wallets(wallets)
    for stake in stakes:
        table.add_row(
            stake.get('stake_address'), stake.get('state'), stake.get('balance'), stake.get('rewards'))

    console.print(table)


@ada.command("rewards")
def rewards(accounts: list[str] = None, wallets: list[str] = None, stake_addresses: list[str] = None):
    """
    Show rewards of Cardano stakes.
    """
    cfg = get_current_config_or_die()

    # Use the default configured account if no option specified.
    if not accounts and not wallets and not stake_addresses:
        accounts = [cfg.get("kiln-account")]

    k = Kiln(env=cfg.get("kiln-env"), api_token=cfg.get("kiln-api-token"))

    rewards = []
    if accounts:
        rewards = k.ada.get_rewards_by_accounts(accounts)
    elif stake_addresses:
        rewards = k.ada.get_rewards_by_stake_addresses(stake_addresses)
    elif wallets:
        rewards = k.ada.get_rewards_by_wallets(wallets)

    table = Table(
        "Date", "Active Balance", "Rewards", "Net APY")

    for reward in rewards:
        table.add_row(
            reward.get('date'), reward.get('active_balance'), reward.get('rewards'), str(reward.get('net_apy')))

    console.print(table)
