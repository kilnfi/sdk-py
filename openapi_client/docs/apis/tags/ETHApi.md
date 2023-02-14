<a name="__pageTop"></a>
# openapi_client.apis.tags.eth_api.ETHApi

All URIs are relative to *https://api.devnet.kiln.fi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_eth_stake_transaction_status**](#get_eth_stake_transaction_status) | **get** /v1/eth/transaction/status | Transaction status
[**get_ethereum_network_stats**](#get_ethereum_network_stats) | **get** /v1/eth/network-stats | Network stats
[**get_ethereum_operations**](#get_ethereum_operations) | **get** /v1/eth/operations | Operations
[**get_ethereum_report**](#get_ethereum_report) | **get** /v1/eth/reports | Report
[**get_ethereum_rewards**](#get_ethereum_rewards) | **get** /v1/eth/rewards | Rewards
[**get_ethereum_stakes**](#get_ethereum_stakes) | **get** /v1/eth/stakes | Ethereum stakes
[**post_eth_stake_transaction**](#post_eth_stake_transaction) | **post** /v1/eth/transaction/stake | Stake creation
[**post_eth_transaction_broadcast**](#post_eth_transaction_broadcast) | **post** /v1/eth/transaction/broadcast | Transaction broadcast

# **get_eth_stake_transaction_status**
<a name="get_eth_stake_transaction_status"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_eth_stake_transaction_status(tx_hash)

Transaction status

Get the status of an Ethereum transaction

### Example

* Bearer Authentication (bearerAuth):
```python
import openapi_client
from openapi_client.apis.tags import eth_api
from openapi_client.model.ethereum_unsigned_stake_tx import EthereumUnsignedStakeTx
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
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eth_api.ETHApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'tx_hash': "0x43244f90814b31dec250de24df5bb023a338790c1d5a39244cf1064cf6d98c94",
    }
    try:
        # Transaction status
        api_response = api_instance.get_eth_stake_transaction_status(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ETHApi->get_eth_stake_transaction_status: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json; charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
tx_hash | TxHashSchema | | 


# TxHashSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_eth_stake_transaction_status.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_eth_stake_transaction_status.ApiResponseFor400) | Invalid status value

#### get_eth_stake_transaction_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonCharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonCharsetutf8

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**data** | [**EthereumUnsignedStakeTx**]({{complexTypePrefix}}EthereumUnsignedStakeTx.md) | [**EthereumUnsignedStakeTx**]({{complexTypePrefix}}EthereumUnsignedStakeTx.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_eth_stake_transaction_status.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_ethereum_network_stats**
<a name="get_ethereum_network_stats"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_ethereum_network_stats()

Network stats

Get the network statistics of Ethereum staking

### Example

* Bearer Authentication (bearerAuth):
```python
import openapi_client
from openapi_client.apis.tags import eth_api
from openapi_client.model.ethereum_network_stats import EthereumNetworkStats
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
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eth_api.ETHApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Network stats
        api_response = api_instance.get_ethereum_network_stats()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ETHApi->get_ethereum_network_stats: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_ethereum_network_stats.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_ethereum_network_stats.ApiResponseFor400) | Invalid status value

#### get_ethereum_network_stats.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonCharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonCharsetutf8

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**data** | [**EthereumNetworkStats**]({{complexTypePrefix}}EthereumNetworkStats.md) | [**EthereumNetworkStats**]({{complexTypePrefix}}EthereumNetworkStats.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_ethereum_network_stats.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_ethereum_operations**
<a name="get_ethereum_operations"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_ethereum_operations()

Operations

Get the operations of Ethereum stakes

### Example

* Bearer Authentication (bearerAuth):
```python
import openapi_client
from openapi_client.apis.tags import eth_api
from openapi_client.model.ethereum_operation_execution_reward import EthereumOperationExecutionReward
from openapi_client.model.ethereum_operation_deposit import EthereumOperationDeposit
from openapi_client.model.ethereum_operation_consensus_withdrawal import EthereumOperationConsensusWithdrawal
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
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eth_api.ETHApi(api_client)

    # example passing only optional values
    query_params = {
        'validators': [
        "0x95373bcf8e2c64e1c373a6e534c002f210adbcc84c5abda3b6306677e171430ae50781a51c9f579a47622e334dba2412"
    ],
        'wallets': [
        "0xe1f4acc0affB36a805474e3b6ab786738C6900A2"
    ],
        'accounts': [
        "b7177fd2-fbb3-479f-aa92-db9fb16e229f"
    ],
    }
    try:
        # Operations
        api_response = api_instance.get_ethereum_operations(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ETHApi->get_ethereum_operations: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json; charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
validators | ValidatorsSchema | | optional
wallets | WalletsSchema | | optional
accounts | AccountsSchema | | optional


# ValidatorsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# WalletsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# AccountsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_ethereum_operations.ApiResponseFor200) | successful operation

#### get_ethereum_operations.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonCharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonCharsetutf8

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[data](#data)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[EthereumOperationDeposit]({{complexTypePrefix}}EthereumOperationDeposit.md) | [**EthereumOperationDeposit**]({{complexTypePrefix}}EthereumOperationDeposit.md) | [**EthereumOperationDeposit**]({{complexTypePrefix}}EthereumOperationDeposit.md) |  | 
[EthereumOperationConsensusWithdrawal]({{complexTypePrefix}}EthereumOperationConsensusWithdrawal.md) | [**EthereumOperationConsensusWithdrawal**]({{complexTypePrefix}}EthereumOperationConsensusWithdrawal.md) | [**EthereumOperationConsensusWithdrawal**]({{complexTypePrefix}}EthereumOperationConsensusWithdrawal.md) |  | 
[EthereumOperationExecutionReward]({{complexTypePrefix}}EthereumOperationExecutionReward.md) | [**EthereumOperationExecutionReward**]({{complexTypePrefix}}EthereumOperationExecutionReward.md) | [**EthereumOperationExecutionReward**]({{complexTypePrefix}}EthereumOperationExecutionReward.md) |  | 

### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_ethereum_report**
<a name="get_ethereum_report"></a>
> file_type get_ethereum_report()

Report

Generates a report sheet for the stakes

### Example

* Bearer Authentication (bearerAuth):
```python
import openapi_client
from openapi_client.apis.tags import eth_api
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
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eth_api.ETHApi(api_client)

    # example passing only optional values
    query_params = {
        'validators': [
        "0x95373bcf8e2c64e1c373a6e534c002f210adbcc84c5abda3b6306677e171430ae50781a51c9f579a47622e334dba2412"
    ],
        'wallets': [
        "0xe1f4acc0affB36a805474e3b6ab786738C6900A2"
    ],
        'accounts': [
        "b7177fd2-fbb3-479f-aa92-db9fb16e229f"
    ],
    }
    try:
        # Report
        api_response = api_instance.get_ethereum_report(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ETHApi->get_ethereum_report: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/octet-stream', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
validators | ValidatorsSchema | | optional
wallets | WalletsSchema | | optional
accounts | AccountsSchema | | optional


# ValidatorsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# WalletsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# AccountsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_ethereum_report.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_ethereum_report.ApiResponseFor400) | Invalid status value

#### get_ethereum_report.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationOctetStream, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationOctetStream

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

#### get_ethereum_report.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_ethereum_rewards**
<a name="get_ethereum_rewards"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_ethereum_rewards()

Rewards

Get the rewards of Ethereum stakes

### Example

* Bearer Authentication (bearerAuth):
```python
import openapi_client
from openapi_client.apis.tags import eth_api
from openapi_client.model.ethereum_reward import EthereumReward
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
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eth_api.ETHApi(api_client)

    # example passing only optional values
    query_params = {
        'validators': [
        "0x95373bcf8e2c64e1c373a6e534c002f210adbcc84c5abda3b6306677e171430ae50781a51c9f579a47622e334dba2412"
    ],
        'wallets': [
        "0xe1f4acc0affB36a805474e3b6ab786738C6900A2"
    ],
        'accounts': [
        "b7177fd2-fbb3-479f-aa92-db9fb16e229f"
    ],
    }
    try:
        # Rewards
        api_response = api_instance.get_ethereum_rewards(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ETHApi->get_ethereum_rewards: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json; charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
validators | ValidatorsSchema | | optional
wallets | WalletsSchema | | optional
accounts | AccountsSchema | | optional


# ValidatorsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# WalletsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# AccountsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_ethereum_rewards.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_ethereum_rewards.ApiResponseFor400) | Invalid status value

#### get_ethereum_rewards.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonCharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonCharsetutf8

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[data](#data)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EthereumReward**]({{complexTypePrefix}}EthereumReward.md) | [**EthereumReward**]({{complexTypePrefix}}EthereumReward.md) | [**EthereumReward**]({{complexTypePrefix}}EthereumReward.md) |  | 

#### get_ethereum_rewards.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_ethereum_stakes**
<a name="get_ethereum_stakes"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_ethereum_stakes()

Ethereum stakes

Get the status of Ethereum stakes

### Example

* Bearer Authentication (bearerAuth):
```python
import openapi_client
from openapi_client.apis.tags import eth_api
from openapi_client.model.ethereum_stake import EthereumStake
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
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eth_api.ETHApi(api_client)

    # example passing only optional values
    query_params = {
        'validators': [
        "0x95373bcf8e2c64e1c373a6e534c002f210adbcc84c5abda3b6306677e171430ae50781a51c9f579a47622e334dba2412"
    ],
        'wallets': [
        "0xe1f4acc0affB36a805474e3b6ab786738C6900A2"
    ],
        'accounts': [
        "b7177fd2-fbb3-479f-aa92-db9fb16e229f"
    ],
    }
    try:
        # Ethereum stakes
        api_response = api_instance.get_ethereum_stakes(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ETHApi->get_ethereum_stakes: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json; charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
validators | ValidatorsSchema | | optional
wallets | WalletsSchema | | optional
accounts | AccountsSchema | | optional


# ValidatorsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# WalletsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# AccountsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_ethereum_stakes.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_ethereum_stakes.ApiResponseFor400) | Invalid parameters

#### get_ethereum_stakes.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonCharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonCharsetutf8

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[data](#data)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EthereumStake**]({{complexTypePrefix}}EthereumStake.md) | [**EthereumStake**]({{complexTypePrefix}}EthereumStake.md) | [**EthereumStake**]({{complexTypePrefix}}EthereumStake.md) |  | 

#### get_ethereum_stakes.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_eth_stake_transaction**
<a name="post_eth_stake_transaction"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} post_eth_stake_transaction()

Stake creation

Generates a stake transaction for Ethereum

### Example

* Bearer Authentication (bearerAuth):
```python
import openapi_client
from openapi_client.apis.tags import eth_api
from openapi_client.model.ethereum_unsigned_stake_tx import EthereumUnsignedStakeTx
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
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eth_api.ETHApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Stake creation
        api_response = api_instance.post_eth_stake_transaction()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ETHApi->post_eth_stake_transaction: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#post_eth_stake_transaction.ApiResponseFor201) | successful operation
400 | [ApiResponseFor400](#post_eth_stake_transaction.ApiResponseFor400) | Invalid status value

#### post_eth_stake_transaction.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJsonCharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJsonCharsetutf8

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**data** | [**EthereumUnsignedStakeTx**]({{complexTypePrefix}}EthereumUnsignedStakeTx.md) | [**EthereumUnsignedStakeTx**]({{complexTypePrefix}}EthereumUnsignedStakeTx.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### post_eth_stake_transaction.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_eth_transaction_broadcast**
<a name="post_eth_transaction_broadcast"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} post_eth_transaction_broadcast(ethereum_broadcast_tx_query)

Transaction broadcast

Broadcasts a transaction for Ethereum

### Example

* Bearer Authentication (bearerAuth):
```python
import openapi_client
from openapi_client.apis.tags import eth_api
from openapi_client.model.ethereum_broadcast_tx_response import EthereumBroadcastTxResponse
from openapi_client.model.ethereum_broadcast_tx_query import EthereumBroadcastTxQuery
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
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eth_api.ETHApi(api_client)

    # example passing only required values which don't have defaults set
    body = EthereumBroadcastTxQuery(
        serialized_tx="serialized_tx_example",
    )
    try:
        # Transaction broadcast
        api_response = api_instance.post_eth_transaction_broadcast(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ETHApi->post_eth_transaction_broadcast: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonCharsetutf8] | required |
content_type | str | optional, default is 'application/json; charset&#x3D;utf-8' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json; charset&#x3D;utf-8', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsonCharsetutf8
Type | Description  | Notes
------------- | ------------- | -------------
[**EthereumBroadcastTxQuery**](../../models/EthereumBroadcastTxQuery.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#post_eth_transaction_broadcast.ApiResponseFor201) | successful operation
400 | [ApiResponseFor400](#post_eth_transaction_broadcast.ApiResponseFor400) | Invalid status value

#### post_eth_transaction_broadcast.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJsonCharsetutf8, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJsonCharsetutf8

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**data** | [**EthereumBroadcastTxResponse**]({{complexTypePrefix}}EthereumBroadcastTxResponse.md) | [**EthereumBroadcastTxResponse**]({{complexTypePrefix}}EthereumBroadcastTxResponse.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### post_eth_transaction_broadcast.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

