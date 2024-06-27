# coding: utf-8

"""
    vefaas

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class MountPointForUpdateFunctionInput(object):
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
        'bucket_name': 'str',
        'bucket_path': 'str',
        'endpoint': 'str',
        'local_mount_path': 'str',
        'read_only': 'bool'
    }

    attribute_map = {
        'bucket_name': 'BucketName',
        'bucket_path': 'BucketPath',
        'endpoint': 'Endpoint',
        'local_mount_path': 'LocalMountPath',
        'read_only': 'ReadOnly'
    }

    def __init__(self, bucket_name=None, bucket_path=None, endpoint=None, local_mount_path=None, read_only=None, _configuration=None):  # noqa: E501
        """MountPointForUpdateFunctionInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bucket_name = None
        self._bucket_path = None
        self._endpoint = None
        self._local_mount_path = None
        self._read_only = None
        self.discriminator = None

        if bucket_name is not None:
            self.bucket_name = bucket_name
        if bucket_path is not None:
            self.bucket_path = bucket_path
        if endpoint is not None:
            self.endpoint = endpoint
        if local_mount_path is not None:
            self.local_mount_path = local_mount_path
        if read_only is not None:
            self.read_only = read_only

    @property
    def bucket_name(self):
        """Gets the bucket_name of this MountPointForUpdateFunctionInput.  # noqa: E501


        :return: The bucket_name of this MountPointForUpdateFunctionInput.  # noqa: E501
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this MountPointForUpdateFunctionInput.


        :param bucket_name: The bucket_name of this MountPointForUpdateFunctionInput.  # noqa: E501
        :type: str
        """

        self._bucket_name = bucket_name

    @property
    def bucket_path(self):
        """Gets the bucket_path of this MountPointForUpdateFunctionInput.  # noqa: E501


        :return: The bucket_path of this MountPointForUpdateFunctionInput.  # noqa: E501
        :rtype: str
        """
        return self._bucket_path

    @bucket_path.setter
    def bucket_path(self, bucket_path):
        """Sets the bucket_path of this MountPointForUpdateFunctionInput.


        :param bucket_path: The bucket_path of this MountPointForUpdateFunctionInput.  # noqa: E501
        :type: str
        """

        self._bucket_path = bucket_path

    @property
    def endpoint(self):
        """Gets the endpoint of this MountPointForUpdateFunctionInput.  # noqa: E501


        :return: The endpoint of this MountPointForUpdateFunctionInput.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this MountPointForUpdateFunctionInput.


        :param endpoint: The endpoint of this MountPointForUpdateFunctionInput.  # noqa: E501
        :type: str
        """

        self._endpoint = endpoint

    @property
    def local_mount_path(self):
        """Gets the local_mount_path of this MountPointForUpdateFunctionInput.  # noqa: E501


        :return: The local_mount_path of this MountPointForUpdateFunctionInput.  # noqa: E501
        :rtype: str
        """
        return self._local_mount_path

    @local_mount_path.setter
    def local_mount_path(self, local_mount_path):
        """Sets the local_mount_path of this MountPointForUpdateFunctionInput.


        :param local_mount_path: The local_mount_path of this MountPointForUpdateFunctionInput.  # noqa: E501
        :type: str
        """

        self._local_mount_path = local_mount_path

    @property
    def read_only(self):
        """Gets the read_only of this MountPointForUpdateFunctionInput.  # noqa: E501


        :return: The read_only of this MountPointForUpdateFunctionInput.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this MountPointForUpdateFunctionInput.


        :param read_only: The read_only of this MountPointForUpdateFunctionInput.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

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
        if issubclass(MountPointForUpdateFunctionInput, dict):
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
        if not isinstance(other, MountPointForUpdateFunctionInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MountPointForUpdateFunctionInput):
            return True

        return self.to_dict() != other.to_dict()
