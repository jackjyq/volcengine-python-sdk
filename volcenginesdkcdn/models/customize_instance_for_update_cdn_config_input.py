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


class CustomizeInstanceForUpdateCdnConfigInput(object):
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
        'customize_rule': 'CustomizeRuleForUpdateCdnConfigInput'
    }

    attribute_map = {
        'customize_rule': 'CustomizeRule'
    }

    def __init__(self, customize_rule=None, _configuration=None):  # noqa: E501
        """CustomizeInstanceForUpdateCdnConfigInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._customize_rule = None
        self.discriminator = None

        if customize_rule is not None:
            self.customize_rule = customize_rule

    @property
    def customize_rule(self):
        """Gets the customize_rule of this CustomizeInstanceForUpdateCdnConfigInput.  # noqa: E501


        :return: The customize_rule of this CustomizeInstanceForUpdateCdnConfigInput.  # noqa: E501
        :rtype: CustomizeRuleForUpdateCdnConfigInput
        """
        return self._customize_rule

    @customize_rule.setter
    def customize_rule(self, customize_rule):
        """Sets the customize_rule of this CustomizeInstanceForUpdateCdnConfigInput.


        :param customize_rule: The customize_rule of this CustomizeInstanceForUpdateCdnConfigInput.  # noqa: E501
        :type: CustomizeRuleForUpdateCdnConfigInput
        """

        self._customize_rule = customize_rule

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
        if issubclass(CustomizeInstanceForUpdateCdnConfigInput, dict):
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
        if not isinstance(other, CustomizeInstanceForUpdateCdnConfigInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomizeInstanceForUpdateCdnConfigInput):
            return True

        return self.to_dict() != other.to_dict()
