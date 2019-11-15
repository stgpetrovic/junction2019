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

from openapi_client.configuration import Configuration


class BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse(object):
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
        'long_id': 'str',
        'short_id': 'str',
        'store_id': 'str',
        'expires': 'datetime',
        'total_price': 'float',
        'token': 'str',
        'checkout_done': 'bool',
        'items': 'list[BasketItems]'
    }

    attribute_map = {
        'long_id': 'longId',
        'short_id': 'shortId',
        'store_id': 'storeId',
        'expires': 'expires',
        'total_price': 'totalPrice',
        'token': 'token',
        'checkout_done': 'checkoutDone',
        'items': 'items'
    }

    def __init__(self, long_id=None, short_id=None, store_id=None, expires=None, total_price=None, token=None, checkout_done=None, items=None, local_vars_configuration=None):  # noqa: E501
        """BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._long_id = None
        self._short_id = None
        self._store_id = None
        self._expires = None
        self._total_price = None
        self._token = None
        self._checkout_done = None
        self._items = None
        self.discriminator = None

        if long_id is not None:
            self.long_id = long_id
        if short_id is not None:
            self.short_id = short_id
        if store_id is not None:
            self.store_id = store_id
        if expires is not None:
            self.expires = expires
        if total_price is not None:
            self.total_price = total_price
        if token is not None:
            self.token = token
        if checkout_done is not None:
            self.checkout_done = checkout_done
        if items is not None:
            self.items = items

    @property
    def long_id(self):
        """Gets the long_id of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.  # noqa: E501

        Long or global id of the shopping basket. Equal to `{longBasketId}`. This is unique across the system.   # noqa: E501

        :return: The long_id of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.  # noqa: E501
        :rtype: str
        """
        return self._long_id

    @long_id.setter
    def long_id(self, long_id):
        """Sets the long_id of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.

        Long or global id of the shopping basket. Equal to `{longBasketId}`. This is unique across the system.   # noqa: E501

        :param long_id: The long_id of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.  # noqa: E501
        :type: str
        """

        self._long_id = long_id

    @property
    def short_id(self):
        """Gets the short_id of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.  # noqa: E501

        Shorter id of the shopping basket which must be convenient for users. **Note:** This is unique **per shop**, not globally unique.   # noqa: E501

        :return: The short_id of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.  # noqa: E501
        :rtype: str
        """
        return self._short_id

    @short_id.setter
    def short_id(self, short_id):
        """Sets the short_id of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.

        Shorter id of the shopping basket which must be convenient for users. **Note:** This is unique **per shop**, not globally unique.   # noqa: E501

        :param short_id: The short_id of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.  # noqa: E501
        :type: str
        """

        self._short_id = short_id

    @property
    def store_id(self):
        """Gets the store_id of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.  # noqa: E501


        :return: The store_id of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.


        :param store_id: The store_id of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.  # noqa: E501
        :type: str
        """

        self._store_id = store_id

    @property
    def expires(self):
        """Gets the expires of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.  # noqa: E501


        :return: The expires of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.


        :param expires: The expires of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.  # noqa: E501
        :type: datetime
        """

        self._expires = expires

    @property
    def total_price(self):
        """Gets the total_price of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.  # noqa: E501


        :return: The total_price of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.  # noqa: E501
        :rtype: float
        """
        return self._total_price

    @total_price.setter
    def total_price(self, total_price):
        """Sets the total_price of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.


        :param total_price: The total_price of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.  # noqa: E501
        :type: float
        """

        self._total_price = total_price

    @property
    def token(self):
        """Gets the token of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.  # noqa: E501


        :return: The token of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.


        :param token: The token of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def checkout_done(self):
        """Gets the checkout_done of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.  # noqa: E501


        :return: The checkout_done of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.  # noqa: E501
        :rtype: bool
        """
        return self._checkout_done

    @checkout_done.setter
    def checkout_done(self, checkout_done):
        """Sets the checkout_done of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.


        :param checkout_done: The checkout_done of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.  # noqa: E501
        :type: bool
        """

        self._checkout_done = checkout_done

    @property
    def items(self):
        """Gets the items of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.  # noqa: E501


        :return: The items of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.  # noqa: E501
        :rtype: list[BasketItems]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.


        :param items: The items of this BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse.  # noqa: E501
        :type: list[BasketItems]
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
        if not isinstance(other, BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BasketsLongBasketIdItemsItemIdDelete200ApplicationJsonResponse):
            return True

        return self.to_dict() != other.to_dict()
