# coding: utf-8

"""
    Search API

    Search API is a REST-like API which wraps the underlying ElasticSearch service for most common use cases. While this API is called the \"search\" service, in practice it acts as the main data engine for various Kesko services, providing high performance endpoints for fetching recipe, product, offer, store and article data.    API requests are only served over HTTPS, using TLS 1.0, 1.1, and 1.2. Requests will not be honored over plaintext HTTP.    Use of `accept: application/json` and `content-type: application/json` headers is required when applicable.    The API uses UTF-8 character encoding for all responses. Some fields may include characters that are not in the ASCII range.    As every other Kesko API service in this hackathon, authentication is accomplished by providing `Ocp-Apim-Subscription-Key` header with your subscription key as the value.    Submitting excessive requests to the server may result in a HTTP 429 Too Many Requests status code and temporary limitations to your Subscription. We kindly ask that you to limit the concurrency of your requests and/or insert 50 – 100 milliseconds of delay between the requests you send to the server. (i.e., 10 requests per second on average), since this environment doesn't run with the same specs as the real production instance.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class SearchGroupedGet200ApplicationJsonResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'recipes': 'SearchGroupedGet200ApplicationJsonResponseRecipes',
        'stores': 'SearchGroupedGet200ApplicationJsonResponseStores',
        'products': 'SearchGroupedGet200ApplicationJsonResponseProducts',
        'articles': 'SearchGroupedGet200ApplicationJsonResponseArticles'
    }

    attribute_map = {
        'recipes': 'recipes',
        'stores': 'stores',
        'products': 'products',
        'articles': 'articles'
    }

    def __init__(self, recipes=None, stores=None, products=None, articles=None, local_vars_configuration=None):  # noqa: E501
        """SearchGroupedGet200ApplicationJsonResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._recipes = None
        self._stores = None
        self._products = None
        self._articles = None
        self.discriminator = None

        if recipes is not None:
            self.recipes = recipes
        if stores is not None:
            self.stores = stores
        if products is not None:
            self.products = products
        if articles is not None:
            self.articles = articles

    @property
    def recipes(self):
        """Gets the recipes of this SearchGroupedGet200ApplicationJsonResponse.  # noqa: E501


        :return: The recipes of this SearchGroupedGet200ApplicationJsonResponse.  # noqa: E501
        :rtype: SearchGroupedGet200ApplicationJsonResponseRecipes
        """
        return self._recipes

    @recipes.setter
    def recipes(self, recipes):
        """Sets the recipes of this SearchGroupedGet200ApplicationJsonResponse.


        :param recipes: The recipes of this SearchGroupedGet200ApplicationJsonResponse.  # noqa: E501
        :type: SearchGroupedGet200ApplicationJsonResponseRecipes
        """

        self._recipes = recipes

    @property
    def stores(self):
        """Gets the stores of this SearchGroupedGet200ApplicationJsonResponse.  # noqa: E501


        :return: The stores of this SearchGroupedGet200ApplicationJsonResponse.  # noqa: E501
        :rtype: SearchGroupedGet200ApplicationJsonResponseStores
        """
        return self._stores

    @stores.setter
    def stores(self, stores):
        """Sets the stores of this SearchGroupedGet200ApplicationJsonResponse.


        :param stores: The stores of this SearchGroupedGet200ApplicationJsonResponse.  # noqa: E501
        :type: SearchGroupedGet200ApplicationJsonResponseStores
        """

        self._stores = stores

    @property
    def products(self):
        """Gets the products of this SearchGroupedGet200ApplicationJsonResponse.  # noqa: E501


        :return: The products of this SearchGroupedGet200ApplicationJsonResponse.  # noqa: E501
        :rtype: SearchGroupedGet200ApplicationJsonResponseProducts
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this SearchGroupedGet200ApplicationJsonResponse.


        :param products: The products of this SearchGroupedGet200ApplicationJsonResponse.  # noqa: E501
        :type: SearchGroupedGet200ApplicationJsonResponseProducts
        """

        self._products = products

    @property
    def articles(self):
        """Gets the articles of this SearchGroupedGet200ApplicationJsonResponse.  # noqa: E501


        :return: The articles of this SearchGroupedGet200ApplicationJsonResponse.  # noqa: E501
        :rtype: SearchGroupedGet200ApplicationJsonResponseArticles
        """
        return self._articles

    @articles.setter
    def articles(self, articles):
        """Sets the articles of this SearchGroupedGet200ApplicationJsonResponse.


        :param articles: The articles of this SearchGroupedGet200ApplicationJsonResponse.  # noqa: E501
        :type: SearchGroupedGet200ApplicationJsonResponseArticles
        """

        self._articles = articles

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SearchGroupedGet200ApplicationJsonResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SearchGroupedGet200ApplicationJsonResponse):
            return True

        return self.to_dict() != other.to_dict()
