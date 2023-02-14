# EthereumUnsignedStakeTx


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unsigned_tx_hash** | **str** | Hash of the unsigned transaction | [optional] 
**unsigned_tx_serialized** | **str** | Serialized transaction | [optional] 

## Example

```python
from openapi_client.models.ethereum_unsigned_stake_tx import EthereumUnsignedStakeTx

# TODO update the JSON string below
json = "{}"
# create an instance of EthereumUnsignedStakeTx from a JSON string
ethereum_unsigned_stake_tx_instance = EthereumUnsignedStakeTx.from_json(json)
# print the JSON string representation of the object
print EthereumUnsignedStakeTx.to_json()

# convert the object into a dict
ethereum_unsigned_stake_tx_dict = ethereum_unsigned_stake_tx_instance.to_dict()
# create an instance of EthereumUnsignedStakeTx from a dict
ethereum_unsigned_stake_tx_form_dict = ethereum_unsigned_stake_tx.from_dict(ethereum_unsigned_stake_tx_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


