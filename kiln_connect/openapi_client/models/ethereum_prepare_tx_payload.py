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



from pydantic import BaseModel, Field, StrictStr

class EthereumPrepareTxPayload(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    unsigned_tx_serialized: StrictStr = Field(..., description="Unsigned serialized transaction")
    r: StrictStr = Field(..., description="r part of the ECDSA signature in hex")
    s: StrictStr = Field(..., description="s part of the ECDSA signature in hex")
    v: float = Field(..., description="v part of the ECDSA signature (0 or 1)")
    __properties = ["unsigned_tx_serialized", "r", "s", "v"]

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
    def from_json(cls, json_str: str) -> EthereumPrepareTxPayload:
        """Create an instance of EthereumPrepareTxPayload from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EthereumPrepareTxPayload:
        """Create an instance of EthereumPrepareTxPayload from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return EthereumPrepareTxPayload.parse_obj(obj)

        _obj = EthereumPrepareTxPayload.parse_obj({
            "unsigned_tx_serialized": obj.get("unsigned_tx_serialized"),
            "r": obj.get("r"),
            "s": obj.get("s"),
            "v": obj.get("v")
        })
        return _obj

