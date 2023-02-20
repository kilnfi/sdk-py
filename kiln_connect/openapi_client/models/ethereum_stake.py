# coding: utf-8

"""
    Kiln API

    This API provides reporting staking data on various protocols as well as network wide data, staking transaction crafting features and so on.  In order to use it, you should first get an API token from your Kiln dashboard (applications section). If you don't have access to our dashboard, please get in touch at hello@kiln.fi.  Once you have your API token, you can set it as a bearer token in your request headers.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: contact@kiln.fi
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr

class EthereumStake(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    validator_address: Optional[StrictStr] = None
    state: Optional[StrictStr] = Field(None, description="State of the Ethereum stake as seen be the consensus layer")
    activated_at: Optional[datetime] = Field(None, description="Date of activation on the Ethereum consensus layer")
    activated_epoch: Optional[StrictInt] = Field(None, description="Epoch of activation on the Ethereum consensus layer")
    delegated_block: Optional[StrictInt] = Field(None, description="Block at which the corresponding staking transaction was executed")
    deposit_tx_sender: Optional[StrictStr] = Field(None, description="Address of the sender of the first deposit transaction")
    execution_fee_recipient: Optional[StrictStr] = Field(None, description="Address of the last recipient of an execution reward")
    withdrawal_credentials: Optional[StrictStr] = Field(None, description="Ethereum withdrawal credentials")
    effective_balance: Optional[StrictStr] = Field(None, description="Effective balance in WEI of the stake as seen by the Ethereum consensus layer")
    balance: Optional[StrictStr] = Field(None, description="Current balance in WEI on the Ethereum consensus layer")
    consensus_rewards: Optional[StrictStr] = Field(None, description="Sum of consensus rewards in WEI earned by this stake")
    execution_rewards: Optional[StrictStr] = Field(None, description="Sum of execution rewards in WEI earned by this stake")
    rewards: Optional[StrictStr] = Field(None, description="Sum of consensus and execution rewards in WEI earned by this stake")
    gross_apy: Optional[float] = Field(None, description="Gross annual percentage yield")
    __properties = ["validator_address", "state", "activated_at", "activated_epoch", "delegated_block", "deposit_tx_sender", "execution_fee_recipient", "withdrawal_credentials", "effective_balance", "balance", "consensus_rewards", "execution_rewards", "rewards", "gross_apy"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> EthereumStake:
        """Create an instance of EthereumStake from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if activated_at (nullable) is None
        if self.activated_at is None:
            _dict['activated_at'] = None

        # set to None if activated_epoch (nullable) is None
        if self.activated_epoch is None:
            _dict['activated_epoch'] = None

        # set to None if delegated_block (nullable) is None
        if self.delegated_block is None:
            _dict['delegated_block'] = None

        # set to None if deposit_tx_sender (nullable) is None
        if self.deposit_tx_sender is None:
            _dict['deposit_tx_sender'] = None

        # set to None if execution_fee_recipient (nullable) is None
        if self.execution_fee_recipient is None:
            _dict['execution_fee_recipient'] = None

        # set to None if withdrawal_credentials (nullable) is None
        if self.withdrawal_credentials is None:
            _dict['withdrawal_credentials'] = None

        # set to None if effective_balance (nullable) is None
        if self.effective_balance is None:
            _dict['effective_balance'] = None

        # set to None if balance (nullable) is None
        if self.balance is None:
            _dict['balance'] = None

        # set to None if consensus_rewards (nullable) is None
        if self.consensus_rewards is None:
            _dict['consensus_rewards'] = None

        # set to None if execution_rewards (nullable) is None
        if self.execution_rewards is None:
            _dict['execution_rewards'] = None

        # set to None if rewards (nullable) is None
        if self.rewards is None:
            _dict['rewards'] = None

        # set to None if gross_apy (nullable) is None
        if self.gross_apy is None:
            _dict['gross_apy'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EthereumStake:
        """Create an instance of EthereumStake from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return EthereumStake.parse_obj(obj)

        _obj = EthereumStake.parse_obj({
            "validator_address": obj.get("validator_address"),
            "state": obj.get("state"),
            "activated_at": obj.get("activated_at"),
            "activated_epoch": obj.get("activated_epoch"),
            "delegated_block": obj.get("delegated_block"),
            "deposit_tx_sender": obj.get("deposit_tx_sender"),
            "execution_fee_recipient": obj.get("execution_fee_recipient"),
            "withdrawal_credentials": obj.get("withdrawal_credentials"),
            "effective_balance": obj.get("effective_balance"),
            "balance": obj.get("balance"),
            "consensus_rewards": obj.get("consensus_rewards"),
            "execution_rewards": obj.get("execution_rewards"),
            "rewards": obj.get("rewards"),
            "gross_apy": obj.get("gross_apy")
        })
        return _obj

