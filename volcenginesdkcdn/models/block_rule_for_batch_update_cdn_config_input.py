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


class BlockRuleForBatchUpdateCdnConfigInput(object):
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
        'block_action': 'BlockActionForBatchUpdateCdnConfigInput',
        'condition': 'ConditionForBatchUpdateCdnConfigInput',
        'rule_name': 'str'
    }

    attribute_map = {
        'block_action': 'BlockAction',
        'condition': 'Condition',
        'rule_name': 'RuleName'
    }

    def __init__(self, block_action=None, condition=None, rule_name=None, _configuration=None):  # noqa: E501
        """BlockRuleForBatchUpdateCdnConfigInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._block_action = None
        self._condition = None
        self._rule_name = None
        self.discriminator = None

        if block_action is not None:
            self.block_action = block_action
        if condition is not None:
            self.condition = condition
        if rule_name is not None:
            self.rule_name = rule_name

    @property
    def block_action(self):
        """Gets the block_action of this BlockRuleForBatchUpdateCdnConfigInput.  # noqa: E501


        :return: The block_action of this BlockRuleForBatchUpdateCdnConfigInput.  # noqa: E501
        :rtype: BlockActionForBatchUpdateCdnConfigInput
        """
        return self._block_action

    @block_action.setter
    def block_action(self, block_action):
        """Sets the block_action of this BlockRuleForBatchUpdateCdnConfigInput.


        :param block_action: The block_action of this BlockRuleForBatchUpdateCdnConfigInput.  # noqa: E501
        :type: BlockActionForBatchUpdateCdnConfigInput
        """

        self._block_action = block_action

    @property
    def condition(self):
        """Gets the condition of this BlockRuleForBatchUpdateCdnConfigInput.  # noqa: E501


        :return: The condition of this BlockRuleForBatchUpdateCdnConfigInput.  # noqa: E501
        :rtype: ConditionForBatchUpdateCdnConfigInput
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this BlockRuleForBatchUpdateCdnConfigInput.


        :param condition: The condition of this BlockRuleForBatchUpdateCdnConfigInput.  # noqa: E501
        :type: ConditionForBatchUpdateCdnConfigInput
        """

        self._condition = condition

    @property
    def rule_name(self):
        """Gets the rule_name of this BlockRuleForBatchUpdateCdnConfigInput.  # noqa: E501


        :return: The rule_name of this BlockRuleForBatchUpdateCdnConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this BlockRuleForBatchUpdateCdnConfigInput.


        :param rule_name: The rule_name of this BlockRuleForBatchUpdateCdnConfigInput.  # noqa: E501
        :type: str
        """

        self._rule_name = rule_name

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
        if issubclass(BlockRuleForBatchUpdateCdnConfigInput, dict):
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
        if not isinstance(other, BlockRuleForBatchUpdateCdnConfigInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BlockRuleForBatchUpdateCdnConfigInput):
            return True

        return self.to_dict() != other.to_dict()
