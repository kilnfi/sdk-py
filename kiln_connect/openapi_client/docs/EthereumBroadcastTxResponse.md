# EthereumBroadcastTxResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_hash** | **str** | Hash of the transaction once broadcasted | [optional] 

## Example

```python
from kiln_connect.openapi_client.models.ethereum_broadcast_tx_response import EthereumBroadcastTxResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EthereumBroadcastTxResponse from a JSON string
ethereum_broadcast_tx_response_instance = EthereumBroadcastTxResponse.from_json(json)
# print the JSON string representation of the object
print EthereumBroadcastTxResponse.to_json()

# convert the object into a dict
ethereum_broadcast_tx_response_dict = ethereum_broadcast_tx_response_instance.to_dict()
# create an instance of EthereumBroadcastTxResponse from a dict
ethereum_broadcast_tx_response_form_dict = ethereum_broadcast_tx_response.from_dict(ethereum_broadcast_tx_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


