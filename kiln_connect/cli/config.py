"""Config subcommand.

Configuration is represented by a YAML file under the user's config
directory. Because Kiln has different environments (devnet, testnet
and mainnet), there is a need to be able to switch between each.

This is done by having 3 configuration files:

- kiln-connect.devnet.yaml
- kiln-connect.testnet.yaml
- kiln-connect.mainnet.yaml

And one symlink pointing to the currently used environment:

- kiln-connect.yaml

It is possible to switch from one environment to another by using the
config switch command.
"""

import os
import rich
import textwrap
import typer
import yaml

from enum import Enum
from pathlib import Path
from typing import Optional


config = typer.Typer(
    name='config', help='Configuration of Kiln Connect CLI', no_args_is_help=True)


def get_config_dir() -> str:
    """
    Returns the path to the config directory for Kiln Connect CLI.
    """
    app_dir = typer.get_app_dir('kiln-connect')
    app_dir_path = Path(app_dir)
    app_dir_path.mkdir(parents=True, exist_ok=True)
    return app_dir


def get_config_path_for(env: str) -> Optional[dict]:
    """
    Returns the path to the kiln-connect config file for the given env.
    """
    return get_config_dir() + f"/kiln-connect.{env}.yaml"


def get_current_config_path() -> Optional[dict]:
    """
    Returns the path to the currently used kiln-connect config file.
    """
    return get_config_dir() + f"/kiln-connect.yaml"


def get_config() -> Optional[dict]:
    """
    Returns the current config.
    """
    p = get_current_config_path()
    try:
        with open(p, "r") as stream:
            return yaml.safe_load(stream)
    except:
        pass
    return None


def get_current_config_or_die() -> dict:
    """
    Returns the current config or dies asking the user to configure it.
    """
    p = get_current_config_path()
    try:
        with open(p, "r") as stream:
            return yaml.safe_load(stream)
    except:
        rich.echo(
            "[bold][red]Kiln Connect CLI[/red] was not initialized, please run `kiln-connect config init` [/bold]")
        typer.Abort()
    return None


def write_config_for(config: dict, env: str):
    """
    Writes the config.
    """
    p = get_config_path_for(env)
    with open(p, "w") as stream:
        yaml.dump(p, stream, default_flow_style=False)


def set_current_config(env: str):
    """
    Sets the current config for the given environment.
    """
    source = get_config_path_for(env)
    target = get_current_config_path()

    if os.path.exists(target):
        os.remove(target)

    os.symlink(source, target)


@config.command("init")
def init(force: bool = typer.Option(False, help="force config init.")):
    """
    Initialize the Kiln Connect CLI
    """

    rich.print(textwrap.dedent("""\
    [bold]Welcome to the [green]Kiln Connect CLI[/green]...[/bold]

    Let's initialize your environment, this should take around 2 minutes...
    """))

    typer.confirm("Are you ready to start?")

    if not force and get_config():
        rich.print(
            "config file already exists, use --force if you want to overwrite")
        typer.Exit()

    env = typer.prompt(
        "Enter the environment you want to use (devnet, testnet, or mainnet)")
    if env not in ['devnet', 'testnet', 'mainnet']:
        rich.print("invalid environment provided")
        typer.Abort()
    api_url = f"https://api.{env}.kiln.fi/"
    if env == "mainnet":
        api_url = "https://api.kiln.fi/"

    cfg = {
        "kiln-env": env,
        "kiln-api-url": api_url,
        "kiln-org": typer.prompt("Enter your Kiln Organization Identifier?"),
        "kiln-account": typer.prompt("What's your default Kiln Account Identifier?"),
        "kiln-api-token": typer.prompt("What's your Kiln API key?")
    }

    write_config_for(cfg, env)
    set_current_config(env)

    rich.print("[bold][green]Kiln Connect CLI[/green] properly initialized")
