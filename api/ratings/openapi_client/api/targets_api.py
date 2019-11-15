# coding: utf-8

"""
    Ratings API

    Service which holds ratings of various targets, like recipes.  # noqa: E501

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


class TargetsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_targets_targetnamespace(self, target_namespace, **kwargs):  # noqa: E501
        """Lists all targets currently in the database.  # noqa: E501

        Lists all targets currently in the database.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_targets_targetnamespace(target_namespace, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str target_namespace: Target namespace (required)
        :param int offset: Offset for pagination. Default is **0**. When using this parameter, specify `limit` explicitly. The defaults might change. 
        :param int limit: Limit of returned items. By default, there is no limit as we need all targets in the UI. 
        :param str sort: Sort based on given field. Format: `attribute:direction`. `direction` is optional, default is **asc**. For example: `createdAt`, `updatedAt:desc`, `updatedAt:asc`. 
        :param str x_ip_address: Tells the original requester's IP address to this API. It is needed for moderation purposes. Explained more in [the IP addresses section of the API documentation](../docs/API#ip-addresses). This value is important and should always be included, but isn't strictly required by the API. 
        :param str x_author_id: **Warning:** this ID should be SAME across all services using this rating service. Tells the original requester's user ID. This is used to restrict some actions. For example author with ID `265` should not be able to modify rating created by user with ID `318`. This value is important and should always be included, but isn't strictly required by the API. 
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
        return self.get_targets_targetnamespace_with_http_info(target_namespace, **kwargs)  # noqa: E501

    def get_targets_targetnamespace_with_http_info(self, target_namespace, **kwargs):  # noqa: E501
        """Lists all targets currently in the database.  # noqa: E501

        Lists all targets currently in the database.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_targets_targetnamespace_with_http_info(target_namespace, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str target_namespace: Target namespace (required)
        :param int offset: Offset for pagination. Default is **0**. When using this parameter, specify `limit` explicitly. The defaults might change. 
        :param int limit: Limit of returned items. By default, there is no limit as we need all targets in the UI. 
        :param str sort: Sort based on given field. Format: `attribute:direction`. `direction` is optional, default is **asc**. For example: `createdAt`, `updatedAt:desc`, `updatedAt:asc`. 
        :param str x_ip_address: Tells the original requester's IP address to this API. It is needed for moderation purposes. Explained more in [the IP addresses section of the API documentation](../docs/API#ip-addresses). This value is important and should always be included, but isn't strictly required by the API. 
        :param str x_author_id: **Warning:** this ID should be SAME across all services using this rating service. Tells the original requester's user ID. This is used to restrict some actions. For example author with ID `265` should not be able to modify rating created by user with ID `318`. This value is important and should always be included, but isn't strictly required by the API. 
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

        all_params = ['target_namespace', 'offset', 'limit', 'sort', 'x_ip_address', 'x_author_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_targets_targetnamespace" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'target_namespace' is set
        if self.api_client.client_side_validation and ('target_namespace' not in local_var_params or  # noqa: E501
                                                        local_var_params['target_namespace'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `target_namespace` when calling `get_targets_targetnamespace`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'target_namespace' in local_var_params:
            path_params['targetNamespace'] = local_var_params['target_namespace']  # noqa: E501

        query_params = []
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'sort' in local_var_params and local_var_params['sort'] is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501

        header_params = {}
        if 'x_ip_address' in local_var_params:
            header_params['x-ip-address'] = local_var_params['x_ip_address']  # noqa: E501
        if 'x_author_id' in local_var_params:
            header_params['x-author-id'] = local_var_params['x_author_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/csv'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyHeader', 'apiKeyQuery']  # noqa: E501

        return self.api_client.call_api(
            '/targets/{targetNamespace}', 'GET',
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
