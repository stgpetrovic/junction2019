# coding: utf-8

"""
    Pricing & Availability API

    Pricing & Availability API is a REST-like API which integrates to POS and knows up to date pricing and product availability data for each store. This service can also be used to create and fill temporary shopping baskets, that are kept for 24 hours before they are automatically deleted.    **NOTE:** The API returns money in the responses. You should NOT use that data for actual payment transactions. They are only meant for displaying purposes, but they should work well enough for hackathon purposes.    API requests are only served over HTTPS, using TLS 1.0, 1.1, and 1.2. Requests will not be honored over plaintext HTTP.    Use of `accept: application/json` and `content-type: application/json` headers is required when applicable.    The API uses UTF-8 character encoding for all responses. Some fields may include characters that are not in the ASCII range.    Authentication is accomplished by providing `Ocp-Apim-Subscription-Key` header with your subscription key as the value.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from api.pricing.pricing.configuration import Configuration


class ProductSize(object):
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
        'value': 'float',
        'unit': 'str'
    }

    attribute_map = {
        'value': 'value',
        'unit': 'unit'
    }

    def __init__(self, value=None, unit=None, local_vars_configuration=None):  # noqa: E501
        """ProductSize - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._value = None
        self._unit = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if unit is not None:
            self.unit = unit

    @property
    def value(self):
        """Gets the value of this ProductSize.  # noqa: E501


        :return: The value of this ProductSize.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ProductSize.


        :param value: The value of this ProductSize.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def unit(self):
        """Gets the unit of this ProductSize.  # noqa: E501


        :return: The unit of this ProductSize.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ProductSize.


        :param unit: The unit of this ProductSize.  # noqa: E501
        :type: str
        """

        self._unit = unit

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
        if not isinstance(other, ProductSize):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductSize):
            return True

        return self.to_dict() != other.to_dict()
