# coding: utf-8

"""
    filenas

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class PermissionGroupForDescribeMountPointsOutput(object):
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
        'create_time': 'str',
        'description': 'str',
        'file_system_count': 'int',
        'file_system_type': 'str',
        'mount_points': 'list[MountPointForDescribeMountPointsOutput]',
        'permission_group_id': 'str',
        'permission_group_name': 'str',
        'permission_rule_count': 'int'
    }

    attribute_map = {
        'create_time': 'CreateTime',
        'description': 'Description',
        'file_system_count': 'FileSystemCount',
        'file_system_type': 'FileSystemType',
        'mount_points': 'MountPoints',
        'permission_group_id': 'PermissionGroupId',
        'permission_group_name': 'PermissionGroupName',
        'permission_rule_count': 'PermissionRuleCount'
    }

    def __init__(self, create_time=None, description=None, file_system_count=None, file_system_type=None, mount_points=None, permission_group_id=None, permission_group_name=None, permission_rule_count=None, _configuration=None):  # noqa: E501
        """PermissionGroupForDescribeMountPointsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._create_time = None
        self._description = None
        self._file_system_count = None
        self._file_system_type = None
        self._mount_points = None
        self._permission_group_id = None
        self._permission_group_name = None
        self._permission_rule_count = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if description is not None:
            self.description = description
        if file_system_count is not None:
            self.file_system_count = file_system_count
        if file_system_type is not None:
            self.file_system_type = file_system_type
        if mount_points is not None:
            self.mount_points = mount_points
        if permission_group_id is not None:
            self.permission_group_id = permission_group_id
        if permission_group_name is not None:
            self.permission_group_name = permission_group_name
        if permission_rule_count is not None:
            self.permission_rule_count = permission_rule_count

    @property
    def create_time(self):
        """Gets the create_time of this PermissionGroupForDescribeMountPointsOutput.  # noqa: E501


        :return: The create_time of this PermissionGroupForDescribeMountPointsOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this PermissionGroupForDescribeMountPointsOutput.


        :param create_time: The create_time of this PermissionGroupForDescribeMountPointsOutput.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def description(self):
        """Gets the description of this PermissionGroupForDescribeMountPointsOutput.  # noqa: E501


        :return: The description of this PermissionGroupForDescribeMountPointsOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PermissionGroupForDescribeMountPointsOutput.


        :param description: The description of this PermissionGroupForDescribeMountPointsOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def file_system_count(self):
        """Gets the file_system_count of this PermissionGroupForDescribeMountPointsOutput.  # noqa: E501


        :return: The file_system_count of this PermissionGroupForDescribeMountPointsOutput.  # noqa: E501
        :rtype: int
        """
        return self._file_system_count

    @file_system_count.setter
    def file_system_count(self, file_system_count):
        """Sets the file_system_count of this PermissionGroupForDescribeMountPointsOutput.


        :param file_system_count: The file_system_count of this PermissionGroupForDescribeMountPointsOutput.  # noqa: E501
        :type: int
        """

        self._file_system_count = file_system_count

    @property
    def file_system_type(self):
        """Gets the file_system_type of this PermissionGroupForDescribeMountPointsOutput.  # noqa: E501


        :return: The file_system_type of this PermissionGroupForDescribeMountPointsOutput.  # noqa: E501
        :rtype: str
        """
        return self._file_system_type

    @file_system_type.setter
    def file_system_type(self, file_system_type):
        """Sets the file_system_type of this PermissionGroupForDescribeMountPointsOutput.


        :param file_system_type: The file_system_type of this PermissionGroupForDescribeMountPointsOutput.  # noqa: E501
        :type: str
        """

        self._file_system_type = file_system_type

    @property
    def mount_points(self):
        """Gets the mount_points of this PermissionGroupForDescribeMountPointsOutput.  # noqa: E501


        :return: The mount_points of this PermissionGroupForDescribeMountPointsOutput.  # noqa: E501
        :rtype: list[MountPointForDescribeMountPointsOutput]
        """
        return self._mount_points

    @mount_points.setter
    def mount_points(self, mount_points):
        """Sets the mount_points of this PermissionGroupForDescribeMountPointsOutput.


        :param mount_points: The mount_points of this PermissionGroupForDescribeMountPointsOutput.  # noqa: E501
        :type: list[MountPointForDescribeMountPointsOutput]
        """

        self._mount_points = mount_points

    @property
    def permission_group_id(self):
        """Gets the permission_group_id of this PermissionGroupForDescribeMountPointsOutput.  # noqa: E501


        :return: The permission_group_id of this PermissionGroupForDescribeMountPointsOutput.  # noqa: E501
        :rtype: str
        """
        return self._permission_group_id

    @permission_group_id.setter
    def permission_group_id(self, permission_group_id):
        """Sets the permission_group_id of this PermissionGroupForDescribeMountPointsOutput.


        :param permission_group_id: The permission_group_id of this PermissionGroupForDescribeMountPointsOutput.  # noqa: E501
        :type: str
        """

        self._permission_group_id = permission_group_id

    @property
    def permission_group_name(self):
        """Gets the permission_group_name of this PermissionGroupForDescribeMountPointsOutput.  # noqa: E501


        :return: The permission_group_name of this PermissionGroupForDescribeMountPointsOutput.  # noqa: E501
        :rtype: str
        """
        return self._permission_group_name

    @permission_group_name.setter
    def permission_group_name(self, permission_group_name):
        """Sets the permission_group_name of this PermissionGroupForDescribeMountPointsOutput.


        :param permission_group_name: The permission_group_name of this PermissionGroupForDescribeMountPointsOutput.  # noqa: E501
        :type: str
        """

        self._permission_group_name = permission_group_name

    @property
    def permission_rule_count(self):
        """Gets the permission_rule_count of this PermissionGroupForDescribeMountPointsOutput.  # noqa: E501


        :return: The permission_rule_count of this PermissionGroupForDescribeMountPointsOutput.  # noqa: E501
        :rtype: int
        """
        return self._permission_rule_count

    @permission_rule_count.setter
    def permission_rule_count(self, permission_rule_count):
        """Sets the permission_rule_count of this PermissionGroupForDescribeMountPointsOutput.


        :param permission_rule_count: The permission_rule_count of this PermissionGroupForDescribeMountPointsOutput.  # noqa: E501
        :type: int
        """

        self._permission_rule_count = permission_rule_count

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
        if issubclass(PermissionGroupForDescribeMountPointsOutput, dict):
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
        if not isinstance(other, PermissionGroupForDescribeMountPointsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PermissionGroupForDescribeMountPointsOutput):
            return True

        return self.to_dict() != other.to_dict()
