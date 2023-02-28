# coding: utf-8

"""
    Kiln API Specifications

    This API provides reporting staking data on various protocols as well as network wide data, staking transaction crafting features and so on. In order to use it, you should first get an API token from your Kiln dashboard (applications section). If you don't have access to our dashboard, please get in touch at hello@kiln.fi. Once you have your API token, you can set it as a bearer token in your request headers.  ### Backward Compatibility  Kiln considers the following changes to be backwards-compatible:  - Adding new API routes. - Adding new optional request parameters to existing API methods. - Adding new properties to existing API responses. - Changing the order of properties in existing API responses. - Adding new event types in existing enums.  Non-breaking changes may be introduced silently in our API and subject to modifications before being officialy communicated and documented here. Your application should not depend on them until part of this specification.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: contact@kiln.fi
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field

class EthereumNetworkStats(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    network_gross_apy: Optional[float] = Field(None, description="Gross annual percentage yield")
    supply_staked_percent: Optional[float] = Field(None, description="Supply of Ethereum currently staked")
    __properties = ["network_gross_apy", "supply_staked_percent"]

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
    def from_json(cls, json_str: str) -> EthereumNetworkStats:
        """Create an instance of EthereumNetworkStats from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EthereumNetworkStats:
        """Create an instance of EthereumNetworkStats from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return EthereumNetworkStats.parse_obj(obj)

        _obj = EthereumNetworkStats.parse_obj({
            "network_gross_apy": obj.get("network_gross_apy"),
            "supply_staked_percent": obj.get("supply_staked_percent")
        })
        return _obj

