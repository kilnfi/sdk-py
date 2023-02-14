# GetEthOperations200ResponseDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**var_date** | **datetime** | Date of the operation | [optional] 
**validator_address** | **str** | Validator address of the operation | [optional] 
**tx_hash** | **str** | Hash of the transaction | [optional] 
**tx_gas_used** | **str** | Gas used by the transaction in WEI | [optional] 
**tx_sender** | **str** | Address of the sender of the transaction | [optional] 
**proxied_by** | **str** | First address of the smart-contract called in the deposit chain | [optional] 
**block** | **int** | Block number of the reward | [optional] 
**withdrawal_credentials** | **str** | Withdrawal credentials of the deposit | [optional] 
**amount** | **str** | Amount in WEI of the reward | [optional] 
**fee_recipient** | **str** | Fee recipient of the reward | [optional] 
**mev_payout_tx_hash** | **str** | Hash of the MEV payout transaction if appliable | [optional] 
**mev_payout_tx_sender** | **str** | Sender of the MEV payout transaction if appliable | [optional] 

## Example

```python
from kiln_connect.openapi_client.models.get_eth_operations200_response_data_inner import GetEthOperations200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEthOperations200ResponseDataInner from a JSON string
get_eth_operations200_response_data_inner_instance = GetEthOperations200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print GetEthOperations200ResponseDataInner.to_json()

# convert the object into a dict
get_eth_operations200_response_data_inner_dict = get_eth_operations200_response_data_inner_instance.to_dict()
# create an instance of GetEthOperations200ResponseDataInner from a dict
get_eth_operations200_response_data_inner_form_dict = get_eth_operations200_response_data_inner.from_dict(get_eth_operations200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


