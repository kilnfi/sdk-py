# openapi_client.model.ethereum_stake.EthereumStake

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**validator_address** | str,  | str,  |  | [optional] 
**state** | str,  | str,  | State of the Ethereum stake as seen be the consensus layer | [optional] 
**activated_at** | None, str, datetime,  | NoneClass, str,  | Date of activation on the Ethereum consensus layer | [optional] value must conform to RFC-3339 date-time
**activated_epoch** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Epoch of activation on the Ethereum consensus layer | [optional] 
**delegated_block** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Block at which the corresponding staking transaction was executed | [optional] 
**deposit_tx_sender** | None, str,  | NoneClass, str,  | Address of the sender of the first deposit transaction | [optional] 
**execution_fee_recipient** | None, str,  | NoneClass, str,  | Address of the last recipient of an execution reward | [optional] 
**withdrawal_credentials** | None, str,  | NoneClass, str,  | Ethereum withdrawal credentials | [optional] 
**effective_balance** | None, str,  | NoneClass, str,  | Effective balance in WEI of the stake as seen by the Ethereum consensus layer | [optional] 
**balance** | None, str,  | NoneClass, str,  | Current balance in WEI on the Ethereum consensus layer | [optional] 
**consensus_rewards** | None, str,  | NoneClass, str,  | Sum of consensus rewards in WEI earned by this stake | [optional] 
**execution_rewards** | None, str,  | NoneClass, str,  | Sum of execution rewards in WEI earned by this stake | [optional] 
**rewards** | None, str,  | NoneClass, str,  | Sum of consensus and execution rewards in WEI earned by this stake | [optional] 
**gross_apy** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Gross annual percentage yield | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

