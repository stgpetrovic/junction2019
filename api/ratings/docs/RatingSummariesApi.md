# openapi_client.RatingSummariesApi

All URIs are relative to *https://kesko.azure-api.net/ratings*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_rating_summaries_targetnamespace**](RatingSummariesApi.md#get_rating_summaries_targetnamespace) | **GET** /rating-summaries/{targetNamespace} | List rating summaries in a given target namespace.
[**get_rating_summaries_targetnamespace_targetid**](RatingSummariesApi.md#get_rating_summaries_targetnamespace_targetid) | **GET** /rating-summaries/{targetNamespace}/{targetId} | Return single rating summary.
[**post_rating_summaries_targetnamespace**](RatingSummariesApi.md#post_rating_summaries_targetnamespace) | **POST** /rating-summaries/{targetNamespace} | List rating summaries in a given target namespace.


# **get_rating_summaries_targetnamespace**
> list[object] get_rating_summaries_targetnamespace(target_namespace, target_id=target_id, category=category, sub_category=sub_category, sort=sort, offset=offset, limit=limit, x_ip_address=x_ip_address, x_author_id=x_author_id)

List rating summaries in a given target namespace.

**Notes:**    * Rating summaries are **updated every 10 minutes.**    This must be done to keep the endpoint performant enough.    Use the single rating summary endpoint to return latest data.    * This endpoint does not send `x-total-count` header.    * The results are not necessarily in the same order as    the targetId parameters.    * There might be less items in the array then requested.    If there are a lot of query parameters and the length of the URL gets very long, please consider using the POST version of this API instead.  

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
api_instance = openapi_client.RatingSummariesApi(openapi_client.ApiClient(configuration))
target_namespace = 'target_namespace_example' # str | Target namespace
target_id = 'target_id_example' # str | Search based on one or more targetIds. For example requesting targets [1,2] would be *?targetId=1&targetId=2*.  (optional)
category = 'category_example' # str | Search based on one or more categories. (optional)
sub_category = 'sub_category_example' # str | Search based on one or more sub categories. (optional)
sort = 'average:asc' # str | Sort based on given field. Format: `attribute:direction`. `direction` is optional. For example: `average`, `distribution.usefulness.5:desc:desc`. Default: `average:asc`.  (optional) (default to 'average:asc')
offset = 0 # int | Offset for pagination. Default is **0**. When using this parameter, specify `limit` explicitly. The defaults might change.  (optional) (default to 0)
limit = 10 # int | Limit of returned items. Default is **10**. (optional) (default to 10)
x_ip_address = 'x_ip_address_example' # str | Tells the original requester's IP address to this API. It is needed for moderation purposes. Explained more in [the IP addresses section of the API documentation](../docs/API#ip-addresses). This value is important and should always be included, but isn't strictly required by the API.  (optional)
x_author_id = 'x_author_id_example' # str | **Warning:** this ID should be SAME across all services using this rating service. Tells the original requester's user ID. This is used to restrict some actions. For example author with ID `265` should not be able to modify rating created by user with ID `318`. This value is important and should always be included, but isn't strictly required by the API.  (optional)

try:
    # List rating summaries in a given target namespace.
    api_response = api_instance.get_rating_summaries_targetnamespace(target_namespace, target_id=target_id, category=category, sub_category=sub_category, sort=sort, offset=offset, limit=limit, x_ip_address=x_ip_address, x_author_id=x_author_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingSummariesApi->get_rating_summaries_targetnamespace: %s\n" % e)
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
api_instance = openapi_client.RatingSummariesApi(openapi_client.ApiClient(configuration))
target_namespace = 'target_namespace_example' # str | Target namespace
target_id = 'target_id_example' # str | Search based on one or more targetIds. For example requesting targets [1,2] would be *?targetId=1&targetId=2*.  (optional)
category = 'category_example' # str | Search based on one or more categories. (optional)
sub_category = 'sub_category_example' # str | Search based on one or more sub categories. (optional)
sort = 'average:asc' # str | Sort based on given field. Format: `attribute:direction`. `direction` is optional. For example: `average`, `distribution.usefulness.5:desc:desc`. Default: `average:asc`.  (optional) (default to 'average:asc')
offset = 0 # int | Offset for pagination. Default is **0**. When using this parameter, specify `limit` explicitly. The defaults might change.  (optional) (default to 0)
limit = 10 # int | Limit of returned items. Default is **10**. (optional) (default to 10)
x_ip_address = 'x_ip_address_example' # str | Tells the original requester's IP address to this API. It is needed for moderation purposes. Explained more in [the IP addresses section of the API documentation](../docs/API#ip-addresses). This value is important and should always be included, but isn't strictly required by the API.  (optional)
x_author_id = 'x_author_id_example' # str | **Warning:** this ID should be SAME across all services using this rating service. Tells the original requester's user ID. This is used to restrict some actions. For example author with ID `265` should not be able to modify rating created by user with ID `318`. This value is important and should always be included, but isn't strictly required by the API.  (optional)

try:
    # List rating summaries in a given target namespace.
    api_response = api_instance.get_rating_summaries_targetnamespace(target_namespace, target_id=target_id, category=category, sub_category=sub_category, sort=sort, offset=offset, limit=limit, x_ip_address=x_ip_address, x_author_id=x_author_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingSummariesApi->get_rating_summaries_targetnamespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_namespace** | **str**| Target namespace | 
 **target_id** | **str**| Search based on one or more targetIds. For example requesting targets [1,2] would be *?targetId&#x3D;1&amp;targetId&#x3D;2*.  | [optional] 
 **category** | **str**| Search based on one or more categories. | [optional] 
 **sub_category** | **str**| Search based on one or more sub categories. | [optional] 
 **sort** | **str**| Sort based on given field. Format: &#x60;attribute:direction&#x60;. &#x60;direction&#x60; is optional. For example: &#x60;average&#x60;, &#x60;distribution.usefulness.5:desc:desc&#x60;. Default: &#x60;average:asc&#x60;.  | [optional] [default to &#39;average:asc&#39;]
 **offset** | **int**| Offset for pagination. Default is **0**. When using this parameter, specify &#x60;limit&#x60; explicitly. The defaults might change.  | [optional] [default to 0]
 **limit** | **int**| Limit of returned items. Default is **10**. | [optional] [default to 10]
 **x_ip_address** | **str**| Tells the original requester&#39;s IP address to this API. It is needed for moderation purposes. Explained more in [the IP addresses section of the API documentation](../docs/API#ip-addresses). This value is important and should always be included, but isn&#39;t strictly required by the API.  | [optional] 
 **x_author_id** | **str**| **Warning:** this ID should be SAME across all services using this rating service. Tells the original requester&#39;s user ID. This is used to restrict some actions. For example author with ID &#x60;265&#x60; should not be able to modify rating created by user with ID &#x60;318&#x60;. This value is important and should always be included, but isn&#39;t strictly required by the API.  | [optional] 

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
**200** | List of rating summaries or an empty list if none were found.   |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rating_summaries_targetnamespace_targetid**
> RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse get_rating_summaries_targetnamespace_targetid(target_namespace, target_id, x_ip_address=x_ip_address, x_author_id=x_author_id)

Return single rating summary.

**Note:** Summary for single is cached but the cache is invalidated if the target's rating is modified in some way: update, delete or new rating. In practice this means that this endpoint returns up-to-date data.  

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
api_instance = openapi_client.RatingSummariesApi(openapi_client.ApiClient(configuration))
target_namespace = 'target_namespace_example' # str | Target namespace
target_id = 'target_id_example' # str | Target ID
x_ip_address = 'x_ip_address_example' # str | Tells the original requester's IP address to this API. It is needed for moderation purposes. Explained more in [the IP addresses section of the API documentation](../docs/API#ip-addresses). This value is important and should always be included, but isn't strictly required by the API.  (optional)
x_author_id = 'x_author_id_example' # str | **Warning:** this ID should be SAME across all services using this rating service. Tells the original requester's user ID. This is used to restrict some actions. For example author with ID `265` should not be able to modify rating created by user with ID `318`. This value is important and should always be included, but isn't strictly required by the API.  (optional)

try:
    # Return single rating summary.
    api_response = api_instance.get_rating_summaries_targetnamespace_targetid(target_namespace, target_id, x_ip_address=x_ip_address, x_author_id=x_author_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingSummariesApi->get_rating_summaries_targetnamespace_targetid: %s\n" % e)
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
api_instance = openapi_client.RatingSummariesApi(openapi_client.ApiClient(configuration))
target_namespace = 'target_namespace_example' # str | Target namespace
target_id = 'target_id_example' # str | Target ID
x_ip_address = 'x_ip_address_example' # str | Tells the original requester's IP address to this API. It is needed for moderation purposes. Explained more in [the IP addresses section of the API documentation](../docs/API#ip-addresses). This value is important and should always be included, but isn't strictly required by the API.  (optional)
x_author_id = 'x_author_id_example' # str | **Warning:** this ID should be SAME across all services using this rating service. Tells the original requester's user ID. This is used to restrict some actions. For example author with ID `265` should not be able to modify rating created by user with ID `318`. This value is important and should always be included, but isn't strictly required by the API.  (optional)

try:
    # Return single rating summary.
    api_response = api_instance.get_rating_summaries_targetnamespace_targetid(target_namespace, target_id, x_ip_address=x_ip_address, x_author_id=x_author_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingSummariesApi->get_rating_summaries_targetnamespace_targetid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_namespace** | **str**| Target namespace | 
 **target_id** | **str**| Target ID | 
 **x_ip_address** | **str**| Tells the original requester&#39;s IP address to this API. It is needed for moderation purposes. Explained more in [the IP addresses section of the API documentation](../docs/API#ip-addresses). This value is important and should always be included, but isn&#39;t strictly required by the API.  | [optional] 
 **x_author_id** | **str**| **Warning:** this ID should be SAME across all services using this rating service. Tells the original requester&#39;s user ID. This is used to restrict some actions. For example author with ID &#x60;265&#x60; should not be able to modify rating created by user with ID &#x60;318&#x60;. This value is important and should always be included, but isn&#39;t strictly required by the API.  | [optional] 

### Return type

[**RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse**](RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rating found   |  -  |
**404** | No ratings have been created for the target. *The behavior is unfortunate but rating service doesn&#39;t know any of the targets before the first rating is given for them.*   |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_rating_summaries_targetnamespace**
> list[object] post_rating_summaries_targetnamespace(target_namespace, target_id=target_id, category=category, sub_category=sub_category, sort=sort, offset=offset, limit=limit, x_ip_address=x_ip_address, x_author_id=x_author_id)

List rating summaries in a given target namespace.

Exactly the same as `GET /rating-summaries/:targetNamespace` with the exception that parameters which haven't been supplied as query parameters are searched from the body of the request instead. Therefore makes it possible to send longer parameter lists.  

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
api_instance = openapi_client.RatingSummariesApi(openapi_client.ApiClient(configuration))
target_namespace = 'target_namespace_example' # str | Target namespace
target_id = 'target_id_example' # str | Search based on one or more targetIds. For example requesting targets [1,2] would be *?targetId=1&targetId=2*.  (optional)
category = 'category_example' # str | Search based on one or more categories. (optional)
sub_category = 'sub_category_example' # str | Search based on one or more sub categories. (optional)
sort = 'average:asc' # str | Sort based on given field. Format: `attribute:direction`. `direction` is optional. For example: `average`, `distribution.usefulness.5:desc:desc`. Default: `average:asc`.  (optional) (default to 'average:asc')
offset = 0 # int | Offset for pagination. Default is **0**. When using this parameter, specify `limit` explicitly. The defaults might change.  (optional) (default to 0)
limit = 10 # int | Limit of returned items. Default is **10**. (optional) (default to 10)
x_ip_address = 'x_ip_address_example' # str | Tells the original requester's IP address to this API. It is needed for moderation purposes. Explained more in [the IP addresses section of the API documentation](../docs/API#ip-addresses). This value is important and should always be included, but isn't strictly required by the API.  (optional)
x_author_id = 'x_author_id_example' # str | **Warning:** this ID should be SAME across all services using this rating service. Tells the original requester's user ID. This is used to restrict some actions. For example author with ID `265` should not be able to modify rating created by user with ID `318`. This value is important and should always be included, but isn't strictly required by the API.  (optional)

try:
    # List rating summaries in a given target namespace.
    api_response = api_instance.post_rating_summaries_targetnamespace(target_namespace, target_id=target_id, category=category, sub_category=sub_category, sort=sort, offset=offset, limit=limit, x_ip_address=x_ip_address, x_author_id=x_author_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingSummariesApi->post_rating_summaries_targetnamespace: %s\n" % e)
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
api_instance = openapi_client.RatingSummariesApi(openapi_client.ApiClient(configuration))
target_namespace = 'target_namespace_example' # str | Target namespace
target_id = 'target_id_example' # str | Search based on one or more targetIds. For example requesting targets [1,2] would be *?targetId=1&targetId=2*.  (optional)
category = 'category_example' # str | Search based on one or more categories. (optional)
sub_category = 'sub_category_example' # str | Search based on one or more sub categories. (optional)
sort = 'average:asc' # str | Sort based on given field. Format: `attribute:direction`. `direction` is optional. For example: `average`, `distribution.usefulness.5:desc:desc`. Default: `average:asc`.  (optional) (default to 'average:asc')
offset = 0 # int | Offset for pagination. Default is **0**. When using this parameter, specify `limit` explicitly. The defaults might change.  (optional) (default to 0)
limit = 10 # int | Limit of returned items. Default is **10**. (optional) (default to 10)
x_ip_address = 'x_ip_address_example' # str | Tells the original requester's IP address to this API. It is needed for moderation purposes. Explained more in [the IP addresses section of the API documentation](../docs/API#ip-addresses). This value is important and should always be included, but isn't strictly required by the API.  (optional)
x_author_id = 'x_author_id_example' # str | **Warning:** this ID should be SAME across all services using this rating service. Tells the original requester's user ID. This is used to restrict some actions. For example author with ID `265` should not be able to modify rating created by user with ID `318`. This value is important and should always be included, but isn't strictly required by the API.  (optional)

try:
    # List rating summaries in a given target namespace.
    api_response = api_instance.post_rating_summaries_targetnamespace(target_namespace, target_id=target_id, category=category, sub_category=sub_category, sort=sort, offset=offset, limit=limit, x_ip_address=x_ip_address, x_author_id=x_author_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingSummariesApi->post_rating_summaries_targetnamespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_namespace** | **str**| Target namespace | 
 **target_id** | **str**| Search based on one or more targetIds. For example requesting targets [1,2] would be *?targetId&#x3D;1&amp;targetId&#x3D;2*.  | [optional] 
 **category** | **str**| Search based on one or more categories. | [optional] 
 **sub_category** | **str**| Search based on one or more sub categories. | [optional] 
 **sort** | **str**| Sort based on given field. Format: &#x60;attribute:direction&#x60;. &#x60;direction&#x60; is optional. For example: &#x60;average&#x60;, &#x60;distribution.usefulness.5:desc:desc&#x60;. Default: &#x60;average:asc&#x60;.  | [optional] [default to &#39;average:asc&#39;]
 **offset** | **int**| Offset for pagination. Default is **0**. When using this parameter, specify &#x60;limit&#x60; explicitly. The defaults might change.  | [optional] [default to 0]
 **limit** | **int**| Limit of returned items. Default is **10**. | [optional] [default to 10]
 **x_ip_address** | **str**| Tells the original requester&#39;s IP address to this API. It is needed for moderation purposes. Explained more in [the IP addresses section of the API documentation](../docs/API#ip-addresses). This value is important and should always be included, but isn&#39;t strictly required by the API.  | [optional] 
 **x_author_id** | **str**| **Warning:** this ID should be SAME across all services using this rating service. Tells the original requester&#39;s user ID. This is used to restrict some actions. For example author with ID &#x60;265&#x60; should not be able to modify rating created by user with ID &#x60;318&#x60;. This value is important and should always be included, but isn&#39;t strictly required by the API.  | [optional] 

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
**200** | List of rating summaries or an empty list if none were found.   |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

