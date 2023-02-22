# EthereumStake


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validator_address** | **str** |  | [optional] 
**state** | **str** | State of the Ethereum stake as seen be the consensus layer | [optional] 
**activated_at** | **datetime** | Date of activation on the Ethereum consensus layer | [optional] 
**activated_epoch** | **int** | Epoch of activation on the Ethereum consensus layer | [optional] 
**delegated_block** | **int** | Block at which the corresponding staking transaction was executed | [optional] 
**deposit_tx_sender** | **str** | Address of the sender of the first deposit transaction | [optional] 
**execution_fee_recipient** | **str** | Address of the last recipient of an execution reward | [optional] 
**withdrawal_credentials** | **str** | Ethereum withdrawal credentials | [optional] 
**effective_balance** | **str** | Effective balance in WEI of the stake as seen by the Ethereum consensus layer | [optional] 
**balance** | **str** | Current balance in WEI on the Ethereum consensus layer | [optional] 
**consensus_rewards** | **str** | Sum of consensus rewards in WEI earned by this stake | [optional] 
**execution_rewards** | **str** | Sum of execution rewards in WEI earned by this stake | [optional] 
**rewards** | **str** | Sum of consensus and execution rewards in WEI earned by this stake | [optional] 
**gross_apy** | **float** | Gross annual percentage yield | [optional] 
**updated_at** | **datetime** | Last date this data was updated | [optional] 


