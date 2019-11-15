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


class RecipeOldSubHeadingIngredient(object):
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
        'name': 'list[str]',
        'ean': 'list[str]',
        'amount': 'list[IngredientOldAmount]',
        'amount_info': 'list[str]',
        'package_recipe': 'list[str]',
        'ingredient_type': 'list[str]'
    }

    attribute_map = {
        'name': 'Name',
        'ean': 'Ean',
        'amount': 'Amount',
        'amount_info': 'AmountInfo',
        'package_recipe': 'PackageRecipe',
        'ingredient_type': 'IngredientType'
    }

    def __init__(self, name=None, ean=None, amount=None, amount_info=None, package_recipe=None, ingredient_type=None, local_vars_configuration=None):  # noqa: E501
        """RecipeOldSubHeadingIngredient - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._ean = None
        self._amount = None
        self._amount_info = None
        self._package_recipe = None
        self._ingredient_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if ean is not None:
            self.ean = ean
        if amount is not None:
            self.amount = amount
        if amount_info is not None:
            self.amount_info = amount_info
        if package_recipe is not None:
            self.package_recipe = package_recipe
        if ingredient_type is not None:
            self.ingredient_type = ingredient_type

    @property
    def name(self):
        """Gets the name of this RecipeOldSubHeadingIngredient.  # noqa: E501


        :return: The name of this RecipeOldSubHeadingIngredient.  # noqa: E501
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RecipeOldSubHeadingIngredient.


        :param name: The name of this RecipeOldSubHeadingIngredient.  # noqa: E501
        :type: list[str]
        """

        self._name = name

    @property
    def ean(self):
        """Gets the ean of this RecipeOldSubHeadingIngredient.  # noqa: E501


        :return: The ean of this RecipeOldSubHeadingIngredient.  # noqa: E501
        :rtype: list[str]
        """
        return self._ean

    @ean.setter
    def ean(self, ean):
        """Sets the ean of this RecipeOldSubHeadingIngredient.


        :param ean: The ean of this RecipeOldSubHeadingIngredient.  # noqa: E501
        :type: list[str]
        """

        self._ean = ean

    @property
    def amount(self):
        """Gets the amount of this RecipeOldSubHeadingIngredient.  # noqa: E501


        :return: The amount of this RecipeOldSubHeadingIngredient.  # noqa: E501
        :rtype: list[IngredientOldAmount]
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this RecipeOldSubHeadingIngredient.


        :param amount: The amount of this RecipeOldSubHeadingIngredient.  # noqa: E501
        :type: list[IngredientOldAmount]
        """

        self._amount = amount

    @property
    def amount_info(self):
        """Gets the amount_info of this RecipeOldSubHeadingIngredient.  # noqa: E501


        :return: The amount_info of this RecipeOldSubHeadingIngredient.  # noqa: E501
        :rtype: list[str]
        """
        return self._amount_info

    @amount_info.setter
    def amount_info(self, amount_info):
        """Sets the amount_info of this RecipeOldSubHeadingIngredient.


        :param amount_info: The amount_info of this RecipeOldSubHeadingIngredient.  # noqa: E501
        :type: list[str]
        """

        self._amount_info = amount_info

    @property
    def package_recipe(self):
        """Gets the package_recipe of this RecipeOldSubHeadingIngredient.  # noqa: E501


        :return: The package_recipe of this RecipeOldSubHeadingIngredient.  # noqa: E501
        :rtype: list[str]
        """
        return self._package_recipe

    @package_recipe.setter
    def package_recipe(self, package_recipe):
        """Sets the package_recipe of this RecipeOldSubHeadingIngredient.


        :param package_recipe: The package_recipe of this RecipeOldSubHeadingIngredient.  # noqa: E501
        :type: list[str]
        """

        self._package_recipe = package_recipe

    @property
    def ingredient_type(self):
        """Gets the ingredient_type of this RecipeOldSubHeadingIngredient.  # noqa: E501


        :return: The ingredient_type of this RecipeOldSubHeadingIngredient.  # noqa: E501
        :rtype: list[str]
        """
        return self._ingredient_type

    @ingredient_type.setter
    def ingredient_type(self, ingredient_type):
        """Sets the ingredient_type of this RecipeOldSubHeadingIngredient.


        :param ingredient_type: The ingredient_type of this RecipeOldSubHeadingIngredient.  # noqa: E501
        :type: list[str]
        """

        self._ingredient_type = ingredient_type

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
        if not isinstance(other, RecipeOldSubHeadingIngredient):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecipeOldSubHeadingIngredient):
            return True

        return self.to_dict() != other.to_dict()
