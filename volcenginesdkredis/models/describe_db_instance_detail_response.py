# coding: utf-8

"""
    redis

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeDBInstanceDetailResponse(object):
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
        'auto_renew': 'bool',
        'capacity': 'CapacityForDescribeDBInstanceDetailOutput',
        'charge_type': 'str',
        'create_time': 'str',
        'deletion_protection': 'str',
        'engine_version': 'str',
        'expired_time': 'str',
        'instance_class': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'maintenance_time': 'str',
        'multi_az': 'str',
        'node_number': 'int',
        'project_name': 'str',
        'region_id': 'str',
        'shard_capacity': 'float',
        'shard_capacity_v2': 'int',
        'shard_number': 'int',
        'sharded_cluster': 'int',
        'status': 'str',
        'subnet_id': 'str',
        'tags': 'list[TagForDescribeDBInstanceDetailOutput]',
        'visit_addrs': 'list[VisitAddrForDescribeDBInstanceDetailOutput]',
        'vpc_auth_mode': 'str',
        'vpc_id': 'str',
        'zone_ids': 'list[str]'
    }

    attribute_map = {
        'auto_renew': 'AutoRenew',
        'capacity': 'Capacity',
        'charge_type': 'ChargeType',
        'create_time': 'CreateTime',
        'deletion_protection': 'DeletionProtection',
        'engine_version': 'EngineVersion',
        'expired_time': 'ExpiredTime',
        'instance_class': 'InstanceClass',
        'instance_id': 'InstanceId',
        'instance_name': 'InstanceName',
        'maintenance_time': 'MaintenanceTime',
        'multi_az': 'MultiAZ',
        'node_number': 'NodeNumber',
        'project_name': 'ProjectName',
        'region_id': 'RegionId',
        'shard_capacity': 'ShardCapacity',
        'shard_capacity_v2': 'ShardCapacityV2',
        'shard_number': 'ShardNumber',
        'sharded_cluster': 'ShardedCluster',
        'status': 'Status',
        'subnet_id': 'SubnetId',
        'tags': 'Tags',
        'visit_addrs': 'VisitAddrs',
        'vpc_auth_mode': 'VpcAuthMode',
        'vpc_id': 'VpcId',
        'zone_ids': 'ZoneIds'
    }

    def __init__(self, auto_renew=None, capacity=None, charge_type=None, create_time=None, deletion_protection=None, engine_version=None, expired_time=None, instance_class=None, instance_id=None, instance_name=None, maintenance_time=None, multi_az=None, node_number=None, project_name=None, region_id=None, shard_capacity=None, shard_capacity_v2=None, shard_number=None, sharded_cluster=None, status=None, subnet_id=None, tags=None, visit_addrs=None, vpc_auth_mode=None, vpc_id=None, zone_ids=None, _configuration=None):  # noqa: E501
        """DescribeDBInstanceDetailResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_renew = None
        self._capacity = None
        self._charge_type = None
        self._create_time = None
        self._deletion_protection = None
        self._engine_version = None
        self._expired_time = None
        self._instance_class = None
        self._instance_id = None
        self._instance_name = None
        self._maintenance_time = None
        self._multi_az = None
        self._node_number = None
        self._project_name = None
        self._region_id = None
        self._shard_capacity = None
        self._shard_capacity_v2 = None
        self._shard_number = None
        self._sharded_cluster = None
        self._status = None
        self._subnet_id = None
        self._tags = None
        self._visit_addrs = None
        self._vpc_auth_mode = None
        self._vpc_id = None
        self._zone_ids = None
        self.discriminator = None

        if auto_renew is not None:
            self.auto_renew = auto_renew
        if capacity is not None:
            self.capacity = capacity
        if charge_type is not None:
            self.charge_type = charge_type
        if create_time is not None:
            self.create_time = create_time
        if deletion_protection is not None:
            self.deletion_protection = deletion_protection
        if engine_version is not None:
            self.engine_version = engine_version
        if expired_time is not None:
            self.expired_time = expired_time
        if instance_class is not None:
            self.instance_class = instance_class
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if maintenance_time is not None:
            self.maintenance_time = maintenance_time
        if multi_az is not None:
            self.multi_az = multi_az
        if node_number is not None:
            self.node_number = node_number
        if project_name is not None:
            self.project_name = project_name
        if region_id is not None:
            self.region_id = region_id
        if shard_capacity is not None:
            self.shard_capacity = shard_capacity
        if shard_capacity_v2 is not None:
            self.shard_capacity_v2 = shard_capacity_v2
        if shard_number is not None:
            self.shard_number = shard_number
        if sharded_cluster is not None:
            self.sharded_cluster = sharded_cluster
        if status is not None:
            self.status = status
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if tags is not None:
            self.tags = tags
        if visit_addrs is not None:
            self.visit_addrs = visit_addrs
        if vpc_auth_mode is not None:
            self.vpc_auth_mode = vpc_auth_mode
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if zone_ids is not None:
            self.zone_ids = zone_ids

    @property
    def auto_renew(self):
        """Gets the auto_renew of this DescribeDBInstanceDetailResponse.  # noqa: E501


        :return: The auto_renew of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :rtype: bool
        """
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, auto_renew):
        """Sets the auto_renew of this DescribeDBInstanceDetailResponse.


        :param auto_renew: The auto_renew of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :type: bool
        """

        self._auto_renew = auto_renew

    @property
    def capacity(self):
        """Gets the capacity of this DescribeDBInstanceDetailResponse.  # noqa: E501


        :return: The capacity of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :rtype: CapacityForDescribeDBInstanceDetailOutput
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this DescribeDBInstanceDetailResponse.


        :param capacity: The capacity of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :type: CapacityForDescribeDBInstanceDetailOutput
        """

        self._capacity = capacity

    @property
    def charge_type(self):
        """Gets the charge_type of this DescribeDBInstanceDetailResponse.  # noqa: E501


        :return: The charge_type of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this DescribeDBInstanceDetailResponse.


        :param charge_type: The charge_type of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :type: str
        """

        self._charge_type = charge_type

    @property
    def create_time(self):
        """Gets the create_time of this DescribeDBInstanceDetailResponse.  # noqa: E501


        :return: The create_time of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DescribeDBInstanceDetailResponse.


        :param create_time: The create_time of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def deletion_protection(self):
        """Gets the deletion_protection of this DescribeDBInstanceDetailResponse.  # noqa: E501


        :return: The deletion_protection of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._deletion_protection

    @deletion_protection.setter
    def deletion_protection(self, deletion_protection):
        """Sets the deletion_protection of this DescribeDBInstanceDetailResponse.


        :param deletion_protection: The deletion_protection of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :type: str
        """

        self._deletion_protection = deletion_protection

    @property
    def engine_version(self):
        """Gets the engine_version of this DescribeDBInstanceDetailResponse.  # noqa: E501


        :return: The engine_version of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this DescribeDBInstanceDetailResponse.


        :param engine_version: The engine_version of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :type: str
        """

        self._engine_version = engine_version

    @property
    def expired_time(self):
        """Gets the expired_time of this DescribeDBInstanceDetailResponse.  # noqa: E501


        :return: The expired_time of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._expired_time

    @expired_time.setter
    def expired_time(self, expired_time):
        """Sets the expired_time of this DescribeDBInstanceDetailResponse.


        :param expired_time: The expired_time of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :type: str
        """

        self._expired_time = expired_time

    @property
    def instance_class(self):
        """Gets the instance_class of this DescribeDBInstanceDetailResponse.  # noqa: E501


        :return: The instance_class of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._instance_class

    @instance_class.setter
    def instance_class(self, instance_class):
        """Sets the instance_class of this DescribeDBInstanceDetailResponse.


        :param instance_class: The instance_class of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :type: str
        """

        self._instance_class = instance_class

    @property
    def instance_id(self):
        """Gets the instance_id of this DescribeDBInstanceDetailResponse.  # noqa: E501


        :return: The instance_id of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DescribeDBInstanceDetailResponse.


        :param instance_id: The instance_id of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this DescribeDBInstanceDetailResponse.  # noqa: E501


        :return: The instance_name of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this DescribeDBInstanceDetailResponse.


        :param instance_name: The instance_name of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def maintenance_time(self):
        """Gets the maintenance_time of this DescribeDBInstanceDetailResponse.  # noqa: E501


        :return: The maintenance_time of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._maintenance_time

    @maintenance_time.setter
    def maintenance_time(self, maintenance_time):
        """Sets the maintenance_time of this DescribeDBInstanceDetailResponse.


        :param maintenance_time: The maintenance_time of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :type: str
        """

        self._maintenance_time = maintenance_time

    @property
    def multi_az(self):
        """Gets the multi_az of this DescribeDBInstanceDetailResponse.  # noqa: E501


        :return: The multi_az of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._multi_az

    @multi_az.setter
    def multi_az(self, multi_az):
        """Sets the multi_az of this DescribeDBInstanceDetailResponse.


        :param multi_az: The multi_az of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :type: str
        """

        self._multi_az = multi_az

    @property
    def node_number(self):
        """Gets the node_number of this DescribeDBInstanceDetailResponse.  # noqa: E501


        :return: The node_number of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :rtype: int
        """
        return self._node_number

    @node_number.setter
    def node_number(self, node_number):
        """Sets the node_number of this DescribeDBInstanceDetailResponse.


        :param node_number: The node_number of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :type: int
        """

        self._node_number = node_number

    @property
    def project_name(self):
        """Gets the project_name of this DescribeDBInstanceDetailResponse.  # noqa: E501


        :return: The project_name of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DescribeDBInstanceDetailResponse.


        :param project_name: The project_name of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def region_id(self):
        """Gets the region_id of this DescribeDBInstanceDetailResponse.  # noqa: E501


        :return: The region_id of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this DescribeDBInstanceDetailResponse.


        :param region_id: The region_id of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :type: str
        """

        self._region_id = region_id

    @property
    def shard_capacity(self):
        """Gets the shard_capacity of this DescribeDBInstanceDetailResponse.  # noqa: E501


        :return: The shard_capacity of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :rtype: float
        """
        return self._shard_capacity

    @shard_capacity.setter
    def shard_capacity(self, shard_capacity):
        """Sets the shard_capacity of this DescribeDBInstanceDetailResponse.


        :param shard_capacity: The shard_capacity of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :type: float
        """

        self._shard_capacity = shard_capacity

    @property
    def shard_capacity_v2(self):
        """Gets the shard_capacity_v2 of this DescribeDBInstanceDetailResponse.  # noqa: E501


        :return: The shard_capacity_v2 of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :rtype: int
        """
        return self._shard_capacity_v2

    @shard_capacity_v2.setter
    def shard_capacity_v2(self, shard_capacity_v2):
        """Sets the shard_capacity_v2 of this DescribeDBInstanceDetailResponse.


        :param shard_capacity_v2: The shard_capacity_v2 of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :type: int
        """

        self._shard_capacity_v2 = shard_capacity_v2

    @property
    def shard_number(self):
        """Gets the shard_number of this DescribeDBInstanceDetailResponse.  # noqa: E501


        :return: The shard_number of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :rtype: int
        """
        return self._shard_number

    @shard_number.setter
    def shard_number(self, shard_number):
        """Sets the shard_number of this DescribeDBInstanceDetailResponse.


        :param shard_number: The shard_number of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :type: int
        """

        self._shard_number = shard_number

    @property
    def sharded_cluster(self):
        """Gets the sharded_cluster of this DescribeDBInstanceDetailResponse.  # noqa: E501


        :return: The sharded_cluster of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :rtype: int
        """
        return self._sharded_cluster

    @sharded_cluster.setter
    def sharded_cluster(self, sharded_cluster):
        """Sets the sharded_cluster of this DescribeDBInstanceDetailResponse.


        :param sharded_cluster: The sharded_cluster of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :type: int
        """

        self._sharded_cluster = sharded_cluster

    @property
    def status(self):
        """Gets the status of this DescribeDBInstanceDetailResponse.  # noqa: E501


        :return: The status of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DescribeDBInstanceDetailResponse.


        :param status: The status of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def subnet_id(self):
        """Gets the subnet_id of this DescribeDBInstanceDetailResponse.  # noqa: E501


        :return: The subnet_id of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this DescribeDBInstanceDetailResponse.


        :param subnet_id: The subnet_id of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :type: str
        """

        self._subnet_id = subnet_id

    @property
    def tags(self):
        """Gets the tags of this DescribeDBInstanceDetailResponse.  # noqa: E501


        :return: The tags of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :rtype: list[TagForDescribeDBInstanceDetailOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DescribeDBInstanceDetailResponse.


        :param tags: The tags of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :type: list[TagForDescribeDBInstanceDetailOutput]
        """

        self._tags = tags

    @property
    def visit_addrs(self):
        """Gets the visit_addrs of this DescribeDBInstanceDetailResponse.  # noqa: E501


        :return: The visit_addrs of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :rtype: list[VisitAddrForDescribeDBInstanceDetailOutput]
        """
        return self._visit_addrs

    @visit_addrs.setter
    def visit_addrs(self, visit_addrs):
        """Sets the visit_addrs of this DescribeDBInstanceDetailResponse.


        :param visit_addrs: The visit_addrs of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :type: list[VisitAddrForDescribeDBInstanceDetailOutput]
        """

        self._visit_addrs = visit_addrs

    @property
    def vpc_auth_mode(self):
        """Gets the vpc_auth_mode of this DescribeDBInstanceDetailResponse.  # noqa: E501


        :return: The vpc_auth_mode of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._vpc_auth_mode

    @vpc_auth_mode.setter
    def vpc_auth_mode(self, vpc_auth_mode):
        """Sets the vpc_auth_mode of this DescribeDBInstanceDetailResponse.


        :param vpc_auth_mode: The vpc_auth_mode of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :type: str
        """

        self._vpc_auth_mode = vpc_auth_mode

    @property
    def vpc_id(self):
        """Gets the vpc_id of this DescribeDBInstanceDetailResponse.  # noqa: E501


        :return: The vpc_id of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this DescribeDBInstanceDetailResponse.


        :param vpc_id: The vpc_id of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

    @property
    def zone_ids(self):
        """Gets the zone_ids of this DescribeDBInstanceDetailResponse.  # noqa: E501


        :return: The zone_ids of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._zone_ids

    @zone_ids.setter
    def zone_ids(self, zone_ids):
        """Sets the zone_ids of this DescribeDBInstanceDetailResponse.


        :param zone_ids: The zone_ids of this DescribeDBInstanceDetailResponse.  # noqa: E501
        :type: list[str]
        """

        self._zone_ids = zone_ids

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
        if issubclass(DescribeDBInstanceDetailResponse, dict):
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
        if not isinstance(other, DescribeDBInstanceDetailResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeDBInstanceDetailResponse):
            return True

        return self.to_dict() != other.to_dict()
