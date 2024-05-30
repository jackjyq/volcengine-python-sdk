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


class ResponseHeaderInstanceForBatchUpdateCdnConfigInput(object):
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
        'access_origin_control': 'bool',
        'action': 'str',
        'key': 'str',
        'value': 'str',
        'value_type': 'str'
    }

    attribute_map = {
        'access_origin_control': 'AccessOriginControl',
        'action': 'Action',
        'key': 'Key',
        'value': 'Value',
        'value_type': 'ValueType'
    }

    def __init__(self, access_origin_control=None, action=None, key=None, value=None, value_type=None, _configuration=None):  # noqa: E501
        """ResponseHeaderInstanceForBatchUpdateCdnConfigInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_origin_control = None
        self._action = None
        self._key = None
        self._value = None
        self._value_type = None
        self.discriminator = None

        if access_origin_control is not None:
            self.access_origin_control = access_origin_control
        if action is not None:
            self.action = action
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if value_type is not None:
            self.value_type = value_type

    @property
    def access_origin_control(self):
        """Gets the access_origin_control of this ResponseHeaderInstanceForBatchUpdateCdnConfigInput.  # noqa: E501


        :return: The access_origin_control of this ResponseHeaderInstanceForBatchUpdateCdnConfigInput.  # noqa: E501
        :rtype: bool
        """
        return self._access_origin_control

    @access_origin_control.setter
    def access_origin_control(self, access_origin_control):
        """Sets the access_origin_control of this ResponseHeaderInstanceForBatchUpdateCdnConfigInput.


        :param access_origin_control: The access_origin_control of this ResponseHeaderInstanceForBatchUpdateCdnConfigInput.  # noqa: E501
        :type: bool
        """

        self._access_origin_control = access_origin_control

    @property
    def action(self):
        """Gets the action of this ResponseHeaderInstanceForBatchUpdateCdnConfigInput.  # noqa: E501


        :return: The action of this ResponseHeaderInstanceForBatchUpdateCdnConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ResponseHeaderInstanceForBatchUpdateCdnConfigInput.


        :param action: The action of this ResponseHeaderInstanceForBatchUpdateCdnConfigInput.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def key(self):
        """Gets the key of this ResponseHeaderInstanceForBatchUpdateCdnConfigInput.  # noqa: E501


        :return: The key of this ResponseHeaderInstanceForBatchUpdateCdnConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ResponseHeaderInstanceForBatchUpdateCdnConfigInput.


        :param key: The key of this ResponseHeaderInstanceForBatchUpdateCdnConfigInput.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def value(self):
        """Gets the value of this ResponseHeaderInstanceForBatchUpdateCdnConfigInput.  # noqa: E501


        :return: The value of this ResponseHeaderInstanceForBatchUpdateCdnConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ResponseHeaderInstanceForBatchUpdateCdnConfigInput.


        :param value: The value of this ResponseHeaderInstanceForBatchUpdateCdnConfigInput.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def value_type(self):
        """Gets the value_type of this ResponseHeaderInstanceForBatchUpdateCdnConfigInput.  # noqa: E501


        :return: The value_type of this ResponseHeaderInstanceForBatchUpdateCdnConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this ResponseHeaderInstanceForBatchUpdateCdnConfigInput.


        :param value_type: The value_type of this ResponseHeaderInstanceForBatchUpdateCdnConfigInput.  # noqa: E501
        :type: str
        """

        self._value_type = value_type

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
        if issubclass(ResponseHeaderInstanceForBatchUpdateCdnConfigInput, dict):
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
        if not isinstance(other, ResponseHeaderInstanceForBatchUpdateCdnConfigInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseHeaderInstanceForBatchUpdateCdnConfigInput):
            return True

        return self.to_dict() != other.to_dict()
