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


class SlowQueryForDescribeSlowLogsOutput(object):
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
        'db_name': 'str',
        'execution_start_time': 'str',
        'host_address': 'str',
        'lock_times': 'int',
        'parse_row_counts': 'int',
        'query_text': 'str',
        'query_times': 'int',
        'query_type': 'str',
        'return_row_counts': 'int',
        'user_name': 'str'
    }

    attribute_map = {
        'db_name': 'DBName',
        'execution_start_time': 'ExecutionStartTime',
        'host_address': 'HostAddress',
        'lock_times': 'LockTimes',
        'parse_row_counts': 'ParseRowCounts',
        'query_text': 'QueryText',
        'query_times': 'QueryTimes',
        'query_type': 'QueryType',
        'return_row_counts': 'ReturnRowCounts',
        'user_name': 'UserName'
    }

    def __init__(self, db_name=None, execution_start_time=None, host_address=None, lock_times=None, parse_row_counts=None, query_text=None, query_times=None, query_type=None, return_row_counts=None, user_name=None, _configuration=None):  # noqa: E501
        """SlowQueryForDescribeSlowLogsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._db_name = None
        self._execution_start_time = None
        self._host_address = None
        self._lock_times = None
        self._parse_row_counts = None
        self._query_text = None
        self._query_times = None
        self._query_type = None
        self._return_row_counts = None
        self._user_name = None
        self.discriminator = None

        if db_name is not None:
            self.db_name = db_name
        if execution_start_time is not None:
            self.execution_start_time = execution_start_time
        if host_address is not None:
            self.host_address = host_address
        if lock_times is not None:
            self.lock_times = lock_times
        if parse_row_counts is not None:
            self.parse_row_counts = parse_row_counts
        if query_text is not None:
            self.query_text = query_text
        if query_times is not None:
            self.query_times = query_times
        if query_type is not None:
            self.query_type = query_type
        if return_row_counts is not None:
            self.return_row_counts = return_row_counts
        if user_name is not None:
            self.user_name = user_name

    @property
    def db_name(self):
        """Gets the db_name of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501


        :return: The db_name of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this SlowQueryForDescribeSlowLogsOutput.


        :param db_name: The db_name of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501
        :type: str
        """

        self._db_name = db_name

    @property
    def execution_start_time(self):
        """Gets the execution_start_time of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501


        :return: The execution_start_time of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501
        :rtype: str
        """
        return self._execution_start_time

    @execution_start_time.setter
    def execution_start_time(self, execution_start_time):
        """Sets the execution_start_time of this SlowQueryForDescribeSlowLogsOutput.


        :param execution_start_time: The execution_start_time of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501
        :type: str
        """

        self._execution_start_time = execution_start_time

    @property
    def host_address(self):
        """Gets the host_address of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501


        :return: The host_address of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501
        :rtype: str
        """
        return self._host_address

    @host_address.setter
    def host_address(self, host_address):
        """Sets the host_address of this SlowQueryForDescribeSlowLogsOutput.


        :param host_address: The host_address of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501
        :type: str
        """

        self._host_address = host_address

    @property
    def lock_times(self):
        """Gets the lock_times of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501


        :return: The lock_times of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501
        :rtype: int
        """
        return self._lock_times

    @lock_times.setter
    def lock_times(self, lock_times):
        """Sets the lock_times of this SlowQueryForDescribeSlowLogsOutput.


        :param lock_times: The lock_times of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501
        :type: int
        """

        self._lock_times = lock_times

    @property
    def parse_row_counts(self):
        """Gets the parse_row_counts of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501


        :return: The parse_row_counts of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501
        :rtype: int
        """
        return self._parse_row_counts

    @parse_row_counts.setter
    def parse_row_counts(self, parse_row_counts):
        """Sets the parse_row_counts of this SlowQueryForDescribeSlowLogsOutput.


        :param parse_row_counts: The parse_row_counts of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501
        :type: int
        """

        self._parse_row_counts = parse_row_counts

    @property
    def query_text(self):
        """Gets the query_text of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501


        :return: The query_text of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501
        :rtype: str
        """
        return self._query_text

    @query_text.setter
    def query_text(self, query_text):
        """Sets the query_text of this SlowQueryForDescribeSlowLogsOutput.


        :param query_text: The query_text of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501
        :type: str
        """

        self._query_text = query_text

    @property
    def query_times(self):
        """Gets the query_times of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501


        :return: The query_times of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501
        :rtype: int
        """
        return self._query_times

    @query_times.setter
    def query_times(self, query_times):
        """Sets the query_times of this SlowQueryForDescribeSlowLogsOutput.


        :param query_times: The query_times of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501
        :type: int
        """

        self._query_times = query_times

    @property
    def query_type(self):
        """Gets the query_type of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501


        :return: The query_type of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        """Sets the query_type of this SlowQueryForDescribeSlowLogsOutput.


        :param query_type: The query_type of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501
        :type: str
        """

        self._query_type = query_type

    @property
    def return_row_counts(self):
        """Gets the return_row_counts of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501


        :return: The return_row_counts of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501
        :rtype: int
        """
        return self._return_row_counts

    @return_row_counts.setter
    def return_row_counts(self, return_row_counts):
        """Sets the return_row_counts of this SlowQueryForDescribeSlowLogsOutput.


        :param return_row_counts: The return_row_counts of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501
        :type: int
        """

        self._return_row_counts = return_row_counts

    @property
    def user_name(self):
        """Gets the user_name of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501


        :return: The user_name of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this SlowQueryForDescribeSlowLogsOutput.


        :param user_name: The user_name of this SlowQueryForDescribeSlowLogsOutput.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

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
        if issubclass(SlowQueryForDescribeSlowLogsOutput, dict):
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
        if not isinstance(other, SlowQueryForDescribeSlowLogsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SlowQueryForDescribeSlowLogsOutput):
            return True

        return self.to_dict() != other.to_dict()
