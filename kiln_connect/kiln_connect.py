from kiln_connect.openapi_client import ApiClient, Configuration
from kiln_connect.openapi_client.api import eth_api


class KilnConnect:
    """Main class for Kiln connect.
    """

    def __init__(self, base_url: str, api_token: str):
        cfg = Configuration(host=base_url)
        cfg.access_token = api_token

        self._api = ApiClient(
            configuration=cfg,
        )

        self.eth = eth_api.EthApi(self._api)

    def __enter(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        if self._api:
            self._api.close()
