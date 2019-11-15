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

from api.search.search.configuration import Configuration


class ProductLabelName(object):
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
        'id': 'str',
        'finnish': 'str',
        'swedish': 'str',
        'english': 'str'
    }

    attribute_map = {
        'id': 'id',
        'finnish': 'finnish',
        'swedish': 'swedish',
        'english': 'english'
    }

    def __init__(self, id=None, finnish=None, swedish=None, english=None, local_vars_configuration=None):  # noqa: E501
        """ProductLabelName - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._finnish = None
        self._swedish = None
        self._english = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if finnish is not None:
            self.finnish = finnish
        if swedish is not None:
            self.swedish = swedish
        if english is not None:
            self.english = english

    @property
    def id(self):
        """Gets the id of this ProductLabelName.  # noqa: E501

        ID of the value in question. Only used with `category` and `subcategory`.   # noqa: E501

        :return: The id of this ProductLabelName.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProductLabelName.

        ID of the value in question. Only used with `category` and `subcategory`.   # noqa: E501

        :param id: The id of this ProductLabelName.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def finnish(self):
        """Gets the finnish of this ProductLabelName.  # noqa: E501

        Attribute value in Finnish  # noqa: E501

        :return: The finnish of this ProductLabelName.  # noqa: E501
        :rtype: str
        """
        return self._finnish

    @finnish.setter
    def finnish(self, finnish):
        """Sets the finnish of this ProductLabelName.

        Attribute value in Finnish  # noqa: E501

        :param finnish: The finnish of this ProductLabelName.  # noqa: E501
        :type: str
        """

        self._finnish = finnish

    @property
    def swedish(self):
        """Gets the swedish of this ProductLabelName.  # noqa: E501

        Attribute value in Swedish  # noqa: E501

        :return: The swedish of this ProductLabelName.  # noqa: E501
        :rtype: str
        """
        return self._swedish

    @swedish.setter
    def swedish(self, swedish):
        """Sets the swedish of this ProductLabelName.

        Attribute value in Swedish  # noqa: E501

        :param swedish: The swedish of this ProductLabelName.  # noqa: E501
        :type: str
        """

        self._swedish = swedish

    @property
    def english(self):
        """Gets the english of this ProductLabelName.  # noqa: E501

        Attribute value in English  # noqa: E501

        :return: The english of this ProductLabelName.  # noqa: E501
        :rtype: str
        """
        return self._english

    @english.setter
    def english(self, english):
        """Sets the english of this ProductLabelName.

        Attribute value in English  # noqa: E501

        :param english: The english of this ProductLabelName.  # noqa: E501
        :type: str
        """

        self._english = english

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
        if not isinstance(other, ProductLabelName):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductLabelName):
            return True

        return self.to_dict() != other.to_dict()
