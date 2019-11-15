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

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (
    ApiTypeError,
    ApiValueError
)


class StoreApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_v2_stores(self, **kwargs):  # noqa: E501
        """Get info for multiple stores.  # noqa: E501

        Get info for multiple stores.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v2_stores(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str ids: Store ids.
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
        return self.get_v2_stores_with_http_info(**kwargs)  # noqa: E501

    def get_v2_stores_with_http_info(self, **kwargs):  # noqa: E501
        """Get info for multiple stores.  # noqa: E501

        Get info for multiple stores.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v2_stores_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str ids: Store ids.
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

        all_params = ['ids', 'limit', 'offset', 'last_seen']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_v2_stores" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ids' in local_var_params and local_var_params['ids'] is not None:  # noqa: E501
            query_params.append(('ids', local_var_params['ids']))  # noqa: E501
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
            '/v2/stores', 'GET',
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

    def get_v2_stores_storeid(self, store_id, **kwargs):  # noqa: E501
        """Get info for a single store.  # noqa: E501

        Get info for a single store.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v2_stores_storeid(store_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str store_id: Store id, for example C122. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: V2StoresStoreIdGet200ApplicationJsonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_v2_stores_storeid_with_http_info(store_id, **kwargs)  # noqa: E501

    def get_v2_stores_storeid_with_http_info(self, store_id, **kwargs):  # noqa: E501
        """Get info for a single store.  # noqa: E501

        Get info for a single store.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_v2_stores_storeid_with_http_info(store_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str store_id: Store id, for example C122. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(V2StoresStoreIdGet200ApplicationJsonResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['store_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_v2_stores_storeid" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'store_id' is set
        if self.api_client.client_side_validation and ('store_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['store_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `store_id` when calling `get_v2_stores_storeid`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'store_id' in local_var_params:
            path_params['storeId'] = local_var_params['store_id']  # noqa: E501

        query_params = []

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
            '/v2/stores/{storeId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V2StoresStoreIdGet200ApplicationJsonResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
