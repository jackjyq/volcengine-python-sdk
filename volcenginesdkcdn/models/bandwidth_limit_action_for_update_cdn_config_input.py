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


class BandwidthLimitActionForUpdateCdnConfigInput(object):
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
        'bandwidth_threshold': 'int',
        'limit_type': 'str',
        'speed_limit_rate': 'int',
        'speed_limit_rate_max': 'int'
    }

    attribute_map = {
        'bandwidth_threshold': 'BandwidthThreshold',
        'limit_type': 'LimitType',
        'speed_limit_rate': 'SpeedLimitRate',
        'speed_limit_rate_max': 'SpeedLimitRateMax'
    }

    def __init__(self, bandwidth_threshold=None, limit_type=None, speed_limit_rate=None, speed_limit_rate_max=None, _configuration=None):  # noqa: E501
        """BandwidthLimitActionForUpdateCdnConfigInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bandwidth_threshold = None
        self._limit_type = None
        self._speed_limit_rate = None
        self._speed_limit_rate_max = None
        self.discriminator = None

        if bandwidth_threshold is not None:
            self.bandwidth_threshold = bandwidth_threshold
        if limit_type is not None:
            self.limit_type = limit_type
        if speed_limit_rate is not None:
            self.speed_limit_rate = speed_limit_rate
        if speed_limit_rate_max is not None:
            self.speed_limit_rate_max = speed_limit_rate_max

    @property
    def bandwidth_threshold(self):
        """Gets the bandwidth_threshold of this BandwidthLimitActionForUpdateCdnConfigInput.  # noqa: E501


        :return: The bandwidth_threshold of this BandwidthLimitActionForUpdateCdnConfigInput.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth_threshold

    @bandwidth_threshold.setter
    def bandwidth_threshold(self, bandwidth_threshold):
        """Sets the bandwidth_threshold of this BandwidthLimitActionForUpdateCdnConfigInput.


        :param bandwidth_threshold: The bandwidth_threshold of this BandwidthLimitActionForUpdateCdnConfigInput.  # noqa: E501
        :type: int
        """

        self._bandwidth_threshold = bandwidth_threshold

    @property
    def limit_type(self):
        """Gets the limit_type of this BandwidthLimitActionForUpdateCdnConfigInput.  # noqa: E501


        :return: The limit_type of this BandwidthLimitActionForUpdateCdnConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._limit_type

    @limit_type.setter
    def limit_type(self, limit_type):
        """Sets the limit_type of this BandwidthLimitActionForUpdateCdnConfigInput.


        :param limit_type: The limit_type of this BandwidthLimitActionForUpdateCdnConfigInput.  # noqa: E501
        :type: str
        """

        self._limit_type = limit_type

    @property
    def speed_limit_rate(self):
        """Gets the speed_limit_rate of this BandwidthLimitActionForUpdateCdnConfigInput.  # noqa: E501


        :return: The speed_limit_rate of this BandwidthLimitActionForUpdateCdnConfigInput.  # noqa: E501
        :rtype: int
        """
        return self._speed_limit_rate

    @speed_limit_rate.setter
    def speed_limit_rate(self, speed_limit_rate):
        """Sets the speed_limit_rate of this BandwidthLimitActionForUpdateCdnConfigInput.


        :param speed_limit_rate: The speed_limit_rate of this BandwidthLimitActionForUpdateCdnConfigInput.  # noqa: E501
        :type: int
        """

        self._speed_limit_rate = speed_limit_rate

    @property
    def speed_limit_rate_max(self):
        """Gets the speed_limit_rate_max of this BandwidthLimitActionForUpdateCdnConfigInput.  # noqa: E501


        :return: The speed_limit_rate_max of this BandwidthLimitActionForUpdateCdnConfigInput.  # noqa: E501
        :rtype: int
        """
        return self._speed_limit_rate_max

    @speed_limit_rate_max.setter
    def speed_limit_rate_max(self, speed_limit_rate_max):
        """Sets the speed_limit_rate_max of this BandwidthLimitActionForUpdateCdnConfigInput.


        :param speed_limit_rate_max: The speed_limit_rate_max of this BandwidthLimitActionForUpdateCdnConfigInput.  # noqa: E501
        :type: int
        """

        self._speed_limit_rate_max = speed_limit_rate_max

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
        if issubclass(BandwidthLimitActionForUpdateCdnConfigInput, dict):
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
        if not isinstance(other, BandwidthLimitActionForUpdateCdnConfigInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BandwidthLimitActionForUpdateCdnConfigInput):
            return True

        return self.to_dict() != other.to_dict()