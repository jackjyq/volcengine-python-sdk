# coding: utf-8

"""
    cdn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeUserDataRequest(object):
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
        'domain': 'str',
        'end_time': 'int',
        'interval': 'str',
        'ip_version': 'str',
        'location': 'str',
        'province': 'str',
        'start_time': 'int'
    }

    attribute_map = {
        'domain': 'Domain',
        'end_time': 'EndTime',
        'interval': 'Interval',
        'ip_version': 'IpVersion',
        'location': 'Location',
        'province': 'Province',
        'start_time': 'StartTime'
    }

    def __init__(self, domain=None, end_time=None, interval=None, ip_version=None, location=None, province=None, start_time=None, _configuration=None):  # noqa: E501
        """DescribeUserDataRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._domain = None
        self._end_time = None
        self._interval = None
        self._ip_version = None
        self._location = None
        self._province = None
        self._start_time = None
        self.discriminator = None

        self.domain = domain
        self.end_time = end_time
        self.interval = interval
        if ip_version is not None:
            self.ip_version = ip_version
        if location is not None:
            self.location = location
        if province is not None:
            self.province = province
        self.start_time = start_time

    @property
    def domain(self):
        """Gets the domain of this DescribeUserDataRequest.  # noqa: E501


        :return: The domain of this DescribeUserDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this DescribeUserDataRequest.


        :param domain: The domain of this DescribeUserDataRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def end_time(self):
        """Gets the end_time of this DescribeUserDataRequest.  # noqa: E501


        :return: The end_time of this DescribeUserDataRequest.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this DescribeUserDataRequest.


        :param end_time: The end_time of this DescribeUserDataRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def interval(self):
        """Gets the interval of this DescribeUserDataRequest.  # noqa: E501


        :return: The interval of this DescribeUserDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this DescribeUserDataRequest.


        :param interval: The interval of this DescribeUserDataRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and interval is None:
            raise ValueError("Invalid value for `interval`, must not be `None`")  # noqa: E501

        self._interval = interval

    @property
    def ip_version(self):
        """Gets the ip_version of this DescribeUserDataRequest.  # noqa: E501


        :return: The ip_version of this DescribeUserDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this DescribeUserDataRequest.


        :param ip_version: The ip_version of this DescribeUserDataRequest.  # noqa: E501
        :type: str
        """

        self._ip_version = ip_version

    @property
    def location(self):
        """Gets the location of this DescribeUserDataRequest.  # noqa: E501


        :return: The location of this DescribeUserDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this DescribeUserDataRequest.


        :param location: The location of this DescribeUserDataRequest.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def province(self):
        """Gets the province of this DescribeUserDataRequest.  # noqa: E501


        :return: The province of this DescribeUserDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        """Sets the province of this DescribeUserDataRequest.


        :param province: The province of this DescribeUserDataRequest.  # noqa: E501
        :type: str
        """

        self._province = province

    @property
    def start_time(self):
        """Gets the start_time of this DescribeUserDataRequest.  # noqa: E501


        :return: The start_time of this DescribeUserDataRequest.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DescribeUserDataRequest.


        :param start_time: The start_time of this DescribeUserDataRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

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
        if issubclass(DescribeUserDataRequest, dict):
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
        if not isinstance(other, DescribeUserDataRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeUserDataRequest):
            return True

        return self.to_dict() != other.to_dict()
