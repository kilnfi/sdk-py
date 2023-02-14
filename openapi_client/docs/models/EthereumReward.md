# openapi_client.model.ethereum_reward.EthereumReward

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**time** | str, date,  | str,  | Day for this reward entry | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**consensus_rewards** | str,  | str,  | Accumulated consensus rewards WEI during the day | [optional] 
**execution_rewards** | str,  | str,  | Accumulated execution rewards in WEI during the day | [optional] 
**rewards** | str,  | str,  | Accumulated consensus and execution rewards in WEI during the day | [optional] 
**stake_balance** | str,  | str,  | Staked balance in WEI that contributed to this rewards | [optional] 
**gross_apy** | decimal.Decimal, int, float,  | decimal.Decimal,  | Gross annual percentage yield | [optional] 
**cl_apy** | decimal.Decimal, int, float,  | decimal.Decimal,  | Consensus annual percentage yield | [optional] 
**el_apy** | decimal.Decimal, int, float,  | decimal.Decimal,  | Execution annual percentage yield | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

