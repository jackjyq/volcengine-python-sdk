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


class ModifyCrossBackupPolicyRequest(object):
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
        'backup_enabled': 'bool',
        'cross_backup_region': 'str',
        'instance_id': 'str',
        'log_backup_enabled': 'bool',
        'retention': 'int'
    }

    attribute_map = {
        'backup_enabled': 'BackupEnabled',
        'cross_backup_region': 'CrossBackupRegion',
        'instance_id': 'InstanceId',
        'log_backup_enabled': 'LogBackupEnabled',
        'retention': 'Retention'
    }

    def __init__(self, backup_enabled=None, cross_backup_region=None, instance_id=None, log_backup_enabled=None, retention=None, _configuration=None):  # noqa: E501
        """ModifyCrossBackupPolicyRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._backup_enabled = None
        self._cross_backup_region = None
        self._instance_id = None
        self._log_backup_enabled = None
        self._retention = None
        self.discriminator = None

        if backup_enabled is not None:
            self.backup_enabled = backup_enabled
        if cross_backup_region is not None:
            self.cross_backup_region = cross_backup_region
        if instance_id is not None:
            self.instance_id = instance_id
        if log_backup_enabled is not None:
            self.log_backup_enabled = log_backup_enabled
        if retention is not None:
            self.retention = retention

    @property
    def backup_enabled(self):
        """Gets the backup_enabled of this ModifyCrossBackupPolicyRequest.  # noqa: E501


        :return: The backup_enabled of this ModifyCrossBackupPolicyRequest.  # noqa: E501
        :rtype: bool
        """
        return self._backup_enabled

    @backup_enabled.setter
    def backup_enabled(self, backup_enabled):
        """Sets the backup_enabled of this ModifyCrossBackupPolicyRequest.


        :param backup_enabled: The backup_enabled of this ModifyCrossBackupPolicyRequest.  # noqa: E501
        :type: bool
        """

        self._backup_enabled = backup_enabled

    @property
    def cross_backup_region(self):
        """Gets the cross_backup_region of this ModifyCrossBackupPolicyRequest.  # noqa: E501


        :return: The cross_backup_region of this ModifyCrossBackupPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._cross_backup_region

    @cross_backup_region.setter
    def cross_backup_region(self, cross_backup_region):
        """Sets the cross_backup_region of this ModifyCrossBackupPolicyRequest.


        :param cross_backup_region: The cross_backup_region of this ModifyCrossBackupPolicyRequest.  # noqa: E501
        :type: str
        """

        self._cross_backup_region = cross_backup_region

    @property
    def instance_id(self):
        """Gets the instance_id of this ModifyCrossBackupPolicyRequest.  # noqa: E501


        :return: The instance_id of this ModifyCrossBackupPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ModifyCrossBackupPolicyRequest.


        :param instance_id: The instance_id of this ModifyCrossBackupPolicyRequest.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def log_backup_enabled(self):
        """Gets the log_backup_enabled of this ModifyCrossBackupPolicyRequest.  # noqa: E501


        :return: The log_backup_enabled of this ModifyCrossBackupPolicyRequest.  # noqa: E501
        :rtype: bool
        """
        return self._log_backup_enabled

    @log_backup_enabled.setter
    def log_backup_enabled(self, log_backup_enabled):
        """Sets the log_backup_enabled of this ModifyCrossBackupPolicyRequest.


        :param log_backup_enabled: The log_backup_enabled of this ModifyCrossBackupPolicyRequest.  # noqa: E501
        :type: bool
        """

        self._log_backup_enabled = log_backup_enabled

    @property
    def retention(self):
        """Gets the retention of this ModifyCrossBackupPolicyRequest.  # noqa: E501


        :return: The retention of this ModifyCrossBackupPolicyRequest.  # noqa: E501
        :rtype: int
        """
        return self._retention

    @retention.setter
    def retention(self, retention):
        """Sets the retention of this ModifyCrossBackupPolicyRequest.


        :param retention: The retention of this ModifyCrossBackupPolicyRequest.  # noqa: E501
        :type: int
        """

        self._retention = retention

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
        if issubclass(ModifyCrossBackupPolicyRequest, dict):
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
        if not isinstance(other, ModifyCrossBackupPolicyRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyCrossBackupPolicyRequest):
            return True

        return self.to_dict() != other.to_dict()
