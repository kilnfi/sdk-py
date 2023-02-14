# GetEthOperations200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GetEthOperations200ResponseDataInner]**](GetEthOperations200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_eth_operations200_response import GetEthOperations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEthOperations200Response from a JSON string
get_eth_operations200_response_instance = GetEthOperations200Response.from_json(json)
# print the JSON string representation of the object
print GetEthOperations200Response.to_json()

# convert the object into a dict
get_eth_operations200_response_dict = get_eth_operations200_response_instance.to_dict()
# create an instance of GetEthOperations200Response from a dict
get_eth_operations200_response_form_dict = get_eth_operations200_response.from_dict(get_eth_operations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


