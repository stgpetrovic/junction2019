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


class ItemBasketResponseBasket(object):
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
        'basket_id': 'str',
        'basket_short_id': 'str',
        'date': 'str',
        'time': 'str',
        'store': 'ItemBasketResponseBasketStore',
        'items': 'ItemBasketResponseBasketItems'
    }

    attribute_map = {
        'basket_id': 'BasketId',
        'basket_short_id': 'BasketShortId',
        'date': 'Date',
        'time': 'Time',
        'store': 'Store',
        'items': 'Items'
    }

    def __init__(self, basket_id=None, basket_short_id=None, date=None, time=None, store=None, items=None, local_vars_configuration=None):  # noqa: E501
        """ItemBasketResponseBasket - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._basket_id = None
        self._basket_short_id = None
        self._date = None
        self._time = None
        self._store = None
        self._items = None
        self.discriminator = None

        if basket_id is not None:
            self.basket_id = basket_id
        if basket_short_id is not None:
            self.basket_short_id = basket_short_id
        if date is not None:
            self.date = date
        if time is not None:
            self.time = time
        if store is not None:
            self.store = store
        if items is not None:
            self.items = items

    @property
    def basket_id(self):
        """Gets the basket_id of this ItemBasketResponseBasket.  # noqa: E501


        :return: The basket_id of this ItemBasketResponseBasket.  # noqa: E501
        :rtype: str
        """
        return self._basket_id

    @basket_id.setter
    def basket_id(self, basket_id):
        """Sets the basket_id of this ItemBasketResponseBasket.


        :param basket_id: The basket_id of this ItemBasketResponseBasket.  # noqa: E501
        :type: str
        """

        self._basket_id = basket_id

    @property
    def basket_short_id(self):
        """Gets the basket_short_id of this ItemBasketResponseBasket.  # noqa: E501


        :return: The basket_short_id of this ItemBasketResponseBasket.  # noqa: E501
        :rtype: str
        """
        return self._basket_short_id

    @basket_short_id.setter
    def basket_short_id(self, basket_short_id):
        """Sets the basket_short_id of this ItemBasketResponseBasket.


        :param basket_short_id: The basket_short_id of this ItemBasketResponseBasket.  # noqa: E501
        :type: str
        """

        self._basket_short_id = basket_short_id

    @property
    def date(self):
        """Gets the date of this ItemBasketResponseBasket.  # noqa: E501


        :return: The date of this ItemBasketResponseBasket.  # noqa: E501
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this ItemBasketResponseBasket.


        :param date: The date of this ItemBasketResponseBasket.  # noqa: E501
        :type: str
        """

        self._date = date

    @property
    def time(self):
        """Gets the time of this ItemBasketResponseBasket.  # noqa: E501


        :return: The time of this ItemBasketResponseBasket.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ItemBasketResponseBasket.


        :param time: The time of this ItemBasketResponseBasket.  # noqa: E501
        :type: str
        """

        self._time = time

    @property
    def store(self):
        """Gets the store of this ItemBasketResponseBasket.  # noqa: E501


        :return: The store of this ItemBasketResponseBasket.  # noqa: E501
        :rtype: ItemBasketResponseBasketStore
        """
        return self._store

    @store.setter
    def store(self, store):
        """Sets the store of this ItemBasketResponseBasket.


        :param store: The store of this ItemBasketResponseBasket.  # noqa: E501
        :type: ItemBasketResponseBasketStore
        """

        self._store = store

    @property
    def items(self):
        """Gets the items of this ItemBasketResponseBasket.  # noqa: E501


        :return: The items of this ItemBasketResponseBasket.  # noqa: E501
        :rtype: ItemBasketResponseBasketItems
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ItemBasketResponseBasket.


        :param items: The items of this ItemBasketResponseBasket.  # noqa: E501
        :type: ItemBasketResponseBasketItems
        """

        self._items = items

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
        if not isinstance(other, ItemBasketResponseBasket):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemBasketResponseBasket):
            return True

        return self.to_dict() != other.to_dict()
