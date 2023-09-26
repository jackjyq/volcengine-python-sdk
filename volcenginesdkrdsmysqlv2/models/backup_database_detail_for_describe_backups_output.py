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


class BackupDatabaseDetailForDescribeBackupsOutput(object):
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
        'backup_end_time': 'str',
        'backup_file_name': 'str',
        'backup_file_size': 'int',
        'backup_start_time': 'str',
        'backup_type': 'str',
        'database_name': 'str'
    }

    attribute_map = {
        'backup_end_time': 'BackupEndTime',
        'backup_file_name': 'BackupFileName',
        'backup_file_size': 'BackupFileSize',
        'backup_start_time': 'BackupStartTime',
        'backup_type': 'BackupType',
        'database_name': 'DatabaseName'
    }

    def __init__(self, backup_end_time=None, backup_file_name=None, backup_file_size=None, backup_start_time=None, backup_type=None, database_name=None, _configuration=None):  # noqa: E501
        """BackupDatabaseDetailForDescribeBackupsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._backup_end_time = None
        self._backup_file_name = None
        self._backup_file_size = None
        self._backup_start_time = None
        self._backup_type = None
        self._database_name = None
        self.discriminator = None

        if backup_end_time is not None:
            self.backup_end_time = backup_end_time
        if backup_file_name is not None:
            self.backup_file_name = backup_file_name
        if backup_file_size is not None:
            self.backup_file_size = backup_file_size
        if backup_start_time is not None:
            self.backup_start_time = backup_start_time
        if backup_type is not None:
            self.backup_type = backup_type
        if database_name is not None:
            self.database_name = database_name

    @property
    def backup_end_time(self):
        """Gets the backup_end_time of this BackupDatabaseDetailForDescribeBackupsOutput.  # noqa: E501


        :return: The backup_end_time of this BackupDatabaseDetailForDescribeBackupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._backup_end_time

    @backup_end_time.setter
    def backup_end_time(self, backup_end_time):
        """Sets the backup_end_time of this BackupDatabaseDetailForDescribeBackupsOutput.


        :param backup_end_time: The backup_end_time of this BackupDatabaseDetailForDescribeBackupsOutput.  # noqa: E501
        :type: str
        """

        self._backup_end_time = backup_end_time

    @property
    def backup_file_name(self):
        """Gets the backup_file_name of this BackupDatabaseDetailForDescribeBackupsOutput.  # noqa: E501


        :return: The backup_file_name of this BackupDatabaseDetailForDescribeBackupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._backup_file_name

    @backup_file_name.setter
    def backup_file_name(self, backup_file_name):
        """Sets the backup_file_name of this BackupDatabaseDetailForDescribeBackupsOutput.


        :param backup_file_name: The backup_file_name of this BackupDatabaseDetailForDescribeBackupsOutput.  # noqa: E501
        :type: str
        """

        self._backup_file_name = backup_file_name

    @property
    def backup_file_size(self):
        """Gets the backup_file_size of this BackupDatabaseDetailForDescribeBackupsOutput.  # noqa: E501


        :return: The backup_file_size of this BackupDatabaseDetailForDescribeBackupsOutput.  # noqa: E501
        :rtype: int
        """
        return self._backup_file_size

    @backup_file_size.setter
    def backup_file_size(self, backup_file_size):
        """Sets the backup_file_size of this BackupDatabaseDetailForDescribeBackupsOutput.


        :param backup_file_size: The backup_file_size of this BackupDatabaseDetailForDescribeBackupsOutput.  # noqa: E501
        :type: int
        """

        self._backup_file_size = backup_file_size

    @property
    def backup_start_time(self):
        """Gets the backup_start_time of this BackupDatabaseDetailForDescribeBackupsOutput.  # noqa: E501


        :return: The backup_start_time of this BackupDatabaseDetailForDescribeBackupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._backup_start_time

    @backup_start_time.setter
    def backup_start_time(self, backup_start_time):
        """Sets the backup_start_time of this BackupDatabaseDetailForDescribeBackupsOutput.


        :param backup_start_time: The backup_start_time of this BackupDatabaseDetailForDescribeBackupsOutput.  # noqa: E501
        :type: str
        """

        self._backup_start_time = backup_start_time

    @property
    def backup_type(self):
        """Gets the backup_type of this BackupDatabaseDetailForDescribeBackupsOutput.  # noqa: E501


        :return: The backup_type of this BackupDatabaseDetailForDescribeBackupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        """Sets the backup_type of this BackupDatabaseDetailForDescribeBackupsOutput.


        :param backup_type: The backup_type of this BackupDatabaseDetailForDescribeBackupsOutput.  # noqa: E501
        :type: str
        """

        self._backup_type = backup_type

    @property
    def database_name(self):
        """Gets the database_name of this BackupDatabaseDetailForDescribeBackupsOutput.  # noqa: E501


        :return: The database_name of this BackupDatabaseDetailForDescribeBackupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this BackupDatabaseDetailForDescribeBackupsOutput.


        :param database_name: The database_name of this BackupDatabaseDetailForDescribeBackupsOutput.  # noqa: E501
        :type: str
        """

        self._database_name = database_name

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
        if issubclass(BackupDatabaseDetailForDescribeBackupsOutput, dict):
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
        if not isinstance(other, BackupDatabaseDetailForDescribeBackupsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BackupDatabaseDetailForDescribeBackupsOutput):
            return True

        return self.to_dict() != other.to_dict()