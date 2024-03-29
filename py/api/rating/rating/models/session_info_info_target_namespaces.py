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


class SessionInfoInfoTargetNamespaces(object):
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
        'id': 'str'
    }

    attribute_map = {
        'id': 'id'
    }

    def __init__(self, id=None, local_vars_configuration=None):  # noqa: E501
        """SessionInfoInfoTargetNamespaces - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self.discriminator = None

        if id is not None:
            self.id = id

    @property
    def id(self):
        """Gets the id of this SessionInfoInfoTargetNamespaces.  # noqa: E501

        Namespace of the rating targets. This is provided because external services might have targets with collisioning IDs. For example service A might have product with id 1, and service B product with also id 1. This attribute makes it possible to separate those two products. All external service which use this API should agree on unique namespaces. For example all food products register could have namespace: `food-products`.   # noqa: E501

        :return: The id of this SessionInfoInfoTargetNamespaces.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SessionInfoInfoTargetNamespaces.

        Namespace of the rating targets. This is provided because external services might have targets with collisioning IDs. For example service A might have product with id 1, and service B product with also id 1. This attribute makes it possible to separate those two products. All external service which use this API should agree on unique namespaces. For example all food products register could have namespace: `food-products`.   # noqa: E501

        :param id: The id of this SessionInfoInfoTargetNamespaces.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) > 64):
            raise ValueError("Invalid value for `id`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) < 1):
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and not re.search(r'[A-Za-z0-9\-_]', id)):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/[A-Za-z0-9\-_]/`")  # noqa: E501

        self._id = id

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
        if not isinstance(other, SessionInfoInfoTargetNamespaces):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SessionInfoInfoTargetNamespaces):
            return True

        return self.to_dict() != other.to_dict()
