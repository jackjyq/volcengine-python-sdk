# coding: utf-8

"""
    rds_mysql_v2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class FeatureStateForDescribeDBProxyConfigOutput(object):
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
        'enable': 'bool',
        'feature_name': 'str',
        'support': 'bool'
    }

    attribute_map = {
        'enable': 'Enable',
        'feature_name': 'FeatureName',
        'support': 'Support'
    }

    def __init__(self, enable=None, feature_name=None, support=None, _configuration=None):  # noqa: E501
        """FeatureStateForDescribeDBProxyConfigOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._enable = None
        self._feature_name = None
        self._support = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if feature_name is not None:
            self.feature_name = feature_name
        if support is not None:
            self.support = support

    @property
    def enable(self):
        """Gets the enable of this FeatureStateForDescribeDBProxyConfigOutput.  # noqa: E501


        :return: The enable of this FeatureStateForDescribeDBProxyConfigOutput.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this FeatureStateForDescribeDBProxyConfigOutput.


        :param enable: The enable of this FeatureStateForDescribeDBProxyConfigOutput.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def feature_name(self):
        """Gets the feature_name of this FeatureStateForDescribeDBProxyConfigOutput.  # noqa: E501


        :return: The feature_name of this FeatureStateForDescribeDBProxyConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._feature_name

    @feature_name.setter
    def feature_name(self, feature_name):
        """Sets the feature_name of this FeatureStateForDescribeDBProxyConfigOutput.


        :param feature_name: The feature_name of this FeatureStateForDescribeDBProxyConfigOutput.  # noqa: E501
        :type: str
        """

        self._feature_name = feature_name

    @property
    def support(self):
        """Gets the support of this FeatureStateForDescribeDBProxyConfigOutput.  # noqa: E501


        :return: The support of this FeatureStateForDescribeDBProxyConfigOutput.  # noqa: E501
        :rtype: bool
        """
        return self._support

    @support.setter
    def support(self, support):
        """Sets the support of this FeatureStateForDescribeDBProxyConfigOutput.


        :param support: The support of this FeatureStateForDescribeDBProxyConfigOutput.  # noqa: E501
        :type: bool
        """

        self._support = support

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
        if issubclass(FeatureStateForDescribeDBProxyConfigOutput, dict):
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
        if not isinstance(other, FeatureStateForDescribeDBProxyConfigOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FeatureStateForDescribeDBProxyConfigOutput):
            return True

        return self.to_dict() != other.to_dict()
