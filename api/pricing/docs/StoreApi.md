# pricing.StoreApi

All URIs are relative to *https://kesko.azure-api.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_v2_stores**](StoreApi.md#get_v2_stores) | **GET** /v2/stores | Get info for multiple stores.
[**get_v2_stores_storeid**](StoreApi.md#get_v2_stores_storeid) | **GET** /v2/stores/{storeId} | Get info for a single store.


# **get_v2_stores**
> dict(str, object) get_v2_stores(ids=ids, limit=limit, offset=offset, last_seen=last_seen)

Get info for multiple stores.

Get info for multiple stores.

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
api_instance = pricing.StoreApi(pricing.ApiClient(configuration))
ids = 'ids_example' # str | Store ids. (optional)
limit = 20 # int | Limit for the quantity of returned results. Default: 20.  (optional) (default to 20)
offset = 0 # int | Offset for the current \"page\" ie. how many results to skip and when to start returning new results up to the defined limit. Default: 0.  (optional) (default to 0)
last_seen = 'last_seen_example' # str | Last seen EAN. (optional)

try:
    # Get info for multiple stores.
    api_response = api_instance.get_v2_stores(ids=ids, limit=limit, offset=offset, last_seen=last_seen)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreApi->get_v2_stores: %s\n" % e)
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
api_instance = pricing.StoreApi(pricing.ApiClient(configuration))
ids = 'ids_example' # str | Store ids. (optional)
limit = 20 # int | Limit for the quantity of returned results. Default: 20.  (optional) (default to 20)
offset = 0 # int | Offset for the current \"page\" ie. how many results to skip and when to start returning new results up to the defined limit. Default: 0.  (optional) (default to 0)
last_seen = 'last_seen_example' # str | Last seen EAN. (optional)

try:
    # Get info for multiple stores.
    api_response = api_instance.get_v2_stores(ids=ids, limit=limit, offset=offset, last_seen=last_seen)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreApi->get_v2_stores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| Store ids. | [optional] 
 **limit** | **int**| Limit for the quantity of returned results. Default: 20.  | [optional] [default to 20]
 **offset** | **int**| Offset for the current \&quot;page\&quot; ie. how many results to skip and when to start returning new results up to the defined limit. Default: 0.  | [optional] [default to 0]
 **last_seen** | **str**| Last seen EAN. | [optional] 

### Return type

**dict(str, object)**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object where keys are store ids and values are Store objects. |  -  |
**400** | Bad query parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_stores_storeid**
> V2StoresStoreIdGet200ApplicationJsonResponse get_v2_stores_storeid(store_id)

Get info for a single store.

Get info for a single store.

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
api_instance = pricing.StoreApi(pricing.ApiClient(configuration))
store_id = 'store_id_example' # str | Store id, for example C122.

try:
    # Get info for a single store.
    api_response = api_instance.get_v2_stores_storeid(store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreApi->get_v2_stores_storeid: %s\n" % e)
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
api_instance = pricing.StoreApi(pricing.ApiClient(configuration))
store_id = 'store_id_example' # str | Store id, for example C122.

try:
    # Get info for a single store.
    api_response = api_instance.get_v2_stores_storeid(store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreApi->get_v2_stores_storeid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| Store id, for example C122. | 

### Return type

[**V2StoresStoreIdGet200ApplicationJsonResponse**](V2StoresStoreIdGet200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found store object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

