# coding: utf-8

"""
    privatelink

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ZoneForCreateVpcEndpointInput(object):
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
        'private_ip_address': 'str',
        'subnet_id': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'private_ip_address': 'PrivateIpAddress',
        'subnet_id': 'SubnetId',
        'zone_id': 'ZoneId'
    }

    def __init__(self, private_ip_address=None, subnet_id=None, zone_id=None, _configuration=None):  # noqa: E501
        """ZoneForCreateVpcEndpointInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._private_ip_address = None
        self._subnet_id = None
        self._zone_id = None
        self.discriminator = None

        if private_ip_address is not None:
            self.private_ip_address = private_ip_address
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def private_ip_address(self):
        """Gets the private_ip_address of this ZoneForCreateVpcEndpointInput.  # noqa: E501


        :return: The private_ip_address of this ZoneForCreateVpcEndpointInput.  # noqa: E501
        :rtype: str
        """
        return self._private_ip_address

    @private_ip_address.setter
    def private_ip_address(self, private_ip_address):
        """Sets the private_ip_address of this ZoneForCreateVpcEndpointInput.


        :param private_ip_address: The private_ip_address of this ZoneForCreateVpcEndpointInput.  # noqa: E501
        :type: str
        """

        self._private_ip_address = private_ip_address

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ZoneForCreateVpcEndpointInput.  # noqa: E501


        :return: The subnet_id of this ZoneForCreateVpcEndpointInput.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ZoneForCreateVpcEndpointInput.


        :param subnet_id: The subnet_id of this ZoneForCreateVpcEndpointInput.  # noqa: E501
        :type: str
        """

        self._subnet_id = subnet_id

    @property
    def zone_id(self):
        """Gets the zone_id of this ZoneForCreateVpcEndpointInput.  # noqa: E501


        :return: The zone_id of this ZoneForCreateVpcEndpointInput.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this ZoneForCreateVpcEndpointInput.


        :param zone_id: The zone_id of this ZoneForCreateVpcEndpointInput.  # noqa: E501
        :type: str
        """

        self._zone_id = zone_id

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
        if issubclass(ZoneForCreateVpcEndpointInput, dict):
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
        if not isinstance(other, ZoneForCreateVpcEndpointInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ZoneForCreateVpcEndpointInput):
            return True

        return self.to_dict() != other.to_dict()
