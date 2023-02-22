# coding: utf-8

"""
    Kiln API Specifications

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


from typing import Optional
from pydantic import BaseModel
from kiln_connect.openapi_client.models.ethereum_kiln_stats_gross_apy import EthereumKilnStatsGrossApy

class EthereumKilnStats(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    gross_apy: Optional[EthereumKilnStatsGrossApy] = None
    __properties = ["gross_apy"]

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
    def from_json(cls, json_str: str) -> EthereumKilnStats:
        """Create an instance of EthereumKilnStats from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of gross_apy
        if self.gross_apy:
            _dict['gross_apy'] = self.gross_apy.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EthereumKilnStats:
        """Create an instance of EthereumKilnStats from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return EthereumKilnStats.parse_obj(obj)

        _obj = EthereumKilnStats.parse_obj({
            "gross_apy": EthereumKilnStatsGrossApy.from_dict(obj.get("gross_apy")) if obj.get("gross_apy") is not None else None
        })
        return _obj

