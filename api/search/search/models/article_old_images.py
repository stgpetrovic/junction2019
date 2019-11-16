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


class ArticleOldImages(object):
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
        'image': 'str',
        'teaser_image11': 'str',
        'teaser_image169': 'str'
    }

    attribute_map = {
        'image': 'Image',
        'teaser_image11': 'TeaserImage11',
        'teaser_image169': 'TeaserImage169'
    }

    def __init__(self, image=None, teaser_image11=None, teaser_image169=None, local_vars_configuration=None):  # noqa: E501
        """ArticleOldImages - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._image = None
        self._teaser_image11 = None
        self._teaser_image169 = None
        self.discriminator = None

        self.image = image
        if teaser_image11 is not None:
            self.teaser_image11 = teaser_image11
        if teaser_image169 is not None:
            self.teaser_image169 = teaser_image169

    @property
    def image(self):
        """Gets the image of this ArticleOldImages.  # noqa: E501

        Image url  # noqa: E501

        :return: The image of this ArticleOldImages.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ArticleOldImages.

        Image url  # noqa: E501

        :param image: The image of this ArticleOldImages.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and image is None:  # noqa: E501
            raise ValueError("Invalid value for `image`, must not be `None`")  # noqa: E501

        self._image = image

    @property
    def teaser_image11(self):
        """Gets the teaser_image11 of this ArticleOldImages.  # noqa: E501

        Image url  # noqa: E501

        :return: The teaser_image11 of this ArticleOldImages.  # noqa: E501
        :rtype: str
        """
        return self._teaser_image11

    @teaser_image11.setter
    def teaser_image11(self, teaser_image11):
        """Sets the teaser_image11 of this ArticleOldImages.

        Image url  # noqa: E501

        :param teaser_image11: The teaser_image11 of this ArticleOldImages.  # noqa: E501
        :type: str
        """

        self._teaser_image11 = teaser_image11

    @property
    def teaser_image169(self):
        """Gets the teaser_image169 of this ArticleOldImages.  # noqa: E501

        Image url  # noqa: E501

        :return: The teaser_image169 of this ArticleOldImages.  # noqa: E501
        :rtype: str
        """
        return self._teaser_image169

    @teaser_image169.setter
    def teaser_image169(self, teaser_image169):
        """Sets the teaser_image169 of this ArticleOldImages.

        Image url  # noqa: E501

        :param teaser_image169: The teaser_image169 of this ArticleOldImages.  # noqa: E501
        :type: str
        """

        self._teaser_image169 = teaser_image169

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
        if not isinstance(other, ArticleOldImages):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ArticleOldImages):
            return True

        return self.to_dict() != other.to_dict()