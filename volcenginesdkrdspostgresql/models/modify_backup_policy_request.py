# coding: utf-8

"""
    rds_postgresql

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ModifyBackupPolicyRequest(object):
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
        'backup_retention_period': 'int',
        'full_backup_period': 'str',
        'full_backup_time': 'str',
        'increment_backup_frequency': 'int',
        'instance_id': 'str'
    }

    attribute_map = {
        'backup_retention_period': 'BackupRetentionPeriod',
        'full_backup_period': 'FullBackupPeriod',
        'full_backup_time': 'FullBackupTime',
        'increment_backup_frequency': 'IncrementBackupFrequency',
        'instance_id': 'InstanceId'
    }

    def __init__(self, backup_retention_period=None, full_backup_period=None, full_backup_time=None, increment_backup_frequency=None, instance_id=None, _configuration=None):  # noqa: E501
        """ModifyBackupPolicyRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._backup_retention_period = None
        self._full_backup_period = None
        self._full_backup_time = None
        self._increment_backup_frequency = None
        self._instance_id = None
        self.discriminator = None

        if backup_retention_period is not None:
            self.backup_retention_period = backup_retention_period
        if full_backup_period is not None:
            self.full_backup_period = full_backup_period
        if full_backup_time is not None:
            self.full_backup_time = full_backup_time
        if increment_backup_frequency is not None:
            self.increment_backup_frequency = increment_backup_frequency
        self.instance_id = instance_id

    @property
    def backup_retention_period(self):
        """Gets the backup_retention_period of this ModifyBackupPolicyRequest.  # noqa: E501


        :return: The backup_retention_period of this ModifyBackupPolicyRequest.  # noqa: E501
        :rtype: int
        """
        return self._backup_retention_period

    @backup_retention_period.setter
    def backup_retention_period(self, backup_retention_period):
        """Sets the backup_retention_period of this ModifyBackupPolicyRequest.


        :param backup_retention_period: The backup_retention_period of this ModifyBackupPolicyRequest.  # noqa: E501
        :type: int
        """

        self._backup_retention_period = backup_retention_period

    @property
    def full_backup_period(self):
        """Gets the full_backup_period of this ModifyBackupPolicyRequest.  # noqa: E501


        :return: The full_backup_period of this ModifyBackupPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._full_backup_period

    @full_backup_period.setter
    def full_backup_period(self, full_backup_period):
        """Sets the full_backup_period of this ModifyBackupPolicyRequest.


        :param full_backup_period: The full_backup_period of this ModifyBackupPolicyRequest.  # noqa: E501
        :type: str
        """

        self._full_backup_period = full_backup_period

    @property
    def full_backup_time(self):
        """Gets the full_backup_time of this ModifyBackupPolicyRequest.  # noqa: E501


        :return: The full_backup_time of this ModifyBackupPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._full_backup_time

    @full_backup_time.setter
    def full_backup_time(self, full_backup_time):
        """Sets the full_backup_time of this ModifyBackupPolicyRequest.


        :param full_backup_time: The full_backup_time of this ModifyBackupPolicyRequest.  # noqa: E501
        :type: str
        """

        self._full_backup_time = full_backup_time

    @property
    def increment_backup_frequency(self):
        """Gets the increment_backup_frequency of this ModifyBackupPolicyRequest.  # noqa: E501


        :return: The increment_backup_frequency of this ModifyBackupPolicyRequest.  # noqa: E501
        :rtype: int
        """
        return self._increment_backup_frequency

    @increment_backup_frequency.setter
    def increment_backup_frequency(self, increment_backup_frequency):
        """Sets the increment_backup_frequency of this ModifyBackupPolicyRequest.


        :param increment_backup_frequency: The increment_backup_frequency of this ModifyBackupPolicyRequest.  # noqa: E501
        :type: int
        """

        self._increment_backup_frequency = increment_backup_frequency

    @property
    def instance_id(self):
        """Gets the instance_id of this ModifyBackupPolicyRequest.  # noqa: E501


        :return: The instance_id of this ModifyBackupPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ModifyBackupPolicyRequest.


        :param instance_id: The instance_id of this ModifyBackupPolicyRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

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
        if issubclass(ModifyBackupPolicyRequest, dict):
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
        if not isinstance(other, ModifyBackupPolicyRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyBackupPolicyRequest):
            return True

        return self.to_dict() != other.to_dict()
