# GetEthNetworkStats200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EthereumNetworkStats**](EthereumNetworkStats.md) |  | [optional] 

## Example

```python
from kiln_connect.openapi_client.models.get_eth_network_stats200_response import GetEthNetworkStats200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEthNetworkStats200Response from a JSON string
get_eth_network_stats200_response_instance = GetEthNetworkStats200Response.from_json(json)
# print the JSON string representation of the object
print GetEthNetworkStats200Response.to_json()

# convert the object into a dict
get_eth_network_stats200_response_dict = get_eth_network_stats200_response_instance.to_dict()
# create an instance of GetEthNetworkStats200Response from a dict
get_eth_network_stats200_response_form_dict = get_eth_network_stats200_response.from_dict(get_eth_network_stats200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


