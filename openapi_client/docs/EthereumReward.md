# EthereumReward


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **date** | Day for this reward entry | [optional] 
**consensus_rewards** | **str** | Accumulated consensus rewards WEI during the day | [optional] 
**execution_rewards** | **str** | Accumulated execution rewards in WEI during the day | [optional] 
**rewards** | **str** | Accumulated consensus and execution rewards in WEI during the day | [optional] 
**stake_balance** | **str** | Staked balance in WEI that contributed to this rewards | [optional] 
**gross_apy** | **float** | Gross annual percentage yield | [optional] 
**cl_apy** | **float** | Consensus annual percentage yield | [optional] 
**el_apy** | **float** | Execution annual percentage yield | [optional] 

## Example

```python
from openapi_client.models.ethereum_reward import EthereumReward

# TODO update the JSON string below
json = "{}"
# create an instance of EthereumReward from a JSON string
ethereum_reward_instance = EthereumReward.from_json(json)
# print the JSON string representation of the object
print EthereumReward.to_json()

# convert the object into a dict
ethereum_reward_dict = ethereum_reward_instance.to_dict()
# create an instance of EthereumReward from a dict
ethereum_reward_form_dict = ethereum_reward.from_dict(ethereum_reward_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


