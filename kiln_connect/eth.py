"""Ethereum wrapper class.

This ETH class is meant to be accessed via KilnConnect.eth, it is
publicly exported in the SDK. This file contains helpers to
integration our Ethereum API with integrations such as Fireblocks. It
provides convenient shortcuts to use our SDK.
"""

from kiln_connect.integrations import Integrations
from kiln_connect.openapi_client import (
    ApiClient,
)
from kiln_connect.openapi_client import (
    EthApi,
    EthereumCraftStakeTxPayload,
    EthereumPrepareTxPayload,
    EthereumBroadcastTxPayload,
    EthereumBroadcastTxResponse,
)


class ETH(EthApi):
    """Wrapper for the Ethereum API.
    """

    def __init__(self, api: ApiClient, integrations: Integrations):
        super().__init__(api)
        self.integrations = integrations

    def stake(self, integration: str, account_id: str, wallet: str, amount_wei: int) -> EthereumBroadcastTxResponse:
        """Helper to stake on Ethereum using Fireblocks
        """
        fb = self.integrations.get_integration(integration)

        # Craft TX.
        craft_tx = EthereumCraftStakeTxPayload(
            account_id=account_id,
            wallet=wallet,
            amount_wei=str(amount_wei),
        )
        response = super().post_eth_stake_tx(craft_tx)

        unsigned_tx_payload = response.data.unsigned_tx_serialized
        unsigned_tx_hash = response.data.unsigned_tx_hash

        # Sign TX.
        sig = fb.sign('eth', unsigned_tx_hash)

        # Prepare TX.
        prepare_tx = EthereumPrepareTxPayload(
            unsigned_tx_serialized=unsigned_tx_payload,
            r=sig.get("r"),
            s=sig.get("s"),
            v=sig.get("v", 0)
        )
        response = super().post_eth_prepare_tx(prepare_tx)

        # Broadcast TX.
        broadcast_tx = EthereumBroadcastTxPayload(
            tx_serialized=response.data.signed_tx_serialized,
        )
        response = super().post_eth_broadcast_tx(broadcast_tx)

        # Likely need to check response here and throw appropriate errors.

        return response.data
