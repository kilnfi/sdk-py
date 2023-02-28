# EthereumPostKeysCliResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | Format of the key | [optional] 
**pubkey** | **str** | Public key of the validator | [optional] 
**withdrawal_credentials** | **str** | Withdrawals credentials of the validator | [optional] 
**amount** | **float** | Amount in GWEI that needs to be deposited to activate the validator | [optional] 
**signature** | **str** | BLS signature for the deposit data structure required to stake on the Ethereum chain | [optional] 
**deposit_message_root** | **str** | Root hash ensuring the deposit message integrity | [optional] 
**deposit_data_root** | **str** | Root hash ensuring the deposit data integrity | [optional] 
**fork_version** | **str** | Identifier for the fork version | [optional] 
**network_name** | **str** | Ethereum network for the generated validation key(s) | [optional] 
**deposit_cli_version** | **str** | Version of the deposit-cli tool used to generate the validation key | [optional] 


