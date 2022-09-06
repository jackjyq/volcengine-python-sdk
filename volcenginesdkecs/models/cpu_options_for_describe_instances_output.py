# coding: utf-8

"""
    ecs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CpuOptionsForDescribeInstancesOutput(object):
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
        'core_count': 'int',
        'threads_per_core': 'int'
    }

    attribute_map = {
        'core_count': 'CoreCount',
        'threads_per_core': 'ThreadsPerCore'
    }

    def __init__(self, core_count=None, threads_per_core=None, _configuration=None):  # noqa: E501
        """CpuOptionsForDescribeInstancesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._core_count = None
        self._threads_per_core = None
        self.discriminator = None

        if core_count is not None:
            self.core_count = core_count
        if threads_per_core is not None:
            self.threads_per_core = threads_per_core

    @property
    def core_count(self):
        """Gets the core_count of this CpuOptionsForDescribeInstancesOutput.  # noqa: E501


        :return: The core_count of this CpuOptionsForDescribeInstancesOutput.  # noqa: E501
        :rtype: int
        """
        return self._core_count

    @core_count.setter
    def core_count(self, core_count):
        """Sets the core_count of this CpuOptionsForDescribeInstancesOutput.


        :param core_count: The core_count of this CpuOptionsForDescribeInstancesOutput.  # noqa: E501
        :type: int
        """

        self._core_count = core_count

    @property
    def threads_per_core(self):
        """Gets the threads_per_core of this CpuOptionsForDescribeInstancesOutput.  # noqa: E501


        :return: The threads_per_core of this CpuOptionsForDescribeInstancesOutput.  # noqa: E501
        :rtype: int
        """
        return self._threads_per_core

    @threads_per_core.setter
    def threads_per_core(self, threads_per_core):
        """Sets the threads_per_core of this CpuOptionsForDescribeInstancesOutput.


        :param threads_per_core: The threads_per_core of this CpuOptionsForDescribeInstancesOutput.  # noqa: E501
        :type: int
        """

        self._threads_per_core = threads_per_core

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
        if issubclass(CpuOptionsForDescribeInstancesOutput, dict):
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
        if not isinstance(other, CpuOptionsForDescribeInstancesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CpuOptionsForDescribeInstancesOutput):
            return True

        return self.to_dict() != other.to_dict()
