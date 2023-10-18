# coding: utf-8

"""
    vedbm

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class AddressForDescribeDBInstanceDetailOutput(object):
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
        'dns_visibility': 'bool',
        'domain': 'str',
        'eip_id': 'str',
        'ip_address': 'str',
        'network_type': 'str',
        'port': 'str',
        'subnet_id': 'str'
    }

    attribute_map = {
        'dns_visibility': 'DNSVisibility',
        'domain': 'Domain',
        'eip_id': 'EipId',
        'ip_address': 'IPAddress',
        'network_type': 'NetworkType',
        'port': 'Port',
        'subnet_id': 'SubnetId'
    }

    def __init__(self, dns_visibility=None, domain=None, eip_id=None, ip_address=None, network_type=None, port=None, subnet_id=None, _configuration=None):  # noqa: E501
        """AddressForDescribeDBInstanceDetailOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._dns_visibility = None
        self._domain = None
        self._eip_id = None
        self._ip_address = None
        self._network_type = None
        self._port = None
        self._subnet_id = None
        self.discriminator = None

        if dns_visibility is not None:
            self.dns_visibility = dns_visibility
        if domain is not None:
            self.domain = domain
        if eip_id is not None:
            self.eip_id = eip_id
        if ip_address is not None:
            self.ip_address = ip_address
        if network_type is not None:
            self.network_type = network_type
        if port is not None:
            self.port = port
        if subnet_id is not None:
            self.subnet_id = subnet_id

    @property
    def dns_visibility(self):
        """Gets the dns_visibility of this AddressForDescribeDBInstanceDetailOutput.  # noqa: E501


        :return: The dns_visibility of this AddressForDescribeDBInstanceDetailOutput.  # noqa: E501
        :rtype: bool
        """
        return self._dns_visibility

    @dns_visibility.setter
    def dns_visibility(self, dns_visibility):
        """Sets the dns_visibility of this AddressForDescribeDBInstanceDetailOutput.


        :param dns_visibility: The dns_visibility of this AddressForDescribeDBInstanceDetailOutput.  # noqa: E501
        :type: bool
        """

        self._dns_visibility = dns_visibility

    @property
    def domain(self):
        """Gets the domain of this AddressForDescribeDBInstanceDetailOutput.  # noqa: E501


        :return: The domain of this AddressForDescribeDBInstanceDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this AddressForDescribeDBInstanceDetailOutput.


        :param domain: The domain of this AddressForDescribeDBInstanceDetailOutput.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def eip_id(self):
        """Gets the eip_id of this AddressForDescribeDBInstanceDetailOutput.  # noqa: E501


        :return: The eip_id of this AddressForDescribeDBInstanceDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._eip_id

    @eip_id.setter
    def eip_id(self, eip_id):
        """Sets the eip_id of this AddressForDescribeDBInstanceDetailOutput.


        :param eip_id: The eip_id of this AddressForDescribeDBInstanceDetailOutput.  # noqa: E501
        :type: str
        """

        self._eip_id = eip_id

    @property
    def ip_address(self):
        """Gets the ip_address of this AddressForDescribeDBInstanceDetailOutput.  # noqa: E501


        :return: The ip_address of this AddressForDescribeDBInstanceDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this AddressForDescribeDBInstanceDetailOutput.


        :param ip_address: The ip_address of this AddressForDescribeDBInstanceDetailOutput.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def network_type(self):
        """Gets the network_type of this AddressForDescribeDBInstanceDetailOutput.  # noqa: E501


        :return: The network_type of this AddressForDescribeDBInstanceDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """Sets the network_type of this AddressForDescribeDBInstanceDetailOutput.


        :param network_type: The network_type of this AddressForDescribeDBInstanceDetailOutput.  # noqa: E501
        :type: str
        """

        self._network_type = network_type

    @property
    def port(self):
        """Gets the port of this AddressForDescribeDBInstanceDetailOutput.  # noqa: E501


        :return: The port of this AddressForDescribeDBInstanceDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this AddressForDescribeDBInstanceDetailOutput.


        :param port: The port of this AddressForDescribeDBInstanceDetailOutput.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def subnet_id(self):
        """Gets the subnet_id of this AddressForDescribeDBInstanceDetailOutput.  # noqa: E501


        :return: The subnet_id of this AddressForDescribeDBInstanceDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this AddressForDescribeDBInstanceDetailOutput.


        :param subnet_id: The subnet_id of this AddressForDescribeDBInstanceDetailOutput.  # noqa: E501
        :type: str
        """

        self._subnet_id = subnet_id

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
        if issubclass(AddressForDescribeDBInstanceDetailOutput, dict):
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
        if not isinstance(other, AddressForDescribeDBInstanceDetailOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddressForDescribeDBInstanceDetailOutput):
            return True

        return self.to_dict() != other.to_dict()
