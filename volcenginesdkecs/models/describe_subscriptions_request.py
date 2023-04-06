# coding: utf-8

"""
    ecs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeSubscriptionsRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'created_at_end': 'str',
        'created_at_start': 'str',
        'max_results': 'str',
        'next_token': 'str'
    }

    attribute_map = {
        'created_at_end': 'CreatedAtEnd',
        'created_at_start': 'CreatedAtStart',
        'max_results': 'MaxResults',
        'next_token': 'NextToken'
    }

    def __init__(self, created_at_end=None, created_at_start=None, max_results=None, next_token=None, _configuration=None):  # noqa: E501
        """DescribeSubscriptionsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created_at_end = None
        self._created_at_start = None
        self._max_results = None
        self._next_token = None
        self.discriminator = None

        if created_at_end is not None:
            self.created_at_end = created_at_end
        if created_at_start is not None:
            self.created_at_start = created_at_start
        if max_results is not None:
            self.max_results = max_results
        if next_token is not None:
            self.next_token = next_token

    @property
    def created_at_end(self):
        """Gets the created_at_end of this DescribeSubscriptionsRequest.  # noqa: E501


        :return: The created_at_end of this DescribeSubscriptionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._created_at_end

    @created_at_end.setter
    def created_at_end(self, created_at_end):
        """Sets the created_at_end of this DescribeSubscriptionsRequest.


        :param created_at_end: The created_at_end of this DescribeSubscriptionsRequest.  # noqa: E501
        :type: str
        """

        self._created_at_end = created_at_end

    @property
    def created_at_start(self):
        """Gets the created_at_start of this DescribeSubscriptionsRequest.  # noqa: E501


        :return: The created_at_start of this DescribeSubscriptionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._created_at_start

    @created_at_start.setter
    def created_at_start(self, created_at_start):
        """Sets the created_at_start of this DescribeSubscriptionsRequest.


        :param created_at_start: The created_at_start of this DescribeSubscriptionsRequest.  # noqa: E501
        :type: str
        """

        self._created_at_start = created_at_start

    @property
    def max_results(self):
        """Gets the max_results of this DescribeSubscriptionsRequest.  # noqa: E501


        :return: The max_results of this DescribeSubscriptionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """Sets the max_results of this DescribeSubscriptionsRequest.


        :param max_results: The max_results of this DescribeSubscriptionsRequest.  # noqa: E501
        :type: str
        """

        self._max_results = max_results

    @property
    def next_token(self):
        """Gets the next_token of this DescribeSubscriptionsRequest.  # noqa: E501


        :return: The next_token of this DescribeSubscriptionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this DescribeSubscriptionsRequest.


        :param next_token: The next_token of this DescribeSubscriptionsRequest.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(DescribeSubscriptionsRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DescribeSubscriptionsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeSubscriptionsRequest):
            return True

        return self.to_dict() != other.to_dict()
