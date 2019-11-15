# coding: utf-8

"""
    Search API

    Search API is a REST-like API which wraps the underlying ElasticSearch service for most common use cases. While this API is called the \"search\" service, in practice it acts as the main data engine for various Kesko services, providing high performance endpoints for fetching recipe, product, offer, store and article data.    API requests are only served over HTTPS, using TLS 1.0, 1.1, and 1.2. Requests will not be honored over plaintext HTTP.    Use of `accept: application/json` and `content-type: application/json` headers is required when applicable.    The API uses UTF-8 character encoding for all responses. Some fields may include characters that are not in the ASCII range.    As every other Kesko API service in this hackathon, authentication is accomplished by providing `Ocp-Apim-Subscription-Key` header with your subscription key as the value.    Submitting excessive requests to the server may result in a HTTP 429 Too Many Requests status code and temporary limitations to your Subscription. We kindly ask that you to limit the concurrency of your requests and/or insert 50 – 100 milliseconds of delay between the requests you send to the server. (i.e., 10 requests per second on average), since this environment doesn't run with the same specs as the real production instance.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.models.search_mixed_get200_application_json_response import SearchMixedGet200ApplicationJsonResponse  # noqa: E501
from openapi_client.rest import ApiException


class TestSearchMixedGet200ApplicationJsonResponse(unittest.TestCase):
    """SearchMixedGet200ApplicationJsonResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSearchMixedGet200ApplicationJsonResponse(self):
        """Test SearchMixedGet200ApplicationJsonResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = openapi_client.models.search_mixed_get200_application_json_response.SearchMixedGet200ApplicationJsonResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
