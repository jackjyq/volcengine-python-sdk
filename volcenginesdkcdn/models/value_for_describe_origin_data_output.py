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


class ValueForDescribeOriginDataOutput(object):
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
        'time_stamp': 'int',
        'value': 'float'
    }

    attribute_map = {
        'time_stamp': 'TimeStamp',
        'value': 'Value'
    }

    def __init__(self, time_stamp=None, value=None, _configuration=None):  # noqa: E501
        """ValueForDescribeOriginDataOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._time_stamp = None
        self._value = None
        self.discriminator = None

        if time_stamp is not None:
            self.time_stamp = time_stamp
        if value is not None:
            self.value = value

    @property
    def time_stamp(self):
        """Gets the time_stamp of this ValueForDescribeOriginDataOutput.  # noqa: E501


        :return: The time_stamp of this ValueForDescribeOriginDataOutput.  # noqa: E501
        :rtype: int
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this ValueForDescribeOriginDataOutput.


        :param time_stamp: The time_stamp of this ValueForDescribeOriginDataOutput.  # noqa: E501
        :type: int
        """

        self._time_stamp = time_stamp

    @property
    def value(self):
        """Gets the value of this ValueForDescribeOriginDataOutput.  # noqa: E501


        :return: The value of this ValueForDescribeOriginDataOutput.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ValueForDescribeOriginDataOutput.


        :param value: The value of this ValueForDescribeOriginDataOutput.  # noqa: E501
        :type: float
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
        if issubclass(ValueForDescribeOriginDataOutput, dict):
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
        if not isinstance(other, ValueForDescribeOriginDataOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ValueForDescribeOriginDataOutput):
            return True

        return self.to_dict() != other.to_dict()
