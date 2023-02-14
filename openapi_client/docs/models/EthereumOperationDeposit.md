# openapi_client.model.ethereum_operation_deposit.EthereumOperationDeposit

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | type of the operation | [optional] 
**date** | str, datetime,  | str,  | Date of the operation | [optional] value must conform to RFC-3339 date-time
**validator_address** | str,  | str,  | Validator address of the operation | [optional] 
**tx_hash** | str,  | str,  | Hash of the transaction | [optional] 
**tx_gas_used** | str,  | str,  | Gas used by the transaction in WEI | [optional] 
**tx_sender** | str,  | str,  | Address of the sender of the transaction | [optional] 
**proxied_by** | None, str,  | NoneClass, str,  | First address of the smart-contract called in the deposit chain | [optional] 
**block** | decimal.Decimal, int,  | decimal.Decimal,  | Block number containing the transaction | [optional] 
**withdrawal_credentials** | str,  | str,  | Withdrawal credentials of the deposit | [optional] 
**amount** | str,  | str,  | Amount in WEI of the deposit transaction | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

