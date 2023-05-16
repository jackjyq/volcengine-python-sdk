# coding: utf-8

"""
    clb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class LoadBalancerForDescribeLoadBalancersOutput(object):
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
        'business_status': 'str',
        'create_time': 'str',
        'deleted_time': 'str',
        'description': 'str',
        'eip_address': 'str',
        'eip_id': 'str',
        'eni_address': 'str',
        'eni_id': 'str',
        'expired_time': 'str',
        'load_balancer_billing_type': 'int',
        'load_balancer_id': 'str',
        'load_balancer_name': 'str',
        'load_balancer_spec': 'str',
        'lock_reason': 'str',
        'master_zone_id': 'str',
        'modification_protection_reason': 'str',
        'modification_protection_status': 'str',
        'overdue_time': 'str',
        'project_name': 'str',
        'service_managed': 'bool',
        'slave_zone_id': 'str',
        'status': 'str',
        'subnet_id': 'str',
        'tags': 'list[TagForDescribeLoadBalancersOutput]',
        'type': 'str',
        'update_time': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'business_status': 'BusinessStatus',
        'create_time': 'CreateTime',
        'deleted_time': 'DeletedTime',
        'description': 'Description',
        'eip_address': 'EipAddress',
        'eip_id': 'EipID',
        'eni_address': 'EniAddress',
        'eni_id': 'EniID',
        'expired_time': 'ExpiredTime',
        'load_balancer_billing_type': 'LoadBalancerBillingType',
        'load_balancer_id': 'LoadBalancerId',
        'load_balancer_name': 'LoadBalancerName',
        'load_balancer_spec': 'LoadBalancerSpec',
        'lock_reason': 'LockReason',
        'master_zone_id': 'MasterZoneId',
        'modification_protection_reason': 'ModificationProtectionReason',
        'modification_protection_status': 'ModificationProtectionStatus',
        'overdue_time': 'OverdueTime',
        'project_name': 'ProjectName',
        'service_managed': 'ServiceManaged',
        'slave_zone_id': 'SlaveZoneId',
        'status': 'Status',
        'subnet_id': 'SubnetId',
        'tags': 'Tags',
        'type': 'Type',
        'update_time': 'UpdateTime',
        'vpc_id': 'VpcId'
    }

    def __init__(self, business_status=None, create_time=None, deleted_time=None, description=None, eip_address=None, eip_id=None, eni_address=None, eni_id=None, expired_time=None, load_balancer_billing_type=None, load_balancer_id=None, load_balancer_name=None, load_balancer_spec=None, lock_reason=None, master_zone_id=None, modification_protection_reason=None, modification_protection_status=None, overdue_time=None, project_name=None, service_managed=None, slave_zone_id=None, status=None, subnet_id=None, tags=None, type=None, update_time=None, vpc_id=None, _configuration=None):  # noqa: E501
        """LoadBalancerForDescribeLoadBalancersOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._business_status = None
        self._create_time = None
        self._deleted_time = None
        self._description = None
        self._eip_address = None
        self._eip_id = None
        self._eni_address = None
        self._eni_id = None
        self._expired_time = None
        self._load_balancer_billing_type = None
        self._load_balancer_id = None
        self._load_balancer_name = None
        self._load_balancer_spec = None
        self._lock_reason = None
        self._master_zone_id = None
        self._modification_protection_reason = None
        self._modification_protection_status = None
        self._overdue_time = None
        self._project_name = None
        self._service_managed = None
        self._slave_zone_id = None
        self._status = None
        self._subnet_id = None
        self._tags = None
        self._type = None
        self._update_time = None
        self._vpc_id = None
        self.discriminator = None

        if business_status is not None:
            self.business_status = business_status
        if create_time is not None:
            self.create_time = create_time
        if deleted_time is not None:
            self.deleted_time = deleted_time
        if description is not None:
            self.description = description
        if eip_address is not None:
            self.eip_address = eip_address
        if eip_id is not None:
            self.eip_id = eip_id
        if eni_address is not None:
            self.eni_address = eni_address
        if eni_id is not None:
            self.eni_id = eni_id
        if expired_time is not None:
            self.expired_time = expired_time
        if load_balancer_billing_type is not None:
            self.load_balancer_billing_type = load_balancer_billing_type
        if load_balancer_id is not None:
            self.load_balancer_id = load_balancer_id
        if load_balancer_name is not None:
            self.load_balancer_name = load_balancer_name
        if load_balancer_spec is not None:
            self.load_balancer_spec = load_balancer_spec
        if lock_reason is not None:
            self.lock_reason = lock_reason
        if master_zone_id is not None:
            self.master_zone_id = master_zone_id
        if modification_protection_reason is not None:
            self.modification_protection_reason = modification_protection_reason
        if modification_protection_status is not None:
            self.modification_protection_status = modification_protection_status
        if overdue_time is not None:
            self.overdue_time = overdue_time
        if project_name is not None:
            self.project_name = project_name
        if service_managed is not None:
            self.service_managed = service_managed
        if slave_zone_id is not None:
            self.slave_zone_id = slave_zone_id
        if status is not None:
            self.status = status
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if tags is not None:
            self.tags = tags
        if type is not None:
            self.type = type
        if update_time is not None:
            self.update_time = update_time
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def business_status(self):
        """Gets the business_status of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501


        :return: The business_status of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :rtype: str
        """
        return self._business_status

    @business_status.setter
    def business_status(self, business_status):
        """Sets the business_status of this LoadBalancerForDescribeLoadBalancersOutput.


        :param business_status: The business_status of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :type: str
        """

        self._business_status = business_status

    @property
    def create_time(self):
        """Gets the create_time of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501


        :return: The create_time of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this LoadBalancerForDescribeLoadBalancersOutput.


        :param create_time: The create_time of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def deleted_time(self):
        """Gets the deleted_time of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501


        :return: The deleted_time of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :rtype: str
        """
        return self._deleted_time

    @deleted_time.setter
    def deleted_time(self, deleted_time):
        """Sets the deleted_time of this LoadBalancerForDescribeLoadBalancersOutput.


        :param deleted_time: The deleted_time of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :type: str
        """

        self._deleted_time = deleted_time

    @property
    def description(self):
        """Gets the description of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501


        :return: The description of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LoadBalancerForDescribeLoadBalancersOutput.


        :param description: The description of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def eip_address(self):
        """Gets the eip_address of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501


        :return: The eip_address of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :rtype: str
        """
        return self._eip_address

    @eip_address.setter
    def eip_address(self, eip_address):
        """Sets the eip_address of this LoadBalancerForDescribeLoadBalancersOutput.


        :param eip_address: The eip_address of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :type: str
        """

        self._eip_address = eip_address

    @property
    def eip_id(self):
        """Gets the eip_id of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501


        :return: The eip_id of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :rtype: str
        """
        return self._eip_id

    @eip_id.setter
    def eip_id(self, eip_id):
        """Sets the eip_id of this LoadBalancerForDescribeLoadBalancersOutput.


        :param eip_id: The eip_id of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :type: str
        """

        self._eip_id = eip_id

    @property
    def eni_address(self):
        """Gets the eni_address of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501


        :return: The eni_address of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :rtype: str
        """
        return self._eni_address

    @eni_address.setter
    def eni_address(self, eni_address):
        """Sets the eni_address of this LoadBalancerForDescribeLoadBalancersOutput.


        :param eni_address: The eni_address of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :type: str
        """

        self._eni_address = eni_address

    @property
    def eni_id(self):
        """Gets the eni_id of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501


        :return: The eni_id of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :rtype: str
        """
        return self._eni_id

    @eni_id.setter
    def eni_id(self, eni_id):
        """Sets the eni_id of this LoadBalancerForDescribeLoadBalancersOutput.


        :param eni_id: The eni_id of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :type: str
        """

        self._eni_id = eni_id

    @property
    def expired_time(self):
        """Gets the expired_time of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501


        :return: The expired_time of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :rtype: str
        """
        return self._expired_time

    @expired_time.setter
    def expired_time(self, expired_time):
        """Sets the expired_time of this LoadBalancerForDescribeLoadBalancersOutput.


        :param expired_time: The expired_time of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :type: str
        """

        self._expired_time = expired_time

    @property
    def load_balancer_billing_type(self):
        """Gets the load_balancer_billing_type of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501


        :return: The load_balancer_billing_type of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :rtype: int
        """
        return self._load_balancer_billing_type

    @load_balancer_billing_type.setter
    def load_balancer_billing_type(self, load_balancer_billing_type):
        """Sets the load_balancer_billing_type of this LoadBalancerForDescribeLoadBalancersOutput.


        :param load_balancer_billing_type: The load_balancer_billing_type of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :type: int
        """

        self._load_balancer_billing_type = load_balancer_billing_type

    @property
    def load_balancer_id(self):
        """Gets the load_balancer_id of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501


        :return: The load_balancer_id of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :rtype: str
        """
        return self._load_balancer_id

    @load_balancer_id.setter
    def load_balancer_id(self, load_balancer_id):
        """Sets the load_balancer_id of this LoadBalancerForDescribeLoadBalancersOutput.


        :param load_balancer_id: The load_balancer_id of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :type: str
        """

        self._load_balancer_id = load_balancer_id

    @property
    def load_balancer_name(self):
        """Gets the load_balancer_name of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501


        :return: The load_balancer_name of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :rtype: str
        """
        return self._load_balancer_name

    @load_balancer_name.setter
    def load_balancer_name(self, load_balancer_name):
        """Sets the load_balancer_name of this LoadBalancerForDescribeLoadBalancersOutput.


        :param load_balancer_name: The load_balancer_name of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :type: str
        """

        self._load_balancer_name = load_balancer_name

    @property
    def load_balancer_spec(self):
        """Gets the load_balancer_spec of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501


        :return: The load_balancer_spec of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :rtype: str
        """
        return self._load_balancer_spec

    @load_balancer_spec.setter
    def load_balancer_spec(self, load_balancer_spec):
        """Sets the load_balancer_spec of this LoadBalancerForDescribeLoadBalancersOutput.


        :param load_balancer_spec: The load_balancer_spec of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :type: str
        """

        self._load_balancer_spec = load_balancer_spec

    @property
    def lock_reason(self):
        """Gets the lock_reason of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501


        :return: The lock_reason of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :rtype: str
        """
        return self._lock_reason

    @lock_reason.setter
    def lock_reason(self, lock_reason):
        """Sets the lock_reason of this LoadBalancerForDescribeLoadBalancersOutput.


        :param lock_reason: The lock_reason of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :type: str
        """

        self._lock_reason = lock_reason

    @property
    def master_zone_id(self):
        """Gets the master_zone_id of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501


        :return: The master_zone_id of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :rtype: str
        """
        return self._master_zone_id

    @master_zone_id.setter
    def master_zone_id(self, master_zone_id):
        """Sets the master_zone_id of this LoadBalancerForDescribeLoadBalancersOutput.


        :param master_zone_id: The master_zone_id of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :type: str
        """

        self._master_zone_id = master_zone_id

    @property
    def modification_protection_reason(self):
        """Gets the modification_protection_reason of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501


        :return: The modification_protection_reason of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :rtype: str
        """
        return self._modification_protection_reason

    @modification_protection_reason.setter
    def modification_protection_reason(self, modification_protection_reason):
        """Sets the modification_protection_reason of this LoadBalancerForDescribeLoadBalancersOutput.


        :param modification_protection_reason: The modification_protection_reason of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :type: str
        """

        self._modification_protection_reason = modification_protection_reason

    @property
    def modification_protection_status(self):
        """Gets the modification_protection_status of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501


        :return: The modification_protection_status of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :rtype: str
        """
        return self._modification_protection_status

    @modification_protection_status.setter
    def modification_protection_status(self, modification_protection_status):
        """Sets the modification_protection_status of this LoadBalancerForDescribeLoadBalancersOutput.


        :param modification_protection_status: The modification_protection_status of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :type: str
        """

        self._modification_protection_status = modification_protection_status

    @property
    def overdue_time(self):
        """Gets the overdue_time of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501


        :return: The overdue_time of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :rtype: str
        """
        return self._overdue_time

    @overdue_time.setter
    def overdue_time(self, overdue_time):
        """Sets the overdue_time of this LoadBalancerForDescribeLoadBalancersOutput.


        :param overdue_time: The overdue_time of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :type: str
        """

        self._overdue_time = overdue_time

    @property
    def project_name(self):
        """Gets the project_name of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501


        :return: The project_name of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this LoadBalancerForDescribeLoadBalancersOutput.


        :param project_name: The project_name of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def service_managed(self):
        """Gets the service_managed of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501


        :return: The service_managed of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :rtype: bool
        """
        return self._service_managed

    @service_managed.setter
    def service_managed(self, service_managed):
        """Sets the service_managed of this LoadBalancerForDescribeLoadBalancersOutput.


        :param service_managed: The service_managed of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :type: bool
        """

        self._service_managed = service_managed

    @property
    def slave_zone_id(self):
        """Gets the slave_zone_id of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501


        :return: The slave_zone_id of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :rtype: str
        """
        return self._slave_zone_id

    @slave_zone_id.setter
    def slave_zone_id(self, slave_zone_id):
        """Sets the slave_zone_id of this LoadBalancerForDescribeLoadBalancersOutput.


        :param slave_zone_id: The slave_zone_id of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :type: str
        """

        self._slave_zone_id = slave_zone_id

    @property
    def status(self):
        """Gets the status of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501


        :return: The status of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LoadBalancerForDescribeLoadBalancersOutput.


        :param status: The status of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def subnet_id(self):
        """Gets the subnet_id of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501


        :return: The subnet_id of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this LoadBalancerForDescribeLoadBalancersOutput.


        :param subnet_id: The subnet_id of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :type: str
        """

        self._subnet_id = subnet_id

    @property
    def tags(self):
        """Gets the tags of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501


        :return: The tags of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :rtype: list[TagForDescribeLoadBalancersOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this LoadBalancerForDescribeLoadBalancersOutput.


        :param tags: The tags of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :type: list[TagForDescribeLoadBalancersOutput]
        """

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501


        :return: The type of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LoadBalancerForDescribeLoadBalancersOutput.


        :param type: The type of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def update_time(self):
        """Gets the update_time of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501


        :return: The update_time of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this LoadBalancerForDescribeLoadBalancersOutput.


        :param update_time: The update_time of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

    @property
    def vpc_id(self):
        """Gets the vpc_id of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501


        :return: The vpc_id of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this LoadBalancerForDescribeLoadBalancersOutput.


        :param vpc_id: The vpc_id of this LoadBalancerForDescribeLoadBalancersOutput.  # noqa: E501
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
        if issubclass(LoadBalancerForDescribeLoadBalancersOutput, dict):
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
        if not isinstance(other, LoadBalancerForDescribeLoadBalancersOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LoadBalancerForDescribeLoadBalancersOutput):
            return True

        return self.to_dict() != other.to_dict()
