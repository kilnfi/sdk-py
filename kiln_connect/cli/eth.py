import typer


eth = typer.Typer(name='eth', help='Staking utilities for Ethereum', no_args_is_help=True)


@eth.command("stakes")
def stakes():
    """
    List Ethereum stakes.
    """
    typer.echo(f"listing stakes")


@eth.command("rewards")
def stakes():
    """
    Show Ethereum rewards for a stake.
    """
    typer.echo(f"listing rewards")
