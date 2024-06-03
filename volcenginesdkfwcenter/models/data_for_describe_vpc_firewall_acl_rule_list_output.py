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


class DataForDescribeVpcFirewallAclRuleListOutput(object):
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
        'action': 'str',
        'description': 'str',
        'dest_port': 'str',
        'dest_port_group_type': 'str',
        'dest_port_list': 'list[str]',
        'dest_port_type': 'str',
        'destination': 'str',
        'destination_cidr_list': 'list[str]',
        'destination_group_type': 'str',
        'destination_type': 'str',
        'hit_cnt': 'int',
        'prio': 'int',
        'proto': 'str',
        'rule_id': 'str',
        'source': 'str',
        'source_cidr_list': 'list[str]',
        'source_group_type': 'str',
        'source_type': 'str',
        'status': 'bool',
        'use_count': 'int',
        'vpc_firewall_id': 'str',
        'vpc_firewall_name': 'str'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'action': 'Action',
        'description': 'Description',
        'dest_port': 'DestPort',
        'dest_port_group_type': 'DestPortGroupType',
        'dest_port_list': 'DestPortList',
        'dest_port_type': 'DestPortType',
        'destination': 'Destination',
        'destination_cidr_list': 'DestinationCidrList',
        'destination_group_type': 'DestinationGroupType',
        'destination_type': 'DestinationType',
        'hit_cnt': 'HitCnt',
        'prio': 'Prio',
        'proto': 'Proto',
        'rule_id': 'RuleId',
        'source': 'Source',
        'source_cidr_list': 'SourceCidrList',
        'source_group_type': 'SourceGroupType',
        'source_type': 'SourceType',
        'status': 'Status',
        'use_count': 'UseCount',
        'vpc_firewall_id': 'VpcFirewallId',
        'vpc_firewall_name': 'VpcFirewallName'
    }

    def __init__(self, account_id=None, action=None, description=None, dest_port=None, dest_port_group_type=None, dest_port_list=None, dest_port_type=None, destination=None, destination_cidr_list=None, destination_group_type=None, destination_type=None, hit_cnt=None, prio=None, proto=None, rule_id=None, source=None, source_cidr_list=None, source_group_type=None, source_type=None, status=None, use_count=None, vpc_firewall_id=None, vpc_firewall_name=None, _configuration=None):  # noqa: E501
        """DataForDescribeVpcFirewallAclRuleListOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._action = None
        self._description = None
        self._dest_port = None
        self._dest_port_group_type = None
        self._dest_port_list = None
        self._dest_port_type = None
        self._destination = None
        self._destination_cidr_list = None
        self._destination_group_type = None
        self._destination_type = None
        self._hit_cnt = None
        self._prio = None
        self._proto = None
        self._rule_id = None
        self._source = None
        self._source_cidr_list = None
        self._source_group_type = None
        self._source_type = None
        self._status = None
        self._use_count = None
        self._vpc_firewall_id = None
        self._vpc_firewall_name = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if action is not None:
            self.action = action
        if description is not None:
            self.description = description
        if dest_port is not None:
            self.dest_port = dest_port
        if dest_port_group_type is not None:
            self.dest_port_group_type = dest_port_group_type
        if dest_port_list is not None:
            self.dest_port_list = dest_port_list
        if dest_port_type is not None:
            self.dest_port_type = dest_port_type
        if destination is not None:
            self.destination = destination
        if destination_cidr_list is not None:
            self.destination_cidr_list = destination_cidr_list
        if destination_group_type is not None:
            self.destination_group_type = destination_group_type
        if destination_type is not None:
            self.destination_type = destination_type
        if hit_cnt is not None:
            self.hit_cnt = hit_cnt
        if prio is not None:
            self.prio = prio
        if proto is not None:
            self.proto = proto
        if rule_id is not None:
            self.rule_id = rule_id
        if source is not None:
            self.source = source
        if source_cidr_list is not None:
            self.source_cidr_list = source_cidr_list
        if source_group_type is not None:
            self.source_group_type = source_group_type
        if source_type is not None:
            self.source_type = source_type
        if status is not None:
            self.status = status
        if use_count is not None:
            self.use_count = use_count
        if vpc_firewall_id is not None:
            self.vpc_firewall_id = vpc_firewall_id
        if vpc_firewall_name is not None:
            self.vpc_firewall_name = vpc_firewall_name

    @property
    def account_id(self):
        """Gets the account_id of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501


        :return: The account_id of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this DataForDescribeVpcFirewallAclRuleListOutput.


        :param account_id: The account_id of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def action(self):
        """Gets the action of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501


        :return: The action of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this DataForDescribeVpcFirewallAclRuleListOutput.


        :param action: The action of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def description(self):
        """Gets the description of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501


        :return: The description of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DataForDescribeVpcFirewallAclRuleListOutput.


        :param description: The description of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def dest_port(self):
        """Gets the dest_port of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501


        :return: The dest_port of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :rtype: str
        """
        return self._dest_port

    @dest_port.setter
    def dest_port(self, dest_port):
        """Sets the dest_port of this DataForDescribeVpcFirewallAclRuleListOutput.


        :param dest_port: The dest_port of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :type: str
        """

        self._dest_port = dest_port

    @property
    def dest_port_group_type(self):
        """Gets the dest_port_group_type of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501


        :return: The dest_port_group_type of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :rtype: str
        """
        return self._dest_port_group_type

    @dest_port_group_type.setter
    def dest_port_group_type(self, dest_port_group_type):
        """Sets the dest_port_group_type of this DataForDescribeVpcFirewallAclRuleListOutput.


        :param dest_port_group_type: The dest_port_group_type of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :type: str
        """

        self._dest_port_group_type = dest_port_group_type

    @property
    def dest_port_list(self):
        """Gets the dest_port_list of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501


        :return: The dest_port_list of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._dest_port_list

    @dest_port_list.setter
    def dest_port_list(self, dest_port_list):
        """Sets the dest_port_list of this DataForDescribeVpcFirewallAclRuleListOutput.


        :param dest_port_list: The dest_port_list of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :type: list[str]
        """

        self._dest_port_list = dest_port_list

    @property
    def dest_port_type(self):
        """Gets the dest_port_type of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501


        :return: The dest_port_type of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :rtype: str
        """
        return self._dest_port_type

    @dest_port_type.setter
    def dest_port_type(self, dest_port_type):
        """Sets the dest_port_type of this DataForDescribeVpcFirewallAclRuleListOutput.


        :param dest_port_type: The dest_port_type of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :type: str
        """

        self._dest_port_type = dest_port_type

    @property
    def destination(self):
        """Gets the destination of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501


        :return: The destination of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this DataForDescribeVpcFirewallAclRuleListOutput.


        :param destination: The destination of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :type: str
        """

        self._destination = destination

    @property
    def destination_cidr_list(self):
        """Gets the destination_cidr_list of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501


        :return: The destination_cidr_list of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._destination_cidr_list

    @destination_cidr_list.setter
    def destination_cidr_list(self, destination_cidr_list):
        """Sets the destination_cidr_list of this DataForDescribeVpcFirewallAclRuleListOutput.


        :param destination_cidr_list: The destination_cidr_list of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :type: list[str]
        """

        self._destination_cidr_list = destination_cidr_list

    @property
    def destination_group_type(self):
        """Gets the destination_group_type of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501


        :return: The destination_group_type of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :rtype: str
        """
        return self._destination_group_type

    @destination_group_type.setter
    def destination_group_type(self, destination_group_type):
        """Sets the destination_group_type of this DataForDescribeVpcFirewallAclRuleListOutput.


        :param destination_group_type: The destination_group_type of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :type: str
        """

        self._destination_group_type = destination_group_type

    @property
    def destination_type(self):
        """Gets the destination_type of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501


        :return: The destination_type of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        """Sets the destination_type of this DataForDescribeVpcFirewallAclRuleListOutput.


        :param destination_type: The destination_type of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :type: str
        """

        self._destination_type = destination_type

    @property
    def hit_cnt(self):
        """Gets the hit_cnt of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501


        :return: The hit_cnt of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :rtype: int
        """
        return self._hit_cnt

    @hit_cnt.setter
    def hit_cnt(self, hit_cnt):
        """Sets the hit_cnt of this DataForDescribeVpcFirewallAclRuleListOutput.


        :param hit_cnt: The hit_cnt of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :type: int
        """

        self._hit_cnt = hit_cnt

    @property
    def prio(self):
        """Gets the prio of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501


        :return: The prio of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :rtype: int
        """
        return self._prio

    @prio.setter
    def prio(self, prio):
        """Sets the prio of this DataForDescribeVpcFirewallAclRuleListOutput.


        :param prio: The prio of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :type: int
        """

        self._prio = prio

    @property
    def proto(self):
        """Gets the proto of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501


        :return: The proto of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :rtype: str
        """
        return self._proto

    @proto.setter
    def proto(self, proto):
        """Sets the proto of this DataForDescribeVpcFirewallAclRuleListOutput.


        :param proto: The proto of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :type: str
        """

        self._proto = proto

    @property
    def rule_id(self):
        """Gets the rule_id of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501


        :return: The rule_id of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this DataForDescribeVpcFirewallAclRuleListOutput.


        :param rule_id: The rule_id of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :type: str
        """

        self._rule_id = rule_id

    @property
    def source(self):
        """Gets the source of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501


        :return: The source of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this DataForDescribeVpcFirewallAclRuleListOutput.


        :param source: The source of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def source_cidr_list(self):
        """Gets the source_cidr_list of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501


        :return: The source_cidr_list of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._source_cidr_list

    @source_cidr_list.setter
    def source_cidr_list(self, source_cidr_list):
        """Sets the source_cidr_list of this DataForDescribeVpcFirewallAclRuleListOutput.


        :param source_cidr_list: The source_cidr_list of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :type: list[str]
        """

        self._source_cidr_list = source_cidr_list

    @property
    def source_group_type(self):
        """Gets the source_group_type of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501


        :return: The source_group_type of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :rtype: str
        """
        return self._source_group_type

    @source_group_type.setter
    def source_group_type(self, source_group_type):
        """Sets the source_group_type of this DataForDescribeVpcFirewallAclRuleListOutput.


        :param source_group_type: The source_group_type of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :type: str
        """

        self._source_group_type = source_group_type

    @property
    def source_type(self):
        """Gets the source_type of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501


        :return: The source_type of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this DataForDescribeVpcFirewallAclRuleListOutput.


        :param source_type: The source_type of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :type: str
        """

        self._source_type = source_type

    @property
    def status(self):
        """Gets the status of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501


        :return: The status of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DataForDescribeVpcFirewallAclRuleListOutput.


        :param status: The status of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :type: bool
        """

        self._status = status

    @property
    def use_count(self):
        """Gets the use_count of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501


        :return: The use_count of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :rtype: int
        """
        return self._use_count

    @use_count.setter
    def use_count(self, use_count):
        """Sets the use_count of this DataForDescribeVpcFirewallAclRuleListOutput.


        :param use_count: The use_count of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :type: int
        """

        self._use_count = use_count

    @property
    def vpc_firewall_id(self):
        """Gets the vpc_firewall_id of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501


        :return: The vpc_firewall_id of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :rtype: str
        """
        return self._vpc_firewall_id

    @vpc_firewall_id.setter
    def vpc_firewall_id(self, vpc_firewall_id):
        """Sets the vpc_firewall_id of this DataForDescribeVpcFirewallAclRuleListOutput.


        :param vpc_firewall_id: The vpc_firewall_id of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :type: str
        """

        self._vpc_firewall_id = vpc_firewall_id

    @property
    def vpc_firewall_name(self):
        """Gets the vpc_firewall_name of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501


        :return: The vpc_firewall_name of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
        :rtype: str
        """
        return self._vpc_firewall_name

    @vpc_firewall_name.setter
    def vpc_firewall_name(self, vpc_firewall_name):
        """Sets the vpc_firewall_name of this DataForDescribeVpcFirewallAclRuleListOutput.


        :param vpc_firewall_name: The vpc_firewall_name of this DataForDescribeVpcFirewallAclRuleListOutput.  # noqa: E501
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
        if issubclass(DataForDescribeVpcFirewallAclRuleListOutput, dict):
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
        if not isinstance(other, DataForDescribeVpcFirewallAclRuleListOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataForDescribeVpcFirewallAclRuleListOutput):
            return True

        return self.to_dict() != other.to_dict()