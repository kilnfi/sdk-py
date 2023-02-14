# openapi_client.ETHApi

All URIs are relative to *https://api.devnet.kiln.fi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_eth_network_stats**](ETHApi.md#get_eth_network_stats) | **GET** /v1/eth/network-stats | Network stats
[**get_eth_operations**](ETHApi.md#get_eth_operations) | **GET** /v1/eth/operations | Operations
[**get_eth_report**](ETHApi.md#get_eth_report) | **GET** /v1/eth/reports | Report
[**get_eth_rewards**](ETHApi.md#get_eth_rewards) | **GET** /v1/eth/rewards | Rewards
[**get_eth_stake_transaction_status**](ETHApi.md#get_eth_stake_transaction_status) | **GET** /v1/eth/transaction/status | Transaction status
[**get_eth_stakes**](ETHApi.md#get_eth_stakes) | **GET** /v1/eth/stakes | Ethereum stakes
[**post_eth_stake_transaction**](ETHApi.md#post_eth_stake_transaction) | **POST** /v1/eth/transaction/stake | Stake creation
[**post_eth_transaction_broadcast**](ETHApi.md#post_eth_transaction_broadcast) | **POST** /v1/eth/transaction/broadcast | Transaction broadcast


# **get_eth_network_stats**
> GetEthNetworkStats200Response get_eth_network_stats()

Network stats

Get the network statistics of Ethereum staking

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.devnet.kiln.fi
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.devnet.kiln.fi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ETHApi(api_client)

    try:
        # Network stats
        api_response = api_instance.get_eth_network_stats()
        print("The response of ETHApi->get_eth_network_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ETHApi->get_eth_network_stats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetEthNetworkStats200Response**](GetEthNetworkStats200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid status value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_eth_operations**
> GetEthOperations200Response get_eth_operations(validators=validators, wallets=wallets, accounts=accounts)

Operations

Get the operations of Ethereum stakes

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.devnet.kiln.fi
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.devnet.kiln.fi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ETHApi(api_client)
    validators = ['validators_example'] # List[str] | Comma-separated list of validators addresses (optional)
    wallets = ['wallets_example'] # List[str] | Comma-separated list of wallets addresses (optional)
    accounts = ['accounts_example'] # List[str] | Comma-separated list of Kiln accounts identifiers (optional)

    try:
        # Operations
        api_response = api_instance.get_eth_operations(validators=validators, wallets=wallets, accounts=accounts)
        print("The response of ETHApi->get_eth_operations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ETHApi->get_eth_operations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validators** | [**List[str]**](str.md)| Comma-separated list of validators addresses | [optional] 
 **wallets** | [**List[str]**](str.md)| Comma-separated list of wallets addresses | [optional] 
 **accounts** | [**List[str]**](str.md)| Comma-separated list of Kiln accounts identifiers | [optional] 

### Return type

[**GetEthOperations200Response**](GetEthOperations200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_eth_report**
> str get_eth_report(validators=validators, wallets=wallets, accounts=accounts)

Report

Generates a report sheet for the stakes

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.devnet.kiln.fi
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.devnet.kiln.fi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ETHApi(api_client)
    validators = ['validators_example'] # List[str] | Comma-separated list of validators addresses (optional)
    wallets = ['wallets_example'] # List[str] | Comma-separated list of wallets addresses (optional)
    accounts = ['accounts_example'] # List[str] | Comma-separated list of Kiln accounts identifiers (optional)

    try:
        # Report
        api_response = api_instance.get_eth_report(validators=validators, wallets=wallets, accounts=accounts)
        print("The response of ETHApi->get_eth_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ETHApi->get_eth_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validators** | [**List[str]**](str.md)| Comma-separated list of validators addresses | [optional] 
 **wallets** | [**List[str]**](str.md)| Comma-separated list of wallets addresses | [optional] 
 **accounts** | [**List[str]**](str.md)| Comma-separated list of Kiln accounts identifiers | [optional] 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid status value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_eth_rewards**
> GetEthRewards200Response get_eth_rewards(validators=validators, wallets=wallets, accounts=accounts)

Rewards

Get the rewards of Ethereum stakes

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.devnet.kiln.fi
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.devnet.kiln.fi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ETHApi(api_client)
    validators = ['validators_example'] # List[str] | Comma-separated list of validators addresses (optional)
    wallets = ['wallets_example'] # List[str] | Comma-separated list of wallets addresses (optional)
    accounts = ['accounts_example'] # List[str] | Comma-separated list of Kiln accounts identifiers (optional)

    try:
        # Rewards
        api_response = api_instance.get_eth_rewards(validators=validators, wallets=wallets, accounts=accounts)
        print("The response of ETHApi->get_eth_rewards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ETHApi->get_eth_rewards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validators** | [**List[str]**](str.md)| Comma-separated list of validators addresses | [optional] 
 **wallets** | [**List[str]**](str.md)| Comma-separated list of wallets addresses | [optional] 
 **accounts** | [**List[str]**](str.md)| Comma-separated list of Kiln accounts identifiers | [optional] 

### Return type

[**GetEthRewards200Response**](GetEthRewards200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid status value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_eth_stake_transaction_status**
> PostEthStakeTransaction201Response get_eth_stake_transaction_status(tx_hash)

Transaction status

Get the status of an Ethereum transaction

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.devnet.kiln.fi
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.devnet.kiln.fi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ETHApi(api_client)
    tx_hash = '0x43244f90814b31dec250de24df5bb023a338790c1d5a39244cf1064cf6d98c94' # str | Hash of the transaction

    try:
        # Transaction status
        api_response = api_instance.get_eth_stake_transaction_status(tx_hash)
        print("The response of ETHApi->get_eth_stake_transaction_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ETHApi->get_eth_stake_transaction_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tx_hash** | **str**| Hash of the transaction | 

### Return type

[**PostEthStakeTransaction201Response**](PostEthStakeTransaction201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid status value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_eth_stakes**
> GetEthStakes200Response get_eth_stakes(validators=validators, wallets=wallets, accounts=accounts)

Ethereum stakes

Get the status of Ethereum stakes

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.devnet.kiln.fi
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.devnet.kiln.fi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ETHApi(api_client)
    validators = ['validators_example'] # List[str] | Comma-separated list of validators addresses (optional)
    wallets = ['wallets_example'] # List[str] | Comma-separated list of wallets addresses (optional)
    accounts = ['accounts_example'] # List[str] | Comma-separated list of Kiln accounts identifiers (optional)

    try:
        # Ethereum stakes
        api_response = api_instance.get_eth_stakes(validators=validators, wallets=wallets, accounts=accounts)
        print("The response of ETHApi->get_eth_stakes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ETHApi->get_eth_stakes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validators** | [**List[str]**](str.md)| Comma-separated list of validators addresses | [optional] 
 **wallets** | [**List[str]**](str.md)| Comma-separated list of wallets addresses | [optional] 
 **accounts** | [**List[str]**](str.md)| Comma-separated list of Kiln accounts identifiers | [optional] 

### Return type

[**GetEthStakes200Response**](GetEthStakes200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_eth_stake_transaction**
> PostEthStakeTransaction201Response post_eth_stake_transaction()

Stake creation

Generates a stake transaction for Ethereum

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.devnet.kiln.fi
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.devnet.kiln.fi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ETHApi(api_client)

    try:
        # Stake creation
        api_response = api_instance.post_eth_stake_transaction()
        print("The response of ETHApi->post_eth_stake_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ETHApi->post_eth_stake_transaction: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PostEthStakeTransaction201Response**](PostEthStakeTransaction201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | successful operation |  -  |
**400** | Invalid status value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_eth_transaction_broadcast**
> PostEthTransactionBroadcast201Response post_eth_transaction_broadcast(ethereum_broadcast_tx_query)

Transaction broadcast

Broadcasts a transaction for Ethereum

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.devnet.kiln.fi
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.devnet.kiln.fi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ETHApi(api_client)
    ethereum_broadcast_tx_query = openapi_client.EthereumBroadcastTxQuery() # EthereumBroadcastTxQuery | Transaction to broadcast

    try:
        # Transaction broadcast
        api_response = api_instance.post_eth_transaction_broadcast(ethereum_broadcast_tx_query)
        print("The response of ETHApi->post_eth_transaction_broadcast:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ETHApi->post_eth_transaction_broadcast: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ethereum_broadcast_tx_query** | [**EthereumBroadcastTxQuery**](EthereumBroadcastTxQuery.md)| Transaction to broadcast | 

### Return type

[**PostEthTransactionBroadcast201Response**](PostEthTransactionBroadcast201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | successful operation |  -  |
**400** | Invalid status value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

