# search.SuggestionsApi

All URIs are relative to *https://kesko.azure-api.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_suggestions_articles**](SuggestionsApi.md#post_suggestions_articles) | **POST** /suggestions/articles | Article suggestions (autocomplete)
[**post_suggestions_products**](SuggestionsApi.md#post_suggestions_products) | **POST** /suggestions/products | Product suggestions (autocomplete)
[**post_suggestions_recipes**](SuggestionsApi.md#post_suggestions_recipes) | **POST** /suggestions/recipes | Recipe suggestions (autocomplete)
[**post_suggestions_stores**](SuggestionsApi.md#post_suggestions_stores) | **POST** /suggestions/stores | Store suggestions (autocomplete)


# **post_suggestions_articles**
> SuggestionsArticlesPost200ApplicationJsonResponse post_suggestions_articles(payload=payload)

Article suggestions (autocomplete)

Endpoint for search autocomplete, which returns list of possible complete word suggestions based on the current search query.  

### Example

* Api Key Authentication (apiKeyHeader):
```python
from __future__ import print_function
import time
import search
from search.rest import ApiException
from pprint import pprint
configuration = search.Configuration()
# Configure API key authorization: apiKeyHeader
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
configuration = search.Configuration()
# Configure API key authorization: apiKeyQuery
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# Defining host is optional and default to https://kesko.azure-api.net/v1
configuration.host = "https://kesko.azure-api.net/v1"
# Create an instance of the API class
api_instance = search.SuggestionsApi(search.ApiClient(configuration))
payload = search.Payload() # Payload | JSON payload similar to a normal search request. (optional)

try:
    # Article suggestions (autocomplete)
    api_response = api_instance.post_suggestions_articles(payload=payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuggestionsApi->post_suggestions_articles: %s\n" % e)
```

* Api Key Authentication (apiKeyQuery):
```python
from __future__ import print_function
import time
import search
from search.rest import ApiException
from pprint import pprint
configuration = search.Configuration()
# Configure API key authorization: apiKeyHeader
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
configuration = search.Configuration()
# Configure API key authorization: apiKeyQuery
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# Defining host is optional and default to https://kesko.azure-api.net/v1
configuration.host = "https://kesko.azure-api.net/v1"
# Create an instance of the API class
api_instance = search.SuggestionsApi(search.ApiClient(configuration))
payload = search.Payload() # Payload | JSON payload similar to a normal search request. (optional)

try:
    # Article suggestions (autocomplete)
    api_response = api_instance.post_suggestions_articles(payload=payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuggestionsApi->post_suggestions_articles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**Payload**](Payload.md)| JSON payload similar to a normal search request. | [optional] 

### Return type

[**SuggestionsArticlesPost200ApplicationJsonResponse**](SuggestionsArticlesPost200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid input parameter. |  -  |
**500** | Processing Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_suggestions_products**
> SuggestionsProductsPost200ApplicationJsonResponse post_suggestions_products(payload=payload)

Product suggestions (autocomplete)

Endpoint for search autocomplete, which returns list of possible complete word suggestions based on the current search query.  

### Example

* Api Key Authentication (apiKeyHeader):
```python
from __future__ import print_function
import time
import search
from search.rest import ApiException
from pprint import pprint
configuration = search.Configuration()
# Configure API key authorization: apiKeyHeader
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
configuration = search.Configuration()
# Configure API key authorization: apiKeyQuery
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# Defining host is optional and default to https://kesko.azure-api.net/v1
configuration.host = "https://kesko.azure-api.net/v1"
# Create an instance of the API class
api_instance = search.SuggestionsApi(search.ApiClient(configuration))
payload = search.Payload() # Payload | JSON payload similar to a normal search request. (optional)

try:
    # Product suggestions (autocomplete)
    api_response = api_instance.post_suggestions_products(payload=payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuggestionsApi->post_suggestions_products: %s\n" % e)
```

* Api Key Authentication (apiKeyQuery):
```python
from __future__ import print_function
import time
import search
from search.rest import ApiException
from pprint import pprint
configuration = search.Configuration()
# Configure API key authorization: apiKeyHeader
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
configuration = search.Configuration()
# Configure API key authorization: apiKeyQuery
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# Defining host is optional and default to https://kesko.azure-api.net/v1
configuration.host = "https://kesko.azure-api.net/v1"
# Create an instance of the API class
api_instance = search.SuggestionsApi(search.ApiClient(configuration))
payload = search.Payload() # Payload | JSON payload similar to a normal search request. (optional)

try:
    # Product suggestions (autocomplete)
    api_response = api_instance.post_suggestions_products(payload=payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuggestionsApi->post_suggestions_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**Payload**](Payload.md)| JSON payload similar to a normal search request. | [optional] 

### Return type

[**SuggestionsProductsPost200ApplicationJsonResponse**](SuggestionsProductsPost200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid input parameter. |  -  |
**500** | Processing Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_suggestions_recipes**
> SuggestionsRecipesPost200ApplicationJsonResponse post_suggestions_recipes(payload=payload)

Recipe suggestions (autocomplete)

Endpoint for search autocomplete, which returns list of possible complete word suggestions based on the current search query.  

### Example

* Api Key Authentication (apiKeyHeader):
```python
from __future__ import print_function
import time
import search
from search.rest import ApiException
from pprint import pprint
configuration = search.Configuration()
# Configure API key authorization: apiKeyHeader
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
configuration = search.Configuration()
# Configure API key authorization: apiKeyQuery
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# Defining host is optional and default to https://kesko.azure-api.net/v1
configuration.host = "https://kesko.azure-api.net/v1"
# Create an instance of the API class
api_instance = search.SuggestionsApi(search.ApiClient(configuration))
payload = search.Payload() # Payload | JSON payload similar to a normal search request. (optional)

try:
    # Recipe suggestions (autocomplete)
    api_response = api_instance.post_suggestions_recipes(payload=payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuggestionsApi->post_suggestions_recipes: %s\n" % e)
```

* Api Key Authentication (apiKeyQuery):
```python
from __future__ import print_function
import time
import search
from search.rest import ApiException
from pprint import pprint
configuration = search.Configuration()
# Configure API key authorization: apiKeyHeader
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
configuration = search.Configuration()
# Configure API key authorization: apiKeyQuery
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# Defining host is optional and default to https://kesko.azure-api.net/v1
configuration.host = "https://kesko.azure-api.net/v1"
# Create an instance of the API class
api_instance = search.SuggestionsApi(search.ApiClient(configuration))
payload = search.Payload() # Payload | JSON payload similar to a normal search request. (optional)

try:
    # Recipe suggestions (autocomplete)
    api_response = api_instance.post_suggestions_recipes(payload=payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuggestionsApi->post_suggestions_recipes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**Payload**](Payload.md)| JSON payload similar to a normal search request. | [optional] 

### Return type

[**SuggestionsRecipesPost200ApplicationJsonResponse**](SuggestionsRecipesPost200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid input parameter. |  -  |
**500** | Processing Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_suggestions_stores**
> SuggestionsStoresPost200ApplicationJsonResponse post_suggestions_stores(payload=payload)

Store suggestions (autocomplete)

Endpoint for search autocomplete, which returns list of possible complete word suggestions based on the current search query.  

### Example

* Api Key Authentication (apiKeyHeader):
```python
from __future__ import print_function
import time
import search
from search.rest import ApiException
from pprint import pprint
configuration = search.Configuration()
# Configure API key authorization: apiKeyHeader
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
configuration = search.Configuration()
# Configure API key authorization: apiKeyQuery
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# Defining host is optional and default to https://kesko.azure-api.net/v1
configuration.host = "https://kesko.azure-api.net/v1"
# Create an instance of the API class
api_instance = search.SuggestionsApi(search.ApiClient(configuration))
payload = search.Payload() # Payload | JSON payload similar to a normal search request. (optional)

try:
    # Store suggestions (autocomplete)
    api_response = api_instance.post_suggestions_stores(payload=payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuggestionsApi->post_suggestions_stores: %s\n" % e)
```

* Api Key Authentication (apiKeyQuery):
```python
from __future__ import print_function
import time
import search
from search.rest import ApiException
from pprint import pprint
configuration = search.Configuration()
# Configure API key authorization: apiKeyHeader
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
configuration = search.Configuration()
# Configure API key authorization: apiKeyQuery
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# Defining host is optional and default to https://kesko.azure-api.net/v1
configuration.host = "https://kesko.azure-api.net/v1"
# Create an instance of the API class
api_instance = search.SuggestionsApi(search.ApiClient(configuration))
payload = search.Payload() # Payload | JSON payload similar to a normal search request. (optional)

try:
    # Store suggestions (autocomplete)
    api_response = api_instance.post_suggestions_stores(payload=payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuggestionsApi->post_suggestions_stores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**Payload**](Payload.md)| JSON payload similar to a normal search request. | [optional] 

### Return type

[**SuggestionsStoresPost200ApplicationJsonResponse**](SuggestionsStoresPost200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid input parameter. |  -  |
**500** | Processing Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

