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

from openapi_client.configuration import Configuration


class SessionInfo(object):
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
        'info': 'SessionInfoInfo',
        'type': 'str',
        'user_role': 'str'
    }

    attribute_map = {
        'info': 'info',
        'type': 'type',
        'user_role': 'userRole'
    }

    def __init__(self, info=None, type=None, user_role=None, local_vars_configuration=None):  # noqa: E501
        """SessionInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._info = None
        self._type = None
        self._user_role = None
        self.discriminator = None

        if info is not None:
            self.info = info
        if type is not None:
            self.type = type
        if user_role is not None:
            self.user_role = user_role

    @property
    def info(self):
        """Gets the info of this SessionInfo.  # noqa: E501


        :return: The info of this SessionInfo.  # noqa: E501
        :rtype: SessionInfoInfo
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this SessionInfo.


        :param info: The info of this SessionInfo.  # noqa: E501
        :type: SessionInfoInfo
        """

        self._info = info

    @property
    def type(self):
        """Gets the type of this SessionInfo.  # noqa: E501


        :return: The type of this SessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SessionInfo.


        :param type: The type of this SessionInfo.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def user_role(self):
        """Gets the user_role of this SessionInfo.  # noqa: E501


        :return: The user_role of this SessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._user_role

    @user_role.setter
    def user_role(self, user_role):
        """Sets the user_role of this SessionInfo.


        :param user_role: The user_role of this SessionInfo.  # noqa: E501
        :type: str
        """

        self._user_role = user_role

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
        if not isinstance(other, SessionInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SessionInfo):
            return True

        return self.to_dict() != other.to_dict()
