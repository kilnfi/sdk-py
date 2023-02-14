# EthereumNetworkStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_gross_apy** | **float** | Gross annual percentage yield | [optional] 
**supply_staked_percent** | **float** | Supply of Ethereum currently staked | [optional] 

## Example

```python
from openapi_client.models.ethereum_network_stats import EthereumNetworkStats

# TODO update the JSON string below
json = "{}"
# create an instance of EthereumNetworkStats from a JSON string
ethereum_network_stats_instance = EthereumNetworkStats.from_json(json)
# print the JSON string representation of the object
print EthereumNetworkStats.to_json()

# convert the object into a dict
ethereum_network_stats_dict = ethereum_network_stats_instance.to_dict()
# create an instance of EthereumNetworkStats from a dict
ethereum_network_stats_form_dict = ethereum_network_stats.from_dict(ethereum_network_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


