# coding: utf-8

"""
    vpn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeVpnConnectionsRequest(object):
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
        'customer_gateway_id': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'vpn_connection_ids': 'list[str]',
        'vpn_connection_name': 'str',
        'vpn_gateway_id': 'str'
    }

    attribute_map = {
        'customer_gateway_id': 'CustomerGatewayId',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'vpn_connection_ids': 'VpnConnectionIds',
        'vpn_connection_name': 'VpnConnectionName',
        'vpn_gateway_id': 'VpnGatewayId'
    }

    def __init__(self, customer_gateway_id=None, page_number=None, page_size=None, vpn_connection_ids=None, vpn_connection_name=None, vpn_gateway_id=None, _configuration=None):  # noqa: E501
        """DescribeVpnConnectionsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._customer_gateway_id = None
        self._page_number = None
        self._page_size = None
        self._vpn_connection_ids = None
        self._vpn_connection_name = None
        self._vpn_gateway_id = None
        self.discriminator = None

        if customer_gateway_id is not None:
            self.customer_gateway_id = customer_gateway_id
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if vpn_connection_ids is not None:
            self.vpn_connection_ids = vpn_connection_ids
        if vpn_connection_name is not None:
            self.vpn_connection_name = vpn_connection_name
        if vpn_gateway_id is not None:
            self.vpn_gateway_id = vpn_gateway_id

    @property
    def customer_gateway_id(self):
        """Gets the customer_gateway_id of this DescribeVpnConnectionsRequest.  # noqa: E501


        :return: The customer_gateway_id of this DescribeVpnConnectionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._customer_gateway_id

    @customer_gateway_id.setter
    def customer_gateway_id(self, customer_gateway_id):
        """Sets the customer_gateway_id of this DescribeVpnConnectionsRequest.


        :param customer_gateway_id: The customer_gateway_id of this DescribeVpnConnectionsRequest.  # noqa: E501
        :type: str
        """

        self._customer_gateway_id = customer_gateway_id

    @property
    def page_number(self):
        """Gets the page_number of this DescribeVpnConnectionsRequest.  # noqa: E501


        :return: The page_number of this DescribeVpnConnectionsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeVpnConnectionsRequest.


        :param page_number: The page_number of this DescribeVpnConnectionsRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeVpnConnectionsRequest.  # noqa: E501


        :return: The page_size of this DescribeVpnConnectionsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeVpnConnectionsRequest.


        :param page_size: The page_size of this DescribeVpnConnectionsRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def vpn_connection_ids(self):
        """Gets the vpn_connection_ids of this DescribeVpnConnectionsRequest.  # noqa: E501


        :return: The vpn_connection_ids of this DescribeVpnConnectionsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._vpn_connection_ids

    @vpn_connection_ids.setter
    def vpn_connection_ids(self, vpn_connection_ids):
        """Sets the vpn_connection_ids of this DescribeVpnConnectionsRequest.


        :param vpn_connection_ids: The vpn_connection_ids of this DescribeVpnConnectionsRequest.  # noqa: E501
        :type: list[str]
        """

        self._vpn_connection_ids = vpn_connection_ids

    @property
    def vpn_connection_name(self):
        """Gets the vpn_connection_name of this DescribeVpnConnectionsRequest.  # noqa: E501


        :return: The vpn_connection_name of this DescribeVpnConnectionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpn_connection_name

    @vpn_connection_name.setter
    def vpn_connection_name(self, vpn_connection_name):
        """Sets the vpn_connection_name of this DescribeVpnConnectionsRequest.


        :param vpn_connection_name: The vpn_connection_name of this DescribeVpnConnectionsRequest.  # noqa: E501
        :type: str
        """

        self._vpn_connection_name = vpn_connection_name

    @property
    def vpn_gateway_id(self):
        """Gets the vpn_gateway_id of this DescribeVpnConnectionsRequest.  # noqa: E501


        :return: The vpn_gateway_id of this DescribeVpnConnectionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpn_gateway_id

    @vpn_gateway_id.setter
    def vpn_gateway_id(self, vpn_gateway_id):
        """Sets the vpn_gateway_id of this DescribeVpnConnectionsRequest.


        :param vpn_gateway_id: The vpn_gateway_id of this DescribeVpnConnectionsRequest.  # noqa: E501
        :type: str
        """

        self._vpn_gateway_id = vpn_gateway_id

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
        if issubclass(DescribeVpnConnectionsRequest, dict):
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
        if not isinstance(other, DescribeVpnConnectionsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeVpnConnectionsRequest):
            return True

        return self.to_dict() != other.to_dict()
