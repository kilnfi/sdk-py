# EthereumBroadcastTxQuery


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serialized_tx** | **str** | Serialized transaction | [optional] 

## Example

```python
from kiln_connect.openapi_client.models.ethereum_broadcast_tx_query import EthereumBroadcastTxQuery

# TODO update the JSON string below
json = "{}"
# create an instance of EthereumBroadcastTxQuery from a JSON string
ethereum_broadcast_tx_query_instance = EthereumBroadcastTxQuery.from_json(json)
# print the JSON string representation of the object
print EthereumBroadcastTxQuery.to_json()

# convert the object into a dict
ethereum_broadcast_tx_query_dict = ethereum_broadcast_tx_query_instance.to_dict()
# create an instance of EthereumBroadcastTxQuery from a dict
ethereum_broadcast_tx_query_form_dict = ethereum_broadcast_tx_query.from_dict(ethereum_broadcast_tx_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


