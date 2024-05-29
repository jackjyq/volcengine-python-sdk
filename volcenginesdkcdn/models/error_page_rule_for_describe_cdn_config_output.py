# coding: utf-8

"""
    cdn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ErrorPageRuleForDescribeCdnConfigOutput(object):
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
        'error_page_action': 'ErrorPageActionForDescribeCdnConfigOutput'
    }

    attribute_map = {
        'error_page_action': 'ErrorPageAction'
    }

    def __init__(self, error_page_action=None, _configuration=None):  # noqa: E501
        """ErrorPageRuleForDescribeCdnConfigOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._error_page_action = None
        self.discriminator = None

        if error_page_action is not None:
            self.error_page_action = error_page_action

    @property
    def error_page_action(self):
        """Gets the error_page_action of this ErrorPageRuleForDescribeCdnConfigOutput.  # noqa: E501


        :return: The error_page_action of this ErrorPageRuleForDescribeCdnConfigOutput.  # noqa: E501
        :rtype: ErrorPageActionForDescribeCdnConfigOutput
        """
        return self._error_page_action

    @error_page_action.setter
    def error_page_action(self, error_page_action):
        """Sets the error_page_action of this ErrorPageRuleForDescribeCdnConfigOutput.


        :param error_page_action: The error_page_action of this ErrorPageRuleForDescribeCdnConfigOutput.  # noqa: E501
        :type: ErrorPageActionForDescribeCdnConfigOutput
        """

        self._error_page_action = error_page_action

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
        if issubclass(ErrorPageRuleForDescribeCdnConfigOutput, dict):
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
        if not isinstance(other, ErrorPageRuleForDescribeCdnConfigOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ErrorPageRuleForDescribeCdnConfigOutput):
            return True

        return self.to_dict() != other.to_dict()
