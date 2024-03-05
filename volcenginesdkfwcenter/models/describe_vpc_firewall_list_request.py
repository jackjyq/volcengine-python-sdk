# coding: utf-8

"""
    fwcenter

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeVpcFirewallListRequest(object):
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
        'firewall_status': 'list[str]',
        'page_number': 'int',
        'page_size': 'int',
        'region_code': 'list[str]',
        'route_mode': 'list[str]',
        'route_policy_status': 'list[str]',
        'transit_router_id': 'str',
        'transit_router_name': 'str',
        'vpc_firewall_id': 'str',
        'vpc_firewall_name': 'str'
    }

    attribute_map = {
        'firewall_status': 'FirewallStatus',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'region_code': 'RegionCode',
        'route_mode': 'RouteMode',
        'route_policy_status': 'RoutePolicyStatus',
        'transit_router_id': 'TransitRouterId',
        'transit_router_name': 'TransitRouterName',
        'vpc_firewall_id': 'VpcFirewallId',
        'vpc_firewall_name': 'VpcFirewallName'
    }

    def __init__(self, firewall_status=None, page_number=None, page_size=None, region_code=None, route_mode=None, route_policy_status=None, transit_router_id=None, transit_router_name=None, vpc_firewall_id=None, vpc_firewall_name=None, _configuration=None):  # noqa: E501
        """DescribeVpcFirewallListRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._firewall_status = None
        self._page_number = None
        self._page_size = None
        self._region_code = None
        self._route_mode = None
        self._route_policy_status = None
        self._transit_router_id = None
        self._transit_router_name = None
        self._vpc_firewall_id = None
        self._vpc_firewall_name = None
        self.discriminator = None

        if firewall_status is not None:
            self.firewall_status = firewall_status
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if region_code is not None:
            self.region_code = region_code
        if route_mode is not None:
            self.route_mode = route_mode
        if route_policy_status is not None:
            self.route_policy_status = route_policy_status
        if transit_router_id is not None:
            self.transit_router_id = transit_router_id
        if transit_router_name is not None:
            self.transit_router_name = transit_router_name
        if vpc_firewall_id is not None:
            self.vpc_firewall_id = vpc_firewall_id
        if vpc_firewall_name is not None:
            self.vpc_firewall_name = vpc_firewall_name

    @property
    def firewall_status(self):
        """Gets the firewall_status of this DescribeVpcFirewallListRequest.  # noqa: E501


        :return: The firewall_status of this DescribeVpcFirewallListRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._firewall_status

    @firewall_status.setter
    def firewall_status(self, firewall_status):
        """Sets the firewall_status of this DescribeVpcFirewallListRequest.


        :param firewall_status: The firewall_status of this DescribeVpcFirewallListRequest.  # noqa: E501
        :type: list[str]
        """

        self._firewall_status = firewall_status

    @property
    def page_number(self):
        """Gets the page_number of this DescribeVpcFirewallListRequest.  # noqa: E501


        :return: The page_number of this DescribeVpcFirewallListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeVpcFirewallListRequest.


        :param page_number: The page_number of this DescribeVpcFirewallListRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeVpcFirewallListRequest.  # noqa: E501


        :return: The page_size of this DescribeVpcFirewallListRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeVpcFirewallListRequest.


        :param page_size: The page_size of this DescribeVpcFirewallListRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def region_code(self):
        """Gets the region_code of this DescribeVpcFirewallListRequest.  # noqa: E501


        :return: The region_code of this DescribeVpcFirewallListRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this DescribeVpcFirewallListRequest.


        :param region_code: The region_code of this DescribeVpcFirewallListRequest.  # noqa: E501
        :type: list[str]
        """

        self._region_code = region_code

    @property
    def route_mode(self):
        """Gets the route_mode of this DescribeVpcFirewallListRequest.  # noqa: E501


        :return: The route_mode of this DescribeVpcFirewallListRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._route_mode

    @route_mode.setter
    def route_mode(self, route_mode):
        """Sets the route_mode of this DescribeVpcFirewallListRequest.


        :param route_mode: The route_mode of this DescribeVpcFirewallListRequest.  # noqa: E501
        :type: list[str]
        """

        self._route_mode = route_mode

    @property
    def route_policy_status(self):
        """Gets the route_policy_status of this DescribeVpcFirewallListRequest.  # noqa: E501


        :return: The route_policy_status of this DescribeVpcFirewallListRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._route_policy_status

    @route_policy_status.setter
    def route_policy_status(self, route_policy_status):
        """Sets the route_policy_status of this DescribeVpcFirewallListRequest.


        :param route_policy_status: The route_policy_status of this DescribeVpcFirewallListRequest.  # noqa: E501
        :type: list[str]
        """

        self._route_policy_status = route_policy_status

    @property
    def transit_router_id(self):
        """Gets the transit_router_id of this DescribeVpcFirewallListRequest.  # noqa: E501


        :return: The transit_router_id of this DescribeVpcFirewallListRequest.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_id

    @transit_router_id.setter
    def transit_router_id(self, transit_router_id):
        """Sets the transit_router_id of this DescribeVpcFirewallListRequest.


        :param transit_router_id: The transit_router_id of this DescribeVpcFirewallListRequest.  # noqa: E501
        :type: str
        """

        self._transit_router_id = transit_router_id

    @property
    def transit_router_name(self):
        """Gets the transit_router_name of this DescribeVpcFirewallListRequest.  # noqa: E501


        :return: The transit_router_name of this DescribeVpcFirewallListRequest.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_name

    @transit_router_name.setter
    def transit_router_name(self, transit_router_name):
        """Sets the transit_router_name of this DescribeVpcFirewallListRequest.


        :param transit_router_name: The transit_router_name of this DescribeVpcFirewallListRequest.  # noqa: E501
        :type: str
        """

        self._transit_router_name = transit_router_name

    @property
    def vpc_firewall_id(self):
        """Gets the vpc_firewall_id of this DescribeVpcFirewallListRequest.  # noqa: E501


        :return: The vpc_firewall_id of this DescribeVpcFirewallListRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_firewall_id

    @vpc_firewall_id.setter
    def vpc_firewall_id(self, vpc_firewall_id):
        """Sets the vpc_firewall_id of this DescribeVpcFirewallListRequest.


        :param vpc_firewall_id: The vpc_firewall_id of this DescribeVpcFirewallListRequest.  # noqa: E501
        :type: str
        """

        self._vpc_firewall_id = vpc_firewall_id

    @property
    def vpc_firewall_name(self):
        """Gets the vpc_firewall_name of this DescribeVpcFirewallListRequest.  # noqa: E501


        :return: The vpc_firewall_name of this DescribeVpcFirewallListRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_firewall_name

    @vpc_firewall_name.setter
    def vpc_firewall_name(self, vpc_firewall_name):
        """Sets the vpc_firewall_name of this DescribeVpcFirewallListRequest.


        :param vpc_firewall_name: The vpc_firewall_name of this DescribeVpcFirewallListRequest.  # noqa: E501
        :type: str
        """

        self._vpc_firewall_name = vpc_firewall_name

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
        if issubclass(DescribeVpcFirewallListRequest, dict):
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
        if not isinstance(other, DescribeVpcFirewallListRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeVpcFirewallListRequest):
            return True

        return self.to_dict() != other.to_dict()
