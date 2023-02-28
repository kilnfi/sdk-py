# Documentation for EthApi

All URIs are relative to *https://api.devnet.kiln.fi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_eth_kiln_stats**](EthApi.md#get_eth_kiln_stats) | **GET** /v1/eth/kiln-stats | Kiln Stats
[**get_eth_network_stats**](EthApi.md#get_eth_network_stats) | **GET** /v1/eth/network-stats | Network Stats
[**get_eth_operations**](EthApi.md#get_eth_operations) | **GET** /v1/eth/operations | Operations
[**get_eth_reports**](EthApi.md#get_eth_reports) | **GET** /v1/eth/reports | Excel Reports
[**get_eth_rewards**](EthApi.md#get_eth_rewards) | **GET** /v1/eth/rewards | Rewards
[**get_eth_stakes**](EthApi.md#get_eth_stakes) | **GET** /v1/eth/stakes | Stakes
[**get_eth_tx_status**](EthApi.md#get_eth_tx_status) | **GET** /v1/eth/transaction/status | Transaction Status
[**post_eth_broadcast_tx**](EthApi.md#post_eth_broadcast_tx) | **POST** /v1/eth/transaction/broadcast | Broadcast Transaction
[**post_eth_keys**](EthApi.md#post_eth_keys) | **POST** /v1/eth/keys | Validation Keys
[**post_eth_prepare_tx**](EthApi.md#post_eth_prepare_tx) | **POST** /v1/eth/transaction/prepare | Prepare Transaction
[**post_eth_stake_tx**](EthApi.md#post_eth_stake_tx) | **POST** /v1/eth/transaction/stake | Stake Transaction


# **get_eth_kiln_stats**
> GetEthKilnStats200Response kiln.eth.get_eth_kiln_stats()

Kiln Stats

Get some Kiln statistics on Ethereum staking

### Example

```python
import kiln_connect
import os

with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kiln:
    response = kiln.eth.get_eth_kiln_stats()
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetEthKilnStats200Response**](GetEthKilnStats200Response.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#)
# **get_eth_network_stats**
> GetEthNetworkStats200Response kiln.eth.get_eth_network_stats()

Network Stats

Get some network statistics on Ethereum staking

### Example

```python
import kiln_connect
import os

with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kiln:
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
**200** | Successful operation |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#)
# **get_eth_operations**
> GetEthOperations200Response kiln.eth.get_eth_operations(validators=validators, wallets=wallets, accounts=accounts)

Operations

Get the operations of Ethereum stakes

### Example

```python
import kiln_connect
import os

with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kiln:
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
**200** | Successful operation |  -  |
**400** | Invalid parameters |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#)
# **get_eth_reports**
> str kiln.eth.get_eth_reports(validators=validators, wallets=wallets, accounts=accounts)

Excel Reports

Generates an Excel report sheet for your stakes and rewards

### Example

```python
import kiln_connect
import os

with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kiln:
    validators = ['validators_example'] # List[str] | Comma-separated list of validators addresses (optional)
    wallets = ['wallets_example'] # List[str] | Comma-separated list of wallets addresses (optional)
    accounts = ['accounts_example'] # List[str] | Comma-separated list of Kiln accounts identifiers (optional)
    response = kiln.eth.get_eth_reports(validators=validators, wallets=wallets, accounts=accounts)
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
**200** | Successful operation |  -  |
**400** | Invalid parameters |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#)
# **get_eth_rewards**
> GetEthRewards200Response kiln.eth.get_eth_rewards(validators=validators, wallets=wallets, accounts=accounts, start_date=start_date, end_date=end_date)

Rewards

Get historical rewards by day of Ethereum stakes

### Example

```python
import kiln_connect
import os

with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kiln:
    validators = ['validators_example'] # List[str] | Comma-separated list of validators addresses (optional)
    wallets = ['wallets_example'] # List[str] | Comma-separated list of wallets addresses (optional)
    accounts = ['accounts_example'] # List[str] | Comma-separated list of Kiln accounts identifiers (optional)
    start_date = 'Tue Jan 10 00:00:00 GMT 2023' # date | Get rewards from this date (YYYY-MM-DD) (optional)
    end_date = 'Fri Jan 20 00:00:00 GMT 2023' # date | Get rewards to this date (YYYY-MM-DD) (optional)
    response = kiln.eth.get_eth_rewards(validators=validators, wallets=wallets, accounts=accounts, start_date=start_date, end_date=end_date)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validators** | [**List[str]**](str.md)| Comma-separated list of validators addresses | [optional] 
 **wallets** | [**List[str]**](str.md)| Comma-separated list of wallets addresses | [optional] 
 **accounts** | [**List[str]**](str.md)| Comma-separated list of Kiln accounts identifiers | [optional] 
 **start_date** | **date**| Get rewards from this date (YYYY-MM-DD) | [optional] 
 **end_date** | **date**| Get rewards to this date (YYYY-MM-DD) | [optional] 

### Return type

[**GetEthRewards200Response**](GetEthRewards200Response.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Invalid parameters |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#)
# **get_eth_stakes**
> GetEthStakes200Response kiln.eth.get_eth_stakes(validators=validators, wallets=wallets, accounts=accounts)

Stakes

Get the status of Ethereum stakes

### Example

```python
import kiln_connect
import os

with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kiln:
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
**200** | Successful operation |  -  |
**400** | Invalid parameters |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#)
# **get_eth_tx_status**
> PostEthStakeTx201Response kiln.eth.get_eth_tx_status(tx_hash)

Transaction Status

Get the status of an Ethereum transaction

### Example

```python
import kiln_connect
import os

with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kiln:
    tx_hash = '0x43244f90814b31dec250de24df5bb023a338790c1d5a39244cf1064cf6d98c94' # str | Hash of the transaction
    response = kiln.eth.get_eth_tx_status(tx_hash)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tx_hash** | **str**| Hash of the transaction | 

### Return type

[**PostEthStakeTx201Response**](PostEthStakeTx201Response.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Invalid parameters |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#)
# **post_eth_broadcast_tx**
> PostEthBroadcastTx201Response kiln.eth.post_eth_broadcast_tx(ethereum_broadcast_tx_payload)

Broadcast Transaction

Broadcasts a signed Ethereum transaction

### Example

```python
import kiln_connect
import os

with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kiln:
    ethereum_broadcast_tx_payload = kiln_connect.openapi_client.EthereumBroadcastTxPayload() # EthereumBroadcastTxPayload | Transaction to broadcast
    response = kiln.eth.post_eth_broadcast_tx(ethereum_broadcast_tx_payload)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ethereum_broadcast_tx_payload** | [**EthereumBroadcastTxPayload**](EthereumBroadcastTxPayload.md)| Transaction to broadcast | 

### Return type

[**PostEthBroadcastTx201Response**](PostEthBroadcastTx201Response.md)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation |  -  |
**400** | Invalid parameters |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#)
# **post_eth_keys**
> PostEthKeys201Response kiln.eth.post_eth_keys(ethereum_post_keys_payload)

Validation Keys

Create Ethereum validation keys on Kiln's infrastructure.

### Example

```python
import kiln_connect
import os

with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kiln:
    ethereum_post_keys_payload = kiln_connect.openapi_client.EthereumPostKeysPayload() # EthereumPostKeysPayload | Ethereum keys to generate
    response = kiln.eth.post_eth_keys(ethereum_post_keys_payload)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ethereum_post_keys_payload** | [**EthereumPostKeysPayload**](EthereumPostKeysPayload.md)| Ethereum keys to generate | 

### Return type

[**PostEthKeys201Response**](PostEthKeys201Response.md)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation |  -  |
**400** | Invalid parameters |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#)
# **post_eth_prepare_tx**
> PostEthPrepareTx201Response kiln.eth.post_eth_prepare_tx(ethereum_prepare_tx_payload)

Prepare Transaction

Prepare an Ethereum transaction for broadcasting. It takes a serialized transaction and its signatures and returns a serialized signed transaction that can be broadcasted.

### Example

```python
import kiln_connect
import os

with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kiln:
    ethereum_prepare_tx_payload = kiln_connect.openapi_client.EthereumPrepareTxPayload() # EthereumPrepareTxPayload | Transaction to prepare
    response = kiln.eth.post_eth_prepare_tx(ethereum_prepare_tx_payload)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ethereum_prepare_tx_payload** | [**EthereumPrepareTxPayload**](EthereumPrepareTxPayload.md)| Transaction to prepare | 

### Return type

[**PostEthPrepareTx201Response**](PostEthPrepareTx201Response.md)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation |  -  |
**400** | Invalid parameters |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#)
# **post_eth_stake_tx**
> PostEthStakeTx201Response kiln.eth.post_eth_stake_tx(ethereum_craft_stake_tx_payload)

Stake Transaction

Generates an Ethereum EIP 1559 stake transaction

### Example

```python
import kiln_connect
import os

with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kiln:
    ethereum_craft_stake_tx_payload = kiln_connect.openapi_client.EthereumCraftStakeTxPayload() # EthereumCraftStakeTxPayload | Transaction to craft
    response = kiln.eth.post_eth_stake_tx(ethereum_craft_stake_tx_payload)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ethereum_craft_stake_tx_payload** | [**EthereumCraftStakeTxPayload**](EthereumCraftStakeTxPayload.md)| Transaction to craft | 

### Return type

[**PostEthStakeTx201Response**](PostEthStakeTx201Response.md)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation |  -  |
**400** | Invalid parameters |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#)
