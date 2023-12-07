# coding: utf-8

"""
    vke

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class TaintForCreateDefaultNodePoolInput(object):
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
        'effect': 'str',
        'key': 'str',
        'value': 'str'
    }

    attribute_map = {
        'effect': 'Effect',
        'key': 'Key',
        'value': 'Value'
    }

    def __init__(self, effect=None, key=None, value=None, _configuration=None):  # noqa: E501
        """TaintForCreateDefaultNodePoolInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._effect = None
        self._key = None
        self._value = None
        self.discriminator = None

        if effect is not None:
            self.effect = effect
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value

    @property
    def effect(self):
        """Gets the effect of this TaintForCreateDefaultNodePoolInput.  # noqa: E501


        :return: The effect of this TaintForCreateDefaultNodePoolInput.  # noqa: E501
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this TaintForCreateDefaultNodePoolInput.


        :param effect: The effect of this TaintForCreateDefaultNodePoolInput.  # noqa: E501
        :type: str
        """
        allowed_values = ["NoSchedule", "NoExecute", "PreferNoSchedule"]  # noqa: E501
        if (self._configuration.client_side_validation and
                effect not in allowed_values):
            raise ValueError(
                "Invalid value for `effect` ({0}), must be one of {1}"  # noqa: E501
                .format(effect, allowed_values)
            )

        self._effect = effect

    @property
    def key(self):
        """Gets the key of this TaintForCreateDefaultNodePoolInput.  # noqa: E501


        :return: The key of this TaintForCreateDefaultNodePoolInput.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this TaintForCreateDefaultNodePoolInput.


        :param key: The key of this TaintForCreateDefaultNodePoolInput.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def value(self):
        """Gets the value of this TaintForCreateDefaultNodePoolInput.  # noqa: E501


        :return: The value of this TaintForCreateDefaultNodePoolInput.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TaintForCreateDefaultNodePoolInput.


        :param value: The value of this TaintForCreateDefaultNodePoolInput.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(TaintForCreateDefaultNodePoolInput, dict):
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
        if not isinstance(other, TaintForCreateDefaultNodePoolInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaintForCreateDefaultNodePoolInput):
            return True

        return self.to_dict() != other.to_dict()
