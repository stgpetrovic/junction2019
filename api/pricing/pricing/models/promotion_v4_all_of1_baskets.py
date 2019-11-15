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


class PromotionV4AllOf1Baskets(object):
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
        'size': 'float',
        'base_eans': 'list[str]',
        'groups': 'list[str]'
    }

    attribute_map = {
        'size': 'size',
        'base_eans': 'baseEans',
        'groups': 'groups'
    }

    def __init__(self, size=None, base_eans=None, groups=None, local_vars_configuration=None):  # noqa: E501
        """PromotionV4AllOf1Baskets - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._size = None
        self._base_eans = None
        self._groups = None
        self.discriminator = None

        self.size = size
        if base_eans is not None:
            self.base_eans = base_eans
        if groups is not None:
            self.groups = groups

    @property
    def size(self):
        """Gets the size of this PromotionV4AllOf1Baskets.  # noqa: E501

        Basket size ie. how many items from this basket should be bought for promotion to be valid.   # noqa: E501

        :return: The size of this PromotionV4AllOf1Baskets.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this PromotionV4AllOf1Baskets.

        Basket size ie. how many items from this basket should be bought for promotion to be valid.   # noqa: E501

        :param size: The size of this PromotionV4AllOf1Baskets.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def base_eans(self):
        """Gets the base_eans of this PromotionV4AllOf1Baskets.  # noqa: E501

        Array of base EAN codes included in the basket  # noqa: E501

        :return: The base_eans of this PromotionV4AllOf1Baskets.  # noqa: E501
        :rtype: list[str]
        """
        return self._base_eans

    @base_eans.setter
    def base_eans(self, base_eans):
        """Sets the base_eans of this PromotionV4AllOf1Baskets.

        Array of base EAN codes included in the basket  # noqa: E501

        :param base_eans: The base_eans of this PromotionV4AllOf1Baskets.  # noqa: E501
        :type: list[str]
        """

        self._base_eans = base_eans

    @property
    def groups(self):
        """Gets the groups of this PromotionV4AllOf1Baskets.  # noqa: E501

        Array of product groups included in the basket  # noqa: E501

        :return: The groups of this PromotionV4AllOf1Baskets.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this PromotionV4AllOf1Baskets.

        Array of product groups included in the basket  # noqa: E501

        :param groups: The groups of this PromotionV4AllOf1Baskets.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

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
        if not isinstance(other, PromotionV4AllOf1Baskets):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PromotionV4AllOf1Baskets):
            return True

        return self.to_dict() != other.to_dict()
