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


class ExportsPost201ApplicationJsonResponse(object):
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
        'id': 'int',
        'status': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt'
    }

    def __init__(self, id=None, status=None, created_at=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """ExportsPost201ApplicationJsonResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this ExportsPost201ApplicationJsonResponse.  # noqa: E501


        :return: The id of this ExportsPost201ApplicationJsonResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExportsPost201ApplicationJsonResponse.


        :param id: The id of this ExportsPost201ApplicationJsonResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def status(self):
        """Gets the status of this ExportsPost201ApplicationJsonResponse.  # noqa: E501

        Task status  # noqa: E501

        :return: The status of this ExportsPost201ApplicationJsonResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ExportsPost201ApplicationJsonResponse.

        Task status  # noqa: E501

        :param status: The status of this ExportsPost201ApplicationJsonResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["IN_QUEUE", "PROCESSING", "DONE", "ERROR"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this ExportsPost201ApplicationJsonResponse.  # noqa: E501

        Created at timestamp  # noqa: E501

        :return: The created_at of this ExportsPost201ApplicationJsonResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ExportsPost201ApplicationJsonResponse.

        Created at timestamp  # noqa: E501

        :param created_at: The created_at of this ExportsPost201ApplicationJsonResponse.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ExportsPost201ApplicationJsonResponse.  # noqa: E501

        Updated at timestamp  # noqa: E501

        :return: The updated_at of this ExportsPost201ApplicationJsonResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ExportsPost201ApplicationJsonResponse.

        Updated at timestamp  # noqa: E501

        :param updated_at: The updated_at of this ExportsPost201ApplicationJsonResponse.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

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
        if not isinstance(other, ExportsPost201ApplicationJsonResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExportsPost201ApplicationJsonResponse):
            return True

        return self.to_dict() != other.to_dict()
