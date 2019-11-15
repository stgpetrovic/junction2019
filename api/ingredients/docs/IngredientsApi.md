# openapi_client.IngredientsApi

All URIs are relative to *https://kesko.azure-api.net/ingredients*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ingredients**](IngredientsApi.md#get_ingredients) | **GET** /ingredients | List all ingredients.
[**get_ingredients_id**](IngredientsApi.md#get_ingredients_id) | **GET** /ingredients/{id} | Get single ingredient by its ID.


# **get_ingredients**
> get_ingredients(query_term=query_term, exact_match=exact_match)

List all ingredients.

Recipes consist of ingredients, and this service keeps track of known recipe ingredients. Ingredients have their unique ID, which is also returned from [Recipe Search API](https://kesko.portal.azure-api.net/docs/services/search/operations/post-search-recipes). <br><br> Most ingredients also belong to some product department, which can be used to classify ingredients into different groups. <br><br> Some ingredients also have one or more default products defined to them as list of EAN codes. These can be used to translate the 'free text' ingredients ('maitoa') into actual products (EAN 6410405069412, 'Pirkka kevytmaito 1l'). The default products are picked from the most common products sold in most of the Kesko stores. *Note*: Search API can also be used to search default products based on incredient IDs (with `ingredientType` filter), and this service should only be used as the source of raw data. <br><br> This endpoint returns quite verbose data, and some kind of caching is encouraged.  

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

# Defining host is optional and default to https://kesko.azure-api.net/ingredients
configuration.host = "https://kesko.azure-api.net/ingredients"
# Create an instance of the API class
api_instance = openapi_client.IngredientsApi(openapi_client.ApiClient(configuration))
query_term = 'query_term_example' # str | Search based on matching of queryTerm against ingredient names. Can be used for getting as-you-write suggestions for ingredients.  (optional)
exact_match = False # bool | If `true`, queryTerm is compared case-sensitively to the whole ingredient name. If `false`, case insensitive partial matching is used, when comparing `queryTerm` to ingredient names. Default value is `false`.  (optional) (default to False)

try:
    # List all ingredients.
    api_instance.get_ingredients(query_term=query_term, exact_match=exact_match)
except ApiException as e:
    print("Exception when calling IngredientsApi->get_ingredients: %s\n" % e)
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

# Defining host is optional and default to https://kesko.azure-api.net/ingredients
configuration.host = "https://kesko.azure-api.net/ingredients"
# Create an instance of the API class
api_instance = openapi_client.IngredientsApi(openapi_client.ApiClient(configuration))
query_term = 'query_term_example' # str | Search based on matching of queryTerm against ingredient names. Can be used for getting as-you-write suggestions for ingredients.  (optional)
exact_match = False # bool | If `true`, queryTerm is compared case-sensitively to the whole ingredient name. If `false`, case insensitive partial matching is used, when comparing `queryTerm` to ingredient names. Default value is `false`.  (optional) (default to False)

try:
    # List all ingredients.
    api_instance.get_ingredients(query_term=query_term, exact_match=exact_match)
except ApiException as e:
    print("Exception when calling IngredientsApi->get_ingredients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_term** | **str**| Search based on matching of queryTerm against ingredient names. Can be used for getting as-you-write suggestions for ingredients.  | [optional] 
 **exact_match** | **bool**| If &#x60;true&#x60;, queryTerm is compared case-sensitively to the whole ingredient name. If &#x60;false&#x60;, case insensitive partial matching is used, when comparing &#x60;queryTerm&#x60; to ingredient names. Default value is &#x60;false&#x60;.  | [optional] [default to False]

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
**200** | List of ingredients or an empty list if none were found.   |  -  |
**400** | Invalid input parameter. |  -  |
**500** | Processing error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ingredients_id**
> get_ingredients_id(id)

Get single ingredient by its ID.

Get single ingredient by its ID.

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

# Defining host is optional and default to https://kesko.azure-api.net/ingredients
configuration.host = "https://kesko.azure-api.net/ingredients"
# Create an instance of the API class
api_instance = openapi_client.IngredientsApi(openapi_client.ApiClient(configuration))
id = 56 # int | Id of an ingredient.

try:
    # Get single ingredient by its ID.
    api_instance.get_ingredients_id(id)
except ApiException as e:
    print("Exception when calling IngredientsApi->get_ingredients_id: %s\n" % e)
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

# Defining host is optional and default to https://kesko.azure-api.net/ingredients
configuration.host = "https://kesko.azure-api.net/ingredients"
# Create an instance of the API class
api_instance = openapi_client.IngredientsApi(openapi_client.ApiClient(configuration))
id = 56 # int | Id of an ingredient.

try:
    # Get single ingredient by its ID.
    api_instance.get_ingredients_id(id)
except ApiException as e:
    print("Exception when calling IngredientsApi->get_ingredients_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of an ingredient. | 

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
**200** | Ingredient. |  -  |
**400** | Invalid input parameter. |  -  |
**500** | Processing error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

