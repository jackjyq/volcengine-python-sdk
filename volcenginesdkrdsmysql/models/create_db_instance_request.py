# coding: utf-8

"""
    rds_mysql

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateDBInstanceRequest(object):
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
        'charge_type': 'str',
        'db_engine': 'str',
        'db_engine_version': 'str',
        'instance_category': 'str',
        'instance_spec_name': 'str',
        'instance_type': 'str',
        'number': 'int',
        'prepaid_period': 'str',
        'region': 'str',
        'storage_space_gb': 'int',
        'storage_type': 'str',
        'used_time': 'int',
        'vpc_id': 'str',
        'zone': 'str'
    }

    attribute_map = {
        'auto_renew': 'AutoRenew',
        'charge_type': 'ChargeType',
        'db_engine': 'DBEngine',
        'db_engine_version': 'DBEngineVersion',
        'instance_category': 'InstanceCategory',
        'instance_spec_name': 'InstanceSpecName',
        'instance_type': 'InstanceType',
        'number': 'Number',
        'prepaid_period': 'PrepaidPeriod',
        'region': 'Region',
        'storage_space_gb': 'StorageSpaceGB',
        'storage_type': 'StorageType',
        'used_time': 'UsedTime',
        'vpc_id': 'VpcID',
        'zone': 'Zone'
    }

    def __init__(self, auto_renew=None, charge_type=None, db_engine=None, db_engine_version=None, instance_category=None, instance_spec_name=None, instance_type=None, number=None, prepaid_period=None, region=None, storage_space_gb=None, storage_type=None, used_time=None, vpc_id=None, zone=None, _configuration=None):  # noqa: E501
        """CreateDBInstanceRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_renew = None
        self._charge_type = None
        self._db_engine = None
        self._db_engine_version = None
        self._instance_category = None
        self._instance_spec_name = None
        self._instance_type = None
        self._number = None
        self._prepaid_period = None
        self._region = None
        self._storage_space_gb = None
        self._storage_type = None
        self._used_time = None
        self._vpc_id = None
        self._zone = None
        self.discriminator = None

        if auto_renew is not None:
            self.auto_renew = auto_renew
        if charge_type is not None:
            self.charge_type = charge_type
        if db_engine is not None:
            self.db_engine = db_engine
        if db_engine_version is not None:
            self.db_engine_version = db_engine_version
        if instance_category is not None:
            self.instance_category = instance_category
        if instance_spec_name is not None:
            self.instance_spec_name = instance_spec_name
        if instance_type is not None:
            self.instance_type = instance_type
        if number is not None:
            self.number = number
        if prepaid_period is not None:
            self.prepaid_period = prepaid_period
        self.region = region
        self.storage_space_gb = storage_space_gb
        if storage_type is not None:
            self.storage_type = storage_type
        if used_time is not None:
            self.used_time = used_time
        if vpc_id is not None:
            self.vpc_id = vpc_id
        self.zone = zone

    @property
    def auto_renew(self):
        """Gets the auto_renew of this CreateDBInstanceRequest.  # noqa: E501


        :return: The auto_renew of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: bool
        """
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, auto_renew):
        """Sets the auto_renew of this CreateDBInstanceRequest.


        :param auto_renew: The auto_renew of this CreateDBInstanceRequest.  # noqa: E501
        :type: bool
        """

        self._auto_renew = auto_renew

    @property
    def charge_type(self):
        """Gets the charge_type of this CreateDBInstanceRequest.  # noqa: E501


        :return: The charge_type of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this CreateDBInstanceRequest.


        :param charge_type: The charge_type of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["NotEnabled", "PostPaid", "Prepaid"]  # noqa: E501
        if (self._configuration.client_side_validation and
                charge_type not in allowed_values):
            raise ValueError(
                "Invalid value for `charge_type` ({0}), must be one of {1}"  # noqa: E501
                .format(charge_type, allowed_values)
            )

        self._charge_type = charge_type

    @property
    def db_engine(self):
        """Gets the db_engine of this CreateDBInstanceRequest.  # noqa: E501


        :return: The db_engine of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._db_engine

    @db_engine.setter
    def db_engine(self, db_engine):
        """Sets the db_engine of this CreateDBInstanceRequest.


        :param db_engine: The db_engine of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["MySQL", "Postgres", "Sqlserver"]  # noqa: E501
        if (self._configuration.client_side_validation and
                db_engine not in allowed_values):
            raise ValueError(
                "Invalid value for `db_engine` ({0}), must be one of {1}"  # noqa: E501
                .format(db_engine, allowed_values)
            )

        self._db_engine = db_engine

    @property
    def db_engine_version(self):
        """Gets the db_engine_version of this CreateDBInstanceRequest.  # noqa: E501


        :return: The db_engine_version of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._db_engine_version

    @db_engine_version.setter
    def db_engine_version(self, db_engine_version):
        """Sets the db_engine_version of this CreateDBInstanceRequest.


        :param db_engine_version: The db_engine_version of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["MySQL_5_5", "MySQL_5_6", "MySQL_8_0", "MySQL_Community_5_7", "Postgres_12", "SQLServer_2019_Ent", "SQLServer_2019_Std", "SQLServer_2019_Web"]  # noqa: E501
        if (self._configuration.client_side_validation and
                db_engine_version not in allowed_values):
            raise ValueError(
                "Invalid value for `db_engine_version` ({0}), must be one of {1}"  # noqa: E501
                .format(db_engine_version, allowed_values)
            )

        self._db_engine_version = db_engine_version

    @property
    def instance_category(self):
        """Gets the instance_category of this CreateDBInstanceRequest.  # noqa: E501


        :return: The instance_category of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_category

    @instance_category.setter
    def instance_category(self, instance_category):
        """Sets the instance_category of this CreateDBInstanceRequest.


        :param instance_category: The instance_category of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Primary", "ReadOnly"]  # noqa: E501
        if (self._configuration.client_side_validation and
                instance_category not in allowed_values):
            raise ValueError(
                "Invalid value for `instance_category` ({0}), must be one of {1}"  # noqa: E501
                .format(instance_category, allowed_values)
            )

        self._instance_category = instance_category

    @property
    def instance_spec_name(self):
        """Gets the instance_spec_name of this CreateDBInstanceRequest.  # noqa: E501


        :return: The instance_spec_name of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_spec_name

    @instance_spec_name.setter
    def instance_spec_name(self, instance_spec_name):
        """Sets the instance_spec_name of this CreateDBInstanceRequest.


        :param instance_spec_name: The instance_spec_name of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._instance_spec_name = instance_spec_name

    @property
    def instance_type(self):
        """Gets the instance_type of this CreateDBInstanceRequest.  # noqa: E501


        :return: The instance_type of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this CreateDBInstanceRequest.


        :param instance_type: The instance_type of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Basic", "Cluster", "Finance", "HA"]  # noqa: E501
        if (self._configuration.client_side_validation and
                instance_type not in allowed_values):
            raise ValueError(
                "Invalid value for `instance_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instance_type, allowed_values)
            )

        self._instance_type = instance_type

    @property
    def number(self):
        """Gets the number of this CreateDBInstanceRequest.  # noqa: E501


        :return: The number of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this CreateDBInstanceRequest.


        :param number: The number of this CreateDBInstanceRequest.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def prepaid_period(self):
        """Gets the prepaid_period of this CreateDBInstanceRequest.  # noqa: E501


        :return: The prepaid_period of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._prepaid_period

    @prepaid_period.setter
    def prepaid_period(self, prepaid_period):
        """Sets the prepaid_period of this CreateDBInstanceRequest.


        :param prepaid_period: The prepaid_period of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Month", "Year"]  # noqa: E501
        if (self._configuration.client_side_validation and
                prepaid_period not in allowed_values):
            raise ValueError(
                "Invalid value for `prepaid_period` ({0}), must be one of {1}"  # noqa: E501
                .format(prepaid_period, allowed_values)
            )

        self._prepaid_period = prepaid_period

    @property
    def region(self):
        """Gets the region of this CreateDBInstanceRequest.  # noqa: E501


        :return: The region of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CreateDBInstanceRequest.


        :param region: The region of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and region is None:
            raise ValueError("Invalid value for `region`, must not be `None`")  # noqa: E501

        self._region = region

    @property
    def storage_space_gb(self):
        """Gets the storage_space_gb of this CreateDBInstanceRequest.  # noqa: E501


        :return: The storage_space_gb of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._storage_space_gb

    @storage_space_gb.setter
    def storage_space_gb(self, storage_space_gb):
        """Sets the storage_space_gb of this CreateDBInstanceRequest.


        :param storage_space_gb: The storage_space_gb of this CreateDBInstanceRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and storage_space_gb is None:
            raise ValueError("Invalid value for `storage_space_gb`, must not be `None`")  # noqa: E501

        self._storage_space_gb = storage_space_gb

    @property
    def storage_type(self):
        """Gets the storage_type of this CreateDBInstanceRequest.  # noqa: E501


        :return: The storage_type of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this CreateDBInstanceRequest.


        :param storage_type: The storage_type of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["CloudStorage", "ESSDFlexPL", "LocalSSD"]  # noqa: E501
        if (self._configuration.client_side_validation and
                storage_type not in allowed_values):
            raise ValueError(
                "Invalid value for `storage_type` ({0}), must be one of {1}"  # noqa: E501
                .format(storage_type, allowed_values)
            )

        self._storage_type = storage_type

    @property
    def used_time(self):
        """Gets the used_time of this CreateDBInstanceRequest.  # noqa: E501


        :return: The used_time of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._used_time

    @used_time.setter
    def used_time(self, used_time):
        """Sets the used_time of this CreateDBInstanceRequest.


        :param used_time: The used_time of this CreateDBInstanceRequest.  # noqa: E501
        :type: int
        """

        self._used_time = used_time

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateDBInstanceRequest.  # noqa: E501


        :return: The vpc_id of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateDBInstanceRequest.


        :param vpc_id: The vpc_id of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

    @property
    def zone(self):
        """Gets the zone of this CreateDBInstanceRequest.  # noqa: E501


        :return: The zone of this CreateDBInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this CreateDBInstanceRequest.


        :param zone: The zone of this CreateDBInstanceRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and zone is None:
            raise ValueError("Invalid value for `zone`, must not be `None`")  # noqa: E501

        self._zone = zone

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
        if issubclass(CreateDBInstanceRequest, dict):
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
        if not isinstance(other, CreateDBInstanceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDBInstanceRequest):
            return True

        return self.to_dict() != other.to_dict()