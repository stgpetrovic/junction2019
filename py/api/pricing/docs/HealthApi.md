# pricing.HealthApi

All URIs are relative to *https://kesko.azure-api.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health**](HealthApi.md#get_health) | **GET** /health | Simple health check.


# **get_health**
> HealthGet200ApplicationJsonResponse get_health()

Simple health check.

Runs dummy queries on the database and caches.  

### Example

* Api Key Authentication (apiKeyHeader):
```python
from __future__ import print_function
import time
import pricing
from pricing.rest import ApiException
from pprint import pprint
configuration = pricing.Configuration()
# Configure API key authorization: apiKeyHeader
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
configuration = pricing.Configuration()
# Configure API key authorization: apiKeyQuery
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# Defining host is optional and default to https://kesko.azure-api.net
configuration.host = "https://kesko.azure-api.net"
# Create an instance of the API class
api_instance = pricing.HealthApi(pricing.ApiClient(configuration))

try:
    # Simple health check.
    api_response = api_instance.get_health()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthApi->get_health: %s\n" % e)
```

* Api Key Authentication (apiKeyQuery):
```python
from __future__ import print_function
import time
import pricing
from pricing.rest import ApiException
from pprint import pprint
configuration = pricing.Configuration()
# Configure API key authorization: apiKeyHeader
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
configuration = pricing.Configuration()
# Configure API key authorization: apiKeyQuery
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# Defining host is optional and default to https://kesko.azure-api.net
configuration.host = "https://kesko.azure-api.net"
# Create an instance of the API class
api_instance = pricing.HealthApi(pricing.ApiClient(configuration))

try:
    # Simple health check.
    api_response = api_instance.get_health()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthApi->get_health: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HealthGet200ApplicationJsonResponse**](HealthGet200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirmation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

