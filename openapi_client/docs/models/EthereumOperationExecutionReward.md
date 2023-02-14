# openapi_client.model.ethereum_operation_execution_reward.EthereumOperationExecutionReward

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  |  | [optional] 
**date** | str, datetime,  | str,  | Date of the operation | [optional] value must conform to RFC-3339 date-time
**validator_address** | str,  | str,  | Validator address of the operation | [optional] 
**block** | decimal.Decimal, int,  | decimal.Decimal,  | Block number of the reward | [optional] 
**fee_recipient** | str,  | str,  | Fee recipient of the reward | [optional] 
**mev_payout_tx_hash** | None, str,  | NoneClass, str,  | Hash of the MEV payout transaction if appliable | [optional] 
**mev_payout_tx_sender** | None, str,  | NoneClass, str,  | Sender of the MEV payout transaction if appliable | [optional] 
**amount** | str,  | str,  | Amount in WEI of the reward | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

