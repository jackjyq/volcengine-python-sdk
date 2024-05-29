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


class ConditionRuleForUpdateCdnConfigInput(object):
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
        'name': 'str',
        'object': 'str',
        'operator': 'str',
        'type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'object': 'Object',
        'operator': 'Operator',
        'type': 'Type',
        'value': 'Value'
    }

    def __init__(self, name=None, object=None, operator=None, type=None, value=None, _configuration=None):  # noqa: E501
        """ConditionRuleForUpdateCdnConfigInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._object = None
        self._operator = None
        self._type = None
        self._value = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if object is not None:
            self.object = object
        if operator is not None:
            self.operator = operator
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value

    @property
    def name(self):
        """Gets the name of this ConditionRuleForUpdateCdnConfigInput.  # noqa: E501


        :return: The name of this ConditionRuleForUpdateCdnConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConditionRuleForUpdateCdnConfigInput.


        :param name: The name of this ConditionRuleForUpdateCdnConfigInput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def object(self):
        """Gets the object of this ConditionRuleForUpdateCdnConfigInput.  # noqa: E501


        :return: The object of this ConditionRuleForUpdateCdnConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this ConditionRuleForUpdateCdnConfigInput.


        :param object: The object of this ConditionRuleForUpdateCdnConfigInput.  # noqa: E501
        :type: str
        """

        self._object = object

    @property
    def operator(self):
        """Gets the operator of this ConditionRuleForUpdateCdnConfigInput.  # noqa: E501


        :return: The operator of this ConditionRuleForUpdateCdnConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this ConditionRuleForUpdateCdnConfigInput.


        :param operator: The operator of this ConditionRuleForUpdateCdnConfigInput.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def type(self):
        """Gets the type of this ConditionRuleForUpdateCdnConfigInput.  # noqa: E501


        :return: The type of this ConditionRuleForUpdateCdnConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConditionRuleForUpdateCdnConfigInput.


        :param type: The type of this ConditionRuleForUpdateCdnConfigInput.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def value(self):
        """Gets the value of this ConditionRuleForUpdateCdnConfigInput.  # noqa: E501


        :return: The value of this ConditionRuleForUpdateCdnConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ConditionRuleForUpdateCdnConfigInput.


        :param value: The value of this ConditionRuleForUpdateCdnConfigInput.  # noqa: E501
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
        if issubclass(ConditionRuleForUpdateCdnConfigInput, dict):
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
        if not isinstance(other, ConditionRuleForUpdateCdnConfigInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConditionRuleForUpdateCdnConfigInput):
            return True

        return self.to_dict() != other.to_dict()
