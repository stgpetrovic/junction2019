# coding: utf-8

"""
    Ratings API

    Service which holds ratings of various targets, like recipes.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from api.rating.rating.configuration import Configuration


class RatingSummaryDistributions(object):
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
        'main': 'RatingSummaryDistribution',
        'hilarity': 'RatingSummaryDistribution',
        'usefulness': 'RatingSummaryDistribution'
    }

    attribute_map = {
        'main': 'main',
        'hilarity': 'hilarity',
        'usefulness': 'usefulness'
    }

    def __init__(self, main=None, hilarity=None, usefulness=None, local_vars_configuration=None):  # noqa: E501
        """RatingSummaryDistributions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._main = None
        self._hilarity = None
        self._usefulness = None
        self.discriminator = None

        if main is not None:
            self.main = main
        if hilarity is not None:
            self.hilarity = hilarity
        if usefulness is not None:
            self.usefulness = usefulness

    @property
    def main(self):
        """Gets the main of this RatingSummaryDistributions.  # noqa: E501


        :return: The main of this RatingSummaryDistributions.  # noqa: E501
        :rtype: RatingSummaryDistribution
        """
        return self._main

    @main.setter
    def main(self, main):
        """Sets the main of this RatingSummaryDistributions.


        :param main: The main of this RatingSummaryDistributions.  # noqa: E501
        :type: RatingSummaryDistribution
        """

        self._main = main

    @property
    def hilarity(self):
        """Gets the hilarity of this RatingSummaryDistributions.  # noqa: E501


        :return: The hilarity of this RatingSummaryDistributions.  # noqa: E501
        :rtype: RatingSummaryDistribution
        """
        return self._hilarity

    @hilarity.setter
    def hilarity(self, hilarity):
        """Sets the hilarity of this RatingSummaryDistributions.


        :param hilarity: The hilarity of this RatingSummaryDistributions.  # noqa: E501
        :type: RatingSummaryDistribution
        """

        self._hilarity = hilarity

    @property
    def usefulness(self):
        """Gets the usefulness of this RatingSummaryDistributions.  # noqa: E501


        :return: The usefulness of this RatingSummaryDistributions.  # noqa: E501
        :rtype: RatingSummaryDistribution
        """
        return self._usefulness

    @usefulness.setter
    def usefulness(self, usefulness):
        """Sets the usefulness of this RatingSummaryDistributions.


        :param usefulness: The usefulness of this RatingSummaryDistributions.  # noqa: E501
        :type: RatingSummaryDistribution
        """

        self._usefulness = usefulness

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
        if not isinstance(other, RatingSummaryDistributions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RatingSummaryDistributions):
            return True

        return self.to_dict() != other.to_dict()