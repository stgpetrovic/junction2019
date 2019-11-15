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


class RecipePreparationTimeTimeRange(object):
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
        'min_time': 'int',
        'max_time': 'int'
    }

    attribute_map = {
        'min_time': 'MinTime',
        'max_time': 'MaxTime'
    }

    def __init__(self, min_time=None, max_time=None, local_vars_configuration=None):  # noqa: E501
        """RecipePreparationTimeTimeRange - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._min_time = None
        self._max_time = None
        self.discriminator = None

        if min_time is not None:
            self.min_time = min_time
        if max_time is not None:
            self.max_time = max_time

    @property
    def min_time(self):
        """Gets the min_time of this RecipePreparationTimeTimeRange.  # noqa: E501


        :return: The min_time of this RecipePreparationTimeTimeRange.  # noqa: E501
        :rtype: int
        """
        return self._min_time

    @min_time.setter
    def min_time(self, min_time):
        """Sets the min_time of this RecipePreparationTimeTimeRange.


        :param min_time: The min_time of this RecipePreparationTimeTimeRange.  # noqa: E501
        :type: int
        """

        self._min_time = min_time

    @property
    def max_time(self):
        """Gets the max_time of this RecipePreparationTimeTimeRange.  # noqa: E501


        :return: The max_time of this RecipePreparationTimeTimeRange.  # noqa: E501
        :rtype: int
        """
        return self._max_time

    @max_time.setter
    def max_time(self, max_time):
        """Sets the max_time of this RecipePreparationTimeTimeRange.


        :param max_time: The max_time of this RecipePreparationTimeTimeRange.  # noqa: E501
        :type: int
        """

        self._max_time = max_time

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
        if not isinstance(other, RecipePreparationTimeTimeRange):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecipePreparationTimeTimeRange):
            return True

        return self.to_dict() != other.to_dict()
