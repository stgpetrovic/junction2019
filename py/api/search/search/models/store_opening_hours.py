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


class StoreOpeningHours(object):
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
        'date': 'str',
        'opens': 'str',
        'closes': 'str',
        'state': 'str',
        'description': 'str'
    }

    attribute_map = {
        'date': 'Date',
        'opens': 'Opens',
        'closes': 'Closes',
        'state': 'State',
        'description': 'Description'
    }

    def __init__(self, date=None, opens=None, closes=None, state=None, description=None, local_vars_configuration=None):  # noqa: E501
        """StoreOpeningHours - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._date = None
        self._opens = None
        self._closes = None
        self._state = None
        self._description = None
        self.discriminator = None

        self.date = date
        self.opens = opens
        self.closes = closes
        self.state = state
        if description is not None:
            self.description = description

    @property
    def date(self):
        """Gets the date of this StoreOpeningHours.  # noqa: E501


        :return: The date of this StoreOpeningHours.  # noqa: E501
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this StoreOpeningHours.


        :param date: The date of this StoreOpeningHours.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and date is None:  # noqa: E501
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

    @property
    def opens(self):
        """Gets the opens of this StoreOpeningHours.  # noqa: E501

        Opening time  # noqa: E501

        :return: The opens of this StoreOpeningHours.  # noqa: E501
        :rtype: str
        """
        return self._opens

    @opens.setter
    def opens(self, opens):
        """Sets the opens of this StoreOpeningHours.

        Opening time  # noqa: E501

        :param opens: The opens of this StoreOpeningHours.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and opens is None:  # noqa: E501
            raise ValueError("Invalid value for `opens`, must not be `None`")  # noqa: E501

        self._opens = opens

    @property
    def closes(self):
        """Gets the closes of this StoreOpeningHours.  # noqa: E501

        Closing time  # noqa: E501

        :return: The closes of this StoreOpeningHours.  # noqa: E501
        :rtype: str
        """
        return self._closes

    @closes.setter
    def closes(self, closes):
        """Sets the closes of this StoreOpeningHours.

        Closing time  # noqa: E501

        :param closes: The closes of this StoreOpeningHours.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and closes is None:  # noqa: E501
            raise ValueError("Invalid value for `closes`, must not be `None`")  # noqa: E501

        self._closes = closes

    @property
    def state(self):
        """Gets the state of this StoreOpeningHours.  # noqa: E501


        :return: The state of this StoreOpeningHours.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this StoreOpeningHours.


        :param state: The state of this StoreOpeningHours.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and state is None:  # noqa: E501
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["Open", "Closed", "NotAvailable"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def description(self):
        """Gets the description of this StoreOpeningHours.  # noqa: E501

        Information about exceptional opening hours.  # noqa: E501

        :return: The description of this StoreOpeningHours.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StoreOpeningHours.

        Information about exceptional opening hours.  # noqa: E501

        :param description: The description of this StoreOpeningHours.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if not isinstance(other, StoreOpeningHours):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StoreOpeningHours):
            return True

        return self.to_dict() != other.to_dict()