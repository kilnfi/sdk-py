# PostEthTransactionBroadcast201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EthereumBroadcastTxResponse**](EthereumBroadcastTxResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.post_eth_transaction_broadcast201_response import PostEthTransactionBroadcast201Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostEthTransactionBroadcast201Response from a JSON string
post_eth_transaction_broadcast201_response_instance = PostEthTransactionBroadcast201Response.from_json(json)
# print the JSON string representation of the object
print PostEthTransactionBroadcast201Response.to_json()

# convert the object into a dict
post_eth_transaction_broadcast201_response_dict = post_eth_transaction_broadcast201_response_instance.to_dict()
# create an instance of PostEthTransactionBroadcast201Response from a dict
post_eth_transaction_broadcast201_response_form_dict = post_eth_transaction_broadcast201_response.from_dict(post_eth_transaction_broadcast201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


