# coding: utf-8

"""
    Pricing & Availability API

    Pricing & Availability API is a REST-like API which integrates to POS and knows up to date pricing and product availability data for each store. This service can also be used to create and fill temporary shopping baskets, that are kept for 24 hours before they are automatically deleted.    **NOTE:** The API returns money in the responses. You should NOT use that data for actual payment transactions. They are only meant for displaying purposes, but they should work well enough for hackathon purposes.    API requests are only served over HTTPS, using TLS 1.0, 1.1, and 1.2. Requests will not be honored over plaintext HTTP.    Use of `accept: application/json` and `content-type: application/json` headers is required when applicable.    The API uses UTF-8 character encoding for all responses. Some fields may include characters that are not in the ASCII range.    Authentication is accomplished by providing `Ocp-Apim-Subscription-Key` header with your subscription key as the value.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from api.pricing.pricing.api_client import ApiClient
from api.pricing.pricing.exceptions import (
    ApiTypeError,
    ApiValueError
)


class ProductApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_v2_products_ean_ean(self, ean, **kwargs):  # noqa: E501
        """Get availability information for products.  # noqa: E501

        Returns the `pricingUnit` and availability of given products in all stores. If a store is returned in `stores` array, the product should be available in that physical store. If the store also has `web` flag set to true, the product is also available for web sales.  <br><br>[Search API](https://kesko.portal.azure-api.net/docs/services/search/) uses this endpoint check if products are available during indexing process. If you want to check product for availability in your UI, you likely want to use Search APIs availability data.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v2_products_ean_ean(ean, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str ean: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_v2_products_ean_ean_with_http_info(ean, **kwargs)  # noqa: E501

    def get_v2_products_ean_ean_with_http_info(self, ean, **kwargs):  # noqa: E501
        """Get availability information for products.  # noqa: E501

        Returns the `pricingUnit` and availability of given products in all stores. If a store is returned in `stores` array, the product should be available in that physical store. If the store also has `web` flag set to true, the product is also available for web sales.  <br><br>[Search API](https://kesko.portal.azure-api.net/docs/services/search/) uses this endpoint check if products are available during indexing process. If you want to check product for availability in your UI, you likely want to use Search APIs availability data.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v2_products_ean_ean_with_http_info(ean, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str ean: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[object], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['ean']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_v2_products_ean_ean" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'ean' is set
        if self.api_client.client_side_validation and ('ean' not in local_var_params or  # noqa: E501
                                                        local_var_params['ean'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `ean` when calling `get_v2_products_ean_ean`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ean' in local_var_params and local_var_params['ean'] is not None:  # noqa: E501
            query_params.append(('ean', local_var_params['ean']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyHeader', 'apiKeyQuery']  # noqa: E501

        return self.api_client.call_api(
            '/v2/products', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_v4_stores_storeid_products(self, store_id, **kwargs):  # noqa: E501
        """Get product details (pricing, promotions) for a specific store.  # noqa: E501

        This endpoint is used to fetch product details for a specific store. Multiple stores can have the same products with the same EAN codes, but all stores can have independent pricing and promotion details related to the same products, so this information is fetched on a store by store basis.  <br><br>Product details can be queried for specific EAN codes or all of the available products can be queried in a paged manner. Paging is implemented by providing limit and offset attributes.  <br><br>V4 endpoint adds proper support for basket sale sets. Previously the API just returned the number of baskets related to the promotion, but the V4 endpoint returns the basket details instead.  <br><br>Product objects have quite a few optional attributes. Below there are a few examples of different types of products.  <br>Products can have additional texts attached to them:<br><br>  ```  {    \"711719870746\": {      \"ean\": \"711719870746\",      \"baseEan\": \"0711719870746\",      \"name\": \"PlayStation 4 1000Gt + 2 Ohjainta\",      \"group\": \"18950\",      \"price\": 180,      \"pricingUnit\": \"kpl\",      \"vat\": 24,      \"packageSize\": \"1.00\",      \"packageUnit\": \"kpl\",      \"packageType\": \"kpl\",      \"costCenterId\": \"KÄ01\",      \"plussaLimited\": false,      \"discountLimited\": false,      \"type\": \"UTILITY_GOOD\",      \"totalPrice\": 180,      \"texts\": [        {          \"type\": \"warranty\",          \"text\": \"\\\"Tuotteella on 12 kk takuu\\\"\"        }      ]    }  }  ```  <br>Products can consist of multiple `components`, have active `promotions` or `restrictions`. Promotions can affect the price returned by the api, and are automatically calculated:<br><br>  ```  {    \"8594404005409\": {      \"ean\": \"8594404005409\",      \"baseEan\": \"8594404005409\",      \"name\": \"Pilsner Urquell 4,4% 0,5l tlk 4-pack\",      \"group\": \"15243\",      \"price\": 9.8,      \"pricingUnit\": \"kpl\",      \"vat\": 24,      \"packageSize\": \"2.00\",      \"packageUnit\": \"l\",      \"packageType\": \"pakkaus\",      \"costCenterId\": \"PA01\",      \"plussaLimited\": true,      \"discountLimited\": true,      \"type\": \"CONSUMER_GOOD\",      \"components\": [        {          \"baseEan\": \"2000973900008\",          \"name\": \"Tölkkipantti 0,15 0,33l-0,5l\",          \"group\": \"15300\",          \"price\": 0.15,          \"pricingUnit\": \"kpl\",          \"vat\": 24,          \"packageSize\": \"1.00\",          \"packageUnit\": \"kpl\",          \"packageType\": \"kpl\",          \"costCenterId\": \"PM02\",          \"plussaLimited\": false,          \"discountLimited\": true,          \"type\": \"CONSUMER_GOOD\",          \"totalPrice\": 0.6,          \"multiplier\": 4        }      ],      \"totalPrice\": 10.4,      \"restrictions\": {        \"cashierVerifyRequired\": true,        \"ageVerificationRequired\": true,        \"limitedSalesTime\": true      },      \"promotions\": [        {          \"id\": \"8594404005401000000012100001\",          \"type\": 121,          \"startDate\": \"2018-08-27\",          \"endDate\": \"2019-01-02\",          \"plussa\": false,          \"pricingMethod\": \"net\",          \"price\": 9.8,          \"rule\": \"simple\"        }      ]    }  }  ```  <br>Products can have multiplier immutability flag set. If the flag is set, you cannot modify the multiplier of these items:<br><br>  ```  {    \"2000518600004\": {      \"ean\": \"2000518600004\",      \"baseEan\": \"2000518600004\",      \"name\": \"Omena Royal Gala\",      \"group\": \"11523\",      \"price\": 2.59,      \"pricingUnit\": \"kg\",      \"vat\": 14,      \"packageSize\": \"0.00\",      \"packageUnit\": \"kg\",      \"packageType\": \"kilo\",      \"costCenterId\": \"HE01\",      \"plussaLimited\": false,      \"discountLimited\": false,      \"type\": \"CONSUMER_GOOD\",      \"restrictions\": {        \"multiplierImmutable\": true      },      \"totalPrice\": 2.59,      \"scaleNumber\": \"67\",      \"texts\": [        {          \"type\": \"originCountry\",          \"text\": \"ITALIA\"        },        {          \"type\": \"productClass\",          \"text\": \"1LK\"        }      ]    }  }  ```  <br>Some products are sold by their weight. In that case the price is stored as part of the EAN, and baseEan returns the product ean without price:<br><br>  ```  {    \"2000708404321\": {      \"ean\": \"2000708404321\",      \"baseEan\": \"2000708400001\",      \"name\": \"Palvikinkku\",      \"group\": \"11206\",      \"price\": 4.32,      \"pricingUnit\": \"kg\",      \"vat\": 14,      \"packageSize\": \"0.00\",      \"packageUnit\": \"kg\",      \"packageType\": \"kilo\",      \"costCenterId\": \"LJ01\",      \"plussaLimited\": false,      \"discountLimited\": false,      \"type\": \"CONSUMER_GOOD\",      \"restrictions\": {        \"multiplierImmutable\": true      },      \"unitPrice\": 0,      \"totalPrice\": 4.32    }  }  ```    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v4_stores_storeid_products(store_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str store_id: Store id, for example C122. (required)
        :param str ean: An EAN code or multiple EAN codes to return details for. 
        :param int limit: Limit for the quantity of returned results. Default: 20. 
        :param int offset: Offset for the current \"page\" ie. how many results to skip and when to start returning new results up to the defined limit. Default: 0. 
        :param str last_seen: Last seen EAN.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_v4_stores_storeid_products_with_http_info(store_id, **kwargs)  # noqa: E501

    def get_v4_stores_storeid_products_with_http_info(self, store_id, **kwargs):  # noqa: E501
        """Get product details (pricing, promotions) for a specific store.  # noqa: E501

        This endpoint is used to fetch product details for a specific store. Multiple stores can have the same products with the same EAN codes, but all stores can have independent pricing and promotion details related to the same products, so this information is fetched on a store by store basis.  <br><br>Product details can be queried for specific EAN codes or all of the available products can be queried in a paged manner. Paging is implemented by providing limit and offset attributes.  <br><br>V4 endpoint adds proper support for basket sale sets. Previously the API just returned the number of baskets related to the promotion, but the V4 endpoint returns the basket details instead.  <br><br>Product objects have quite a few optional attributes. Below there are a few examples of different types of products.  <br>Products can have additional texts attached to them:<br><br>  ```  {    \"711719870746\": {      \"ean\": \"711719870746\",      \"baseEan\": \"0711719870746\",      \"name\": \"PlayStation 4 1000Gt + 2 Ohjainta\",      \"group\": \"18950\",      \"price\": 180,      \"pricingUnit\": \"kpl\",      \"vat\": 24,      \"packageSize\": \"1.00\",      \"packageUnit\": \"kpl\",      \"packageType\": \"kpl\",      \"costCenterId\": \"KÄ01\",      \"plussaLimited\": false,      \"discountLimited\": false,      \"type\": \"UTILITY_GOOD\",      \"totalPrice\": 180,      \"texts\": [        {          \"type\": \"warranty\",          \"text\": \"\\\"Tuotteella on 12 kk takuu\\\"\"        }      ]    }  }  ```  <br>Products can consist of multiple `components`, have active `promotions` or `restrictions`. Promotions can affect the price returned by the api, and are automatically calculated:<br><br>  ```  {    \"8594404005409\": {      \"ean\": \"8594404005409\",      \"baseEan\": \"8594404005409\",      \"name\": \"Pilsner Urquell 4,4% 0,5l tlk 4-pack\",      \"group\": \"15243\",      \"price\": 9.8,      \"pricingUnit\": \"kpl\",      \"vat\": 24,      \"packageSize\": \"2.00\",      \"packageUnit\": \"l\",      \"packageType\": \"pakkaus\",      \"costCenterId\": \"PA01\",      \"plussaLimited\": true,      \"discountLimited\": true,      \"type\": \"CONSUMER_GOOD\",      \"components\": [        {          \"baseEan\": \"2000973900008\",          \"name\": \"Tölkkipantti 0,15 0,33l-0,5l\",          \"group\": \"15300\",          \"price\": 0.15,          \"pricingUnit\": \"kpl\",          \"vat\": 24,          \"packageSize\": \"1.00\",          \"packageUnit\": \"kpl\",          \"packageType\": \"kpl\",          \"costCenterId\": \"PM02\",          \"plussaLimited\": false,          \"discountLimited\": true,          \"type\": \"CONSUMER_GOOD\",          \"totalPrice\": 0.6,          \"multiplier\": 4        }      ],      \"totalPrice\": 10.4,      \"restrictions\": {        \"cashierVerifyRequired\": true,        \"ageVerificationRequired\": true,        \"limitedSalesTime\": true      },      \"promotions\": [        {          \"id\": \"8594404005401000000012100001\",          \"type\": 121,          \"startDate\": \"2018-08-27\",          \"endDate\": \"2019-01-02\",          \"plussa\": false,          \"pricingMethod\": \"net\",          \"price\": 9.8,          \"rule\": \"simple\"        }      ]    }  }  ```  <br>Products can have multiplier immutability flag set. If the flag is set, you cannot modify the multiplier of these items:<br><br>  ```  {    \"2000518600004\": {      \"ean\": \"2000518600004\",      \"baseEan\": \"2000518600004\",      \"name\": \"Omena Royal Gala\",      \"group\": \"11523\",      \"price\": 2.59,      \"pricingUnit\": \"kg\",      \"vat\": 14,      \"packageSize\": \"0.00\",      \"packageUnit\": \"kg\",      \"packageType\": \"kilo\",      \"costCenterId\": \"HE01\",      \"plussaLimited\": false,      \"discountLimited\": false,      \"type\": \"CONSUMER_GOOD\",      \"restrictions\": {        \"multiplierImmutable\": true      },      \"totalPrice\": 2.59,      \"scaleNumber\": \"67\",      \"texts\": [        {          \"type\": \"originCountry\",          \"text\": \"ITALIA\"        },        {          \"type\": \"productClass\",          \"text\": \"1LK\"        }      ]    }  }  ```  <br>Some products are sold by their weight. In that case the price is stored as part of the EAN, and baseEan returns the product ean without price:<br><br>  ```  {    \"2000708404321\": {      \"ean\": \"2000708404321\",      \"baseEan\": \"2000708400001\",      \"name\": \"Palvikinkku\",      \"group\": \"11206\",      \"price\": 4.32,      \"pricingUnit\": \"kg\",      \"vat\": 14,      \"packageSize\": \"0.00\",      \"packageUnit\": \"kg\",      \"packageType\": \"kilo\",      \"costCenterId\": \"LJ01\",      \"plussaLimited\": false,      \"discountLimited\": false,      \"type\": \"CONSUMER_GOOD\",      \"restrictions\": {        \"multiplierImmutable\": true      },      \"unitPrice\": 0,      \"totalPrice\": 4.32    }  }  ```    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v4_stores_storeid_products_with_http_info(store_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str store_id: Store id, for example C122. (required)
        :param str ean: An EAN code or multiple EAN codes to return details for. 
        :param int limit: Limit for the quantity of returned results. Default: 20. 
        :param int offset: Offset for the current \"page\" ie. how many results to skip and when to start returning new results up to the defined limit. Default: 0. 
        :param str last_seen: Last seen EAN.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(dict(str, object), status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['store_id', 'ean', 'limit', 'offset', 'last_seen']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_v4_stores_storeid_products" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'store_id' is set
        if self.api_client.client_side_validation and ('store_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['store_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `store_id` when calling `get_v4_stores_storeid_products`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'store_id' in local_var_params:
            path_params['storeId'] = local_var_params['store_id']  # noqa: E501

        query_params = []
        if 'ean' in local_var_params and local_var_params['ean'] is not None:  # noqa: E501
            query_params.append(('ean', local_var_params['ean']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'last_seen' in local_var_params and local_var_params['last_seen'] is not None:  # noqa: E501
            query_params.append(('lastSeen', local_var_params['last_seen']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyHeader', 'apiKeyQuery']  # noqa: E501

        return self.api_client.call_api(
            '/v4/stores/{storeId}/products', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, object)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_v2_stores_storeid_price(self, store_id, **kwargs):  # noqa: E501
        """Calculate price for each individual EAN row and the total for the requested EANs.   # noqa: E501

        Calculate price for each individual EAN row and the total for the requested EANs.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_v2_stores_storeid_price(store_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str store_id: Store id, for example C122. (required)
        :param bool plussa:
        :param Products products: An object containing the products for which the prices are fetched. Keys are EANs and values are quantity.  
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: V2StoresStoreIdPricePost200ApplicationJsonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.post_v2_stores_storeid_price_with_http_info(store_id, **kwargs)  # noqa: E501

    def post_v2_stores_storeid_price_with_http_info(self, store_id, **kwargs):  # noqa: E501
        """Calculate price for each individual EAN row and the total for the requested EANs.   # noqa: E501

        Calculate price for each individual EAN row and the total for the requested EANs.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_v2_stores_storeid_price_with_http_info(store_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str store_id: Store id, for example C122. (required)
        :param bool plussa:
        :param Products products: An object containing the products for which the prices are fetched. Keys are EANs and values are quantity.  
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(V2StoresStoreIdPricePost200ApplicationJsonResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['store_id', 'plussa', 'products']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_v2_stores_storeid_price" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'store_id' is set
        if self.api_client.client_side_validation and ('store_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['store_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `store_id` when calling `post_v2_stores_storeid_price`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'store_id' in local_var_params:
            path_params['storeId'] = local_var_params['store_id']  # noqa: E501

        query_params = []
        if 'plussa' in local_var_params and local_var_params['plussa'] is not None:  # noqa: E501
            query_params.append(('plussa', local_var_params['plussa']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'products' in local_var_params:
            body_params = local_var_params['products']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyHeader', 'apiKeyQuery']  # noqa: E501

        return self.api_client.call_api(
            '/v2/stores/{storeId}/price', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V2StoresStoreIdPricePost200ApplicationJsonResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_v2_stores_storeid_product_pricing(self, store_id, **kwargs):  # noqa: E501
        """Get individual product prices with promotion information.  # noqa: E501

        Fetch individual product prices and gather promotion information. This endpoint converts the raw data in to a format utilized by mobile client details view.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_v2_stores_storeid_product_pricing(store_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str store_id: Store id, for example C122. (required)
        :param bool plussa:
        :param Eans eans:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.post_v2_stores_storeid_product_pricing_with_http_info(store_id, **kwargs)  # noqa: E501

    def post_v2_stores_storeid_product_pricing_with_http_info(self, store_id, **kwargs):  # noqa: E501
        """Get individual product prices with promotion information.  # noqa: E501

        Fetch individual product prices and gather promotion information. This endpoint converts the raw data in to a format utilized by mobile client details view.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_v2_stores_storeid_product_pricing_with_http_info(store_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str store_id: Store id, for example C122. (required)
        :param bool plussa:
        :param Eans eans:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(dict(str, object), status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['store_id', 'plussa', 'eans']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_v2_stores_storeid_product_pricing" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'store_id' is set
        if self.api_client.client_side_validation and ('store_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['store_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `store_id` when calling `post_v2_stores_storeid_product_pricing`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'store_id' in local_var_params:
            path_params['storeId'] = local_var_params['store_id']  # noqa: E501

        query_params = []
        if 'plussa' in local_var_params and local_var_params['plussa'] is not None:  # noqa: E501
            query_params.append(('plussa', local_var_params['plussa']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'eans' in local_var_params:
            body_params = local_var_params['eans']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyHeader', 'apiKeyQuery']  # noqa: E501

        return self.api_client.call_api(
            '/v2/stores/{storeId}/product-pricing', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, object)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
