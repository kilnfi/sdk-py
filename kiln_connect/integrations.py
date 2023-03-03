"""Wrapper a bit similar to the Typescript SDK with signing integrations.
"""

import time
from dataclasses import dataclass

import fireblocks_sdk

from .errors import *


@dataclass
class IntegrationConfig:
    """Class to describe the config of an integration"""
    name: str
    provider: str
    parameters: dict


class FireblocksIntegration:
    """Handles the Fireblocks integration.
    """

    def __init__(self, config: IntegrationConfig):
        self.fireblocks = None

        self.src = fireblocks_sdk.TransferPeerPath(
            "VAULT_ACCOUNT", config.parameters['vault_account_id'])
        self.assets = config.parameters['assets']

        with open(config.parameters['raw_key_path'], 'r') as pk:
            d = pk.read()
            self.fb = fireblocks_sdk.FireblocksSDK(
                d, config.parameters['api_token'])

    def sign(self, asset: str, unsigned_tx_hash: str) -> dict:
        """Asks fireblocks to sign TX hash and wait for completion.
        """
        msg = fireblocks_sdk.RawMessage(
            [fireblocks_sdk.UnsignedMessage(unsigned_tx_hash)])
        asset = self.assets[asset]
        note = "Staked from Kiln SDK Python"

        sign_tx = self.fb.create_raw_transaction(msg, self.src, asset, note)
        tx_id = sign_tx.get("id")

        failed_states = [
            fireblocks_sdk.TRANSACTION_STATUS_BLOCKED,
            fireblocks_sdk.TRANSACTION_STATUS_FAILED,
            fireblocks_sdk.TRANSACTION_STATUS_REJECTED,
            fireblocks_sdk.TRANSACTION_STATUS_CANCELLED
        ]

        signed_tx = None
        while True:
            signed_tx = self.fb.get_transaction_by_id(tx_id)
            status = signed_tx.get('status')
            if status == fireblocks_sdk.TRANSACTION_STATUS_COMPLETED:
                break
            if status in failed_states:
                break
            time.sleep(1)

        signatures = signed_tx.get("signedMessages")
        if not signatures or len(signatures) != 1:
            raise KilnFireblocksFailedToSignError()

        return signatures[0].get('signature')


class Integrations:
    """Handles integrations.

    For now it's kind of ad-hoc and we don't have a lot of
    integrations so we can keep it simple, once we start having a lot
    we can split each integration accordingly without changing this
    interface.
    """

    def __init__(self, configs: list[IntegrationConfig]):
        self.integrations = dict()

        for config in configs:
            if config.provider == 'fireblocks':
                i = FireblocksIntegration(config)
                self.integrations[config.name] = i

    def get_integration(self, name: str):
        """Returns the configured integration
        """
        return self.integrations[name]
