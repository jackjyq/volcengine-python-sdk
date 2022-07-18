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


class NatGatewayForDescribeNatGatewaysOutput(object):
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
        'billing_type': 'int',
        'business_status': 'str',
        'creation_time': 'str',
        'deleted_time': 'str',
        'description': 'str',
        'eip_addresses': 'list[EipAddressForDescribeNatGatewaysOutput]',
        'expired_time': 'str',
        'lock_reason': 'str',
        'nat_gateway_id': 'str',
        'nat_gateway_name': 'str',
        'network_interface_id': 'str',
        'overdue_time': 'str',
        'spec': 'str',
        'status': 'str',
        'subnet_id': 'str',
        'updated_at': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'billing_type': 'BillingType',
        'business_status': 'BusinessStatus',
        'creation_time': 'CreationTime',
        'deleted_time': 'DeletedTime',
        'description': 'Description',
        'eip_addresses': 'EipAddresses',
        'expired_time': 'ExpiredTime',
        'lock_reason': 'LockReason',
        'nat_gateway_id': 'NatGatewayId',
        'nat_gateway_name': 'NatGatewayName',
        'network_interface_id': 'NetworkInterfaceId',
        'overdue_time': 'OverdueTime',
        'spec': 'Spec',
        'status': 'Status',
        'subnet_id': 'SubnetId',
        'updated_at': 'UpdatedAt',
        'vpc_id': 'VpcId'
    }

    def __init__(self, billing_type=None, business_status=None, creation_time=None, deleted_time=None, description=None, eip_addresses=None, expired_time=None, lock_reason=None, nat_gateway_id=None, nat_gateway_name=None, network_interface_id=None, overdue_time=None, spec=None, status=None, subnet_id=None, updated_at=None, vpc_id=None, _configuration=None):  # noqa: E501
        """NatGatewayForDescribeNatGatewaysOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._billing_type = None
        self._business_status = None
        self._creation_time = None
        self._deleted_time = None
        self._description = None
        self._eip_addresses = None
        self._expired_time = None
        self._lock_reason = None
        self._nat_gateway_id = None
        self._nat_gateway_name = None
        self._network_interface_id = None
        self._overdue_time = None
        self._spec = None
        self._status = None
        self._subnet_id = None
        self._updated_at = None
        self._vpc_id = None
        self.discriminator = None

        if billing_type is not None:
            self.billing_type = billing_type
        if business_status is not None:
            self.business_status = business_status
        if creation_time is not None:
            self.creation_time = creation_time
        if deleted_time is not None:
            self.deleted_time = deleted_time
        if description is not None:
            self.description = description
        if eip_addresses is not None:
            self.eip_addresses = eip_addresses
        if expired_time is not None:
            self.expired_time = expired_time
        if lock_reason is not None:
            self.lock_reason = lock_reason
        if nat_gateway_id is not None:
            self.nat_gateway_id = nat_gateway_id
        if nat_gateway_name is not None:
            self.nat_gateway_name = nat_gateway_name
        if network_interface_id is not None:
            self.network_interface_id = network_interface_id
        if overdue_time is not None:
            self.overdue_time = overdue_time
        if spec is not None:
            self.spec = spec
        if status is not None:
            self.status = status
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if updated_at is not None:
            self.updated_at = updated_at
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def billing_type(self):
        """Gets the billing_type of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501


        :return: The billing_type of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :rtype: int
        """
        return self._billing_type

    @billing_type.setter
    def billing_type(self, billing_type):
        """Sets the billing_type of this NatGatewayForDescribeNatGatewaysOutput.


        :param billing_type: The billing_type of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :type: int
        """

        self._billing_type = billing_type

    @property
    def business_status(self):
        """Gets the business_status of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501


        :return: The business_status of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :rtype: str
        """
        return self._business_status

    @business_status.setter
    def business_status(self, business_status):
        """Sets the business_status of this NatGatewayForDescribeNatGatewaysOutput.


        :param business_status: The business_status of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :type: str
        """

        self._business_status = business_status

    @property
    def creation_time(self):
        """Gets the creation_time of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501


        :return: The creation_time of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this NatGatewayForDescribeNatGatewaysOutput.


        :param creation_time: The creation_time of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def deleted_time(self):
        """Gets the deleted_time of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501


        :return: The deleted_time of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :rtype: str
        """
        return self._deleted_time

    @deleted_time.setter
    def deleted_time(self, deleted_time):
        """Sets the deleted_time of this NatGatewayForDescribeNatGatewaysOutput.


        :param deleted_time: The deleted_time of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :type: str
        """

        self._deleted_time = deleted_time

    @property
    def description(self):
        """Gets the description of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501


        :return: The description of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NatGatewayForDescribeNatGatewaysOutput.


        :param description: The description of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def eip_addresses(self):
        """Gets the eip_addresses of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501


        :return: The eip_addresses of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :rtype: list[EipAddressForDescribeNatGatewaysOutput]
        """
        return self._eip_addresses

    @eip_addresses.setter
    def eip_addresses(self, eip_addresses):
        """Sets the eip_addresses of this NatGatewayForDescribeNatGatewaysOutput.


        :param eip_addresses: The eip_addresses of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :type: list[EipAddressForDescribeNatGatewaysOutput]
        """

        self._eip_addresses = eip_addresses

    @property
    def expired_time(self):
        """Gets the expired_time of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501


        :return: The expired_time of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :rtype: str
        """
        return self._expired_time

    @expired_time.setter
    def expired_time(self, expired_time):
        """Sets the expired_time of this NatGatewayForDescribeNatGatewaysOutput.


        :param expired_time: The expired_time of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :type: str
        """

        self._expired_time = expired_time

    @property
    def lock_reason(self):
        """Gets the lock_reason of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501


        :return: The lock_reason of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :rtype: str
        """
        return self._lock_reason

    @lock_reason.setter
    def lock_reason(self, lock_reason):
        """Sets the lock_reason of this NatGatewayForDescribeNatGatewaysOutput.


        :param lock_reason: The lock_reason of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :type: str
        """

        self._lock_reason = lock_reason

    @property
    def nat_gateway_id(self):
        """Gets the nat_gateway_id of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501


        :return: The nat_gateway_id of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :rtype: str
        """
        return self._nat_gateway_id

    @nat_gateway_id.setter
    def nat_gateway_id(self, nat_gateway_id):
        """Sets the nat_gateway_id of this NatGatewayForDescribeNatGatewaysOutput.


        :param nat_gateway_id: The nat_gateway_id of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :type: str
        """

        self._nat_gateway_id = nat_gateway_id

    @property
    def nat_gateway_name(self):
        """Gets the nat_gateway_name of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501


        :return: The nat_gateway_name of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :rtype: str
        """
        return self._nat_gateway_name

    @nat_gateway_name.setter
    def nat_gateway_name(self, nat_gateway_name):
        """Sets the nat_gateway_name of this NatGatewayForDescribeNatGatewaysOutput.


        :param nat_gateway_name: The nat_gateway_name of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :type: str
        """

        self._nat_gateway_name = nat_gateway_name

    @property
    def network_interface_id(self):
        """Gets the network_interface_id of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501


        :return: The network_interface_id of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :rtype: str
        """
        return self._network_interface_id

    @network_interface_id.setter
    def network_interface_id(self, network_interface_id):
        """Sets the network_interface_id of this NatGatewayForDescribeNatGatewaysOutput.


        :param network_interface_id: The network_interface_id of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :type: str
        """

        self._network_interface_id = network_interface_id

    @property
    def overdue_time(self):
        """Gets the overdue_time of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501


        :return: The overdue_time of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :rtype: str
        """
        return self._overdue_time

    @overdue_time.setter
    def overdue_time(self, overdue_time):
        """Sets the overdue_time of this NatGatewayForDescribeNatGatewaysOutput.


        :param overdue_time: The overdue_time of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :type: str
        """

        self._overdue_time = overdue_time

    @property
    def spec(self):
        """Gets the spec of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501


        :return: The spec of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :rtype: str
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this NatGatewayForDescribeNatGatewaysOutput.


        :param spec: The spec of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :type: str
        """

        self._spec = spec

    @property
    def status(self):
        """Gets the status of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501


        :return: The status of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NatGatewayForDescribeNatGatewaysOutput.


        :param status: The status of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def subnet_id(self):
        """Gets the subnet_id of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501


        :return: The subnet_id of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this NatGatewayForDescribeNatGatewaysOutput.


        :param subnet_id: The subnet_id of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :type: str
        """

        self._subnet_id = subnet_id

    @property
    def updated_at(self):
        """Gets the updated_at of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501


        :return: The updated_at of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this NatGatewayForDescribeNatGatewaysOutput.


        :param updated_at: The updated_at of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def vpc_id(self):
        """Gets the vpc_id of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501


        :return: The vpc_id of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this NatGatewayForDescribeNatGatewaysOutput.


        :param vpc_id: The vpc_id of this NatGatewayForDescribeNatGatewaysOutput.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

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
        if issubclass(NatGatewayForDescribeNatGatewaysOutput, dict):
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
        if not isinstance(other, NatGatewayForDescribeNatGatewaysOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NatGatewayForDescribeNatGatewaysOutput):
            return True

        return self.to_dict() != other.to_dict()
