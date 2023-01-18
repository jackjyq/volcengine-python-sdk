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


class ProcessorForDescribeInstanceTypesOutput(object):
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
        'base_frequency': 'float',
        'cpus': 'int',
        'model': 'str',
        'turbo_frequency': 'float'
    }

    attribute_map = {
        'base_frequency': 'BaseFrequency',
        'cpus': 'Cpus',
        'model': 'Model',
        'turbo_frequency': 'TurboFrequency'
    }

    def __init__(self, base_frequency=None, cpus=None, model=None, turbo_frequency=None, _configuration=None):  # noqa: E501
        """ProcessorForDescribeInstanceTypesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._base_frequency = None
        self._cpus = None
        self._model = None
        self._turbo_frequency = None
        self.discriminator = None

        if base_frequency is not None:
            self.base_frequency = base_frequency
        if cpus is not None:
            self.cpus = cpus
        if model is not None:
            self.model = model
        if turbo_frequency is not None:
            self.turbo_frequency = turbo_frequency

    @property
    def base_frequency(self):
        """Gets the base_frequency of this ProcessorForDescribeInstanceTypesOutput.  # noqa: E501


        :return: The base_frequency of this ProcessorForDescribeInstanceTypesOutput.  # noqa: E501
        :rtype: float
        """
        return self._base_frequency

    @base_frequency.setter
    def base_frequency(self, base_frequency):
        """Sets the base_frequency of this ProcessorForDescribeInstanceTypesOutput.


        :param base_frequency: The base_frequency of this ProcessorForDescribeInstanceTypesOutput.  # noqa: E501
        :type: float
        """

        self._base_frequency = base_frequency

    @property
    def cpus(self):
        """Gets the cpus of this ProcessorForDescribeInstanceTypesOutput.  # noqa: E501


        :return: The cpus of this ProcessorForDescribeInstanceTypesOutput.  # noqa: E501
        :rtype: int
        """
        return self._cpus

    @cpus.setter
    def cpus(self, cpus):
        """Sets the cpus of this ProcessorForDescribeInstanceTypesOutput.


        :param cpus: The cpus of this ProcessorForDescribeInstanceTypesOutput.  # noqa: E501
        :type: int
        """

        self._cpus = cpus

    @property
    def model(self):
        """Gets the model of this ProcessorForDescribeInstanceTypesOutput.  # noqa: E501


        :return: The model of this ProcessorForDescribeInstanceTypesOutput.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this ProcessorForDescribeInstanceTypesOutput.


        :param model: The model of this ProcessorForDescribeInstanceTypesOutput.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def turbo_frequency(self):
        """Gets the turbo_frequency of this ProcessorForDescribeInstanceTypesOutput.  # noqa: E501


        :return: The turbo_frequency of this ProcessorForDescribeInstanceTypesOutput.  # noqa: E501
        :rtype: float
        """
        return self._turbo_frequency

    @turbo_frequency.setter
    def turbo_frequency(self, turbo_frequency):
        """Sets the turbo_frequency of this ProcessorForDescribeInstanceTypesOutput.


        :param turbo_frequency: The turbo_frequency of this ProcessorForDescribeInstanceTypesOutput.  # noqa: E501
        :type: float
        """

        self._turbo_frequency = turbo_frequency

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
        if issubclass(ProcessorForDescribeInstanceTypesOutput, dict):
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
        if not isinstance(other, ProcessorForDescribeInstanceTypesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProcessorForDescribeInstanceTypesOutput):
            return True

        return self.to_dict() != other.to_dict()
