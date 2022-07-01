# coding: utf-8

"""
    natgateway

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateSnatEntryRequest(object):
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
        'eip_id': 'str',
        'nat_gateway_id': 'str',
        'snat_entry_name': 'str',
        'subnet_id': 'str'
    }

    attribute_map = {
        'eip_id': 'EipId',
        'nat_gateway_id': 'NatGatewayId',
        'snat_entry_name': 'SnatEntryName',
        'subnet_id': 'SubnetId'
    }

    def __init__(self, eip_id=None, nat_gateway_id=None, snat_entry_name=None, subnet_id=None, _configuration=None):  # noqa: E501
        """CreateSnatEntryRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._eip_id = None
        self._nat_gateway_id = None
        self._snat_entry_name = None
        self._subnet_id = None
        self.discriminator = None

        self.eip_id = eip_id
        self.nat_gateway_id = nat_gateway_id
        if snat_entry_name is not None:
            self.snat_entry_name = snat_entry_name
        self.subnet_id = subnet_id

    @property
    def eip_id(self):
        """Gets the eip_id of this CreateSnatEntryRequest.  # noqa: E501


        :return: The eip_id of this CreateSnatEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._eip_id

    @eip_id.setter
    def eip_id(self, eip_id):
        """Sets the eip_id of this CreateSnatEntryRequest.


        :param eip_id: The eip_id of this CreateSnatEntryRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and eip_id is None:
            raise ValueError("Invalid value for `eip_id`, must not be `None`")  # noqa: E501

        self._eip_id = eip_id

    @property
    def nat_gateway_id(self):
        """Gets the nat_gateway_id of this CreateSnatEntryRequest.  # noqa: E501


        :return: The nat_gateway_id of this CreateSnatEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._nat_gateway_id

    @nat_gateway_id.setter
    def nat_gateway_id(self, nat_gateway_id):
        """Sets the nat_gateway_id of this CreateSnatEntryRequest.


        :param nat_gateway_id: The nat_gateway_id of this CreateSnatEntryRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and nat_gateway_id is None:
            raise ValueError("Invalid value for `nat_gateway_id`, must not be `None`")  # noqa: E501

        self._nat_gateway_id = nat_gateway_id

    @property
    def snat_entry_name(self):
        """Gets the snat_entry_name of this CreateSnatEntryRequest.  # noqa: E501


        :return: The snat_entry_name of this CreateSnatEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._snat_entry_name

    @snat_entry_name.setter
    def snat_entry_name(self, snat_entry_name):
        """Sets the snat_entry_name of this CreateSnatEntryRequest.


        :param snat_entry_name: The snat_entry_name of this CreateSnatEntryRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                snat_entry_name is not None and len(snat_entry_name) > 128):
            raise ValueError("Invalid value for `snat_entry_name`, length must be less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                snat_entry_name is not None and len(snat_entry_name) < 1):
            raise ValueError("Invalid value for `snat_entry_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._snat_entry_name = snat_entry_name

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CreateSnatEntryRequest.  # noqa: E501


        :return: The subnet_id of this CreateSnatEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CreateSnatEntryRequest.


        :param subnet_id: The subnet_id of this CreateSnatEntryRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and subnet_id is None:
            raise ValueError("Invalid value for `subnet_id`, must not be `None`")  # noqa: E501

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
        if issubclass(CreateSnatEntryRequest, dict):
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
        if not isinstance(other, CreateSnatEntryRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateSnatEntryRequest):
            return True

        return self.to_dict() != other.to_dict()