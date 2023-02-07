"""
Kiln Connect module.

This is the entrypoint of the Kiln SDK.
"""

from dataclasses import dataclass

from .eth import Ethereum
from .errors import *


class Env:
    """
    Kiln environments available.
    """
    DEVNET = 'devnet'
    TESTNET = 'testnet'
    MAINNET = 'mainnet'

    @staticmethod
    def values():
        return [Env.DEVNET, Env.TESTNET, Env.MAINNET]


@dataclass
class Config:
    api_url: str
    api_token: str


def get_api_url(env: str) -> str:
    """
    Returns the Kiln API url for the given environment.
    """
    if env not in Env.values():
        raise InvalidEnvError(f"{env} not in {Env.values()}")

    api_url = f"https://api.{env}.kiln.fi"

    if env == Env.MAINNET:
        api_url = "https://api.kiln.fi"

    return api_url


class Kiln:
    """
    Main class for the Kiln Connect SDK.

    Each protocol is represented by a member handling possible staking
    API calls.
    """

    def __init__(self, env: str, api_token: str):
        cfg = Config(
            api_url=get_api_url(env), api_token=api_token)

        self.eth = Ethereum(cfg)
