# pricing.ProductApi

All URIs are relative to *https://kesko.azure-api.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_v2_products_ean_ean**](ProductApi.md#get_v2_products_ean_ean) | **GET** /v2/products | Get availability information for products.
[**get_v4_stores_storeid_products**](ProductApi.md#get_v4_stores_storeid_products) | **GET** /v4/stores/{storeId}/products | Get product details (pricing, promotions) for a specific store.
[**post_v2_stores_storeid_price**](ProductApi.md#post_v2_stores_storeid_price) | **POST** /v2/stores/{storeId}/price | Calculate price for each individual EAN row and the total for the requested EANs. 
[**post_v2_stores_storeid_product_pricing**](ProductApi.md#post_v2_stores_storeid_product_pricing) | **POST** /v2/stores/{storeId}/product-pricing | Get individual product prices with promotion information.


# **get_v2_products_ean_ean**
> list[object] get_v2_products_ean_ean(ean)

Get availability information for products.

Returns the `pricingUnit` and availability of given products in all stores. If a store is returned in `stores` array, the product should be available in that physical store. If the store also has `web` flag set to true, the product is also available for web sales.  <br><br>[Search API](https://kesko.portal.azure-api.net/docs/services/search/) uses this endpoint check if products are available during indexing process. If you want to check product for availability in your UI, you likely want to use Search APIs availability data.  

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
api_instance = pricing.ProductApi(pricing.ApiClient(configuration))
ean = 'ean_example' # str | 

try:
    # Get availability information for products.
    api_response = api_instance.get_v2_products_ean_ean(ean)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_v2_products_ean_ean: %s\n" % e)
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
api_instance = pricing.ProductApi(pricing.ApiClient(configuration))
ean = 'ean_example' # str | 

try:
    # Get availability information for products.
    api_response = api_instance.get_v2_products_ean_ean(ean)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_v2_products_ean_ean: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ean** | **str**|  | 

### Return type

**list[object]**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array containing product info objects.   |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v4_stores_storeid_products**
> dict(str, object) get_v4_stores_storeid_products(store_id, ean=ean, limit=limit, offset=offset, last_seen=last_seen)

Get product details (pricing, promotions) for a specific store.

This endpoint is used to fetch product details for a specific store. Multiple stores can have the same products with the same EAN codes, but all stores can have independent pricing and promotion details related to the same products, so this information is fetched on a store by store basis.  <br><br>Product details can be queried for specific EAN codes or all of the available products can be queried in a paged manner. Paging is implemented by providing limit and offset attributes.  <br><br>V4 endpoint adds proper support for basket sale sets. Previously the API just returned the number of baskets related to the promotion, but the V4 endpoint returns the basket details instead.  <br><br>Product objects have quite a few optional attributes. Below there are a few examples of different types of products.  <br>Products can have additional texts attached to them:<br><br>  ```  {    \"711719870746\": {      \"ean\": \"711719870746\",      \"baseEan\": \"0711719870746\",      \"name\": \"PlayStation 4 1000Gt + 2 Ohjainta\",      \"group\": \"18950\",      \"price\": 180,      \"pricingUnit\": \"kpl\",      \"vat\": 24,      \"packageSize\": \"1.00\",      \"packageUnit\": \"kpl\",      \"packageType\": \"kpl\",      \"costCenterId\": \"KÄ01\",      \"plussaLimited\": false,      \"discountLimited\": false,      \"type\": \"UTILITY_GOOD\",      \"totalPrice\": 180,      \"texts\": [        {          \"type\": \"warranty\",          \"text\": \"\\\"Tuotteella on 12 kk takuu\\\"\"        }      ]    }  }  ```  <br>Products can consist of multiple `components`, have active `promotions` or `restrictions`. Promotions can affect the price returned by the api, and are automatically calculated:<br><br>  ```  {    \"8594404005409\": {      \"ean\": \"8594404005409\",      \"baseEan\": \"8594404005409\",      \"name\": \"Pilsner Urquell 4,4% 0,5l tlk 4-pack\",      \"group\": \"15243\",      \"price\": 9.8,      \"pricingUnit\": \"kpl\",      \"vat\": 24,      \"packageSize\": \"2.00\",      \"packageUnit\": \"l\",      \"packageType\": \"pakkaus\",      \"costCenterId\": \"PA01\",      \"plussaLimited\": true,      \"discountLimited\": true,      \"type\": \"CONSUMER_GOOD\",      \"components\": [        {          \"baseEan\": \"2000973900008\",          \"name\": \"Tölkkipantti 0,15 0,33l-0,5l\",          \"group\": \"15300\",          \"price\": 0.15,          \"pricingUnit\": \"kpl\",          \"vat\": 24,          \"packageSize\": \"1.00\",          \"packageUnit\": \"kpl\",          \"packageType\": \"kpl\",          \"costCenterId\": \"PM02\",          \"plussaLimited\": false,          \"discountLimited\": true,          \"type\": \"CONSUMER_GOOD\",          \"totalPrice\": 0.6,          \"multiplier\": 4        }      ],      \"totalPrice\": 10.4,      \"restrictions\": {        \"cashierVerifyRequired\": true,        \"ageVerificationRequired\": true,        \"limitedSalesTime\": true      },      \"promotions\": [        {          \"id\": \"8594404005401000000012100001\",          \"type\": 121,          \"startDate\": \"2018-08-27\",          \"endDate\": \"2019-01-02\",          \"plussa\": false,          \"pricingMethod\": \"net\",          \"price\": 9.8,          \"rule\": \"simple\"        }      ]    }  }  ```  <br>Products can have multiplier immutability flag set. If the flag is set, you cannot modify the multiplier of these items:<br><br>  ```  {    \"2000518600004\": {      \"ean\": \"2000518600004\",      \"baseEan\": \"2000518600004\",      \"name\": \"Omena Royal Gala\",      \"group\": \"11523\",      \"price\": 2.59,      \"pricingUnit\": \"kg\",      \"vat\": 14,      \"packageSize\": \"0.00\",      \"packageUnit\": \"kg\",      \"packageType\": \"kilo\",      \"costCenterId\": \"HE01\",      \"plussaLimited\": false,      \"discountLimited\": false,      \"type\": \"CONSUMER_GOOD\",      \"restrictions\": {        \"multiplierImmutable\": true      },      \"totalPrice\": 2.59,      \"scaleNumber\": \"67\",      \"texts\": [        {          \"type\": \"originCountry\",          \"text\": \"ITALIA\"        },        {          \"type\": \"productClass\",          \"text\": \"1LK\"        }      ]    }  }  ```  <br>Some products are sold by their weight. In that case the price is stored as part of the EAN, and baseEan returns the product ean without price:<br><br>  ```  {    \"2000708404321\": {      \"ean\": \"2000708404321\",      \"baseEan\": \"2000708400001\",      \"name\": \"Palvikinkku\",      \"group\": \"11206\",      \"price\": 4.32,      \"pricingUnit\": \"kg\",      \"vat\": 14,      \"packageSize\": \"0.00\",      \"packageUnit\": \"kg\",      \"packageType\": \"kilo\",      \"costCenterId\": \"LJ01\",      \"plussaLimited\": false,      \"discountLimited\": false,      \"type\": \"CONSUMER_GOOD\",      \"restrictions\": {        \"multiplierImmutable\": true      },      \"unitPrice\": 0,      \"totalPrice\": 4.32    }  }  ```  

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
api_instance = pricing.ProductApi(pricing.ApiClient(configuration))
store_id = 'store_id_example' # str | Store id, for example C122.
ean = 'ean_example' # str | An EAN code or multiple EAN codes to return details for.  (optional)
limit = 20 # int | Limit for the quantity of returned results. Default: 20.  (optional) (default to 20)
offset = 0 # int | Offset for the current \"page\" ie. how many results to skip and when to start returning new results up to the defined limit. Default: 0.  (optional) (default to 0)
last_seen = 'last_seen_example' # str | Last seen EAN. (optional)

try:
    # Get product details (pricing, promotions) for a specific store.
    api_response = api_instance.get_v4_stores_storeid_products(store_id, ean=ean, limit=limit, offset=offset, last_seen=last_seen)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_v4_stores_storeid_products: %s\n" % e)
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
api_instance = pricing.ProductApi(pricing.ApiClient(configuration))
store_id = 'store_id_example' # str | Store id, for example C122.
ean = 'ean_example' # str | An EAN code or multiple EAN codes to return details for.  (optional)
limit = 20 # int | Limit for the quantity of returned results. Default: 20.  (optional) (default to 20)
offset = 0 # int | Offset for the current \"page\" ie. how many results to skip and when to start returning new results up to the defined limit. Default: 0.  (optional) (default to 0)
last_seen = 'last_seen_example' # str | Last seen EAN. (optional)

try:
    # Get product details (pricing, promotions) for a specific store.
    api_response = api_instance.get_v4_stores_storeid_products(store_id, ean=ean, limit=limit, offset=offset, last_seen=last_seen)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_v4_stores_storeid_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| Store id, for example C122. | 
 **ean** | **str**| An EAN code or multiple EAN codes to return details for.  | [optional] 
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
**200** | An object where keys are EANs and values are Product objects with added promotion info.   |  -  |
**400** | Bad request |  -  |
**404** | Store not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_stores_storeid_price**
> V2StoresStoreIdPricePost200ApplicationJsonResponse post_v2_stores_storeid_price(store_id, plussa=plussa, products=products)

Calculate price for each individual EAN row and the total for the requested EANs. 

Calculate price for each individual EAN row and the total for the requested EANs.  

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
api_instance = pricing.ProductApi(pricing.ApiClient(configuration))
store_id = 'store_id_example' # str | Store id, for example C122.
plussa = False # bool |  (optional) (default to False)
products = pricing.Products() # Products | An object containing the products for which the prices are fetched. Keys are EANs and values are quantity.   (optional)

try:
    # Calculate price for each individual EAN row and the total for the requested EANs. 
    api_response = api_instance.post_v2_stores_storeid_price(store_id, plussa=plussa, products=products)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->post_v2_stores_storeid_price: %s\n" % e)
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
api_instance = pricing.ProductApi(pricing.ApiClient(configuration))
store_id = 'store_id_example' # str | Store id, for example C122.
plussa = False # bool |  (optional) (default to False)
products = pricing.Products() # Products | An object containing the products for which the prices are fetched. Keys are EANs and values are quantity.   (optional)

try:
    # Calculate price for each individual EAN row and the total for the requested EANs. 
    api_response = api_instance.post_v2_stores_storeid_price(store_id, plussa=plussa, products=products)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->post_v2_stores_storeid_price: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| Store id, for example C122. | 
 **plussa** | **bool**|  | [optional] [default to False]
 **products** | [**Products**](Products.md)| An object containing the products for which the prices are fetched. Keys are EANs and values are quantity.   | [optional] 

### Return type

[**V2StoresStoreIdPricePost200ApplicationJsonResponse**](V2StoresStoreIdPricePost200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object containing prices for the individual products as well as the total price. Product keys are EANs and values are prices.   |  -  |
**400** | Bad request |  -  |
**404** | Store not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_stores_storeid_product_pricing**
> dict(str, object) post_v2_stores_storeid_product_pricing(store_id, plussa=plussa, eans=eans)

Get individual product prices with promotion information.

Fetch individual product prices and gather promotion information. This endpoint converts the raw data in to a format utilized by mobile client details view.  

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
api_instance = pricing.ProductApi(pricing.ApiClient(configuration))
store_id = 'store_id_example' # str | Store id, for example C122.
plussa = False # bool |  (optional) (default to False)
eans = pricing.Eans() # Eans |  (optional)

try:
    # Get individual product prices with promotion information.
    api_response = api_instance.post_v2_stores_storeid_product_pricing(store_id, plussa=plussa, eans=eans)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->post_v2_stores_storeid_product_pricing: %s\n" % e)
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
api_instance = pricing.ProductApi(pricing.ApiClient(configuration))
store_id = 'store_id_example' # str | Store id, for example C122.
plussa = False # bool |  (optional) (default to False)
eans = pricing.Eans() # Eans |  (optional)

try:
    # Get individual product prices with promotion information.
    api_response = api_instance.post_v2_stores_storeid_product_pricing(store_id, plussa=plussa, eans=eans)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->post_v2_stores_storeid_product_pricing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| Store id, for example C122. | 
 **plussa** | **bool**|  | [optional] [default to False]
 **eans** | [**Eans**](Eans.md)|  | [optional] 

### Return type

**dict(str, object)**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found store object |  -  |
**400** | Bad request |  -  |
**404** | Store not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

