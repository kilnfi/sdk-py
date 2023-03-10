# Documentation for XtzApi

All URIs are relative to *https://api.devnet.kiln.fi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_xtz_network_stats**](XtzApi.md#get_xtz_network_stats) | **GET** /v1/xtz/network-stats | Network Stats
[**get_xtz_rewards**](XtzApi.md#get_xtz_rewards) | **GET** /v1/xtz/rewards | Rewards
[**get_xtz_stakes**](XtzApi.md#get_xtz_stakes) | **GET** /v1/xtz/stakes | Stakes


# **get_xtz_network_stats**
> GetXtzNetworkStats200Response kiln.xtz.get_xtz_network_stats()

Network Stats

Get some network statistics on Tezos staking

### Example

```python
import kiln_connect
import os

with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kiln:
    response = kiln.xtz.get_xtz_network_stats()
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetXtzNetworkStats200Response**](GetXtzNetworkStats200Response.md)

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
# **get_xtz_rewards**
> GetXtzRewards200Response kiln.xtz.get_xtz_rewards(wallets=wallets, accounts=accounts, format=format, start_date=start_date, end_date=end_date, start_cycle=start_cycle, end_cycle=end_cycle)

Rewards

Get historical rewards of Tezos stakes

### Example

```python
import kiln_connect
import os

with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kiln:
    wallets = ['wallets_example'] # List[str] | Comma-separated list of wallets addresses (optional)
    accounts = ['accounts_example'] # List[str] | Comma-separated list of Kiln accounts identifiers (optional)
    format = 'format_example' # str | The format of the response. Defaults to daily (optional)
    start_date = 'Tue Jan 10 00:00:00 GMT 2023' # date | Get rewards from this date (YYYY-MM-DD) (optional)
    end_date = 'Fri Jan 20 00:00:00 GMT 2023' # date | Get rewards to this date (YYYY-MM-DD) (optional)
    start_cycle = 542 # float | The cycle from which we want to fetch rewards. Must be used with format=cycle (optional)
    end_cycle = 542 # float | The cycle until which we want to fetch rewards. Must be used with format=cycle (optional)
    response = kiln.xtz.get_xtz_rewards(wallets=wallets, accounts=accounts, format=format, start_date=start_date, end_date=end_date, start_cycle=start_cycle, end_cycle=end_cycle)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallets** | [**List[str]**](str.md)| Comma-separated list of wallets addresses | [optional] 
 **accounts** | [**List[str]**](str.md)| Comma-separated list of Kiln accounts identifiers | [optional] 
 **format** | **str**| The format of the response. Defaults to daily | [optional] 
 **start_date** | **date**| Get rewards from this date (YYYY-MM-DD) | [optional] 
 **end_date** | **date**| Get rewards to this date (YYYY-MM-DD) | [optional] 
 **start_cycle** | **float**| The cycle from which we want to fetch rewards. Must be used with format&#x3D;cycle | [optional] 
 **end_cycle** | **float**| The cycle until which we want to fetch rewards. Must be used with format&#x3D;cycle | [optional] 

### Return type

[**GetXtzRewards200Response**](GetXtzRewards200Response.md)

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
# **get_xtz_stakes**
> GetXtzStakes200Response kiln.xtz.get_xtz_stakes(wallets=wallets, accounts=accounts)

Stakes

Get the status of Tezos stakes

### Example

```python
import kiln_connect
import os

with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kiln:
    wallets = ['wallets_example'] # List[str] | Comma-separated list of wallets addresses (optional)
    accounts = ['accounts_example'] # List[str] | Comma-separated list of Kiln accounts identifiers (optional)
    response = kiln.xtz.get_xtz_stakes(wallets=wallets, accounts=accounts)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallets** | [**List[str]**](str.md)| Comma-separated list of wallets addresses | [optional] 
 **accounts** | [**List[str]**](str.md)| Comma-separated list of Kiln accounts identifiers | [optional] 

### Return type

[**GetXtzStakes200Response**](GetXtzStakes200Response.md)

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
