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


class DescribeEventTypesRequest(object):
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
        'kind': 'str',
        'max_results': 'str',
        'next_token': 'str',
        'response_required': 'bool',
        'types': 'list[str]'
    }

    attribute_map = {
        'kind': 'Kind',
        'max_results': 'MaxResults',
        'next_token': 'NextToken',
        'response_required': 'ResponseRequired',
        'types': 'Types'
    }

    def __init__(self, kind=None, max_results=None, next_token=None, response_required=None, types=None, _configuration=None):  # noqa: E501
        """DescribeEventTypesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._kind = None
        self._max_results = None
        self._next_token = None
        self._response_required = None
        self._types = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if max_results is not None:
            self.max_results = max_results
        if next_token is not None:
            self.next_token = next_token
        if response_required is not None:
            self.response_required = response_required
        if types is not None:
            self.types = types

    @property
    def kind(self):
        """Gets the kind of this DescribeEventTypesRequest.  # noqa: E501


        :return: The kind of this DescribeEventTypesRequest.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this DescribeEventTypesRequest.


        :param kind: The kind of this DescribeEventTypesRequest.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def max_results(self):
        """Gets the max_results of this DescribeEventTypesRequest.  # noqa: E501


        :return: The max_results of this DescribeEventTypesRequest.  # noqa: E501
        :rtype: str
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """Sets the max_results of this DescribeEventTypesRequest.


        :param max_results: The max_results of this DescribeEventTypesRequest.  # noqa: E501
        :type: str
        """

        self._max_results = max_results

    @property
    def next_token(self):
        """Gets the next_token of this DescribeEventTypesRequest.  # noqa: E501


        :return: The next_token of this DescribeEventTypesRequest.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this DescribeEventTypesRequest.


        :param next_token: The next_token of this DescribeEventTypesRequest.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

    @property
    def response_required(self):
        """Gets the response_required of this DescribeEventTypesRequest.  # noqa: E501


        :return: The response_required of this DescribeEventTypesRequest.  # noqa: E501
        :rtype: bool
        """
        return self._response_required

    @response_required.setter
    def response_required(self, response_required):
        """Sets the response_required of this DescribeEventTypesRequest.


        :param response_required: The response_required of this DescribeEventTypesRequest.  # noqa: E501
        :type: bool
        """

        self._response_required = response_required

    @property
    def types(self):
        """Gets the types of this DescribeEventTypesRequest.  # noqa: E501


        :return: The types of this DescribeEventTypesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this DescribeEventTypesRequest.


        :param types: The types of this DescribeEventTypesRequest.  # noqa: E501
        :type: list[str]
        """

        self._types = types

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
        if issubclass(DescribeEventTypesRequest, dict):
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
        if not isinstance(other, DescribeEventTypesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeEventTypesRequest):
            return True

        return self.to_dict() != other.to_dict()
