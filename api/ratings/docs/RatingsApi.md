# openapi_client.RatingsApi

All URIs are relative to *https://kesko.azure-api.net/ratings*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_ratings_targetnamespace_id**](RatingsApi.md#delete_ratings_targetnamespace_id) | **DELETE** /ratings/{targetNamespace}/{id} | Delete rating.
[**get_ratings_targetnamespace**](RatingsApi.md#get_ratings_targetnamespace) | **GET** /ratings/{targetNamespace} | List ratings in a given target namespace.
[**get_ratings_targetnamespace_id**](RatingsApi.md#get_ratings_targetnamespace_id) | **GET** /ratings/{targetNamespace}/{id} | Get rating.
[**post_ratings_targetnamespace**](RatingsApi.md#post_ratings_targetnamespace) | **POST** /ratings/{targetNamespace} | Create rating.
[**put_ratings_targetnamespace_id**](RatingsApi.md#put_ratings_targetnamespace_id) | **PUT** /ratings/{targetNamespace}/{id} | Update rating.


# **delete_ratings_targetnamespace_id**
> delete_ratings_targetnamespace_id(target_namespace, id, x_ip_address=x_ip_address, x_author_id=x_author_id)

Delete rating.

**Authorization:** Author x can't delete author y's rating.  

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
api_instance = openapi_client.RatingsApi(openapi_client.ApiClient(configuration))
target_namespace = 'target_namespace_example' # str | Target namespace
id = 'id_example' # str | Target ID
x_ip_address = 'x_ip_address_example' # str | Tells the original requester's IP address to this API. It is needed for moderation purposes. Explained more in [the IP addresses section of the API documentation](../docs/API#ip-addresses). This value is important and should always be included, but isn't strictly required by the API.  (optional)
x_author_id = 'x_author_id_example' # str | **Warning:** this ID should be SAME across all services using this rating service. Tells the original requester's user ID. This is used to restrict some actions. For example author with ID `265` should not be able to modify rating created by user with ID `318`. This value is important and should always be included, but isn't strictly required by the API.  (optional)

try:
    # Delete rating.
    api_instance.delete_ratings_targetnamespace_id(target_namespace, id, x_ip_address=x_ip_address, x_author_id=x_author_id)
except ApiException as e:
    print("Exception when calling RatingsApi->delete_ratings_targetnamespace_id: %s\n" % e)
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
api_instance = openapi_client.RatingsApi(openapi_client.ApiClient(configuration))
target_namespace = 'target_namespace_example' # str | Target namespace
id = 'id_example' # str | Target ID
x_ip_address = 'x_ip_address_example' # str | Tells the original requester's IP address to this API. It is needed for moderation purposes. Explained more in [the IP addresses section of the API documentation](../docs/API#ip-addresses). This value is important and should always be included, but isn't strictly required by the API.  (optional)
x_author_id = 'x_author_id_example' # str | **Warning:** this ID should be SAME across all services using this rating service. Tells the original requester's user ID. This is used to restrict some actions. For example author with ID `265` should not be able to modify rating created by user with ID `318`. This value is important and should always be included, but isn't strictly required by the API.  (optional)

try:
    # Delete rating.
    api_instance.delete_ratings_targetnamespace_id(target_namespace, id, x_ip_address=x_ip_address, x_author_id=x_author_id)
except ApiException as e:
    print("Exception when calling RatingsApi->delete_ratings_targetnamespace_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_namespace** | **str**| Target namespace | 
 **id** | **str**| Target ID | 
 **x_ip_address** | **str**| Tells the original requester&#39;s IP address to this API. It is needed for moderation purposes. Explained more in [the IP addresses section of the API documentation](../docs/API#ip-addresses). This value is important and should always be included, but isn&#39;t strictly required by the API.  | [optional] 
 **x_author_id** | **str**| **Warning:** this ID should be SAME across all services using this rating service. Tells the original requester&#39;s user ID. This is used to restrict some actions. For example author with ID &#x60;265&#x60; should not be able to modify rating created by user with ID &#x60;318&#x60;. This value is important and should always be included, but isn&#39;t strictly required by the API.  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ratings_targetnamespace**
> list[object] get_ratings_targetnamespace(target_namespace, target_id=target_id, author_id=author_id, author_role=author_role, category=category, sub_category=sub_category, has_rating=has_rating, has_comment=has_comment, reply_requested=reply_requested, moderated=moderated, published=published, sort=sort, offset=offset, limit=limit, x_ip_address=x_ip_address, x_author_id=x_author_id)

List ratings in a given target namespace.

List ratings in a given target namespace. If requesting as a service user, unpublished ratings will not be returned.  

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
api_instance = openapi_client.RatingsApi(openapi_client.ApiClient(configuration))
target_namespace = 'target_namespace_example' # str | Target namespace
target_id = 'target_id_example' # str | Search based on one or more targetIds. For example requesting targets [1,2] would be *?targetId=1&targetId=2*.  (optional)
author_id = 'author_id_example' # str | Search based on one or more authorIds. (optional)
author_role = 'author_role_example' # str | Search based on one or more authorRoles. **(only for above service role)**  (optional)
category = 'category_example' # str | Search based on one or more categories. (optional)
sub_category = 'sub_category_example' # str | Search based on one or more sub categories. (optional)
has_rating = True # bool | Search based on if the rating has a numeric rating or not. If `true`, only ratings with a numeric rating are returned.  (optional)
has_comment = True # bool | Search based on if the rating has a comment or not. If true, only ratings with comment are returned.  (optional)
reply_requested = True # bool | Search based on if the rating's author wants a reply for their comment. **(only for above service role)**  (optional)
moderated = True # bool | Search based on if the rating is moderated or not. **(only for above service role)**  (optional)
published = True # bool | Search based on if the rating is published or not. **(only for above service role)**  (optional)
sort = 'sort_example' # str | Sort based on given field. Format: `attribute:direction`. `direction` is optional, default is **asc**. For example: `createdAt`, `updatedAt:desc`, `updatedAt:asc`.  (optional)
offset = 0 # int | Offset for pagination. Default is **0**. When using this parameter, specify `limit` explicitly. The defaults might change.  (optional) (default to 0)
limit = 10 # int | Limit of returned items. Default is **10**. (optional) (default to 10)
x_ip_address = 'x_ip_address_example' # str | Tells the original requester's IP address to this API. It is needed for moderation purposes. Explained more in [the IP addresses section of the API documentation](../docs/API#ip-addresses). This value is important and should always be included, but isn't strictly required by the API.  (optional)
x_author_id = 'x_author_id_example' # str | **Warning:** this ID should be SAME across all services using this rating service. Tells the original requester's user ID. This is used to restrict some actions. For example author with ID `265` should not be able to modify rating created by user with ID `318`. This value is important and should always be included, but isn't strictly required by the API.  (optional)

try:
    # List ratings in a given target namespace.
    api_response = api_instance.get_ratings_targetnamespace(target_namespace, target_id=target_id, author_id=author_id, author_role=author_role, category=category, sub_category=sub_category, has_rating=has_rating, has_comment=has_comment, reply_requested=reply_requested, moderated=moderated, published=published, sort=sort, offset=offset, limit=limit, x_ip_address=x_ip_address, x_author_id=x_author_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingsApi->get_ratings_targetnamespace: %s\n" % e)
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
api_instance = openapi_client.RatingsApi(openapi_client.ApiClient(configuration))
target_namespace = 'target_namespace_example' # str | Target namespace
target_id = 'target_id_example' # str | Search based on one or more targetIds. For example requesting targets [1,2] would be *?targetId=1&targetId=2*.  (optional)
author_id = 'author_id_example' # str | Search based on one or more authorIds. (optional)
author_role = 'author_role_example' # str | Search based on one or more authorRoles. **(only for above service role)**  (optional)
category = 'category_example' # str | Search based on one or more categories. (optional)
sub_category = 'sub_category_example' # str | Search based on one or more sub categories. (optional)
has_rating = True # bool | Search based on if the rating has a numeric rating or not. If `true`, only ratings with a numeric rating are returned.  (optional)
has_comment = True # bool | Search based on if the rating has a comment or not. If true, only ratings with comment are returned.  (optional)
reply_requested = True # bool | Search based on if the rating's author wants a reply for their comment. **(only for above service role)**  (optional)
moderated = True # bool | Search based on if the rating is moderated or not. **(only for above service role)**  (optional)
published = True # bool | Search based on if the rating is published or not. **(only for above service role)**  (optional)
sort = 'sort_example' # str | Sort based on given field. Format: `attribute:direction`. `direction` is optional, default is **asc**. For example: `createdAt`, `updatedAt:desc`, `updatedAt:asc`.  (optional)
offset = 0 # int | Offset for pagination. Default is **0**. When using this parameter, specify `limit` explicitly. The defaults might change.  (optional) (default to 0)
limit = 10 # int | Limit of returned items. Default is **10**. (optional) (default to 10)
x_ip_address = 'x_ip_address_example' # str | Tells the original requester's IP address to this API. It is needed for moderation purposes. Explained more in [the IP addresses section of the API documentation](../docs/API#ip-addresses). This value is important and should always be included, but isn't strictly required by the API.  (optional)
x_author_id = 'x_author_id_example' # str | **Warning:** this ID should be SAME across all services using this rating service. Tells the original requester's user ID. This is used to restrict some actions. For example author with ID `265` should not be able to modify rating created by user with ID `318`. This value is important and should always be included, but isn't strictly required by the API.  (optional)

try:
    # List ratings in a given target namespace.
    api_response = api_instance.get_ratings_targetnamespace(target_namespace, target_id=target_id, author_id=author_id, author_role=author_role, category=category, sub_category=sub_category, has_rating=has_rating, has_comment=has_comment, reply_requested=reply_requested, moderated=moderated, published=published, sort=sort, offset=offset, limit=limit, x_ip_address=x_ip_address, x_author_id=x_author_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingsApi->get_ratings_targetnamespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_namespace** | **str**| Target namespace | 
 **target_id** | **str**| Search based on one or more targetIds. For example requesting targets [1,2] would be *?targetId&#x3D;1&amp;targetId&#x3D;2*.  | [optional] 
 **author_id** | **str**| Search based on one or more authorIds. | [optional] 
 **author_role** | **str**| Search based on one or more authorRoles. **(only for above service role)**  | [optional] 
 **category** | **str**| Search based on one or more categories. | [optional] 
 **sub_category** | **str**| Search based on one or more sub categories. | [optional] 
 **has_rating** | **bool**| Search based on if the rating has a numeric rating or not. If &#x60;true&#x60;, only ratings with a numeric rating are returned.  | [optional] 
 **has_comment** | **bool**| Search based on if the rating has a comment or not. If true, only ratings with comment are returned.  | [optional] 
 **reply_requested** | **bool**| Search based on if the rating&#39;s author wants a reply for their comment. **(only for above service role)**  | [optional] 
 **moderated** | **bool**| Search based on if the rating is moderated or not. **(only for above service role)**  | [optional] 
 **published** | **bool**| Search based on if the rating is published or not. **(only for above service role)**  | [optional] 
 **sort** | **str**| Sort based on given field. Format: &#x60;attribute:direction&#x60;. &#x60;direction&#x60; is optional, default is **asc**. For example: &#x60;createdAt&#x60;, &#x60;updatedAt:desc&#x60;, &#x60;updatedAt:asc&#x60;.  | [optional] 
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
**200** | List of ratings or an empty list if none were found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ratings_targetnamespace_id**
> RatingsTargetNamespaceIdGet200ApplicationJsonResponse get_ratings_targetnamespace_id(target_namespace, id, x_ip_address=x_ip_address, x_author_id=x_author_id)

Get rating.

**Note:** Response is cached, but the cache is invalidated if the target's rating is modified in some way: update, delete or new rating. In practice this means that this endpoint returns up-to-date data.  

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
api_instance = openapi_client.RatingsApi(openapi_client.ApiClient(configuration))
target_namespace = 'target_namespace_example' # str | Target namespace
id = 'id_example' # str | Target ID
x_ip_address = 'x_ip_address_example' # str | Tells the original requester's IP address to this API. It is needed for moderation purposes. Explained more in [the IP addresses section of the API documentation](../docs/API#ip-addresses). This value is important and should always be included, but isn't strictly required by the API.  (optional)
x_author_id = 'x_author_id_example' # str | **Warning:** this ID should be SAME across all services using this rating service. Tells the original requester's user ID. This is used to restrict some actions. For example author with ID `265` should not be able to modify rating created by user with ID `318`. This value is important and should always be included, but isn't strictly required by the API.  (optional)

try:
    # Get rating.
    api_response = api_instance.get_ratings_targetnamespace_id(target_namespace, id, x_ip_address=x_ip_address, x_author_id=x_author_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingsApi->get_ratings_targetnamespace_id: %s\n" % e)
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
api_instance = openapi_client.RatingsApi(openapi_client.ApiClient(configuration))
target_namespace = 'target_namespace_example' # str | Target namespace
id = 'id_example' # str | Target ID
x_ip_address = 'x_ip_address_example' # str | Tells the original requester's IP address to this API. It is needed for moderation purposes. Explained more in [the IP addresses section of the API documentation](../docs/API#ip-addresses). This value is important and should always be included, but isn't strictly required by the API.  (optional)
x_author_id = 'x_author_id_example' # str | **Warning:** this ID should be SAME across all services using this rating service. Tells the original requester's user ID. This is used to restrict some actions. For example author with ID `265` should not be able to modify rating created by user with ID `318`. This value is important and should always be included, but isn't strictly required by the API.  (optional)

try:
    # Get rating.
    api_response = api_instance.get_ratings_targetnamespace_id(target_namespace, id, x_ip_address=x_ip_address, x_author_id=x_author_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingsApi->get_ratings_targetnamespace_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_namespace** | **str**| Target namespace | 
 **id** | **str**| Target ID | 
 **x_ip_address** | **str**| Tells the original requester&#39;s IP address to this API. It is needed for moderation purposes. Explained more in [the IP addresses section of the API documentation](../docs/API#ip-addresses). This value is important and should always be included, but isn&#39;t strictly required by the API.  | [optional] 
 **x_author_id** | **str**| **Warning:** this ID should be SAME across all services using this rating service. Tells the original requester&#39;s user ID. This is used to restrict some actions. For example author with ID &#x60;265&#x60; should not be able to modify rating created by user with ID &#x60;318&#x60;. This value is important and should always be included, but isn&#39;t strictly required by the API.  | [optional] 

### Return type

[**RatingsTargetNamespaceIdGet200ApplicationJsonResponse**](RatingsTargetNamespaceIdGet200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rating object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ratings_targetnamespace**
> RatingsTargetNamespacePost200ApplicationJsonResponse post_ratings_targetnamespace(target_namespace, x_ip_address=x_ip_address, x_author_id=x_author_id, rating=rating)

Create rating.

The service needs authorId to prevent users from creating more than one rating for same target and also for other restrictions.  

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
api_instance = openapi_client.RatingsApi(openapi_client.ApiClient(configuration))
target_namespace = 'target_namespace_example' # str | Target namespace
x_ip_address = 'x_ip_address_example' # str | Tells the original requester's IP address to this API. It is needed for moderation purposes. Explained more in [the IP addresses section of the API documentation](../docs/API#ip-addresses). This value is important and should always be included, but isn't strictly required by the API.  (optional)
x_author_id = 'x_author_id_example' # str | **Warning:** this ID should be SAME across all services using this rating service. Tells the original requester's user ID. This is used to restrict some actions. For example author with ID `265` should not be able to modify rating created by user with ID `318`. This value is important and should always be included, but isn't strictly required by the API.  (optional)
rating = openapi_client.Rating() # Rating | Rating object (optional)

try:
    # Create rating.
    api_response = api_instance.post_ratings_targetnamespace(target_namespace, x_ip_address=x_ip_address, x_author_id=x_author_id, rating=rating)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingsApi->post_ratings_targetnamespace: %s\n" % e)
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
api_instance = openapi_client.RatingsApi(openapi_client.ApiClient(configuration))
target_namespace = 'target_namespace_example' # str | Target namespace
x_ip_address = 'x_ip_address_example' # str | Tells the original requester's IP address to this API. It is needed for moderation purposes. Explained more in [the IP addresses section of the API documentation](../docs/API#ip-addresses). This value is important and should always be included, but isn't strictly required by the API.  (optional)
x_author_id = 'x_author_id_example' # str | **Warning:** this ID should be SAME across all services using this rating service. Tells the original requester's user ID. This is used to restrict some actions. For example author with ID `265` should not be able to modify rating created by user with ID `318`. This value is important and should always be included, but isn't strictly required by the API.  (optional)
rating = openapi_client.Rating() # Rating | Rating object (optional)

try:
    # Create rating.
    api_response = api_instance.post_ratings_targetnamespace(target_namespace, x_ip_address=x_ip_address, x_author_id=x_author_id, rating=rating)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingsApi->post_ratings_targetnamespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_namespace** | **str**| Target namespace | 
 **x_ip_address** | **str**| Tells the original requester&#39;s IP address to this API. It is needed for moderation purposes. Explained more in [the IP addresses section of the API documentation](../docs/API#ip-addresses). This value is important and should always be included, but isn&#39;t strictly required by the API.  | [optional] 
 **x_author_id** | **str**| **Warning:** this ID should be SAME across all services using this rating service. Tells the original requester&#39;s user ID. This is used to restrict some actions. For example author with ID &#x60;265&#x60; should not be able to modify rating created by user with ID &#x60;318&#x60;. This value is important and should always be included, but isn&#39;t strictly required by the API.  | [optional] 
 **rating** | [**Rating**](Rating.md)| Rating object | [optional] 

### Return type

[**RatingsTargetNamespacePost200ApplicationJsonResponse**](RatingsTargetNamespacePost200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rating object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_ratings_targetnamespace_id**
> RatingsTargetNamespaceIdPut200ApplicationJsonResponse put_ratings_targetnamespace_id(target_namespace, id, x_ip_address=x_ip_address, x_author_id=x_author_id, rating=rating)

Update rating.

Body of the request should be a full rating object.  **Note:** `targetNamespace` is being pulled from request body instead of url. That way it's also possible to update `targetNamespace`.  **Authorization:** Author x can't update author y's rating.  **Warning: You must send the full object on each PUT request. Fields which are not sent, will be considered as \"removed\" fields!**  

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
api_instance = openapi_client.RatingsApi(openapi_client.ApiClient(configuration))
target_namespace = 'target_namespace_example' # str | Target namespace
id = 'id_example' # str | Target ID
x_ip_address = 'x_ip_address_example' # str | Tells the original requester's IP address to this API. It is needed for moderation purposes. Explained more in [the IP addresses section of the API documentation](../docs/API#ip-addresses). This value is important and should always be included, but isn't strictly required by the API.  (optional)
x_author_id = 'x_author_id_example' # str | **Warning:** this ID should be SAME across all services using this rating service. Tells the original requester's user ID. This is used to restrict some actions. For example author with ID `265` should not be able to modify rating created by user with ID `318`. This value is important and should always be included, but isn't strictly required by the API.  (optional)
rating = openapi_client.Rating() # Rating | Rating object (optional)

try:
    # Update rating.
    api_response = api_instance.put_ratings_targetnamespace_id(target_namespace, id, x_ip_address=x_ip_address, x_author_id=x_author_id, rating=rating)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingsApi->put_ratings_targetnamespace_id: %s\n" % e)
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
api_instance = openapi_client.RatingsApi(openapi_client.ApiClient(configuration))
target_namespace = 'target_namespace_example' # str | Target namespace
id = 'id_example' # str | Target ID
x_ip_address = 'x_ip_address_example' # str | Tells the original requester's IP address to this API. It is needed for moderation purposes. Explained more in [the IP addresses section of the API documentation](../docs/API#ip-addresses). This value is important and should always be included, but isn't strictly required by the API.  (optional)
x_author_id = 'x_author_id_example' # str | **Warning:** this ID should be SAME across all services using this rating service. Tells the original requester's user ID. This is used to restrict some actions. For example author with ID `265` should not be able to modify rating created by user with ID `318`. This value is important and should always be included, but isn't strictly required by the API.  (optional)
rating = openapi_client.Rating() # Rating | Rating object (optional)

try:
    # Update rating.
    api_response = api_instance.put_ratings_targetnamespace_id(target_namespace, id, x_ip_address=x_ip_address, x_author_id=x_author_id, rating=rating)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingsApi->put_ratings_targetnamespace_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_namespace** | **str**| Target namespace | 
 **id** | **str**| Target ID | 
 **x_ip_address** | **str**| Tells the original requester&#39;s IP address to this API. It is needed for moderation purposes. Explained more in [the IP addresses section of the API documentation](../docs/API#ip-addresses). This value is important and should always be included, but isn&#39;t strictly required by the API.  | [optional] 
 **x_author_id** | **str**| **Warning:** this ID should be SAME across all services using this rating service. Tells the original requester&#39;s user ID. This is used to restrict some actions. For example author with ID &#x60;265&#x60; should not be able to modify rating created by user with ID &#x60;318&#x60;. This value is important and should always be included, but isn&#39;t strictly required by the API.  | [optional] 
 **rating** | [**Rating**](Rating.md)| Rating object | [optional] 

### Return type

[**RatingsTargetNamespaceIdPut200ApplicationJsonResponse**](RatingsTargetNamespaceIdPut200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rating object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

