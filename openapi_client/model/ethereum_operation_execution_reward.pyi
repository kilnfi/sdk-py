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


class EthereumOperationExecutionReward(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            type = schemas.StrSchema
            date = schemas.DateTimeSchema
            validator_address = schemas.StrSchema
            block = schemas.IntSchema
            fee_recipient = schemas.StrSchema
            
            
            class mev_payout_tx_hash(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'mev_payout_tx_hash':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class mev_payout_tx_sender(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'mev_payout_tx_sender':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            amount = schemas.StrSchema
            __annotations__ = {
                "type": type,
                "date": date,
                "validator_address": validator_address,
                "block": block,
                "fee_recipient": fee_recipient,
                "mev_payout_tx_hash": mev_payout_tx_hash,
                "mev_payout_tx_sender": mev_payout_tx_sender,
                "amount": amount,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["validator_address"]) -> MetaOapg.properties.validator_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block"]) -> MetaOapg.properties.block: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fee_recipient"]) -> MetaOapg.properties.fee_recipient: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mev_payout_tx_hash"]) -> MetaOapg.properties.mev_payout_tx_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mev_payout_tx_sender"]) -> MetaOapg.properties.mev_payout_tx_sender: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "date", "validator_address", "block", "fee_recipient", "mev_payout_tx_hash", "mev_payout_tx_sender", "amount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> typing.Union[MetaOapg.properties.date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["validator_address"]) -> typing.Union[MetaOapg.properties.validator_address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block"]) -> typing.Union[MetaOapg.properties.block, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fee_recipient"]) -> typing.Union[MetaOapg.properties.fee_recipient, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mev_payout_tx_hash"]) -> typing.Union[MetaOapg.properties.mev_payout_tx_hash, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mev_payout_tx_sender"]) -> typing.Union[MetaOapg.properties.mev_payout_tx_sender, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "date", "validator_address", "block", "fee_recipient", "mev_payout_tx_hash", "mev_payout_tx_sender", "amount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        date: typing.Union[MetaOapg.properties.date, str, datetime, schemas.Unset] = schemas.unset,
        validator_address: typing.Union[MetaOapg.properties.validator_address, str, schemas.Unset] = schemas.unset,
        block: typing.Union[MetaOapg.properties.block, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        fee_recipient: typing.Union[MetaOapg.properties.fee_recipient, str, schemas.Unset] = schemas.unset,
        mev_payout_tx_hash: typing.Union[MetaOapg.properties.mev_payout_tx_hash, None, str, schemas.Unset] = schemas.unset,
        mev_payout_tx_sender: typing.Union[MetaOapg.properties.mev_payout_tx_sender, None, str, schemas.Unset] = schemas.unset,
        amount: typing.Union[MetaOapg.properties.amount, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EthereumOperationExecutionReward':
        return super().__new__(
            cls,
            *_args,
            type=type,
            date=date,
            validator_address=validator_address,
            block=block,
            fee_recipient=fee_recipient,
            mev_payout_tx_hash=mev_payout_tx_hash,
            mev_payout_tx_sender=mev_payout_tx_sender,
            amount=amount,
            _configuration=_configuration,
            **kwargs,
        )