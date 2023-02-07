import rich
import typer

from rich.console import Console
from rich.table import Table
from typing import Optional

from ..sdk import Kiln
from .config import get_current_config_or_die


sol = typer.Typer(
    name='sol', help='Staking utilities for Solana', no_args_is_help=True)


console = Console()


@sol.command("stakes")
def stakes(accounts: list[str] = None, wallets: list[str] = None, stake_accounts: list[str] = None):
    """
    Show status of Solana stakes.
    """
    cfg = get_current_config_or_die()

    # Use the default configured account if no option specified.
    if not accounts and not wallets and not stake_accounts:
        accounts = [cfg.get("kiln-account")]

    k = Kiln(env=cfg.get("kiln-env"), api_token=cfg.get("kiln-api-token"))

    table = Table("Stake Account", "State", "Balance", "Rewards")

    stakes = []
    if accounts:
        stakes = k.sol.get_stakes_by_accounts(accounts)
    elif stake_accounts:
        stakes = k.sol.get_stakes_by_stake_accounts(stake_accounts)
    elif wallets:
        stakes = k.sol.get_stakes_by_wallets(wallets)
    for stake in stakes:
        table.add_row(
            stake.get('stake_account'), stake.get('state'), stake.get('balance'), stake.get('rewards'))

    console.print(table)


@sol.command("rewards")
def rewards(accounts: list[str] = None, wallets: list[str] = None, stake_accounts: list[str] = None):
    """
    Show rewards of Solana stakes.
    """
    cfg = get_current_config_or_die()

    # Use the default configured account if no option specified.
    if not accounts and not wallets and not stake_accounts:
        accounts = [cfg.get("kiln-account")]

    k = Kiln(env=cfg.get("kiln-env"), api_token=cfg.get("kiln-api-token"))

    rewards = []
    if accounts:
        rewards = k.sol.get_rewards_by_accounts(accounts)
    elif stake_accounts:
        rewards = k.sol.get_rewards_by_stake_accounts(stake_accounts)
    elif wallets:
        rewards = k.sol.get_rewards_by_wallets(wallets)

    table = Table(
        "Date", "Active Balance", "Rewards", "Net APY")

    for reward in rewards:
        table.add_row(
            reward.get('date'), reward.get('active_balance'), reward.get('rewards'), str(reward.get('net_apy')))

    console.print(table)
