# openapi_client.TargetsApi

All URIs are relative to *https://kesko.azure-api.net/ratings*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_targets_targetnamespace**](TargetsApi.md#get_targets_targetnamespace) | **GET** /targets/{targetNamespace} | Lists all targets currently in the database.


# **get_targets_targetnamespace**
> list[object] get_targets_targetnamespace(target_namespace, offset=offset, limit=limit, sort=sort, x_ip_address=x_ip_address, x_author_id=x_author_id)

Lists all targets currently in the database.

Lists all targets currently in the database.

### Example

* Api Key Authentication (apiKeyHeader):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure API key authorization: apiKeyHeader
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure API key authorization: apiKeyQuery
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# Defining host is optional and default to https://kesko.azure-api.net/ratings
configuration.host = "https://kesko.azure-api.net/ratings"
# Create an instance of the API class
api_instance = openapi_client.TargetsApi(openapi_client.ApiClient(configuration))
target_namespace = 'target_namespace_example' # str | Target namespace
offset = 0 # int | Offset for pagination. Default is **0**. When using this parameter, specify `limit` explicitly. The defaults might change.  (optional) (default to 0)
limit = 56 # int | Limit of returned items. By default, there is no limit as we need all targets in the UI.  (optional)
sort = 'sort_example' # str | Sort based on given field. Format: `attribute:direction`. `direction` is optional, default is **asc**. For example: `createdAt`, `updatedAt:desc`, `updatedAt:asc`.  (optional)
x_ip_address = 'x_ip_address_example' # str | Tells the original requester's IP address to this API. It is needed for moderation purposes. Explained more in [the IP addresses section of the API documentation](../docs/API#ip-addresses). This value is important and should always be included, but isn't strictly required by the API.  (optional)
x_author_id = 'x_author_id_example' # str | **Warning:** this ID should be SAME across all services using this rating service. Tells the original requester's user ID. This is used to restrict some actions. For example author with ID `265` should not be able to modify rating created by user with ID `318`. This value is important and should always be included, but isn't strictly required by the API.  (optional)

try:
    # Lists all targets currently in the database.
    api_response = api_instance.get_targets_targetnamespace(target_namespace, offset=offset, limit=limit, sort=sort, x_ip_address=x_ip_address, x_author_id=x_author_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->get_targets_targetnamespace: %s\n" % e)
```

* Api Key Authentication (apiKeyQuery):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure API key authorization: apiKeyHeader
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure API key authorization: apiKeyQuery
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# Defining host is optional and default to https://kesko.azure-api.net/ratings
configuration.host = "https://kesko.azure-api.net/ratings"
# Create an instance of the API class
api_instance = openapi_client.TargetsApi(openapi_client.ApiClient(configuration))
target_namespace = 'target_namespace_example' # str | Target namespace
offset = 0 # int | Offset for pagination. Default is **0**. When using this parameter, specify `limit` explicitly. The defaults might change.  (optional) (default to 0)
limit = 56 # int | Limit of returned items. By default, there is no limit as we need all targets in the UI.  (optional)
sort = 'sort_example' # str | Sort based on given field. Format: `attribute:direction`. `direction` is optional, default is **asc**. For example: `createdAt`, `updatedAt:desc`, `updatedAt:asc`.  (optional)
x_ip_address = 'x_ip_address_example' # str | Tells the original requester's IP address to this API. It is needed for moderation purposes. Explained more in [the IP addresses section of the API documentation](../docs/API#ip-addresses). This value is important and should always be included, but isn't strictly required by the API.  (optional)
x_author_id = 'x_author_id_example' # str | **Warning:** this ID should be SAME across all services using this rating service. Tells the original requester's user ID. This is used to restrict some actions. For example author with ID `265` should not be able to modify rating created by user with ID `318`. This value is important and should always be included, but isn't strictly required by the API.  (optional)

try:
    # Lists all targets currently in the database.
    api_response = api_instance.get_targets_targetnamespace(target_namespace, offset=offset, limit=limit, sort=sort, x_ip_address=x_ip_address, x_author_id=x_author_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->get_targets_targetnamespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_namespace** | **str**| Target namespace | 
 **offset** | **int**| Offset for pagination. Default is **0**. When using this parameter, specify &#x60;limit&#x60; explicitly. The defaults might change.  | [optional] [default to 0]
 **limit** | **int**| Limit of returned items. By default, there is no limit as we need all targets in the UI.  | [optional] 
 **sort** | **str**| Sort based on given field. Format: &#x60;attribute:direction&#x60;. &#x60;direction&#x60; is optional, default is **asc**. For example: &#x60;createdAt&#x60;, &#x60;updatedAt:desc&#x60;, &#x60;updatedAt:asc&#x60;.  | [optional] 
 **x_ip_address** | **str**| Tells the original requester&#39;s IP address to this API. It is needed for moderation purposes. Explained more in [the IP addresses section of the API documentation](../docs/API#ip-addresses). This value is important and should always be included, but isn&#39;t strictly required by the API.  | [optional] 
 **x_author_id** | **str**| **Warning:** this ID should be SAME across all services using this rating service. Tells the original requester&#39;s user ID. This is used to restrict some actions. For example author with ID &#x60;265&#x60; should not be able to modify rating created by user with ID &#x60;318&#x60;. This value is important and should always be included, but isn&#39;t strictly required by the API.  | [optional] 

### Return type

**list[object]**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of targets or an empty list if none were found.   |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

