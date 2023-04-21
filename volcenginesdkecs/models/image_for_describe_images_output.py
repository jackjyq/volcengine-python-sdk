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


class ImageForDescribeImagesOutput(object):
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
        'architecture': 'str',
        'boot_mode': 'str',
        'created_at': 'str',
        'description': 'str',
        'image_id': 'str',
        'image_name': 'str',
        'image_owner_id': 'str',
        'is_support_cloud_init': 'bool',
        'os_name': 'str',
        'os_type': 'str',
        'platform': 'str',
        'platform_version': 'str',
        'project_name': 'str',
        'share_status': 'str',
        'size': 'int',
        'status': 'str',
        'updated_at': 'str',
        'virtual_size': 'str',
        'visibility': 'str'
    }

    attribute_map = {
        'architecture': 'Architecture',
        'boot_mode': 'BootMode',
        'created_at': 'CreatedAt',
        'description': 'Description',
        'image_id': 'ImageId',
        'image_name': 'ImageName',
        'image_owner_id': 'ImageOwnerId',
        'is_support_cloud_init': 'IsSupportCloudInit',
        'os_name': 'OsName',
        'os_type': 'OsType',
        'platform': 'Platform',
        'platform_version': 'PlatformVersion',
        'project_name': 'ProjectName',
        'share_status': 'ShareStatus',
        'size': 'Size',
        'status': 'Status',
        'updated_at': 'UpdatedAt',
        'virtual_size': 'VirtualSize',
        'visibility': 'Visibility'
    }

    def __init__(self, architecture=None, boot_mode=None, created_at=None, description=None, image_id=None, image_name=None, image_owner_id=None, is_support_cloud_init=None, os_name=None, os_type=None, platform=None, platform_version=None, project_name=None, share_status=None, size=None, status=None, updated_at=None, virtual_size=None, visibility=None, _configuration=None):  # noqa: E501
        """ImageForDescribeImagesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._architecture = None
        self._boot_mode = None
        self._created_at = None
        self._description = None
        self._image_id = None
        self._image_name = None
        self._image_owner_id = None
        self._is_support_cloud_init = None
        self._os_name = None
        self._os_type = None
        self._platform = None
        self._platform_version = None
        self._project_name = None
        self._share_status = None
        self._size = None
        self._status = None
        self._updated_at = None
        self._virtual_size = None
        self._visibility = None
        self.discriminator = None

        if architecture is not None:
            self.architecture = architecture
        if boot_mode is not None:
            self.boot_mode = boot_mode
        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if image_id is not None:
            self.image_id = image_id
        if image_name is not None:
            self.image_name = image_name
        if image_owner_id is not None:
            self.image_owner_id = image_owner_id
        if is_support_cloud_init is not None:
            self.is_support_cloud_init = is_support_cloud_init
        if os_name is not None:
            self.os_name = os_name
        if os_type is not None:
            self.os_type = os_type
        if platform is not None:
            self.platform = platform
        if platform_version is not None:
            self.platform_version = platform_version
        if project_name is not None:
            self.project_name = project_name
        if share_status is not None:
            self.share_status = share_status
        if size is not None:
            self.size = size
        if status is not None:
            self.status = status
        if updated_at is not None:
            self.updated_at = updated_at
        if virtual_size is not None:
            self.virtual_size = virtual_size
        if visibility is not None:
            self.visibility = visibility

    @property
    def architecture(self):
        """Gets the architecture of this ImageForDescribeImagesOutput.  # noqa: E501


        :return: The architecture of this ImageForDescribeImagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """Sets the architecture of this ImageForDescribeImagesOutput.


        :param architecture: The architecture of this ImageForDescribeImagesOutput.  # noqa: E501
        :type: str
        """

        self._architecture = architecture

    @property
    def boot_mode(self):
        """Gets the boot_mode of this ImageForDescribeImagesOutput.  # noqa: E501


        :return: The boot_mode of this ImageForDescribeImagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._boot_mode

    @boot_mode.setter
    def boot_mode(self, boot_mode):
        """Sets the boot_mode of this ImageForDescribeImagesOutput.


        :param boot_mode: The boot_mode of this ImageForDescribeImagesOutput.  # noqa: E501
        :type: str
        """

        self._boot_mode = boot_mode

    @property
    def created_at(self):
        """Gets the created_at of this ImageForDescribeImagesOutput.  # noqa: E501


        :return: The created_at of this ImageForDescribeImagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ImageForDescribeImagesOutput.


        :param created_at: The created_at of this ImageForDescribeImagesOutput.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this ImageForDescribeImagesOutput.  # noqa: E501


        :return: The description of this ImageForDescribeImagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ImageForDescribeImagesOutput.


        :param description: The description of this ImageForDescribeImagesOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def image_id(self):
        """Gets the image_id of this ImageForDescribeImagesOutput.  # noqa: E501


        :return: The image_id of this ImageForDescribeImagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ImageForDescribeImagesOutput.


        :param image_id: The image_id of this ImageForDescribeImagesOutput.  # noqa: E501
        :type: str
        """

        self._image_id = image_id

    @property
    def image_name(self):
        """Gets the image_name of this ImageForDescribeImagesOutput.  # noqa: E501


        :return: The image_name of this ImageForDescribeImagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this ImageForDescribeImagesOutput.


        :param image_name: The image_name of this ImageForDescribeImagesOutput.  # noqa: E501
        :type: str
        """

        self._image_name = image_name

    @property
    def image_owner_id(self):
        """Gets the image_owner_id of this ImageForDescribeImagesOutput.  # noqa: E501


        :return: The image_owner_id of this ImageForDescribeImagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._image_owner_id

    @image_owner_id.setter
    def image_owner_id(self, image_owner_id):
        """Sets the image_owner_id of this ImageForDescribeImagesOutput.


        :param image_owner_id: The image_owner_id of this ImageForDescribeImagesOutput.  # noqa: E501
        :type: str
        """

        self._image_owner_id = image_owner_id

    @property
    def is_support_cloud_init(self):
        """Gets the is_support_cloud_init of this ImageForDescribeImagesOutput.  # noqa: E501


        :return: The is_support_cloud_init of this ImageForDescribeImagesOutput.  # noqa: E501
        :rtype: bool
        """
        return self._is_support_cloud_init

    @is_support_cloud_init.setter
    def is_support_cloud_init(self, is_support_cloud_init):
        """Sets the is_support_cloud_init of this ImageForDescribeImagesOutput.


        :param is_support_cloud_init: The is_support_cloud_init of this ImageForDescribeImagesOutput.  # noqa: E501
        :type: bool
        """

        self._is_support_cloud_init = is_support_cloud_init

    @property
    def os_name(self):
        """Gets the os_name of this ImageForDescribeImagesOutput.  # noqa: E501


        :return: The os_name of this ImageForDescribeImagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        """Sets the os_name of this ImageForDescribeImagesOutput.


        :param os_name: The os_name of this ImageForDescribeImagesOutput.  # noqa: E501
        :type: str
        """

        self._os_name = os_name

    @property
    def os_type(self):
        """Gets the os_type of this ImageForDescribeImagesOutput.  # noqa: E501


        :return: The os_type of this ImageForDescribeImagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this ImageForDescribeImagesOutput.


        :param os_type: The os_type of this ImageForDescribeImagesOutput.  # noqa: E501
        :type: str
        """

        self._os_type = os_type

    @property
    def platform(self):
        """Gets the platform of this ImageForDescribeImagesOutput.  # noqa: E501


        :return: The platform of this ImageForDescribeImagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this ImageForDescribeImagesOutput.


        :param platform: The platform of this ImageForDescribeImagesOutput.  # noqa: E501
        :type: str
        """

        self._platform = platform

    @property
    def platform_version(self):
        """Gets the platform_version of this ImageForDescribeImagesOutput.  # noqa: E501


        :return: The platform_version of this ImageForDescribeImagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._platform_version

    @platform_version.setter
    def platform_version(self, platform_version):
        """Sets the platform_version of this ImageForDescribeImagesOutput.


        :param platform_version: The platform_version of this ImageForDescribeImagesOutput.  # noqa: E501
        :type: str
        """

        self._platform_version = platform_version

    @property
    def project_name(self):
        """Gets the project_name of this ImageForDescribeImagesOutput.  # noqa: E501


        :return: The project_name of this ImageForDescribeImagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ImageForDescribeImagesOutput.


        :param project_name: The project_name of this ImageForDescribeImagesOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def share_status(self):
        """Gets the share_status of this ImageForDescribeImagesOutput.  # noqa: E501


        :return: The share_status of this ImageForDescribeImagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._share_status

    @share_status.setter
    def share_status(self, share_status):
        """Sets the share_status of this ImageForDescribeImagesOutput.


        :param share_status: The share_status of this ImageForDescribeImagesOutput.  # noqa: E501
        :type: str
        """

        self._share_status = share_status

    @property
    def size(self):
        """Gets the size of this ImageForDescribeImagesOutput.  # noqa: E501


        :return: The size of this ImageForDescribeImagesOutput.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ImageForDescribeImagesOutput.


        :param size: The size of this ImageForDescribeImagesOutput.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def status(self):
        """Gets the status of this ImageForDescribeImagesOutput.  # noqa: E501


        :return: The status of this ImageForDescribeImagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ImageForDescribeImagesOutput.


        :param status: The status of this ImageForDescribeImagesOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def updated_at(self):
        """Gets the updated_at of this ImageForDescribeImagesOutput.  # noqa: E501


        :return: The updated_at of this ImageForDescribeImagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ImageForDescribeImagesOutput.


        :param updated_at: The updated_at of this ImageForDescribeImagesOutput.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def virtual_size(self):
        """Gets the virtual_size of this ImageForDescribeImagesOutput.  # noqa: E501


        :return: The virtual_size of this ImageForDescribeImagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._virtual_size

    @virtual_size.setter
    def virtual_size(self, virtual_size):
        """Sets the virtual_size of this ImageForDescribeImagesOutput.


        :param virtual_size: The virtual_size of this ImageForDescribeImagesOutput.  # noqa: E501
        :type: str
        """

        self._virtual_size = virtual_size

    @property
    def visibility(self):
        """Gets the visibility of this ImageForDescribeImagesOutput.  # noqa: E501


        :return: The visibility of this ImageForDescribeImagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this ImageForDescribeImagesOutput.


        :param visibility: The visibility of this ImageForDescribeImagesOutput.  # noqa: E501
        :type: str
        """

        self._visibility = visibility

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
        if issubclass(ImageForDescribeImagesOutput, dict):
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
        if not isinstance(other, ImageForDescribeImagesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImageForDescribeImagesOutput):
            return True

        return self.to_dict() != other.to_dict()
