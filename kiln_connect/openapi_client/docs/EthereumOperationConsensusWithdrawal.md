# EthereumOperationConsensusWithdrawal


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**var_date** | **datetime** | Date of the operation | [optional] 
**validator_address** | **str** | Validator address of the operation | [optional] 
**block** | **int** | Block number of the reward | [optional] 
**fee_recipient** | **str** | Fee recipient of the reward | [optional] 
**amount** | **str** | Amount in WEI of the reward | [optional] 

## Example

```python
from kiln_connect.openapi_client.models.ethereum_operation_consensus_withdrawal import EthereumOperationConsensusWithdrawal

# TODO update the JSON string below
json = "{}"
# create an instance of EthereumOperationConsensusWithdrawal from a JSON string
ethereum_operation_consensus_withdrawal_instance = EthereumOperationConsensusWithdrawal.from_json(json)
# print the JSON string representation of the object
print EthereumOperationConsensusWithdrawal.to_json()

# convert the object into a dict
ethereum_operation_consensus_withdrawal_dict = ethereum_operation_consensus_withdrawal_instance.to_dict()
# create an instance of EthereumOperationConsensusWithdrawal from a dict
ethereum_operation_consensus_withdrawal_form_dict = ethereum_operation_consensus_withdrawal.from_dict(ethereum_operation_consensus_withdrawal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


