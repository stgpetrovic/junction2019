# pricing.MobileApi

All URIs are relative to *https://kesko.azure-api.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_baskets_longbasketid**](MobileApi.md#delete_baskets_longbasketid) | **DELETE** /baskets/{longBasketId} | Delete shopping basket.
[**delete_baskets_longbasketid_items_itemid**](MobileApi.md#delete_baskets_longbasketid_items_itemid) | **DELETE** /baskets/{longBasketId}/items/{itemId} | Remove item from shopping basket.
[**get_baskets_longbasketid**](MobileApi.md#get_baskets_longbasketid) | **GET** /baskets/{longBasketId} | Get shopping basket information with long id.
[**get_baskets_store_storeid_shortbasketid**](MobileApi.md#get_baskets_store_storeid_shortbasketid) | **GET** /baskets/store/{storeId}/{shortBasketId} | Get shopping basket information for store with short id.
[**get_products_storeid_ean**](MobileApi.md#get_products_storeid_ean) | **GET** /products/{storeId}/{ean} | Get info for a single product.
[**patch_baskets_longbasketid_items_itemid**](MobileApi.md#patch_baskets_longbasketid_items_itemid) | **PATCH** /baskets/{longBasketId}/items/{itemId} | Update an item in shopping basket.
[**post_baskets_storeid**](MobileApi.md#post_baskets_storeid) | **POST** /baskets/{storeId} | Creates a new shopping basket for a certain store.
[**post_products_storeid**](MobileApi.md#post_products_storeid) | **POST** /products/{storeId} | Get information for multiple products at once.
[**put_baskets_longbasketid_items**](MobileApi.md#put_baskets_longbasketid_items) | **PUT** /baskets/{longBasketId}/items | Add multiple items to the shopping basket at once.
[**put_baskets_longbasketid_items_itemid**](MobileApi.md#put_baskets_longbasketid_items_itemid) | **PUT** /baskets/{longBasketId}/items/{itemId} | Create a new item to shopping basket.


# **delete_baskets_longbasketid**
> delete_baskets_longbasketid(long_basket_id, x_basket_token)

Delete shopping basket.

Delete shopping basket.    ** NOTE: This endpoint retuns the \"token\", which must be used in subsequent basket requests as the `x-basket-token` header value. Otherwise the API will return 403 error. ***

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
api_instance = pricing.MobileApi(pricing.ApiClient(configuration))
long_basket_id = 'long_basket_id_example' # str | Long id of the shopping basket
x_basket_token = 'x_basket_token_example' # str | Basket authorization token

try:
    # Delete shopping basket.
    api_instance.delete_baskets_longbasketid(long_basket_id, x_basket_token)
except ApiException as e:
    print("Exception when calling MobileApi->delete_baskets_longbasketid: %s\n" % e)
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
api_instance = pricing.MobileApi(pricing.ApiClient(configuration))
long_basket_id = 'long_basket_id_example' # str | Long id of the shopping basket
x_basket_token = 'x_basket_token_example' # str | Basket authorization token

try:
    # Delete shopping basket.
    api_instance.delete_baskets_longbasketid(long_basket_id, x_basket_token)
except ApiException as e:
    print("Exception when calling MobileApi->delete_baskets_longbasketid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **long_basket_id** | **str**| Long id of the shopping basket | 
 **x_basket_token** | **str**| Basket authorization token | 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Basket was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_baskets_longbasketid_items_itemid**
> BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse delete_baskets_longbasketid_items_itemid(long_basket_id, item_id, x_basket_token, include_promotion_details=include_promotion_details)

Remove item from shopping basket.

Remove item from shopping basket.    ** NOTE: This endpoint retuns the \"token\", which must be used in subsequent basket requests as the `x-basket-token` header value. Otherwise the API will return 403 error. ***

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
api_instance = pricing.MobileApi(pricing.ApiClient(configuration))
long_basket_id = 'long_basket_id_example' # str | Long id of the shopping basket
item_id = 56 # int | Id of the basket item. **Note:** This should be an integer value and basket items are sorted based on this value, lowest id first. 
x_basket_token = 'x_basket_token_example' # str | Basket authorization token from basket creation response
include_promotion_details = True # bool |  (optional)

try:
    # Remove item from shopping basket.
    api_response = api_instance.delete_baskets_longbasketid_items_itemid(long_basket_id, item_id, x_basket_token, include_promotion_details=include_promotion_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->delete_baskets_longbasketid_items_itemid: %s\n" % e)
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
api_instance = pricing.MobileApi(pricing.ApiClient(configuration))
long_basket_id = 'long_basket_id_example' # str | Long id of the shopping basket
item_id = 56 # int | Id of the basket item. **Note:** This should be an integer value and basket items are sorted based on this value, lowest id first. 
x_basket_token = 'x_basket_token_example' # str | Basket authorization token from basket creation response
include_promotion_details = True # bool |  (optional)

try:
    # Remove item from shopping basket.
    api_response = api_instance.delete_baskets_longbasketid_items_itemid(long_basket_id, item_id, x_basket_token, include_promotion_details=include_promotion_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->delete_baskets_longbasketid_items_itemid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **long_basket_id** | **str**| Long id of the shopping basket | 
 **item_id** | **int**| Id of the basket item. **Note:** This should be an integer value and basket items are sorted based on this value, lowest id first.  | 
 **x_basket_token** | **str**| Basket authorization token from basket creation response | 
 **include_promotion_details** | **bool**|  | [optional] 

### Return type

[**BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse**](BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Basket object. The new state of shopping basket is returned.   |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_baskets_longbasketid**
> BasketsLongBasketIdGet200ApplicationJsonResponse get_baskets_longbasketid(long_basket_id, x_basket_token, include_promotion_details=include_promotion_details)

Get shopping basket information with long id.

Get shopping basket information with long id.    ** NOTE: This endpoint retuns the \"token\", which must be used in subsequent basket requests as the `x-basket-token` header value. Otherwise the API will return 403 error. ***

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
api_instance = pricing.MobileApi(pricing.ApiClient(configuration))
long_basket_id = 'long_basket_id_example' # str | Long id of the shopping basket
x_basket_token = 'x_basket_token_example' # str | Basket authorization token 
include_promotion_details = True # bool |  (optional)

try:
    # Get shopping basket information with long id.
    api_response = api_instance.get_baskets_longbasketid(long_basket_id, x_basket_token, include_promotion_details=include_promotion_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->get_baskets_longbasketid: %s\n" % e)
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
api_instance = pricing.MobileApi(pricing.ApiClient(configuration))
long_basket_id = 'long_basket_id_example' # str | Long id of the shopping basket
x_basket_token = 'x_basket_token_example' # str | Basket authorization token 
include_promotion_details = True # bool |  (optional)

try:
    # Get shopping basket information with long id.
    api_response = api_instance.get_baskets_longbasketid(long_basket_id, x_basket_token, include_promotion_details=include_promotion_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->get_baskets_longbasketid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **long_basket_id** | **str**| Long id of the shopping basket | 
 **x_basket_token** | **str**| Basket authorization token  | 
 **include_promotion_details** | **bool**|  | [optional] 

### Return type

[**BasketsLongBasketIdGet200ApplicationJsonResponse**](BasketsLongBasketIdGet200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Basket object |  -  |
**404** | Basket was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_baskets_store_storeid_shortbasketid**
> BasketsStoreStoreIdShortBasketIdGet200ApplicationJsonResponse get_baskets_store_storeid_shortbasketid(store_id, short_basket_id, x_basket_token, include_promotion_details=include_promotion_details)

Get shopping basket information for store with short id.

Get shopping basket information for store with short id.    ** NOTE: This endpoint retuns the \"token\", which must be used in subsequent basket requests as the `x-basket-token` header value. Otherwise the API will return 403 error. ***

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
api_instance = pricing.MobileApi(pricing.ApiClient(configuration))
store_id = 'store_id_example' # str | Store id, for example C122.
short_basket_id = 'short_basket_id_example' # str | Short id of the shopping basket
x_basket_token = 'x_basket_token_example' # str | Basket authorization token
include_promotion_details = True # bool |  (optional)

try:
    # Get shopping basket information for store with short id.
    api_response = api_instance.get_baskets_store_storeid_shortbasketid(store_id, short_basket_id, x_basket_token, include_promotion_details=include_promotion_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->get_baskets_store_storeid_shortbasketid: %s\n" % e)
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
api_instance = pricing.MobileApi(pricing.ApiClient(configuration))
store_id = 'store_id_example' # str | Store id, for example C122.
short_basket_id = 'short_basket_id_example' # str | Short id of the shopping basket
x_basket_token = 'x_basket_token_example' # str | Basket authorization token
include_promotion_details = True # bool |  (optional)

try:
    # Get shopping basket information for store with short id.
    api_response = api_instance.get_baskets_store_storeid_shortbasketid(store_id, short_basket_id, x_basket_token, include_promotion_details=include_promotion_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->get_baskets_store_storeid_shortbasketid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| Store id, for example C122. | 
 **short_basket_id** | **str**| Short id of the shopping basket | 
 **x_basket_token** | **str**| Basket authorization token | 
 **include_promotion_details** | **bool**|  | [optional] 

### Return type

[**BasketsStoreStoreIdShortBasketIdGet200ApplicationJsonResponse**](BasketsStoreStoreIdShortBasketIdGet200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Basket object |  -  |
**404** | Basket was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_products_storeid_ean**
> ProductsStoreIdEanGet200ApplicationJsonResponse get_products_storeid_ean(store_id, ean)

Get info for a single product.

Get info for a single product.

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
api_instance = pricing.MobileApi(pricing.ApiClient(configuration))
store_id = 'store_id_example' # str | Store id, for example C122.
ean = 'ean_example' # str | EAN code of the product

try:
    # Get info for a single product.
    api_response = api_instance.get_products_storeid_ean(store_id, ean)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->get_products_storeid_ean: %s\n" % e)
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
api_instance = pricing.MobileApi(pricing.ApiClient(configuration))
store_id = 'store_id_example' # str | Store id, for example C122.
ean = 'ean_example' # str | EAN code of the product

try:
    # Get info for a single product.
    api_response = api_instance.get_products_storeid_ean(store_id, ean)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->get_products_storeid_ean: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| Store id, for example C122. | 
 **ean** | **str**| EAN code of the product | 

### Return type

[**ProductsStoreIdEanGet200ApplicationJsonResponse**](ProductsStoreIdEanGet200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product object |  -  |
**400** | Bad request |  -  |
**404** | Store not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_baskets_longbasketid_items_itemid**
> BasketsLongBasketIdItemsItemIdPatch200ApplicationJsonResponse patch_baskets_longbasketid_items_itemid(long_basket_id, item_id, x_basket_token, include_promotion_details=include_promotion_details, item=item)

Update an item in shopping basket.

** NOTE: This endpoint retuns the \"token\", which must be used in subsequent basket requests as the `x-basket-token` header value. Otherwise the API will return 403 error. ***    This can be used to update the meta data of an item in basket. You are not allowed to change the actual content of the item. That is enforced by allowing only partial basket item objects in write operations.  

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
api_instance = pricing.MobileApi(pricing.ApiClient(configuration))
long_basket_id = 'long_basket_id_example' # str | Long id of the shopping basket
item_id = 56 # int | Id of the basket item. **Note:** This should be an integer value and basket items are sorted based on this value, lowest id first. 
x_basket_token = 'x_basket_token_example' # str | Basket authorization token, returned from basket creation request
include_promotion_details = True # bool |  (optional)
item = pricing.Item() # Item | Item object. This object also specifies the multiplier of items added.   (optional)

try:
    # Update an item in shopping basket.
    api_response = api_instance.patch_baskets_longbasketid_items_itemid(long_basket_id, item_id, x_basket_token, include_promotion_details=include_promotion_details, item=item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->patch_baskets_longbasketid_items_itemid: %s\n" % e)
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
api_instance = pricing.MobileApi(pricing.ApiClient(configuration))
long_basket_id = 'long_basket_id_example' # str | Long id of the shopping basket
item_id = 56 # int | Id of the basket item. **Note:** This should be an integer value and basket items are sorted based on this value, lowest id first. 
x_basket_token = 'x_basket_token_example' # str | Basket authorization token, returned from basket creation request
include_promotion_details = True # bool |  (optional)
item = pricing.Item() # Item | Item object. This object also specifies the multiplier of items added.   (optional)

try:
    # Update an item in shopping basket.
    api_response = api_instance.patch_baskets_longbasketid_items_itemid(long_basket_id, item_id, x_basket_token, include_promotion_details=include_promotion_details, item=item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->patch_baskets_longbasketid_items_itemid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **long_basket_id** | **str**| Long id of the shopping basket | 
 **item_id** | **int**| Id of the basket item. **Note:** This should be an integer value and basket items are sorted based on this value, lowest id first.  | 
 **x_basket_token** | **str**| Basket authorization token, returned from basket creation request | 
 **include_promotion_details** | **bool**|  | [optional] 
 **item** | [**Item**](Item.md)| Item object. This object also specifies the multiplier of items added.   | [optional] 

### Return type

[**BasketsLongBasketIdItemsItemIdPatch200ApplicationJsonResponse**](BasketsLongBasketIdItemsItemIdPatch200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Basket object. The new state of shopping basket is returned.   |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_baskets_storeid**
> BasketsStoreIdPost200ApplicationJsonResponse post_baskets_storeid(store_id, include_promotion_details=include_promotion_details)

Creates a new shopping basket for a certain store.

Body of the request should be empty. The basket is deleted after 24 hours!    ** NOTE: This endpoint retuns the \"token\", which must be used in subsequent basket requests as the `x-basket-token` header value. Otherwise the API will return 403 error. ***  

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
api_instance = pricing.MobileApi(pricing.ApiClient(configuration))
store_id = 'store_id_example' # str | Store id, for example C122.
include_promotion_details = True # bool |  (optional)

try:
    # Creates a new shopping basket for a certain store.
    api_response = api_instance.post_baskets_storeid(store_id, include_promotion_details=include_promotion_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->post_baskets_storeid: %s\n" % e)
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
api_instance = pricing.MobileApi(pricing.ApiClient(configuration))
store_id = 'store_id_example' # str | Store id, for example C122.
include_promotion_details = True # bool |  (optional)

try:
    # Creates a new shopping basket for a certain store.
    api_response = api_instance.post_baskets_storeid(store_id, include_promotion_details=include_promotion_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->post_baskets_storeid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| Store id, for example C122. | 
 **include_promotion_details** | **bool**|  | [optional] 

### Return type

[**BasketsStoreIdPost200ApplicationJsonResponse**](BasketsStoreIdPost200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty basket object with no items in it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_products_storeid**
> object post_products_storeid(store_id, eans=eans)

Get information for multiple products at once.

Get information for multiple products at once.

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
api_instance = pricing.MobileApi(pricing.ApiClient(configuration))
store_id = 'store_id_example' # str | Store id, for example C122.
eans = pricing.Eans() # Eans |  (optional)

try:
    # Get information for multiple products at once.
    api_response = api_instance.post_products_storeid(store_id, eans=eans)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->post_products_storeid: %s\n" % e)
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
api_instance = pricing.MobileApi(pricing.ApiClient(configuration))
store_id = 'store_id_example' # str | Store id, for example C122.
eans = pricing.Eans() # Eans |  (optional)

try:
    # Get information for multiple products at once.
    api_response = api_instance.post_products_storeid(store_id, eans=eans)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->post_products_storeid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| Store id, for example C122. | 
 **eans** | [**Eans**](Eans.md)|  | [optional] 

### Return type

**object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object where keys are EANs and values are Product objects. |  -  |
**400** | Bad request |  -  |
**404** | Store not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_baskets_longbasketid_items**
> BasketsLongBasketIdItemsPut200ApplicationJsonResponse put_baskets_longbasketid_items(long_basket_id, x_basket_token, include_promotion_details=include_promotion_details, payload=payload)

Add multiple items to the shopping basket at once.

Sets an array of items as the content of the basket. The first item in the array will have an item id of 0, the second one will have 1 and so on.  Existing items in the basket are replaced if a supplied item has the same id, but otherwise items already existing in the basket will not be touched.  Endpoint validation allows for items with empty EAN-codes or items with multipliers of zero. Such items won't be added to the basket and will be skipped and logged.    ** NOTE: This endpoint retuns the \"token\", which must be used in subsequent basket requests as the `x-basket-token` header value. Otherwise the API will return 403 error. ***

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
api_instance = pricing.MobileApi(pricing.ApiClient(configuration))
long_basket_id = 'long_basket_id_example' # str | Long id of the shopping basket
x_basket_token = 'x_basket_token_example' # str | Basket authorization token
include_promotion_details = True # bool |  (optional)
payload = pricing.Payload() # Payload | Bulk item object containing multiple partial basket item objects.   (optional)

try:
    # Add multiple items to the shopping basket at once.
    api_response = api_instance.put_baskets_longbasketid_items(long_basket_id, x_basket_token, include_promotion_details=include_promotion_details, payload=payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->put_baskets_longbasketid_items: %s\n" % e)
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
api_instance = pricing.MobileApi(pricing.ApiClient(configuration))
long_basket_id = 'long_basket_id_example' # str | Long id of the shopping basket
x_basket_token = 'x_basket_token_example' # str | Basket authorization token
include_promotion_details = True # bool |  (optional)
payload = pricing.Payload() # Payload | Bulk item object containing multiple partial basket item objects.   (optional)

try:
    # Add multiple items to the shopping basket at once.
    api_response = api_instance.put_baskets_longbasketid_items(long_basket_id, x_basket_token, include_promotion_details=include_promotion_details, payload=payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->put_baskets_longbasketid_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **long_basket_id** | **str**| Long id of the shopping basket | 
 **x_basket_token** | **str**| Basket authorization token | 
 **include_promotion_details** | **bool**|  | [optional] 
 **payload** | [**Payload**](Payload.md)| Bulk item object containing multiple partial basket item objects.   | [optional] 

### Return type

[**BasketsLongBasketIdItemsPut200ApplicationJsonResponse**](BasketsLongBasketIdItemsPut200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Basket object. The new state of shopping basket is returned.   |  -  |
**400** | Validation error / Too many items being added at once |  -  |
**404** | Basket not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_baskets_longbasketid_items_itemid**
> BasketsLongBasketIdItemsItemIdPut200ApplicationJsonResponse put_baskets_longbasketid_items_itemid(long_basket_id, item_id, x_basket_token, include_promotion_details=include_promotion_details, item=item)

Create a new item to shopping basket.

It is up to the client to generate and handle the basket item id.    ** NOTE: This endpoint requires `x-basket-token` header value. The token is returned by the basket creation request. Otherwise the API will return 403 error. ***  

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
api_instance = pricing.MobileApi(pricing.ApiClient(configuration))
long_basket_id = 'long_basket_id_example' # str | Long id of the shopping basket
item_id = 56 # int | Id of the basket item. **Note:** This should be an integer value and basket items are sorted based on this value, lowest id first. 
x_basket_token = 'x_basket_token_example' # str | Basket authorization token
include_promotion_details = True # bool |  (optional)
item = pricing.Item() # Item | Item object. This object also specifies the multiplier of items added.   (optional)

try:
    # Create a new item to shopping basket.
    api_response = api_instance.put_baskets_longbasketid_items_itemid(long_basket_id, item_id, x_basket_token, include_promotion_details=include_promotion_details, item=item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->put_baskets_longbasketid_items_itemid: %s\n" % e)
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
api_instance = pricing.MobileApi(pricing.ApiClient(configuration))
long_basket_id = 'long_basket_id_example' # str | Long id of the shopping basket
item_id = 56 # int | Id of the basket item. **Note:** This should be an integer value and basket items are sorted based on this value, lowest id first. 
x_basket_token = 'x_basket_token_example' # str | Basket authorization token
include_promotion_details = True # bool |  (optional)
item = pricing.Item() # Item | Item object. This object also specifies the multiplier of items added.   (optional)

try:
    # Create a new item to shopping basket.
    api_response = api_instance.put_baskets_longbasketid_items_itemid(long_basket_id, item_id, x_basket_token, include_promotion_details=include_promotion_details, item=item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->put_baskets_longbasketid_items_itemid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **long_basket_id** | **str**| Long id of the shopping basket | 
 **item_id** | **int**| Id of the basket item. **Note:** This should be an integer value and basket items are sorted based on this value, lowest id first.  | 
 **x_basket_token** | **str**| Basket authorization token | 
 **include_promotion_details** | **bool**|  | [optional] 
 **item** | [**Item**](Item.md)| Item object. This object also specifies the multiplier of items added.   | [optional] 

### Return type

[**BasketsLongBasketIdItemsItemIdPut200ApplicationJsonResponse**](BasketsLongBasketIdItemsItemIdPut200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Basket object. The new state of shopping basket is returned.   |  -  |
**406** | Basket is full and item couldn&#39;t be added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

