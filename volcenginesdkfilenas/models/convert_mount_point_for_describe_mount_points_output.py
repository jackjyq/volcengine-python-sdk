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


class ConvertMountPointForDescribeMountPointsOutput(object):
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
        'domain': 'str',
        'ip': 'str',
        'mount_point_id': 'str',
        'mount_point_name': 'str',
        'permission_group': 'PermissionGroupForDescribeMountPointsOutput',
        'status': 'str',
        'subnet_id': 'str',
        'subnet_name': 'str',
        'update_time': 'str',
        'vpc_id': 'str',
        'vpc_name': 'str'
    }

    attribute_map = {
        'create_time': 'CreateTime',
        'domain': 'Domain',
        'ip': 'Ip',
        'mount_point_id': 'MountPointId',
        'mount_point_name': 'MountPointName',
        'permission_group': 'PermissionGroup',
        'status': 'Status',
        'subnet_id': 'SubnetId',
        'subnet_name': 'SubnetName',
        'update_time': 'UpdateTime',
        'vpc_id': 'VpcId',
        'vpc_name': 'VpcName'
    }

    def __init__(self, create_time=None, domain=None, ip=None, mount_point_id=None, mount_point_name=None, permission_group=None, status=None, subnet_id=None, subnet_name=None, update_time=None, vpc_id=None, vpc_name=None, _configuration=None):  # noqa: E501
        """ConvertMountPointForDescribeMountPointsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._create_time = None
        self._domain = None
        self._ip = None
        self._mount_point_id = None
        self._mount_point_name = None
        self._permission_group = None
        self._status = None
        self._subnet_id = None
        self._subnet_name = None
        self._update_time = None
        self._vpc_id = None
        self._vpc_name = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if domain is not None:
            self.domain = domain
        if ip is not None:
            self.ip = ip
        if mount_point_id is not None:
            self.mount_point_id = mount_point_id
        if mount_point_name is not None:
            self.mount_point_name = mount_point_name
        if permission_group is not None:
            self.permission_group = permission_group
        if status is not None:
            self.status = status
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if subnet_name is not None:
            self.subnet_name = subnet_name
        if update_time is not None:
            self.update_time = update_time
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if vpc_name is not None:
            self.vpc_name = vpc_name

    @property
    def create_time(self):
        """Gets the create_time of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501


        :return: The create_time of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ConvertMountPointForDescribeMountPointsOutput.


        :param create_time: The create_time of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def domain(self):
        """Gets the domain of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501


        :return: The domain of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ConvertMountPointForDescribeMountPointsOutput.


        :param domain: The domain of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def ip(self):
        """Gets the ip of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501


        :return: The ip of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ConvertMountPointForDescribeMountPointsOutput.


        :param ip: The ip of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def mount_point_id(self):
        """Gets the mount_point_id of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501


        :return: The mount_point_id of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501
        :rtype: str
        """
        return self._mount_point_id

    @mount_point_id.setter
    def mount_point_id(self, mount_point_id):
        """Sets the mount_point_id of this ConvertMountPointForDescribeMountPointsOutput.


        :param mount_point_id: The mount_point_id of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501
        :type: str
        """

        self._mount_point_id = mount_point_id

    @property
    def mount_point_name(self):
        """Gets the mount_point_name of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501


        :return: The mount_point_name of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501
        :rtype: str
        """
        return self._mount_point_name

    @mount_point_name.setter
    def mount_point_name(self, mount_point_name):
        """Sets the mount_point_name of this ConvertMountPointForDescribeMountPointsOutput.


        :param mount_point_name: The mount_point_name of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501
        :type: str
        """

        self._mount_point_name = mount_point_name

    @property
    def permission_group(self):
        """Gets the permission_group of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501


        :return: The permission_group of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501
        :rtype: PermissionGroupForDescribeMountPointsOutput
        """
        return self._permission_group

    @permission_group.setter
    def permission_group(self, permission_group):
        """Sets the permission_group of this ConvertMountPointForDescribeMountPointsOutput.


        :param permission_group: The permission_group of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501
        :type: PermissionGroupForDescribeMountPointsOutput
        """

        self._permission_group = permission_group

    @property
    def status(self):
        """Gets the status of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501


        :return: The status of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ConvertMountPointForDescribeMountPointsOutput.


        :param status: The status of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501


        :return: The subnet_id of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ConvertMountPointForDescribeMountPointsOutput.


        :param subnet_id: The subnet_id of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501
        :type: str
        """

        self._subnet_id = subnet_id

    @property
    def subnet_name(self):
        """Gets the subnet_name of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501


        :return: The subnet_name of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501
        :rtype: str
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, subnet_name):
        """Sets the subnet_name of this ConvertMountPointForDescribeMountPointsOutput.


        :param subnet_name: The subnet_name of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501
        :type: str
        """

        self._subnet_name = subnet_name

    @property
    def update_time(self):
        """Gets the update_time of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501


        :return: The update_time of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ConvertMountPointForDescribeMountPointsOutput.


        :param update_time: The update_time of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501


        :return: The vpc_id of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ConvertMountPointForDescribeMountPointsOutput.


        :param vpc_id: The vpc_id of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

    @property
    def vpc_name(self):
        """Gets the vpc_name of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501


        :return: The vpc_name of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        """Sets the vpc_name of this ConvertMountPointForDescribeMountPointsOutput.


        :param vpc_name: The vpc_name of this ConvertMountPointForDescribeMountPointsOutput.  # noqa: E501
        :type: str
        """

        self._vpc_name = vpc_name

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
        if issubclass(ConvertMountPointForDescribeMountPointsOutput, dict):
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
        if not isinstance(other, ConvertMountPointForDescribeMountPointsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConvertMountPointForDescribeMountPointsOutput):
            return True

        return self.to_dict() != other.to_dict()