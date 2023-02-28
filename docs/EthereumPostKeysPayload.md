# EthereumPostKeysPayload


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Kiln Account ID to stake into | 
**withdrawal_address** | **str** | Ethereum withdrawal address used for the withdrawals credentials of the validators. BLS format is not supported. | 
**number** | **float** | Number of validator keys to generate. You can generate up to 150 keys at once. | 
**format** | **str** | Response format. Use \&quot;cli_deposit\&quot; for more information about each key. | [optional] [default to 'batch_deposit']


