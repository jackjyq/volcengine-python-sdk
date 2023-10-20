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


class DescribeErrorLogsRequest(object):
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
        'error_level': 'str',
        'error_log_end_time': 'str',
        'error_log_start_time': 'str',
        'instance_id': 'str',
        'node_id': 'str',
        'page_number': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'error_level': 'ErrorLevel',
        'error_log_end_time': 'ErrorLogEndTime',
        'error_log_start_time': 'ErrorLogStartTime',
        'instance_id': 'InstanceId',
        'node_id': 'NodeId',
        'page_number': 'PageNumber',
        'page_size': 'PageSize'
    }

    def __init__(self, error_level=None, error_log_end_time=None, error_log_start_time=None, instance_id=None, node_id=None, page_number=None, page_size=None, _configuration=None):  # noqa: E501
        """DescribeErrorLogsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._error_level = None
        self._error_log_end_time = None
        self._error_log_start_time = None
        self._instance_id = None
        self._node_id = None
        self._page_number = None
        self._page_size = None
        self.discriminator = None

        if error_level is not None:
            self.error_level = error_level
        if error_log_end_time is not None:
            self.error_log_end_time = error_log_end_time
        if error_log_start_time is not None:
            self.error_log_start_time = error_log_start_time
        self.instance_id = instance_id
        if node_id is not None:
            self.node_id = node_id
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size

    @property
    def error_level(self):
        """Gets the error_level of this DescribeErrorLogsRequest.  # noqa: E501


        :return: The error_level of this DescribeErrorLogsRequest.  # noqa: E501
        :rtype: str
        """
        return self._error_level

    @error_level.setter
    def error_level(self, error_level):
        """Sets the error_level of this DescribeErrorLogsRequest.


        :param error_level: The error_level of this DescribeErrorLogsRequest.  # noqa: E501
        :type: str
        """

        self._error_level = error_level

    @property
    def error_log_end_time(self):
        """Gets the error_log_end_time of this DescribeErrorLogsRequest.  # noqa: E501


        :return: The error_log_end_time of this DescribeErrorLogsRequest.  # noqa: E501
        :rtype: str
        """
        return self._error_log_end_time

    @error_log_end_time.setter
    def error_log_end_time(self, error_log_end_time):
        """Sets the error_log_end_time of this DescribeErrorLogsRequest.


        :param error_log_end_time: The error_log_end_time of this DescribeErrorLogsRequest.  # noqa: E501
        :type: str
        """

        self._error_log_end_time = error_log_end_time

    @property
    def error_log_start_time(self):
        """Gets the error_log_start_time of this DescribeErrorLogsRequest.  # noqa: E501


        :return: The error_log_start_time of this DescribeErrorLogsRequest.  # noqa: E501
        :rtype: str
        """
        return self._error_log_start_time

    @error_log_start_time.setter
    def error_log_start_time(self, error_log_start_time):
        """Sets the error_log_start_time of this DescribeErrorLogsRequest.


        :param error_log_start_time: The error_log_start_time of this DescribeErrorLogsRequest.  # noqa: E501
        :type: str
        """

        self._error_log_start_time = error_log_start_time

    @property
    def instance_id(self):
        """Gets the instance_id of this DescribeErrorLogsRequest.  # noqa: E501


        :return: The instance_id of this DescribeErrorLogsRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DescribeErrorLogsRequest.


        :param instance_id: The instance_id of this DescribeErrorLogsRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def node_id(self):
        """Gets the node_id of this DescribeErrorLogsRequest.  # noqa: E501


        :return: The node_id of this DescribeErrorLogsRequest.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this DescribeErrorLogsRequest.


        :param node_id: The node_id of this DescribeErrorLogsRequest.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def page_number(self):
        """Gets the page_number of this DescribeErrorLogsRequest.  # noqa: E501


        :return: The page_number of this DescribeErrorLogsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeErrorLogsRequest.


        :param page_number: The page_number of this DescribeErrorLogsRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeErrorLogsRequest.  # noqa: E501


        :return: The page_size of this DescribeErrorLogsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeErrorLogsRequest.


        :param page_size: The page_size of this DescribeErrorLogsRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

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
        if issubclass(DescribeErrorLogsRequest, dict):
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
        if not isinstance(other, DescribeErrorLogsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeErrorLogsRequest):
            return True

        return self.to_dict() != other.to_dict()
