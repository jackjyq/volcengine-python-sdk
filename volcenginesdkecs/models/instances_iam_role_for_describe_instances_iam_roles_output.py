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


class InstancesIamRoleForDescribeInstancesIamRolesOutput(object):
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
        'instance_id': 'str',
        'role_names': 'list[str]'
    }

    attribute_map = {
        'instance_id': 'InstanceId',
        'role_names': 'RoleNames'
    }

    def __init__(self, instance_id=None, role_names=None, _configuration=None):  # noqa: E501
        """InstancesIamRoleForDescribeInstancesIamRolesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._instance_id = None
        self._role_names = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if role_names is not None:
            self.role_names = role_names

    @property
    def instance_id(self):
        """Gets the instance_id of this InstancesIamRoleForDescribeInstancesIamRolesOutput.  # noqa: E501


        :return: The instance_id of this InstancesIamRoleForDescribeInstancesIamRolesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this InstancesIamRoleForDescribeInstancesIamRolesOutput.


        :param instance_id: The instance_id of this InstancesIamRoleForDescribeInstancesIamRolesOutput.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def role_names(self):
        """Gets the role_names of this InstancesIamRoleForDescribeInstancesIamRolesOutput.  # noqa: E501


        :return: The role_names of this InstancesIamRoleForDescribeInstancesIamRolesOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._role_names

    @role_names.setter
    def role_names(self, role_names):
        """Sets the role_names of this InstancesIamRoleForDescribeInstancesIamRolesOutput.


        :param role_names: The role_names of this InstancesIamRoleForDescribeInstancesIamRolesOutput.  # noqa: E501
        :type: list[str]
        """

        self._role_names = role_names

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
        if issubclass(InstancesIamRoleForDescribeInstancesIamRolesOutput, dict):
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
        if not isinstance(other, InstancesIamRoleForDescribeInstancesIamRolesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstancesIamRoleForDescribeInstancesIamRolesOutput):
            return True

        return self.to_dict() != other.to_dict()
