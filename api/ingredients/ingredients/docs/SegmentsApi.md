# ingredients.SegmentsApi

All URIs are relative to *https://kesko.azure-api.net/ingredients*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_segments**](SegmentsApi.md#get_segments) | **GET** /segments | List all segments


# **get_segments**
> get_segments()

List all segments

Returns list of known segments and their the IDs of department they belong to. <br><br> Ingredients (and products) belong to segments. The hierarchy of ingredient classification is: <br><br> `Department` > `Segment` > `Ingredient` (or `Product`) <br><br> Usually with products departments aren't used, and they are instead classified by category: <br><br> `Category` > `Subcategory` > `Segment` > `Product`  

### Example

* Api Key Authentication (apiKeyHeader):
```python
from __future__ import print_function
import time
import ingredients
from ingredients.rest import ApiException
from pprint import pprint
configuration = ingredients.Configuration()
# Configure API key authorization: apiKeyHeader
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
configuration = ingredients.Configuration()
# Configure API key authorization: apiKeyQuery
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# Defining host is optional and default to https://kesko.azure-api.net/ingredients
configuration.host = "https://kesko.azure-api.net/ingredients"
# Create an instance of the API class
api_instance = ingredients.SegmentsApi(ingredients.ApiClient(configuration))

try:
    # List all segments
    api_instance.get_segments()
except ApiException as e:
    print("Exception when calling SegmentsApi->get_segments: %s\n" % e)
```

* Api Key Authentication (apiKeyQuery):
```python
from __future__ import print_function
import time
import ingredients
from ingredients.rest import ApiException
from pprint import pprint
configuration = ingredients.Configuration()
# Configure API key authorization: apiKeyHeader
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
configuration = ingredients.Configuration()
# Configure API key authorization: apiKeyQuery
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# Defining host is optional and default to https://kesko.azure-api.net/ingredients
configuration.host = "https://kesko.azure-api.net/ingredients"
# Create an instance of the API class
api_instance = ingredients.SegmentsApi(ingredients.ApiClient(configuration))

try:
    # List all segments
    api_instance.get_segments()
except ApiException as e:
    print("Exception when calling SegmentsApi->get_segments: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of segments or an empty list if none were found.   |  -  |
**500** | Processing error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

