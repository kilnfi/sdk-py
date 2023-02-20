import os

from dataclasses import dataclass

from fireblocks_sdk import FireblocksSDK
from kiln_connect.openapi_client import ApiClient, Configuration
from kiln_connect.openapi_client.api import eth_api


class KilnError(Exception):
    """Base class for Kiln errors.
    """


@dataclass
class KilnConfig:
    """Configuration of the Kiln Connect SDK.
    """
    kiln_base_url: str
    kiln_api_token: str
    fireblocks_api_token: str
    fireblocks_raw_key_path: str

    @staticmethod
    def from_env():
        """Initialize the Config.
        """
        return KilnConfig(
            kiln_base_url=os.getenv('KILN_API_URL'),
            kiln_api_token=os.getenv('KILN_API_TOKEN'),
            fireblocks_api_token=os.getenv('FIREBLOCKS_API_KEY'),
            fireblocks_raw_key_path=os.getenv('FIREBLOCKS_RAW_KEY_PATH')
        )


class KilnConnect:
    """Main class for Kiln connect.
    """

    def __init__(self, config: KilnConfig):
        self.config = config

        cfg = Configuration(host=config.kiln_base_url)
        cfg.access_token = config.kiln_api_token

        self._api = ApiClient(
            configuration=cfg,
        )

        self.fireblocks = None
        if config.fireblocks_api_token:
            with open(config.fireblocks_raw_key_path, 'r') as pk:
                d = pk.read()
                self.fireblocks = FireblocksSDK(
                    d, config.fireblocks_api_token)

        self.eth = eth_api.EthApi(self._api)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        if self._api:
            self._api.close()
