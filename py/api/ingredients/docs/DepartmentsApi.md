# ingredients.DepartmentsApi

All URIs are relative to *https://kesko.azure-api.net/ingredients*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_departments**](DepartmentsApi.md#get_departments) | **GET** /departments | List all departments.


# **get_departments**
> get_departments()

List all departments.

Returns list of departments and their order number (in shopping list views etc). Segments belong to departments. The hierarchy of ingredient classification is: <br><br> `Department` > `Segment` > `Ingredient` (or `Product`) <br><br> Usually with products departments aren't used, and they are instead classified by category: <br><br> `Category` > `Subcategory` > `Segment` > `Product`  

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
api_instance = ingredients.DepartmentsApi(ingredients.ApiClient(configuration))

try:
    # List all departments.
    api_instance.get_departments()
except ApiException as e:
    print("Exception when calling DepartmentsApi->get_departments: %s\n" % e)
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
api_instance = ingredients.DepartmentsApi(ingredients.ApiClient(configuration))

try:
    # List all departments.
    api_instance.get_departments()
except ApiException as e:
    print("Exception when calling DepartmentsApi->get_departments: %s\n" % e)
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
**200** | Segments belong to departments.   |  -  |
**500** | Processing error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

