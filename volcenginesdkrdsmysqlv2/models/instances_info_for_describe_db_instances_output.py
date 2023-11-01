# coding: utf-8

"""
    rds_mysql_v2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class InstancesInfoForDescribeDBInstancesOutput(object):
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
        'address_object': 'list[AddressObjectForDescribeDBInstancesOutput]',
        'allow_list_version': 'str',
        'charge_detail': 'ChargeDetailForDescribeDBInstancesOutput',
        'create_time': 'str',
        'db_engine_version': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'instance_status': 'str',
        'instance_type': 'str',
        'lower_case_table_names': 'str',
        'node_detail_info': 'list[NodeDetailInfoForDescribeDBInstancesOutput]',
        'node_number': 'int',
        'node_spec': 'str',
        'port': 'str',
        'project_name': 'str',
        'region_id': 'str',
        'server_collation': 'str',
        'shard_number': 'int',
        'storage_space': 'int',
        'storage_type': 'str',
        'storage_use': 'int',
        'subnet_id': 'str',
        'time_zone': 'str',
        'vpc_id': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'address_object': 'AddressObject',
        'allow_list_version': 'AllowListVersion',
        'charge_detail': 'ChargeDetail',
        'create_time': 'CreateTime',
        'db_engine_version': 'DBEngineVersion',
        'instance_id': 'InstanceId',
        'instance_name': 'InstanceName',
        'instance_status': 'InstanceStatus',
        'instance_type': 'InstanceType',
        'lower_case_table_names': 'LowerCaseTableNames',
        'node_detail_info': 'NodeDetailInfo',
        'node_number': 'NodeNumber',
        'node_spec': 'NodeSpec',
        'port': 'Port',
        'project_name': 'ProjectName',
        'region_id': 'RegionId',
        'server_collation': 'ServerCollation',
        'shard_number': 'ShardNumber',
        'storage_space': 'StorageSpace',
        'storage_type': 'StorageType',
        'storage_use': 'StorageUse',
        'subnet_id': 'SubnetId',
        'time_zone': 'TimeZone',
        'vpc_id': 'VpcId',
        'zone_id': 'ZoneId'
    }

    def __init__(self, account_id=None, address_object=None, allow_list_version=None, charge_detail=None, create_time=None, db_engine_version=None, instance_id=None, instance_name=None, instance_status=None, instance_type=None, lower_case_table_names=None, node_detail_info=None, node_number=None, node_spec=None, port=None, project_name=None, region_id=None, server_collation=None, shard_number=None, storage_space=None, storage_type=None, storage_use=None, subnet_id=None, time_zone=None, vpc_id=None, zone_id=None, _configuration=None):  # noqa: E501
        """InstancesInfoForDescribeDBInstancesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._address_object = None
        self._allow_list_version = None
        self._charge_detail = None
        self._create_time = None
        self._db_engine_version = None
        self._instance_id = None
        self._instance_name = None
        self._instance_status = None
        self._instance_type = None
        self._lower_case_table_names = None
        self._node_detail_info = None
        self._node_number = None
        self._node_spec = None
        self._port = None
        self._project_name = None
        self._region_id = None
        self._server_collation = None
        self._shard_number = None
        self._storage_space = None
        self._storage_type = None
        self._storage_use = None
        self._subnet_id = None
        self._time_zone = None
        self._vpc_id = None
        self._zone_id = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if address_object is not None:
            self.address_object = address_object
        if allow_list_version is not None:
            self.allow_list_version = allow_list_version
        if charge_detail is not None:
            self.charge_detail = charge_detail
        if create_time is not None:
            self.create_time = create_time
        if db_engine_version is not None:
            self.db_engine_version = db_engine_version
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_status is not None:
            self.instance_status = instance_status
        if instance_type is not None:
            self.instance_type = instance_type
        if lower_case_table_names is not None:
            self.lower_case_table_names = lower_case_table_names
        if node_detail_info is not None:
            self.node_detail_info = node_detail_info
        if node_number is not None:
            self.node_number = node_number
        if node_spec is not None:
            self.node_spec = node_spec
        if port is not None:
            self.port = port
        if project_name is not None:
            self.project_name = project_name
        if region_id is not None:
            self.region_id = region_id
        if server_collation is not None:
            self.server_collation = server_collation
        if shard_number is not None:
            self.shard_number = shard_number
        if storage_space is not None:
            self.storage_space = storage_space
        if storage_type is not None:
            self.storage_type = storage_type
        if storage_use is not None:
            self.storage_use = storage_use
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if time_zone is not None:
            self.time_zone = time_zone
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def account_id(self):
        """Gets the account_id of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501


        :return: The account_id of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this InstancesInfoForDescribeDBInstancesOutput.


        :param account_id: The account_id of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def address_object(self):
        """Gets the address_object of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501


        :return: The address_object of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: list[AddressObjectForDescribeDBInstancesOutput]
        """
        return self._address_object

    @address_object.setter
    def address_object(self, address_object):
        """Sets the address_object of this InstancesInfoForDescribeDBInstancesOutput.


        :param address_object: The address_object of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :type: list[AddressObjectForDescribeDBInstancesOutput]
        """

        self._address_object = address_object

    @property
    def allow_list_version(self):
        """Gets the allow_list_version of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501


        :return: The allow_list_version of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._allow_list_version

    @allow_list_version.setter
    def allow_list_version(self, allow_list_version):
        """Sets the allow_list_version of this InstancesInfoForDescribeDBInstancesOutput.


        :param allow_list_version: The allow_list_version of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._allow_list_version = allow_list_version

    @property
    def charge_detail(self):
        """Gets the charge_detail of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501


        :return: The charge_detail of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: ChargeDetailForDescribeDBInstancesOutput
        """
        return self._charge_detail

    @charge_detail.setter
    def charge_detail(self, charge_detail):
        """Sets the charge_detail of this InstancesInfoForDescribeDBInstancesOutput.


        :param charge_detail: The charge_detail of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :type: ChargeDetailForDescribeDBInstancesOutput
        """

        self._charge_detail = charge_detail

    @property
    def create_time(self):
        """Gets the create_time of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501


        :return: The create_time of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this InstancesInfoForDescribeDBInstancesOutput.


        :param create_time: The create_time of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def db_engine_version(self):
        """Gets the db_engine_version of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501


        :return: The db_engine_version of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._db_engine_version

    @db_engine_version.setter
    def db_engine_version(self, db_engine_version):
        """Sets the db_engine_version of this InstancesInfoForDescribeDBInstancesOutput.


        :param db_engine_version: The db_engine_version of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._db_engine_version = db_engine_version

    @property
    def instance_id(self):
        """Gets the instance_id of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501


        :return: The instance_id of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this InstancesInfoForDescribeDBInstancesOutput.


        :param instance_id: The instance_id of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501


        :return: The instance_name of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this InstancesInfoForDescribeDBInstancesOutput.


        :param instance_name: The instance_name of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def instance_status(self):
        """Gets the instance_status of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501


        :return: The instance_status of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        """Sets the instance_status of this InstancesInfoForDescribeDBInstancesOutput.


        :param instance_status: The instance_status of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._instance_status = instance_status

    @property
    def instance_type(self):
        """Gets the instance_type of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501


        :return: The instance_type of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this InstancesInfoForDescribeDBInstancesOutput.


        :param instance_type: The instance_type of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._instance_type = instance_type

    @property
    def lower_case_table_names(self):
        """Gets the lower_case_table_names of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501


        :return: The lower_case_table_names of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._lower_case_table_names

    @lower_case_table_names.setter
    def lower_case_table_names(self, lower_case_table_names):
        """Sets the lower_case_table_names of this InstancesInfoForDescribeDBInstancesOutput.


        :param lower_case_table_names: The lower_case_table_names of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._lower_case_table_names = lower_case_table_names

    @property
    def node_detail_info(self):
        """Gets the node_detail_info of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501


        :return: The node_detail_info of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: list[NodeDetailInfoForDescribeDBInstancesOutput]
        """
        return self._node_detail_info

    @node_detail_info.setter
    def node_detail_info(self, node_detail_info):
        """Sets the node_detail_info of this InstancesInfoForDescribeDBInstancesOutput.


        :param node_detail_info: The node_detail_info of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :type: list[NodeDetailInfoForDescribeDBInstancesOutput]
        """

        self._node_detail_info = node_detail_info

    @property
    def node_number(self):
        """Gets the node_number of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501


        :return: The node_number of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: int
        """
        return self._node_number

    @node_number.setter
    def node_number(self, node_number):
        """Sets the node_number of this InstancesInfoForDescribeDBInstancesOutput.


        :param node_number: The node_number of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :type: int
        """

        self._node_number = node_number

    @property
    def node_spec(self):
        """Gets the node_spec of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501


        :return: The node_spec of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._node_spec

    @node_spec.setter
    def node_spec(self, node_spec):
        """Sets the node_spec of this InstancesInfoForDescribeDBInstancesOutput.


        :param node_spec: The node_spec of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._node_spec = node_spec

    @property
    def port(self):
        """Gets the port of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501


        :return: The port of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this InstancesInfoForDescribeDBInstancesOutput.


        :param port: The port of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def project_name(self):
        """Gets the project_name of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501


        :return: The project_name of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this InstancesInfoForDescribeDBInstancesOutput.


        :param project_name: The project_name of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def region_id(self):
        """Gets the region_id of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501


        :return: The region_id of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this InstancesInfoForDescribeDBInstancesOutput.


        :param region_id: The region_id of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._region_id = region_id

    @property
    def server_collation(self):
        """Gets the server_collation of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501


        :return: The server_collation of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._server_collation

    @server_collation.setter
    def server_collation(self, server_collation):
        """Sets the server_collation of this InstancesInfoForDescribeDBInstancesOutput.


        :param server_collation: The server_collation of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._server_collation = server_collation

    @property
    def shard_number(self):
        """Gets the shard_number of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501


        :return: The shard_number of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: int
        """
        return self._shard_number

    @shard_number.setter
    def shard_number(self, shard_number):
        """Sets the shard_number of this InstancesInfoForDescribeDBInstancesOutput.


        :param shard_number: The shard_number of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :type: int
        """

        self._shard_number = shard_number

    @property
    def storage_space(self):
        """Gets the storage_space of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501


        :return: The storage_space of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: int
        """
        return self._storage_space

    @storage_space.setter
    def storage_space(self, storage_space):
        """Sets the storage_space of this InstancesInfoForDescribeDBInstancesOutput.


        :param storage_space: The storage_space of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :type: int
        """

        self._storage_space = storage_space

    @property
    def storage_type(self):
        """Gets the storage_type of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501


        :return: The storage_type of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this InstancesInfoForDescribeDBInstancesOutput.


        :param storage_type: The storage_type of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._storage_type = storage_type

    @property
    def storage_use(self):
        """Gets the storage_use of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501


        :return: The storage_use of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: int
        """
        return self._storage_use

    @storage_use.setter
    def storage_use(self, storage_use):
        """Sets the storage_use of this InstancesInfoForDescribeDBInstancesOutput.


        :param storage_use: The storage_use of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :type: int
        """

        self._storage_use = storage_use

    @property
    def subnet_id(self):
        """Gets the subnet_id of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501


        :return: The subnet_id of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this InstancesInfoForDescribeDBInstancesOutput.


        :param subnet_id: The subnet_id of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._subnet_id = subnet_id

    @property
    def time_zone(self):
        """Gets the time_zone of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501


        :return: The time_zone of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this InstancesInfoForDescribeDBInstancesOutput.


        :param time_zone: The time_zone of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._time_zone = time_zone

    @property
    def vpc_id(self):
        """Gets the vpc_id of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501


        :return: The vpc_id of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this InstancesInfoForDescribeDBInstancesOutput.


        :param vpc_id: The vpc_id of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

    @property
    def zone_id(self):
        """Gets the zone_id of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501


        :return: The zone_id of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this InstancesInfoForDescribeDBInstancesOutput.


        :param zone_id: The zone_id of this InstancesInfoForDescribeDBInstancesOutput.  # noqa: E501
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
        if issubclass(InstancesInfoForDescribeDBInstancesOutput, dict):
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
        if not isinstance(other, InstancesInfoForDescribeDBInstancesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstancesInfoForDescribeDBInstancesOutput):
            return True

        return self.to_dict() != other.to_dict()
