# coding: utf-8

"""
    Pricing & Availability API

    Pricing & Availability API is a REST-like API which integrates to POS and knows up to date pricing and product availability data for each store. This service can also be used to create and fill temporary shopping baskets, that are kept for 24 hours before they are automatically deleted.    **NOTE:** The API returns money in the responses. You should NOT use that data for actual payment transactions. They are only meant for displaying purposes, but they should work well enough for hackathon purposes.    API requests are only served over HTTPS, using TLS 1.0, 1.1, and 1.2. Requests will not be honored over plaintext HTTP.    Use of `accept: application/json` and `content-type: application/json` headers is required when applicable.    The API uses UTF-8 character encoding for all responses. Some fields may include characters that are not in the ASCII range.    Authentication is accomplished by providing `Ocp-Apim-Subscription-Key` header with your subscription key as the value.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pricing
from pricing.models.product_texts import ProductTexts  # noqa: E501
from pricing.rest import ApiException


class TestProductTexts(unittest.TestCase):
    """ProductTexts unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProductTexts(self):
        """Test ProductTexts"""
        # FIXME: construct object with mandatory attributes with example values
        # model = pricing.models.product_texts.ProductTexts()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
