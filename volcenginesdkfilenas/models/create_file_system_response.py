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


class CreateFileSystemResponse(object):
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
        'order_no': 'str'
    }

    attribute_map = {
        'file_system_id': 'FileSystemId',
        'order_no': 'OrderNo'
    }

    def __init__(self, file_system_id=None, order_no=None, _configuration=None):  # noqa: E501
        """CreateFileSystemResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._file_system_id = None
        self._order_no = None
        self.discriminator = None

        if file_system_id is not None:
            self.file_system_id = file_system_id
        if order_no is not None:
            self.order_no = order_no

    @property
    def file_system_id(self):
        """Gets the file_system_id of this CreateFileSystemResponse.  # noqa: E501


        :return: The file_system_id of this CreateFileSystemResponse.  # noqa: E501
        :rtype: str
        """
        return self._file_system_id

    @file_system_id.setter
    def file_system_id(self, file_system_id):
        """Sets the file_system_id of this CreateFileSystemResponse.


        :param file_system_id: The file_system_id of this CreateFileSystemResponse.  # noqa: E501
        :type: str
        """

        self._file_system_id = file_system_id

    @property
    def order_no(self):
        """Gets the order_no of this CreateFileSystemResponse.  # noqa: E501


        :return: The order_no of this CreateFileSystemResponse.  # noqa: E501
        :rtype: str
        """
        return self._order_no

    @order_no.setter
    def order_no(self, order_no):
        """Sets the order_no of this CreateFileSystemResponse.


        :param order_no: The order_no of this CreateFileSystemResponse.  # noqa: E501
        :type: str
        """

        self._order_no = order_no

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
        if issubclass(CreateFileSystemResponse, dict):
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
        if not isinstance(other, CreateFileSystemResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateFileSystemResponse):
            return True

        return self.to_dict() != other.to_dict()
