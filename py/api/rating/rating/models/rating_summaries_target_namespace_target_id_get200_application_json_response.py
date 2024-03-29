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


class RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse(object):
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
        'target_id': 'str',
        'target_namespace': 'str',
        'category': 'str',
        'sub_category': 'str',
        'comment_count': 'int',
        'total_comment_count': 'int',
        'average': 'float',
        'averages': 'RatingSummaryAverages',
        'distribution': 'RatingSummaryDistribution',
        'distributions': 'RatingSummaryDistributions'
    }

    attribute_map = {
        'target_id': 'targetId',
        'target_namespace': 'targetNamespace',
        'category': 'category',
        'sub_category': 'subCategory',
        'comment_count': 'commentCount',
        'total_comment_count': 'totalCommentCount',
        'average': 'average',
        'averages': 'averages',
        'distribution': 'distribution',
        'distributions': 'distributions'
    }

    def __init__(self, target_id=None, target_namespace=None, category=None, sub_category=None, comment_count=None, total_comment_count=None, average=None, averages=None, distribution=None, distributions=None, local_vars_configuration=None):  # noqa: E501
        """RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._target_id = None
        self._target_namespace = None
        self._category = None
        self._sub_category = None
        self._comment_count = None
        self._total_comment_count = None
        self._average = None
        self._averages = None
        self._distribution = None
        self._distributions = None
        self.discriminator = None

        self.target_id = target_id
        self.target_namespace = target_namespace
        if category is not None:
            self.category = category
        if sub_category is not None:
            self.sub_category = sub_category
        self.comment_count = comment_count
        if total_comment_count is not None:
            self.total_comment_count = total_comment_count
        self.average = average
        if averages is not None:
            self.averages = averages
        self.distribution = distribution
        if distributions is not None:
            self.distributions = distributions

    @property
    def target_id(self):
        """Gets the target_id of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501

        Id of the rated object. This id is the external id of the other service.   # noqa: E501

        :return: The target_id of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.

        Id of the rated object. This id is the external id of the other service.   # noqa: E501

        :param target_id: The target_id of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and target_id is None:  # noqa: E501
            raise ValueError("Invalid value for `target_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                target_id is not None and len(target_id) > 64):
            raise ValueError("Invalid value for `target_id`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                target_id is not None and len(target_id) < 1):
            raise ValueError("Invalid value for `target_id`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                target_id is not None and not re.search(r'[A-Za-z0-9\-_.()!@:\/]', target_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `target_id`, must be a follow pattern or equal to `/[A-Za-z0-9\-_.()!@:\/]/`")  # noqa: E501

        self._target_id = target_id

    @property
    def target_namespace(self):
        """Gets the target_namespace of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501

        Namespace of the rating targets. This is provided because external services might have targets with collisioning IDs. For example service A might have product with id 1, and service B product with also id 1. This attribute makes it possible to separate those two products. All external service which use this API should agree on unique namespaces. For example all food products register could have namespace: `food-products`.   # noqa: E501

        :return: The target_namespace of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501
        :rtype: str
        """
        return self._target_namespace

    @target_namespace.setter
    def target_namespace(self, target_namespace):
        """Sets the target_namespace of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.

        Namespace of the rating targets. This is provided because external services might have targets with collisioning IDs. For example service A might have product with id 1, and service B product with also id 1. This attribute makes it possible to separate those two products. All external service which use this API should agree on unique namespaces. For example all food products register could have namespace: `food-products`.   # noqa: E501

        :param target_namespace: The target_namespace of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and target_namespace is None:  # noqa: E501
            raise ValueError("Invalid value for `target_namespace`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                target_namespace is not None and len(target_namespace) > 64):
            raise ValueError("Invalid value for `target_namespace`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                target_namespace is not None and len(target_namespace) < 1):
            raise ValueError("Invalid value for `target_namespace`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                target_namespace is not None and not re.search(r'[A-Za-z0-9\-_]', target_namespace)):  # noqa: E501
            raise ValueError(r"Invalid value for `target_namespace`, must be a follow pattern or equal to `/[A-Za-z0-9\-_]/`")  # noqa: E501

        self._target_namespace = target_namespace

    @property
    def category(self):
        """Gets the category of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501

        Category of the rated object. The external service should have a subset of given categories. These are not designed to be user-speficied categories. For example category with special characters (e.g. Jälkiruoka) does not work.   # noqa: E501

        :return: The category of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.

        Category of the rated object. The external service should have a subset of given categories. These are not designed to be user-speficied categories. For example category with special characters (e.g. Jälkiruoka) does not work.   # noqa: E501

        :param category: The category of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                category is not None and len(category) > 64):
            raise ValueError("Invalid value for `category`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                category is not None and len(category) < 1):
            raise ValueError("Invalid value for `category`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                category is not None and not re.search(r'[A-Za-z0-9\-_]', category)):  # noqa: E501
            raise ValueError(r"Invalid value for `category`, must be a follow pattern or equal to `/[A-Za-z0-9\-_]/`")  # noqa: E501

        self._category = category

    @property
    def sub_category(self):
        """Gets the sub_category of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501

        Sub category of the rated object. The external service should have a subset of given categories. These are not designed to be user-speficied categories. For example category with special characters (e.g. Jälkiruoka) does not work.   # noqa: E501

        :return: The sub_category of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501
        :rtype: str
        """
        return self._sub_category

    @sub_category.setter
    def sub_category(self, sub_category):
        """Sets the sub_category of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.

        Sub category of the rated object. The external service should have a subset of given categories. These are not designed to be user-speficied categories. For example category with special characters (e.g. Jälkiruoka) does not work.   # noqa: E501

        :param sub_category: The sub_category of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                sub_category is not None and len(sub_category) > 64):
            raise ValueError("Invalid value for `sub_category`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sub_category is not None and len(sub_category) < 1):
            raise ValueError("Invalid value for `sub_category`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sub_category is not None and not re.search(r'[A-Za-z0-9\-_]', sub_category)):  # noqa: E501
            raise ValueError(r"Invalid value for `sub_category`, must be a follow pattern or equal to `/[A-Za-z0-9\-_]/`")  # noqa: E501

        self._sub_category = sub_category

    @property
    def comment_count(self):
        """Gets the comment_count of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501

        Total number of published comments given to the given target, includes only published comments.   # noqa: E501

        :return: The comment_count of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501
        :rtype: int
        """
        return self._comment_count

    @comment_count.setter
    def comment_count(self, comment_count):
        """Sets the comment_count of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.

        Total number of published comments given to the given target, includes only published comments.   # noqa: E501

        :param comment_count: The comment_count of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and comment_count is None:  # noqa: E501
            raise ValueError("Invalid value for `comment_count`, must not be `None`")  # noqa: E501

        self._comment_count = comment_count

    @property
    def total_comment_count(self):
        """Gets the total_comment_count of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501

        Total number of comments given to the given target, includes published and unpublished comments.   # noqa: E501

        :return: The total_comment_count of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_comment_count

    @total_comment_count.setter
    def total_comment_count(self, total_comment_count):
        """Sets the total_comment_count of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.

        Total number of comments given to the given target, includes published and unpublished comments.   # noqa: E501

        :param total_comment_count: The total_comment_count of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501
        :type: int
        """

        self._total_comment_count = total_comment_count

    @property
    def average(self):
        """Gets the average of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501

        Average rating of the rated object.  # noqa: E501

        :return: The average of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501
        :rtype: float
        """
        return self._average

    @average.setter
    def average(self, average):
        """Sets the average of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.

        Average rating of the rated object.  # noqa: E501

        :param average: The average of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and average is None:  # noqa: E501
            raise ValueError("Invalid value for `average`, must not be `None`")  # noqa: E501

        self._average = average

    @property
    def averages(self):
        """Gets the averages of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501


        :return: The averages of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501
        :rtype: RatingSummaryAverages
        """
        return self._averages

    @averages.setter
    def averages(self, averages):
        """Sets the averages of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.


        :param averages: The averages of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501
        :type: RatingSummaryAverages
        """

        self._averages = averages

    @property
    def distribution(self):
        """Gets the distribution of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501


        :return: The distribution of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501
        :rtype: RatingSummaryDistribution
        """
        return self._distribution

    @distribution.setter
    def distribution(self, distribution):
        """Sets the distribution of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.


        :param distribution: The distribution of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501
        :type: RatingSummaryDistribution
        """
        if self.local_vars_configuration.client_side_validation and distribution is None:  # noqa: E501
            raise ValueError("Invalid value for `distribution`, must not be `None`")  # noqa: E501

        self._distribution = distribution

    @property
    def distributions(self):
        """Gets the distributions of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501


        :return: The distributions of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501
        :rtype: RatingSummaryDistributions
        """
        return self._distributions

    @distributions.setter
    def distributions(self, distributions):
        """Sets the distributions of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.


        :param distributions: The distributions of this RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse.  # noqa: E501
        :type: RatingSummaryDistributions
        """

        self._distributions = distributions

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
        if not isinstance(other, RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RatingSummariesTargetNamespaceTargetIdGet200ApplicationJsonResponse):
            return True

        return self.to_dict() != other.to_dict()
