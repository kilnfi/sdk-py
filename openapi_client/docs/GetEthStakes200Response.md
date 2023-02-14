# GetEthStakes200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EthereumStake]**](EthereumStake.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_eth_stakes200_response import GetEthStakes200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEthStakes200Response from a JSON string
get_eth_stakes200_response_instance = GetEthStakes200Response.from_json(json)
# print the JSON string representation of the object
print GetEthStakes200Response.to_json()

# convert the object into a dict
get_eth_stakes200_response_dict = get_eth_stakes200_response_instance.to_dict()
# create an instance of GetEthStakes200Response from a dict
get_eth_stakes200_response_form_dict = get_eth_stakes200_response.from_dict(get_eth_stakes200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


