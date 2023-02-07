import typer

from . import config, eth, sol


app = typer.Typer(name='kiln-connect', add_completion=False,
                  help="all-in-one SDK for staking", no_args_is_help=True)
app.add_typer(config.config, name='config')
app.add_typer(eth.eth, name='eth')
app.add_typer(sol.sol, name='sol')
