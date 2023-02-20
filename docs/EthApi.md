# Documentation for EthApi

All URIs are relative to *https://api.testnet.kiln.fi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_eth_network_stats**](EthApi.md#get_eth_network_stats) | **GET** /v1/eth/network-stats | Network stats
[**get_eth_operations**](EthApi.md#get_eth_operations) | **GET** /v1/eth/operations | Operations
[**get_eth_report**](EthApi.md#get_eth_report) | **GET** /v1/eth/reports | Report
[**get_eth_rewards**](EthApi.md#get_eth_rewards) | **GET** /v1/eth/rewards | Rewards
[**get_eth_stake_transaction_status**](EthApi.md#get_eth_stake_transaction_status) | **GET** /v1/eth/transaction/status | TX status
[**get_eth_stakes**](EthApi.md#get_eth_stakes) | **GET** /v1/eth/stakes | Stakes
[**post_eth_stake_transaction**](EthApi.md#post_eth_stake_transaction) | **POST** /v1/eth/transaction/stake | TX Craft
[**post_eth_transaction_broadcast**](EthApi.md#post_eth_transaction_broadcast) | **POST** /v1/eth/transaction/broadcast | TX Broadcast


# **get_eth_network_stats**
> GetEthNetworkStats200Response kiln.eth.get_eth_network_stats()

Network stats

Get the network statistics of Ethereum staking

### Example

```python
from kiln_connect import KilnConfig, KilnConnect
import os

with KilnConnect(KilnConfig.from_env()) as kiln:
    response = kiln.eth.get_eth_network_stats()
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetEthNetworkStats200Response**](GetEthNetworkStats200Response.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid status value |  -  |

[[Back to top]](#)
# **get_eth_operations**
> GetEthOperations200Response kiln.eth.get_eth_operations(validators=validators, wallets=wallets, accounts=accounts)

Operations

Get the operations of Ethereum stakes

### Example

```python
from kiln_connect import KilnConfig, KilnConnect
import os

with KilnConnect(KilnConfig.from_env()) as kiln:
    validators = ['validators_example'] # List[str] | Comma-separated list of validators addresses (optional)
    wallets = ['wallets_example'] # List[str] | Comma-separated list of wallets addresses (optional)
    accounts = ['accounts_example'] # List[str] | Comma-separated list of Kiln accounts identifiers (optional)
    response = kiln.eth.get_eth_operations(validators=validators, wallets=wallets, accounts=accounts)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validators** | [**List[str]**](str.md)| Comma-separated list of validators addresses | [optional] 
 **wallets** | [**List[str]**](str.md)| Comma-separated list of wallets addresses | [optional] 
 **accounts** | [**List[str]**](str.md)| Comma-separated list of Kiln accounts identifiers | [optional] 

### Return type

[**GetEthOperations200Response**](GetEthOperations200Response.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#)
# **get_eth_report**
> str kiln.eth.get_eth_report(validators=validators, wallets=wallets, accounts=accounts)

Report

Generates a report sheet for the stakes

### Example

```python
from kiln_connect import KilnConfig, KilnConnect
import os

with KilnConnect(KilnConfig.from_env()) as kiln:
    validators = ['validators_example'] # List[str] | Comma-separated list of validators addresses (optional)
    wallets = ['wallets_example'] # List[str] | Comma-separated list of wallets addresses (optional)
    accounts = ['accounts_example'] # List[str] | Comma-separated list of Kiln accounts identifiers (optional)
    response = kiln.eth.get_eth_report(validators=validators, wallets=wallets, accounts=accounts)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validators** | [**List[str]**](str.md)| Comma-separated list of validators addresses | [optional] 
 **wallets** | [**List[str]**](str.md)| Comma-separated list of wallets addresses | [optional] 
 **accounts** | [**List[str]**](str.md)| Comma-separated list of Kiln accounts identifiers | [optional] 

### Return type

**str**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid status value |  -  |

[[Back to top]](#)
# **get_eth_rewards**
> GetEthRewards200Response kiln.eth.get_eth_rewards(validators=validators, wallets=wallets, accounts=accounts)

Rewards

Get the rewards of Ethereum stakes

### Example

```python
from kiln_connect import KilnConfig, KilnConnect
import os

with KilnConnect(KilnConfig.from_env()) as kiln:
    validators = ['validators_example'] # List[str] | Comma-separated list of validators addresses (optional)
    wallets = ['wallets_example'] # List[str] | Comma-separated list of wallets addresses (optional)
    accounts = ['accounts_example'] # List[str] | Comma-separated list of Kiln accounts identifiers (optional)
    response = kiln.eth.get_eth_rewards(validators=validators, wallets=wallets, accounts=accounts)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validators** | [**List[str]**](str.md)| Comma-separated list of validators addresses | [optional] 
 **wallets** | [**List[str]**](str.md)| Comma-separated list of wallets addresses | [optional] 
 **accounts** | [**List[str]**](str.md)| Comma-separated list of Kiln accounts identifiers | [optional] 

### Return type

[**GetEthRewards200Response**](GetEthRewards200Response.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid status value |  -  |

[[Back to top]](#)
# **get_eth_stake_transaction_status**
> PostEthStakeTransaction201Response kiln.eth.get_eth_stake_transaction_status(tx_hash)

TX status

Get the status of an Ethereum transaction

### Example

```python
from kiln_connect import KilnConfig, KilnConnect
import os

with KilnConnect(KilnConfig.from_env()) as kiln:
    tx_hash = '0x43244f90814b31dec250de24df5bb023a338790c1d5a39244cf1064cf6d98c94' # str | Hash of the transaction
    response = kiln.eth.get_eth_stake_transaction_status(tx_hash)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tx_hash** | **str**| Hash of the transaction | 

### Return type

[**PostEthStakeTransaction201Response**](PostEthStakeTransaction201Response.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid status value |  -  |

[[Back to top]](#)
# **get_eth_stakes**
> GetEthStakes200Response kiln.eth.get_eth_stakes(validators=validators, wallets=wallets, accounts=accounts)

Stakes

Get the status of Ethereum stakes

### Example

```python
from kiln_connect import KilnConfig, KilnConnect
import os

with KilnConnect(KilnConfig.from_env()) as kiln:
    validators = ['validators_example'] # List[str] | Comma-separated list of validators addresses (optional)
    wallets = ['wallets_example'] # List[str] | Comma-separated list of wallets addresses (optional)
    accounts = ['accounts_example'] # List[str] | Comma-separated list of Kiln accounts identifiers (optional)
    response = kiln.eth.get_eth_stakes(validators=validators, wallets=wallets, accounts=accounts)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validators** | [**List[str]**](str.md)| Comma-separated list of validators addresses | [optional] 
 **wallets** | [**List[str]**](str.md)| Comma-separated list of wallets addresses | [optional] 
 **accounts** | [**List[str]**](str.md)| Comma-separated list of Kiln accounts identifiers | [optional] 

### Return type

[**GetEthStakes200Response**](GetEthStakes200Response.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid parameters |  -  |

[[Back to top]](#)
# **post_eth_stake_transaction**
> PostEthStakeTransaction201Response kiln.eth.post_eth_stake_transaction()

TX Craft

Generates a stake transaction for Ethereum

### Example

```python
from kiln_connect import KilnConfig, KilnConnect
import os

with KilnConnect(KilnConfig.from_env()) as kiln:
    response = kiln.eth.post_eth_stake_transaction()
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**PostEthStakeTransaction201Response**](PostEthStakeTransaction201Response.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | successful operation |  -  |
**400** | Invalid status value |  -  |

[[Back to top]](#)
# **post_eth_transaction_broadcast**
> PostEthTransactionBroadcast201Response kiln.eth.post_eth_transaction_broadcast(ethereum_broadcast_tx_query)

TX Broadcast

Broadcasts a transaction for Ethereum

### Example

```python
from kiln_connect import KilnConfig, KilnConnect
import os

with KilnConnect(KilnConfig.from_env()) as kiln:
    ethereum_broadcast_tx_query = kiln_connect.openapi_client.EthereumBroadcastTxQuery() # EthereumBroadcastTxQuery | Transaction to broadcast
    response = kiln.eth.post_eth_transaction_broadcast(ethereum_broadcast_tx_query)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ethereum_broadcast_tx_query** | [**EthereumBroadcastTxQuery**](EthereumBroadcastTxQuery.md)| Transaction to broadcast | 

### Return type

[**PostEthTransactionBroadcast201Response**](PostEthTransactionBroadcast201Response.md)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | successful operation |  -  |
**400** | Invalid status value |  -  |

[[Back to top]](#)
