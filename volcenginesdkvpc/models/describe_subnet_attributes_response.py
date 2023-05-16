# coding: utf-8

"""
    vpc

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeSubnetAttributesResponse(object):
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
        'account_id': 'str',
        'available_ip_address_count': 'int',
        'cidr_block': 'str',
        'creation_time': 'str',
        'description': 'str',
        'is_default': 'bool',
        'network_acl_id': 'str',
        'project_name': 'str',
        'request_id': 'str',
        'route_table': 'RouteTableForDescribeSubnetAttributesOutput',
        'status': 'str',
        'subnet_id': 'str',
        'subnet_name': 'str',
        'total_ipv4_count': 'int',
        'update_time': 'str',
        'vpc_id': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'available_ip_address_count': 'AvailableIpAddressCount',
        'cidr_block': 'CidrBlock',
        'creation_time': 'CreationTime',
        'description': 'Description',
        'is_default': 'IsDefault',
        'network_acl_id': 'NetworkAclId',
        'project_name': 'ProjectName',
        'request_id': 'RequestId',
        'route_table': 'RouteTable',
        'status': 'Status',
        'subnet_id': 'SubnetId',
        'subnet_name': 'SubnetName',
        'total_ipv4_count': 'TotalIpv4Count',
        'update_time': 'UpdateTime',
        'vpc_id': 'VpcId',
        'zone_id': 'ZoneId'
    }

    def __init__(self, account_id=None, available_ip_address_count=None, cidr_block=None, creation_time=None, description=None, is_default=None, network_acl_id=None, project_name=None, request_id=None, route_table=None, status=None, subnet_id=None, subnet_name=None, total_ipv4_count=None, update_time=None, vpc_id=None, zone_id=None, _configuration=None):  # noqa: E501
        """DescribeSubnetAttributesResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._available_ip_address_count = None
        self._cidr_block = None
        self._creation_time = None
        self._description = None
        self._is_default = None
        self._network_acl_id = None
        self._project_name = None
        self._request_id = None
        self._route_table = None
        self._status = None
        self._subnet_id = None
        self._subnet_name = None
        self._total_ipv4_count = None
        self._update_time = None
        self._vpc_id = None
        self._zone_id = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if available_ip_address_count is not None:
            self.available_ip_address_count = available_ip_address_count
        if cidr_block is not None:
            self.cidr_block = cidr_block
        if creation_time is not None:
            self.creation_time = creation_time
        if description is not None:
            self.description = description
        if is_default is not None:
            self.is_default = is_default
        if network_acl_id is not None:
            self.network_acl_id = network_acl_id
        if project_name is not None:
            self.project_name = project_name
        if request_id is not None:
            self.request_id = request_id
        if route_table is not None:
            self.route_table = route_table
        if status is not None:
            self.status = status
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if subnet_name is not None:
            self.subnet_name = subnet_name
        if total_ipv4_count is not None:
            self.total_ipv4_count = total_ipv4_count
        if update_time is not None:
            self.update_time = update_time
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def account_id(self):
        """Gets the account_id of this DescribeSubnetAttributesResponse.  # noqa: E501


        :return: The account_id of this DescribeSubnetAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this DescribeSubnetAttributesResponse.


        :param account_id: The account_id of this DescribeSubnetAttributesResponse.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def available_ip_address_count(self):
        """Gets the available_ip_address_count of this DescribeSubnetAttributesResponse.  # noqa: E501


        :return: The available_ip_address_count of this DescribeSubnetAttributesResponse.  # noqa: E501
        :rtype: int
        """
        return self._available_ip_address_count

    @available_ip_address_count.setter
    def available_ip_address_count(self, available_ip_address_count):
        """Sets the available_ip_address_count of this DescribeSubnetAttributesResponse.


        :param available_ip_address_count: The available_ip_address_count of this DescribeSubnetAttributesResponse.  # noqa: E501
        :type: int
        """

        self._available_ip_address_count = available_ip_address_count

    @property
    def cidr_block(self):
        """Gets the cidr_block of this DescribeSubnetAttributesResponse.  # noqa: E501


        :return: The cidr_block of this DescribeSubnetAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """Sets the cidr_block of this DescribeSubnetAttributesResponse.


        :param cidr_block: The cidr_block of this DescribeSubnetAttributesResponse.  # noqa: E501
        :type: str
        """

        self._cidr_block = cidr_block

    @property
    def creation_time(self):
        """Gets the creation_time of this DescribeSubnetAttributesResponse.  # noqa: E501


        :return: The creation_time of this DescribeSubnetAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this DescribeSubnetAttributesResponse.


        :param creation_time: The creation_time of this DescribeSubnetAttributesResponse.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def description(self):
        """Gets the description of this DescribeSubnetAttributesResponse.  # noqa: E501


        :return: The description of this DescribeSubnetAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DescribeSubnetAttributesResponse.


        :param description: The description of this DescribeSubnetAttributesResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def is_default(self):
        """Gets the is_default of this DescribeSubnetAttributesResponse.  # noqa: E501


        :return: The is_default of this DescribeSubnetAttributesResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this DescribeSubnetAttributesResponse.


        :param is_default: The is_default of this DescribeSubnetAttributesResponse.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def network_acl_id(self):
        """Gets the network_acl_id of this DescribeSubnetAttributesResponse.  # noqa: E501


        :return: The network_acl_id of this DescribeSubnetAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._network_acl_id

    @network_acl_id.setter
    def network_acl_id(self, network_acl_id):
        """Sets the network_acl_id of this DescribeSubnetAttributesResponse.


        :param network_acl_id: The network_acl_id of this DescribeSubnetAttributesResponse.  # noqa: E501
        :type: str
        """

        self._network_acl_id = network_acl_id

    @property
    def project_name(self):
        """Gets the project_name of this DescribeSubnetAttributesResponse.  # noqa: E501


        :return: The project_name of this DescribeSubnetAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DescribeSubnetAttributesResponse.


        :param project_name: The project_name of this DescribeSubnetAttributesResponse.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def request_id(self):
        """Gets the request_id of this DescribeSubnetAttributesResponse.  # noqa: E501


        :return: The request_id of this DescribeSubnetAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this DescribeSubnetAttributesResponse.


        :param request_id: The request_id of this DescribeSubnetAttributesResponse.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def route_table(self):
        """Gets the route_table of this DescribeSubnetAttributesResponse.  # noqa: E501


        :return: The route_table of this DescribeSubnetAttributesResponse.  # noqa: E501
        :rtype: RouteTableForDescribeSubnetAttributesOutput
        """
        return self._route_table

    @route_table.setter
    def route_table(self, route_table):
        """Sets the route_table of this DescribeSubnetAttributesResponse.


        :param route_table: The route_table of this DescribeSubnetAttributesResponse.  # noqa: E501
        :type: RouteTableForDescribeSubnetAttributesOutput
        """

        self._route_table = route_table

    @property
    def status(self):
        """Gets the status of this DescribeSubnetAttributesResponse.  # noqa: E501


        :return: The status of this DescribeSubnetAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DescribeSubnetAttributesResponse.


        :param status: The status of this DescribeSubnetAttributesResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def subnet_id(self):
        """Gets the subnet_id of this DescribeSubnetAttributesResponse.  # noqa: E501


        :return: The subnet_id of this DescribeSubnetAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this DescribeSubnetAttributesResponse.


        :param subnet_id: The subnet_id of this DescribeSubnetAttributesResponse.  # noqa: E501
        :type: str
        """

        self._subnet_id = subnet_id

    @property
    def subnet_name(self):
        """Gets the subnet_name of this DescribeSubnetAttributesResponse.  # noqa: E501


        :return: The subnet_name of this DescribeSubnetAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, subnet_name):
        """Sets the subnet_name of this DescribeSubnetAttributesResponse.


        :param subnet_name: The subnet_name of this DescribeSubnetAttributesResponse.  # noqa: E501
        :type: str
        """

        self._subnet_name = subnet_name

    @property
    def total_ipv4_count(self):
        """Gets the total_ipv4_count of this DescribeSubnetAttributesResponse.  # noqa: E501


        :return: The total_ipv4_count of this DescribeSubnetAttributesResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_ipv4_count

    @total_ipv4_count.setter
    def total_ipv4_count(self, total_ipv4_count):
        """Sets the total_ipv4_count of this DescribeSubnetAttributesResponse.


        :param total_ipv4_count: The total_ipv4_count of this DescribeSubnetAttributesResponse.  # noqa: E501
        :type: int
        """

        self._total_ipv4_count = total_ipv4_count

    @property
    def update_time(self):
        """Gets the update_time of this DescribeSubnetAttributesResponse.  # noqa: E501


        :return: The update_time of this DescribeSubnetAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this DescribeSubnetAttributesResponse.


        :param update_time: The update_time of this DescribeSubnetAttributesResponse.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

    @property
    def vpc_id(self):
        """Gets the vpc_id of this DescribeSubnetAttributesResponse.  # noqa: E501


        :return: The vpc_id of this DescribeSubnetAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this DescribeSubnetAttributesResponse.


        :param vpc_id: The vpc_id of this DescribeSubnetAttributesResponse.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

    @property
    def zone_id(self):
        """Gets the zone_id of this DescribeSubnetAttributesResponse.  # noqa: E501


        :return: The zone_id of this DescribeSubnetAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this DescribeSubnetAttributesResponse.


        :param zone_id: The zone_id of this DescribeSubnetAttributesResponse.  # noqa: E501
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
        if issubclass(DescribeSubnetAttributesResponse, dict):
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
        if not isinstance(other, DescribeSubnetAttributesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeSubnetAttributesResponse):
            return True

        return self.to_dict() != other.to_dict()
