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


class NegativeCacheForBatchUpdateCdnConfigInput(object):
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
        'condition': 'ConditionForBatchUpdateCdnConfigInput',
        'negative_cache_rule': 'NegativeCacheRuleForBatchUpdateCdnConfigInput'
    }

    attribute_map = {
        'condition': 'Condition',
        'negative_cache_rule': 'NegativeCacheRule'
    }

    def __init__(self, condition=None, negative_cache_rule=None, _configuration=None):  # noqa: E501
        """NegativeCacheForBatchUpdateCdnConfigInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._condition = None
        self._negative_cache_rule = None
        self.discriminator = None

        if condition is not None:
            self.condition = condition
        if negative_cache_rule is not None:
            self.negative_cache_rule = negative_cache_rule

    @property
    def condition(self):
        """Gets the condition of this NegativeCacheForBatchUpdateCdnConfigInput.  # noqa: E501


        :return: The condition of this NegativeCacheForBatchUpdateCdnConfigInput.  # noqa: E501
        :rtype: ConditionForBatchUpdateCdnConfigInput
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this NegativeCacheForBatchUpdateCdnConfigInput.


        :param condition: The condition of this NegativeCacheForBatchUpdateCdnConfigInput.  # noqa: E501
        :type: ConditionForBatchUpdateCdnConfigInput
        """

        self._condition = condition

    @property
    def negative_cache_rule(self):
        """Gets the negative_cache_rule of this NegativeCacheForBatchUpdateCdnConfigInput.  # noqa: E501


        :return: The negative_cache_rule of this NegativeCacheForBatchUpdateCdnConfigInput.  # noqa: E501
        :rtype: NegativeCacheRuleForBatchUpdateCdnConfigInput
        """
        return self._negative_cache_rule

    @negative_cache_rule.setter
    def negative_cache_rule(self, negative_cache_rule):
        """Sets the negative_cache_rule of this NegativeCacheForBatchUpdateCdnConfigInput.


        :param negative_cache_rule: The negative_cache_rule of this NegativeCacheForBatchUpdateCdnConfigInput.  # noqa: E501
        :type: NegativeCacheRuleForBatchUpdateCdnConfigInput
        """

        self._negative_cache_rule = negative_cache_rule

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
        if issubclass(NegativeCacheForBatchUpdateCdnConfigInput, dict):
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
        if not isinstance(other, NegativeCacheForBatchUpdateCdnConfigInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NegativeCacheForBatchUpdateCdnConfigInput):
            return True

        return self.to_dict() != other.to_dict()
