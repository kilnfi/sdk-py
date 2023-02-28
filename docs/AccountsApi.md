# Documentation for AccountsApi

All URIs are relative to *https://api.devnet.kiln.fi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account**](AccountsApi.md#get_account) | **GET** /v1/accounts/{id} | Account
[**get_account_portfolio**](AccountsApi.md#get_account_portfolio) | **GET** /v1/accounts/{id}/portfolio | Account Portfolio
[**get_accounts**](AccountsApi.md#get_accounts) | **GET** /v1/accounts | Accounts
[**post_account**](AccountsApi.md#post_account) | **POST** /v1/accounts | Accounts
[**put_account**](AccountsApi.md#put_account) | **PUT** /v1/accounts/{id} | Account


# **get_account**
> Account kiln.accounts.get_account(id)

Account

Retrieve an account in your organization

### Example

```python
import kiln_connect
import os

with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kiln:
    id = '92f5bfd4-ea38-4824-84f7-686eddff5539' # str | Account id
    response = kiln.accounts.get_account(id)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Account id | 

### Return type

[**Account**](Account.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#)
# **get_account_portfolio**
> AccountPortfolio kiln.accounts.get_account_portfolio(id)

Account Portfolio

Retrieve an account asset portfolio. USD balances are calculated based on recent asset prices. We use CoinGecko API to retrieve asset prices.

### Example

```python
import kiln_connect
import os

with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kiln:
    id = '92f5bfd4-ea38-4824-84f7-686eddff5539' # str | Account id
    response = kiln.accounts.get_account_portfolio(id)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Account id | 

### Return type

[**AccountPortfolio**](AccountPortfolio.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#)
# **get_accounts**
> AccountsResponse kiln.accounts.get_accounts()

Accounts

Retrieve accounts in your organization

### Example

```python
import kiln_connect
import os

with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kiln:
    response = kiln.accounts.get_accounts()
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountsResponse**](AccountsResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#)
# **post_account**
> Account kiln.accounts.post_account(account_payload)

Accounts

Create a new account in your organization

### Example

```python
import kiln_connect
import os

with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kiln:
    account_payload = kiln_connect.openapi_client.AccountPayload() # AccountPayload | Account to create
    response = kiln.accounts.post_account(account_payload)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_payload** | [**AccountPayload**](AccountPayload.md)| Account to create | 

### Return type

[**Account**](Account.md)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation |  -  |
**400** | Invalid parameters |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#)
# **put_account**
> Account kiln.accounts.put_account(id, account_payload)

Account

Update an account in your organization

### Example

```python
import kiln_connect
import os

with kiln_connect.KilnConnect(kiln_connect.KilnConfig.from_env()) as kiln:
    id = '92f5bfd4-ea38-4824-84f7-686eddff5539' # str | Account id
    account_payload = kiln_connect.openapi_client.AccountPayload() # AccountPayload | Account to update
    response = kiln.accounts.put_account(id, account_payload)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Account id | 
 **account_payload** | [**AccountPayload**](AccountPayload.md)| Account to update | 

### Return type

[**Account**](Account.md)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Invalid parameters |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#)
