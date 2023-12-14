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


class DatumForDescribeVpcFirewallListOutput(object):
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
        'attachment_count': 'int',
        'err_message': 'str',
        'firewall_status': 'str',
        'region': 'str',
        'route_policy_status': 'str',
        'transit_router_description': 'str',
        'transit_router_id': 'str',
        'transit_router_name': 'str',
        'vpc_firewall_id': 'str',
        'vpc_firewall_name': 'str'
    }

    attribute_map = {
        'attachment_count': 'AttachmentCount',
        'err_message': 'ErrMessage',
        'firewall_status': 'FirewallStatus',
        'region': 'Region',
        'route_policy_status': 'RoutePolicyStatus',
        'transit_router_description': 'TransitRouterDescription',
        'transit_router_id': 'TransitRouterId',
        'transit_router_name': 'TransitRouterName',
        'vpc_firewall_id': 'VpcFirewallId',
        'vpc_firewall_name': 'VpcFirewallName'
    }

    def __init__(self, attachment_count=None, err_message=None, firewall_status=None, region=None, route_policy_status=None, transit_router_description=None, transit_router_id=None, transit_router_name=None, vpc_firewall_id=None, vpc_firewall_name=None, _configuration=None):  # noqa: E501
        """DatumForDescribeVpcFirewallListOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._attachment_count = None
        self._err_message = None
        self._firewall_status = None
        self._region = None
        self._route_policy_status = None
        self._transit_router_description = None
        self._transit_router_id = None
        self._transit_router_name = None
        self._vpc_firewall_id = None
        self._vpc_firewall_name = None
        self.discriminator = None

        if attachment_count is not None:
            self.attachment_count = attachment_count
        if err_message is not None:
            self.err_message = err_message
        if firewall_status is not None:
            self.firewall_status = firewall_status
        if region is not None:
            self.region = region
        if route_policy_status is not None:
            self.route_policy_status = route_policy_status
        if transit_router_description is not None:
            self.transit_router_description = transit_router_description
        if transit_router_id is not None:
            self.transit_router_id = transit_router_id
        if transit_router_name is not None:
            self.transit_router_name = transit_router_name
        if vpc_firewall_id is not None:
            self.vpc_firewall_id = vpc_firewall_id
        if vpc_firewall_name is not None:
            self.vpc_firewall_name = vpc_firewall_name

    @property
    def attachment_count(self):
        """Gets the attachment_count of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501


        :return: The attachment_count of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501
        :rtype: int
        """
        return self._attachment_count

    @attachment_count.setter
    def attachment_count(self, attachment_count):
        """Sets the attachment_count of this DatumForDescribeVpcFirewallListOutput.


        :param attachment_count: The attachment_count of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501
        :type: int
        """

        self._attachment_count = attachment_count

    @property
    def err_message(self):
        """Gets the err_message of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501


        :return: The err_message of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501
        :rtype: str
        """
        return self._err_message

    @err_message.setter
    def err_message(self, err_message):
        """Sets the err_message of this DatumForDescribeVpcFirewallListOutput.


        :param err_message: The err_message of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501
        :type: str
        """

        self._err_message = err_message

    @property
    def firewall_status(self):
        """Gets the firewall_status of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501


        :return: The firewall_status of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501
        :rtype: str
        """
        return self._firewall_status

    @firewall_status.setter
    def firewall_status(self, firewall_status):
        """Sets the firewall_status of this DatumForDescribeVpcFirewallListOutput.


        :param firewall_status: The firewall_status of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501
        :type: str
        """

        self._firewall_status = firewall_status

    @property
    def region(self):
        """Gets the region of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501


        :return: The region of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this DatumForDescribeVpcFirewallListOutput.


        :param region: The region of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def route_policy_status(self):
        """Gets the route_policy_status of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501


        :return: The route_policy_status of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501
        :rtype: str
        """
        return self._route_policy_status

    @route_policy_status.setter
    def route_policy_status(self, route_policy_status):
        """Sets the route_policy_status of this DatumForDescribeVpcFirewallListOutput.


        :param route_policy_status: The route_policy_status of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501
        :type: str
        """

        self._route_policy_status = route_policy_status

    @property
    def transit_router_description(self):
        """Gets the transit_router_description of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501


        :return: The transit_router_description of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_description

    @transit_router_description.setter
    def transit_router_description(self, transit_router_description):
        """Sets the transit_router_description of this DatumForDescribeVpcFirewallListOutput.


        :param transit_router_description: The transit_router_description of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501
        :type: str
        """

        self._transit_router_description = transit_router_description

    @property
    def transit_router_id(self):
        """Gets the transit_router_id of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501


        :return: The transit_router_id of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_id

    @transit_router_id.setter
    def transit_router_id(self, transit_router_id):
        """Sets the transit_router_id of this DatumForDescribeVpcFirewallListOutput.


        :param transit_router_id: The transit_router_id of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501
        :type: str
        """

        self._transit_router_id = transit_router_id

    @property
    def transit_router_name(self):
        """Gets the transit_router_name of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501


        :return: The transit_router_name of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_name

    @transit_router_name.setter
    def transit_router_name(self, transit_router_name):
        """Sets the transit_router_name of this DatumForDescribeVpcFirewallListOutput.


        :param transit_router_name: The transit_router_name of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501
        :type: str
        """

        self._transit_router_name = transit_router_name

    @property
    def vpc_firewall_id(self):
        """Gets the vpc_firewall_id of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501


        :return: The vpc_firewall_id of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501
        :rtype: str
        """
        return self._vpc_firewall_id

    @vpc_firewall_id.setter
    def vpc_firewall_id(self, vpc_firewall_id):
        """Sets the vpc_firewall_id of this DatumForDescribeVpcFirewallListOutput.


        :param vpc_firewall_id: The vpc_firewall_id of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501
        :type: str
        """

        self._vpc_firewall_id = vpc_firewall_id

    @property
    def vpc_firewall_name(self):
        """Gets the vpc_firewall_name of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501


        :return: The vpc_firewall_name of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501
        :rtype: str
        """
        return self._vpc_firewall_name

    @vpc_firewall_name.setter
    def vpc_firewall_name(self, vpc_firewall_name):
        """Sets the vpc_firewall_name of this DatumForDescribeVpcFirewallListOutput.


        :param vpc_firewall_name: The vpc_firewall_name of this DatumForDescribeVpcFirewallListOutput.  # noqa: E501
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
        if issubclass(DatumForDescribeVpcFirewallListOutput, dict):
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
        if not isinstance(other, DatumForDescribeVpcFirewallListOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DatumForDescribeVpcFirewallListOutput):
            return True

        return self.to_dict() != other.to_dict()