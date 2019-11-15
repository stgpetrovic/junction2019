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


class ProductV3AllOf(object):
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
        'ean': 'str',
        'name': 'str',
        'price': 'float',
        'total_price': 'float',
        'unit_price': 'float',
        'pricing_unit': 'str',
        'package_unit': 'str',
        'package_size': 'str',
        'package_type': 'str',
        'cost_center_id': 'str',
        'discount_limited': 'bool',
        'plussa_limited': 'bool',
        'type': 'str',
        'vat': 'float',
        'group': 'str',
        'size': 'ProductSize',
        'texts': 'list[ProductTexts]',
        'restrictions': 'ProductRestrictions',
        'components': 'list[BasketItemItemComponents]'
    }

    attribute_map = {
        'ean': 'ean',
        'name': 'name',
        'price': 'price',
        'total_price': 'totalPrice',
        'unit_price': 'unitPrice',
        'pricing_unit': 'pricingUnit',
        'package_unit': 'packageUnit',
        'package_size': 'packageSize',
        'package_type': 'packageType',
        'cost_center_id': 'costCenterId',
        'discount_limited': 'discountLimited',
        'plussa_limited': 'plussaLimited',
        'type': 'type',
        'vat': 'vat',
        'group': 'group',
        'size': 'size',
        'texts': 'texts',
        'restrictions': 'restrictions',
        'components': 'components'
    }

    def __init__(self, ean=None, name=None, price=None, total_price=None, unit_price=None, pricing_unit=None, package_unit=None, package_size=None, package_type=None, cost_center_id=None, discount_limited=None, plussa_limited=None, type=None, vat=None, group=None, size=None, texts=None, restrictions=None, components=None, local_vars_configuration=None):  # noqa: E501
        """ProductV3AllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ean = None
        self._name = None
        self._price = None
        self._total_price = None
        self._unit_price = None
        self._pricing_unit = None
        self._package_unit = None
        self._package_size = None
        self._package_type = None
        self._cost_center_id = None
        self._discount_limited = None
        self._plussa_limited = None
        self._type = None
        self._vat = None
        self._group = None
        self._size = None
        self._texts = None
        self._restrictions = None
        self._components = None
        self.discriminator = None

        self.ean = ean
        self.name = name
        if price is not None:
            self.price = price
        if total_price is not None:
            self.total_price = total_price
        if unit_price is not None:
            self.unit_price = unit_price
        if pricing_unit is not None:
            self.pricing_unit = pricing_unit
        if package_unit is not None:
            self.package_unit = package_unit
        if package_size is not None:
            self.package_size = package_size
        if package_type is not None:
            self.package_type = package_type
        if cost_center_id is not None:
            self.cost_center_id = cost_center_id
        if discount_limited is not None:
            self.discount_limited = discount_limited
        if plussa_limited is not None:
            self.plussa_limited = plussa_limited
        if type is not None:
            self.type = type
        if vat is not None:
            self.vat = vat
        if group is not None:
            self.group = group
        if size is not None:
            self.size = size
        if texts is not None:
            self.texts = texts
        if restrictions is not None:
            self.restrictions = restrictions
        if components is not None:
            self.components = components

    @property
    def ean(self):
        """Gets the ean of this ProductV3AllOf.  # noqa: E501


        :return: The ean of this ProductV3AllOf.  # noqa: E501
        :rtype: str
        """
        return self._ean

    @ean.setter
    def ean(self, ean):
        """Sets the ean of this ProductV3AllOf.


        :param ean: The ean of this ProductV3AllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and ean is None:  # noqa: E501
            raise ValueError("Invalid value for `ean`, must not be `None`")  # noqa: E501

        self._ean = ean

    @property
    def name(self):
        """Gets the name of this ProductV3AllOf.  # noqa: E501


        :return: The name of this ProductV3AllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductV3AllOf.


        :param name: The name of this ProductV3AllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def price(self):
        """Gets the price of this ProductV3AllOf.  # noqa: E501


        :return: The price of this ProductV3AllOf.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this ProductV3AllOf.


        :param price: The price of this ProductV3AllOf.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def total_price(self):
        """Gets the total_price of this ProductV3AllOf.  # noqa: E501


        :return: The total_price of this ProductV3AllOf.  # noqa: E501
        :rtype: float
        """
        return self._total_price

    @total_price.setter
    def total_price(self, total_price):
        """Sets the total_price of this ProductV3AllOf.


        :param total_price: The total_price of this ProductV3AllOf.  # noqa: E501
        :type: float
        """

        self._total_price = total_price

    @property
    def unit_price(self):
        """Gets the unit_price of this ProductV3AllOf.  # noqa: E501


        :return: The unit_price of this ProductV3AllOf.  # noqa: E501
        :rtype: float
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this ProductV3AllOf.


        :param unit_price: The unit_price of this ProductV3AllOf.  # noqa: E501
        :type: float
        """

        self._unit_price = unit_price

    @property
    def pricing_unit(self):
        """Gets the pricing_unit of this ProductV3AllOf.  # noqa: E501

        Unit for the product price  # noqa: E501

        :return: The pricing_unit of this ProductV3AllOf.  # noqa: E501
        :rtype: str
        """
        return self._pricing_unit

    @pricing_unit.setter
    def pricing_unit(self, pricing_unit):
        """Sets the pricing_unit of this ProductV3AllOf.

        Unit for the product price  # noqa: E501

        :param pricing_unit: The pricing_unit of this ProductV3AllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["kg", "m", "l", "kpl", "g", "dl", "cl", "ml", "tlk"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and pricing_unit not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `pricing_unit` ({0}), must be one of {1}"  # noqa: E501
                .format(pricing_unit, allowed_values)
            )

        self._pricing_unit = pricing_unit

    @property
    def package_unit(self):
        """Gets the package_unit of this ProductV3AllOf.  # noqa: E501

        Unit for packaging size  # noqa: E501

        :return: The package_unit of this ProductV3AllOf.  # noqa: E501
        :rtype: str
        """
        return self._package_unit

    @package_unit.setter
    def package_unit(self, package_unit):
        """Sets the package_unit of this ProductV3AllOf.

        Unit for packaging size  # noqa: E501

        :param package_unit: The package_unit of this ProductV3AllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["kg", "m", "l", "kpl", "g", "dl", "cl", "ml", "tlk"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and package_unit not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `package_unit` ({0}), must be one of {1}"  # noqa: E501
                .format(package_unit, allowed_values)
            )

        self._package_unit = package_unit

    @property
    def package_size(self):
        """Gets the package_size of this ProductV3AllOf.  # noqa: E501

        Package size, numeric value returned as a string  # noqa: E501

        :return: The package_size of this ProductV3AllOf.  # noqa: E501
        :rtype: str
        """
        return self._package_size

    @package_size.setter
    def package_size(self, package_size):
        """Sets the package_size of this ProductV3AllOf.

        Package size, numeric value returned as a string  # noqa: E501

        :param package_size: The package_size of this ProductV3AllOf.  # noqa: E501
        :type: str
        """

        self._package_size = package_size

    @property
    def package_type(self):
        """Gets the package_type of this ProductV3AllOf.  # noqa: E501

        Freeform field describing the package type  # noqa: E501

        :return: The package_type of this ProductV3AllOf.  # noqa: E501
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """Sets the package_type of this ProductV3AllOf.

        Freeform field describing the package type  # noqa: E501

        :param package_type: The package_type of this ProductV3AllOf.  # noqa: E501
        :type: str
        """

        self._package_type = package_type

    @property
    def cost_center_id(self):
        """Gets the cost_center_id of this ProductV3AllOf.  # noqa: E501

        Cost center ID for the product  # noqa: E501

        :return: The cost_center_id of this ProductV3AllOf.  # noqa: E501
        :rtype: str
        """
        return self._cost_center_id

    @cost_center_id.setter
    def cost_center_id(self, cost_center_id):
        """Sets the cost_center_id of this ProductV3AllOf.

        Cost center ID for the product  # noqa: E501

        :param cost_center_id: The cost_center_id of this ProductV3AllOf.  # noqa: E501
        :type: str
        """

        self._cost_center_id = cost_center_id

    @property
    def discount_limited(self):
        """Gets the discount_limited of this ProductV3AllOf.  # noqa: E501

        Is the product exempt from discounts  # noqa: E501

        :return: The discount_limited of this ProductV3AllOf.  # noqa: E501
        :rtype: bool
        """
        return self._discount_limited

    @discount_limited.setter
    def discount_limited(self, discount_limited):
        """Sets the discount_limited of this ProductV3AllOf.

        Is the product exempt from discounts  # noqa: E501

        :param discount_limited: The discount_limited of this ProductV3AllOf.  # noqa: E501
        :type: bool
        """

        self._discount_limited = discount_limited

    @property
    def plussa_limited(self):
        """Gets the plussa_limited of this ProductV3AllOf.  # noqa: E501

        Is the product exempt from Plussa discounts  # noqa: E501

        :return: The plussa_limited of this ProductV3AllOf.  # noqa: E501
        :rtype: bool
        """
        return self._plussa_limited

    @plussa_limited.setter
    def plussa_limited(self, plussa_limited):
        """Sets the plussa_limited of this ProductV3AllOf.

        Is the product exempt from Plussa discounts  # noqa: E501

        :param plussa_limited: The plussa_limited of this ProductV3AllOf.  # noqa: E501
        :type: bool
        """

        self._plussa_limited = plussa_limited

    @property
    def type(self):
        """Gets the type of this ProductV3AllOf.  # noqa: E501

        Product type. For Citymarket stores products vary between utility and consumer goods. For non-Citymarket stores, all products are considered consumer goods.   # noqa: E501

        :return: The type of this ProductV3AllOf.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProductV3AllOf.

        Product type. For Citymarket stores products vary between utility and consumer goods. For non-Citymarket stores, all products are considered consumer goods.   # noqa: E501

        :param type: The type of this ProductV3AllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["CONSUMER_GOOD", "UTILITY_GOOD"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def vat(self):
        """Gets the vat of this ProductV3AllOf.  # noqa: E501


        :return: The vat of this ProductV3AllOf.  # noqa: E501
        :rtype: float
        """
        return self._vat

    @vat.setter
    def vat(self, vat):
        """Sets the vat of this ProductV3AllOf.


        :param vat: The vat of this ProductV3AllOf.  # noqa: E501
        :type: float
        """

        self._vat = vat

    @property
    def group(self):
        """Gets the group of this ProductV3AllOf.  # noqa: E501


        :return: The group of this ProductV3AllOf.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this ProductV3AllOf.


        :param group: The group of this ProductV3AllOf.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def size(self):
        """Gets the size of this ProductV3AllOf.  # noqa: E501


        :return: The size of this ProductV3AllOf.  # noqa: E501
        :rtype: ProductSize
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ProductV3AllOf.


        :param size: The size of this ProductV3AllOf.  # noqa: E501
        :type: ProductSize
        """

        self._size = size

    @property
    def texts(self):
        """Gets the texts of this ProductV3AllOf.  # noqa: E501


        :return: The texts of this ProductV3AllOf.  # noqa: E501
        :rtype: list[ProductTexts]
        """
        return self._texts

    @texts.setter
    def texts(self, texts):
        """Sets the texts of this ProductV3AllOf.


        :param texts: The texts of this ProductV3AllOf.  # noqa: E501
        :type: list[ProductTexts]
        """

        self._texts = texts

    @property
    def restrictions(self):
        """Gets the restrictions of this ProductV3AllOf.  # noqa: E501


        :return: The restrictions of this ProductV3AllOf.  # noqa: E501
        :rtype: ProductRestrictions
        """
        return self._restrictions

    @restrictions.setter
    def restrictions(self, restrictions):
        """Sets the restrictions of this ProductV3AllOf.


        :param restrictions: The restrictions of this ProductV3AllOf.  # noqa: E501
        :type: ProductRestrictions
        """

        self._restrictions = restrictions

    @property
    def components(self):
        """Gets the components of this ProductV3AllOf.  # noqa: E501


        :return: The components of this ProductV3AllOf.  # noqa: E501
        :rtype: list[BasketItemItemComponents]
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this ProductV3AllOf.


        :param components: The components of this ProductV3AllOf.  # noqa: E501
        :type: list[BasketItemItemComponents]
        """

        self._components = components

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
        if not isinstance(other, ProductV3AllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductV3AllOf):
            return True

        return self.to_dict() != other.to_dict()
