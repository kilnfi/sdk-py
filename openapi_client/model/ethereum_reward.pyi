# coding: utf-8

"""
    Kiln Connect

    This API provides reporting staking data on various protocols as well as network wide data, staking transaction crafting features and so on.  In order to use it, you should first get an API token from your Kiln dashboard (applications section). If you don't have access to our dashboard, please get in touch at hello@kiln.fi.  Once you have your API token, you can set it as a bearer token in your request headers.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: contact@kiln.fi
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class EthereumReward(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            time = schemas.DateSchema
            consensus_rewards = schemas.StrSchema
            execution_rewards = schemas.StrSchema
            rewards = schemas.StrSchema
            stake_balance = schemas.StrSchema
            gross_apy = schemas.NumberSchema
            cl_apy = schemas.NumberSchema
            el_apy = schemas.NumberSchema
            __annotations__ = {
                "time": time,
                "consensus_rewards": consensus_rewards,
                "execution_rewards": execution_rewards,
                "rewards": rewards,
                "stake_balance": stake_balance,
                "gross_apy": gross_apy,
                "cl_apy": cl_apy,
                "el_apy": el_apy,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["time"]) -> MetaOapg.properties.time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["consensus_rewards"]) -> MetaOapg.properties.consensus_rewards: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["execution_rewards"]) -> MetaOapg.properties.execution_rewards: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rewards"]) -> MetaOapg.properties.rewards: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stake_balance"]) -> MetaOapg.properties.stake_balance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gross_apy"]) -> MetaOapg.properties.gross_apy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cl_apy"]) -> MetaOapg.properties.cl_apy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["el_apy"]) -> MetaOapg.properties.el_apy: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["time", "consensus_rewards", "execution_rewards", "rewards", "stake_balance", "gross_apy", "cl_apy", "el_apy", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["time"]) -> typing.Union[MetaOapg.properties.time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["consensus_rewards"]) -> typing.Union[MetaOapg.properties.consensus_rewards, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["execution_rewards"]) -> typing.Union[MetaOapg.properties.execution_rewards, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rewards"]) -> typing.Union[MetaOapg.properties.rewards, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stake_balance"]) -> typing.Union[MetaOapg.properties.stake_balance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gross_apy"]) -> typing.Union[MetaOapg.properties.gross_apy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cl_apy"]) -> typing.Union[MetaOapg.properties.cl_apy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["el_apy"]) -> typing.Union[MetaOapg.properties.el_apy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["time", "consensus_rewards", "execution_rewards", "rewards", "stake_balance", "gross_apy", "cl_apy", "el_apy", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        time: typing.Union[MetaOapg.properties.time, str, date, schemas.Unset] = schemas.unset,
        consensus_rewards: typing.Union[MetaOapg.properties.consensus_rewards, str, schemas.Unset] = schemas.unset,
        execution_rewards: typing.Union[MetaOapg.properties.execution_rewards, str, schemas.Unset] = schemas.unset,
        rewards: typing.Union[MetaOapg.properties.rewards, str, schemas.Unset] = schemas.unset,
        stake_balance: typing.Union[MetaOapg.properties.stake_balance, str, schemas.Unset] = schemas.unset,
        gross_apy: typing.Union[MetaOapg.properties.gross_apy, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        cl_apy: typing.Union[MetaOapg.properties.cl_apy, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        el_apy: typing.Union[MetaOapg.properties.el_apy, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EthereumReward':
        return super().__new__(
            cls,
            *_args,
            time=time,
            consensus_rewards=consensus_rewards,
            execution_rewards=execution_rewards,
            rewards=rewards,
            stake_balance=stake_balance,
            gross_apy=gross_apy,
            cl_apy=cl_apy,
            el_apy=el_apy,
            _configuration=_configuration,
            **kwargs,
        )
