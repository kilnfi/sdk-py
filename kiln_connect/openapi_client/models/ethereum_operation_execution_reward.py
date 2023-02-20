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

class EthereumOperationExecutionReward(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    type: Optional[StrictStr] = None
    var_date: Optional[datetime] = Field(None, alias="date", description="Date of the operation")
    validator_address: Optional[StrictStr] = Field(None, description="Validator address of the operation")
    block: Optional[StrictInt] = Field(None, description="Block number of the reward")
    fee_recipient: Optional[StrictStr] = Field(None, description="Fee recipient of the reward")
    mev_payout_tx_hash: Optional[StrictStr] = Field(None, description="Hash of the MEV payout transaction if appliable")
    mev_payout_tx_sender: Optional[StrictStr] = Field(None, description="Sender of the MEV payout transaction if appliable")
    amount: Optional[StrictStr] = Field(None, description="Amount in WEI of the reward")
    __properties = ["type", "date", "validator_address", "block", "fee_recipient", "mev_payout_tx_hash", "mev_payout_tx_sender", "amount"]

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
    def from_json(cls, json_str: str) -> EthereumOperationExecutionReward:
        """Create an instance of EthereumOperationExecutionReward from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if mev_payout_tx_hash (nullable) is None
        if self.mev_payout_tx_hash is None:
            _dict['mev_payout_tx_hash'] = None

        # set to None if mev_payout_tx_sender (nullable) is None
        if self.mev_payout_tx_sender is None:
            _dict['mev_payout_tx_sender'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EthereumOperationExecutionReward:
        """Create an instance of EthereumOperationExecutionReward from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return EthereumOperationExecutionReward.parse_obj(obj)

        _obj = EthereumOperationExecutionReward.parse_obj({
            "type": obj.get("type"),
            "var_date": obj.get("date"),
            "validator_address": obj.get("validator_address"),
            "block": obj.get("block"),
            "fee_recipient": obj.get("fee_recipient"),
            "mev_payout_tx_hash": obj.get("mev_payout_tx_hash"),
            "mev_payout_tx_sender": obj.get("mev_payout_tx_sender"),
            "amount": obj.get("amount")
        })
        return _obj

