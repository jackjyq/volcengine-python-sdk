# coding: utf-8

"""
    vepfs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CapacityInfoForDescribeFileSystemsOutput(object):
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
        'total_ti_b': 'int',
        'used_gi_b': 'int'
    }

    attribute_map = {
        'total_ti_b': 'TotalTiB',
        'used_gi_b': 'UsedGiB'
    }

    def __init__(self, total_ti_b=None, used_gi_b=None, _configuration=None):  # noqa: E501
        """CapacityInfoForDescribeFileSystemsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._total_ti_b = None
        self._used_gi_b = None
        self.discriminator = None

        if total_ti_b is not None:
            self.total_ti_b = total_ti_b
        if used_gi_b is not None:
            self.used_gi_b = used_gi_b

    @property
    def total_ti_b(self):
        """Gets the total_ti_b of this CapacityInfoForDescribeFileSystemsOutput.  # noqa: E501


        :return: The total_ti_b of this CapacityInfoForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: int
        """
        return self._total_ti_b

    @total_ti_b.setter
    def total_ti_b(self, total_ti_b):
        """Sets the total_ti_b of this CapacityInfoForDescribeFileSystemsOutput.


        :param total_ti_b: The total_ti_b of this CapacityInfoForDescribeFileSystemsOutput.  # noqa: E501
        :type: int
        """

        self._total_ti_b = total_ti_b

    @property
    def used_gi_b(self):
        """Gets the used_gi_b of this CapacityInfoForDescribeFileSystemsOutput.  # noqa: E501


        :return: The used_gi_b of this CapacityInfoForDescribeFileSystemsOutput.  # noqa: E501
        :rtype: int
        """
        return self._used_gi_b

    @used_gi_b.setter
    def used_gi_b(self, used_gi_b):
        """Sets the used_gi_b of this CapacityInfoForDescribeFileSystemsOutput.


        :param used_gi_b: The used_gi_b of this CapacityInfoForDescribeFileSystemsOutput.  # noqa: E501
        :type: int
        """

        self._used_gi_b = used_gi_b

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
        if issubclass(CapacityInfoForDescribeFileSystemsOutput, dict):
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
        if not isinstance(other, CapacityInfoForDescribeFileSystemsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CapacityInfoForDescribeFileSystemsOutput):
            return True

        return self.to_dict() != other.to_dict()
