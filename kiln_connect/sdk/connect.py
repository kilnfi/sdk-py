"""
Kiln Connect module.

This is the entrypoint of the Kiln SDK.
"""


class KilnConnectError(Exception):
    pass


class InvalidEnvError(KilnConnectError):
    pass


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


def get_api_url(env: str) -> str:
    """
    Returns the Kiln API url for the given environment.
    """
    if env not in Env.values():
        raise InvalidEnvError(f"{env} not in {Env.values()}")

    api_url = f"https://api.{env}.kiln.fi/"

    if env == Env.MAINNET:
        api_url = "https://api.kiln.fi/"

    return api_url


class KilnConnect:
    """
    Main class for the Kiln Connect SDK.
    """

    def __init__(self, api_token: str, env: str, org_id: str):
        self.url = get_api_url(env)
        self.api_token = api_token
        self.org_id = org_id
