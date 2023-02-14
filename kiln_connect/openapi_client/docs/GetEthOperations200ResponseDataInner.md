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


