# EthereumOperationDeposit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of the operation | [optional] 
**var_date** | **datetime** | Date of the operation | [optional] 
**validator_address** | **str** | Validator address of the operation | [optional] 
**tx_hash** | **str** | Hash of the transaction | [optional] 
**tx_gas_used** | **str** | Gas used by the transaction in WEI | [optional] 
**tx_sender** | **str** | Address of the sender of the transaction | [optional] 
**proxied_by** | **str** | First address of the smart-contract called in the deposit chain | [optional] 
**block** | **int** | Block number containing the transaction | [optional] 
**withdrawal_credentials** | **str** | Withdrawal credentials of the deposit | [optional] 
**amount** | **str** | Amount in WEI of the deposit transaction | [optional] 

## Example

```python
from openapi_client.models.ethereum_operation_deposit import EthereumOperationDeposit

# TODO update the JSON string below
json = "{}"
# create an instance of EthereumOperationDeposit from a JSON string
ethereum_operation_deposit_instance = EthereumOperationDeposit.from_json(json)
# print the JSON string representation of the object
print EthereumOperationDeposit.to_json()

# convert the object into a dict
ethereum_operation_deposit_dict = ethereum_operation_deposit_instance.to_dict()
# create an instance of EthereumOperationDeposit from a dict
ethereum_operation_deposit_form_dict = ethereum_operation_deposit.from_dict(ethereum_operation_deposit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


