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


class UpdateMountPointRequest(object):
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
        'file_system_id': 'str',
        'mount_point_id': 'str',
        'mount_point_name': 'str',
        'permission_group_id': 'str'
    }

    attribute_map = {
        'file_system_id': 'FileSystemId',
        'mount_point_id': 'MountPointId',
        'mount_point_name': 'MountPointName',
        'permission_group_id': 'PermissionGroupId'
    }

    def __init__(self, file_system_id=None, mount_point_id=None, mount_point_name=None, permission_group_id=None, _configuration=None):  # noqa: E501
        """UpdateMountPointRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._file_system_id = None
        self._mount_point_id = None
        self._mount_point_name = None
        self._permission_group_id = None
        self.discriminator = None

        if file_system_id is not None:
            self.file_system_id = file_system_id
        if mount_point_id is not None:
            self.mount_point_id = mount_point_id
        if mount_point_name is not None:
            self.mount_point_name = mount_point_name
        if permission_group_id is not None:
            self.permission_group_id = permission_group_id

    @property
    def file_system_id(self):
        """Gets the file_system_id of this UpdateMountPointRequest.  # noqa: E501


        :return: The file_system_id of this UpdateMountPointRequest.  # noqa: E501
        :rtype: str
        """
        return self._file_system_id

    @file_system_id.setter
    def file_system_id(self, file_system_id):
        """Sets the file_system_id of this UpdateMountPointRequest.


        :param file_system_id: The file_system_id of this UpdateMountPointRequest.  # noqa: E501
        :type: str
        """

        self._file_system_id = file_system_id

    @property
    def mount_point_id(self):
        """Gets the mount_point_id of this UpdateMountPointRequest.  # noqa: E501


        :return: The mount_point_id of this UpdateMountPointRequest.  # noqa: E501
        :rtype: str
        """
        return self._mount_point_id

    @mount_point_id.setter
    def mount_point_id(self, mount_point_id):
        """Sets the mount_point_id of this UpdateMountPointRequest.


        :param mount_point_id: The mount_point_id of this UpdateMountPointRequest.  # noqa: E501
        :type: str
        """

        self._mount_point_id = mount_point_id

    @property
    def mount_point_name(self):
        """Gets the mount_point_name of this UpdateMountPointRequest.  # noqa: E501


        :return: The mount_point_name of this UpdateMountPointRequest.  # noqa: E501
        :rtype: str
        """
        return self._mount_point_name

    @mount_point_name.setter
    def mount_point_name(self, mount_point_name):
        """Sets the mount_point_name of this UpdateMountPointRequest.


        :param mount_point_name: The mount_point_name of this UpdateMountPointRequest.  # noqa: E501
        :type: str
        """

        self._mount_point_name = mount_point_name

    @property
    def permission_group_id(self):
        """Gets the permission_group_id of this UpdateMountPointRequest.  # noqa: E501


        :return: The permission_group_id of this UpdateMountPointRequest.  # noqa: E501
        :rtype: str
        """
        return self._permission_group_id

    @permission_group_id.setter
    def permission_group_id(self, permission_group_id):
        """Sets the permission_group_id of this UpdateMountPointRequest.


        :param permission_group_id: The permission_group_id of this UpdateMountPointRequest.  # noqa: E501
        :type: str
        """

        self._permission_group_id = permission_group_id

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
        if issubclass(UpdateMountPointRequest, dict):
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
        if not isinstance(other, UpdateMountPointRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateMountPointRequest):
            return True

        return self.to_dict() != other.to_dict()
