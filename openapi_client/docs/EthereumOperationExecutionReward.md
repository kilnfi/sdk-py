# EthereumOperationExecutionReward


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**var_date** | **datetime** | Date of the operation | [optional] 
**validator_address** | **str** | Validator address of the operation | [optional] 
**block** | **int** | Block number of the reward | [optional] 
**fee_recipient** | **str** | Fee recipient of the reward | [optional] 
**mev_payout_tx_hash** | **str** | Hash of the MEV payout transaction if appliable | [optional] 
**mev_payout_tx_sender** | **str** | Sender of the MEV payout transaction if appliable | [optional] 
**amount** | **str** | Amount in WEI of the reward | [optional] 

## Example

```python
from openapi_client.models.ethereum_operation_execution_reward import EthereumOperationExecutionReward

# TODO update the JSON string below
json = "{}"
# create an instance of EthereumOperationExecutionReward from a JSON string
ethereum_operation_execution_reward_instance = EthereumOperationExecutionReward.from_json(json)
# print the JSON string representation of the object
print EthereumOperationExecutionReward.to_json()

# convert the object into a dict
ethereum_operation_execution_reward_dict = ethereum_operation_execution_reward_instance.to_dict()
# create an instance of EthereumOperationExecutionReward from a dict
ethereum_operation_execution_reward_form_dict = ethereum_operation_execution_reward.from_dict(ethereum_operation_execution_reward_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


