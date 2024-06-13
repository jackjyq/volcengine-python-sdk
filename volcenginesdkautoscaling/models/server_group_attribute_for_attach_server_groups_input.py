# coding: utf-8

"""
    auto_scaling

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ServerGroupAttributeForAttachServerGroupsInput(object):
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
        'port': 'int',
        'server_group_id': 'str',
        'type': 'str',
        'weight': 'int'
    }

    attribute_map = {
        'port': 'Port',
        'server_group_id': 'ServerGroupId',
        'type': 'Type',
        'weight': 'Weight'
    }

    def __init__(self, port=None, server_group_id=None, type=None, weight=None, _configuration=None):  # noqa: E501
        """ServerGroupAttributeForAttachServerGroupsInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._port = None
        self._server_group_id = None
        self._type = None
        self._weight = None
        self.discriminator = None

        self.port = port
        self.server_group_id = server_group_id
        if type is not None:
            self.type = type
        self.weight = weight

    @property
    def port(self):
        """Gets the port of this ServerGroupAttributeForAttachServerGroupsInput.  # noqa: E501


        :return: The port of this ServerGroupAttributeForAttachServerGroupsInput.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ServerGroupAttributeForAttachServerGroupsInput.


        :param port: The port of this ServerGroupAttributeForAttachServerGroupsInput.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def server_group_id(self):
        """Gets the server_group_id of this ServerGroupAttributeForAttachServerGroupsInput.  # noqa: E501


        :return: The server_group_id of this ServerGroupAttributeForAttachServerGroupsInput.  # noqa: E501
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        """Sets the server_group_id of this ServerGroupAttributeForAttachServerGroupsInput.


        :param server_group_id: The server_group_id of this ServerGroupAttributeForAttachServerGroupsInput.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and server_group_id is None:
            raise ValueError("Invalid value for `server_group_id`, must not be `None`")  # noqa: E501

        self._server_group_id = server_group_id

    @property
    def type(self):
        """Gets the type of this ServerGroupAttributeForAttachServerGroupsInput.  # noqa: E501


        :return: The type of this ServerGroupAttributeForAttachServerGroupsInput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ServerGroupAttributeForAttachServerGroupsInput.


        :param type: The type of this ServerGroupAttributeForAttachServerGroupsInput.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def weight(self):
        """Gets the weight of this ServerGroupAttributeForAttachServerGroupsInput.  # noqa: E501


        :return: The weight of this ServerGroupAttributeForAttachServerGroupsInput.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this ServerGroupAttributeForAttachServerGroupsInput.


        :param weight: The weight of this ServerGroupAttributeForAttachServerGroupsInput.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and weight is None:
            raise ValueError("Invalid value for `weight`, must not be `None`")  # noqa: E501

        self._weight = weight

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
        if issubclass(ServerGroupAttributeForAttachServerGroupsInput, dict):
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
        if not isinstance(other, ServerGroupAttributeForAttachServerGroupsInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServerGroupAttributeForAttachServerGroupsInput):
            return True

        return self.to_dict() != other.to_dict()
