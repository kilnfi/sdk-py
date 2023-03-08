# TezosStake


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stake_address** | **str** | Wallet address of the delegator | [optional] 
**baker_address** | **str** | Address of the baker | [optional] 
**state** | **str** | State of the Tezos stake | [optional] 
**activated_at** | **datetime** | Date at which the stake started earning rewards | [optional] 
**activated_cycle** | **int** | Cycle at which the stake started earning rewards | [optional] 
**delegated_cycle** | **datetime** | Cycle in which the delegation transaction was made | [optional] 
**delegated_at** | **int** | Date at which the staking transaction was made, corresponds to the block it was part of. | [optional] 
**delegated_block** | **int** | Block at which the corresponding staking transaction was executed | [optional] 
**balance** | **str** | Current balance in mutez | [optional] 
**rewards** | **str** | Sum of rewards in mutez earned by this stake since delegation | [optional] 
**gross_apy** | **float** | Gross annual percentage yield | [optional] 
**updated_at** | **datetime** | Last date this data was updated | [optional] 


