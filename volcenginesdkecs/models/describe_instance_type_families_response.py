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


class DescribeInstanceTypeFamiliesResponse(object):
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
        'instance_type_families': 'list[InstanceTypeFamilyForDescribeInstanceTypeFamiliesOutput]'
    }

    attribute_map = {
        'instance_type_families': 'InstanceTypeFamilies'
    }

    def __init__(self, instance_type_families=None, _configuration=None):  # noqa: E501
        """DescribeInstanceTypeFamiliesResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._instance_type_families = None
        self.discriminator = None

        if instance_type_families is not None:
            self.instance_type_families = instance_type_families

    @property
    def instance_type_families(self):
        """Gets the instance_type_families of this DescribeInstanceTypeFamiliesResponse.  # noqa: E501


        :return: The instance_type_families of this DescribeInstanceTypeFamiliesResponse.  # noqa: E501
        :rtype: list[InstanceTypeFamilyForDescribeInstanceTypeFamiliesOutput]
        """
        return self._instance_type_families

    @instance_type_families.setter
    def instance_type_families(self, instance_type_families):
        """Sets the instance_type_families of this DescribeInstanceTypeFamiliesResponse.


        :param instance_type_families: The instance_type_families of this DescribeInstanceTypeFamiliesResponse.  # noqa: E501
        :type: list[InstanceTypeFamilyForDescribeInstanceTypeFamiliesOutput]
        """

        self._instance_type_families = instance_type_families

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
        if issubclass(DescribeInstanceTypeFamiliesResponse, dict):
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
        if not isinstance(other, DescribeInstanceTypeFamiliesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeInstanceTypeFamiliesResponse):
            return True

        return self.to_dict() != other.to_dict()