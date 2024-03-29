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


class StoreShopkeeper(object):
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
        'marketing_title': 'str',
        'signature': 'str',
        'picture_url': 'str'
    }

    attribute_map = {
        'marketing_title': 'MarketingTitle',
        'signature': 'Signature',
        'picture_url': 'PictureUrl'
    }

    def __init__(self, marketing_title=None, signature=None, picture_url=None, local_vars_configuration=None):  # noqa: E501
        """StoreShopkeeper - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._marketing_title = None
        self._signature = None
        self._picture_url = None
        self.discriminator = None

        if marketing_title is not None:
            self.marketing_title = marketing_title
        if signature is not None:
            self.signature = signature
        if picture_url is not None:
            self.picture_url = picture_url

    @property
    def marketing_title(self):
        """Gets the marketing_title of this StoreShopkeeper.  # noqa: E501


        :return: The marketing_title of this StoreShopkeeper.  # noqa: E501
        :rtype: str
        """
        return self._marketing_title

    @marketing_title.setter
    def marketing_title(self, marketing_title):
        """Sets the marketing_title of this StoreShopkeeper.


        :param marketing_title: The marketing_title of this StoreShopkeeper.  # noqa: E501
        :type: str
        """

        self._marketing_title = marketing_title

    @property
    def signature(self):
        """Gets the signature of this StoreShopkeeper.  # noqa: E501

        Shopkeeper name  # noqa: E501

        :return: The signature of this StoreShopkeeper.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this StoreShopkeeper.

        Shopkeeper name  # noqa: E501

        :param signature: The signature of this StoreShopkeeper.  # noqa: E501
        :type: str
        """

        self._signature = signature

    @property
    def picture_url(self):
        """Gets the picture_url of this StoreShopkeeper.  # noqa: E501

        Shopkeeper picture url  # noqa: E501

        :return: The picture_url of this StoreShopkeeper.  # noqa: E501
        :rtype: str
        """
        return self._picture_url

    @picture_url.setter
    def picture_url(self, picture_url):
        """Sets the picture_url of this StoreShopkeeper.

        Shopkeeper picture url  # noqa: E501

        :param picture_url: The picture_url of this StoreShopkeeper.  # noqa: E501
        :type: str
        """

        self._picture_url = picture_url

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
        if not isinstance(other, StoreShopkeeper):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StoreShopkeeper):
            return True

        return self.to_dict() != other.to_dict()
