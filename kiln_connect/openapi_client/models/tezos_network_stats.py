# coding: utf-8

"""
    Kiln API Specifications

    This API provides reporting staking data on various protocols as well as network wide data, staking transaction crafting features and so on. In order to use it, you should first get an API token from your Kiln dashboard (applications section). If you don't have access to our dashboard, please get in touch at hello@kiln.fi. Once you have your API token, you can set it as a bearer token in your request headers.  ### Backward Compatibility  This is an experimental specification used for development and testing, do not rely on what is here unless you know the implications.  The official Kiln API specification following backward compatible changes can be found [here](/).  # noqa: E501

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
from pydantic import BaseModel, Field

class TezosNetworkStats(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    nb_validators: Optional[float] = Field(None, description="Number of active bakers")
    network_gross_apy: Optional[float] = Field(None, description="Gross annual percentage yield")
    supply_staked_percent: Optional[float] = Field(None, description="Supply percentage of Tezos currently staked")
    updated_at: Optional[datetime] = Field(None, description="Last date this data was updated")
    __properties = ["nb_validators", "network_gross_apy", "supply_staked_percent", "updated_at"]

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
    def from_json(cls, json_str: str) -> TezosNetworkStats:
        """Create an instance of TezosNetworkStats from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if updated_at (nullable) is None
        if self.updated_at is None:
            _dict['updated_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TezosNetworkStats:
        """Create an instance of TezosNetworkStats from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return TezosNetworkStats.parse_obj(obj)

        _obj = TezosNetworkStats.parse_obj({
            "nb_validators": obj.get("nb_validators"),
            "network_gross_apy": obj.get("network_gross_apy"),
            "supply_staked_percent": obj.get("supply_staked_percent"),
            "updated_at": obj.get("updated_at")
        })
        return _obj

