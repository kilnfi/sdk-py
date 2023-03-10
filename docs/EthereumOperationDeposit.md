# EthereumOperationDeposit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of the operation | [optional] 
**time** | **datetime** | Time of the operation | [optional] 
**validator_address** | **str** | Validator address of the operation | [optional] 
**tx_hash** | **str** | Hash of the transaction | [optional] 
**tx_sender** | **str** | Address of the sender of the transaction | [optional] 
**tx_gas_used** | **str** | Gas used by the transaction in WEI | [optional] 
**tx_effective_gas_price** | **str** | Effective gas price used for this TX in WEI | [optional] 
**proxies** | **List[str]** | Ordered list of smart-contracts in the calling chain | [optional] 
**block** | **int** | Block number containing the transaction | [optional] 
**block_base_fee** | **str** | Base fee used for this block in WEI | [optional] 
**withdrawal_credentials** | **str** | Withdrawal credentials of the deposit | [optional] 
**amount** | **str** | Amount in WEI of the deposit transaction | [optional] 


