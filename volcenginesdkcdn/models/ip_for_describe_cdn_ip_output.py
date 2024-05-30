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


class IPForDescribeCdnIPOutput(object):
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
        'cdn_ip': 'bool',
        'ip': 'str',
        'isp': 'str',
        'location': 'str'
    }

    attribute_map = {
        'cdn_ip': 'CdnIp',
        'ip': 'IP',
        'isp': 'ISP',
        'location': 'Location'
    }

    def __init__(self, cdn_ip=None, ip=None, isp=None, location=None, _configuration=None):  # noqa: E501
        """IPForDescribeCdnIPOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cdn_ip = None
        self._ip = None
        self._isp = None
        self._location = None
        self.discriminator = None

        if cdn_ip is not None:
            self.cdn_ip = cdn_ip
        if ip is not None:
            self.ip = ip
        if isp is not None:
            self.isp = isp
        if location is not None:
            self.location = location

    @property
    def cdn_ip(self):
        """Gets the cdn_ip of this IPForDescribeCdnIPOutput.  # noqa: E501


        :return: The cdn_ip of this IPForDescribeCdnIPOutput.  # noqa: E501
        :rtype: bool
        """
        return self._cdn_ip

    @cdn_ip.setter
    def cdn_ip(self, cdn_ip):
        """Sets the cdn_ip of this IPForDescribeCdnIPOutput.


        :param cdn_ip: The cdn_ip of this IPForDescribeCdnIPOutput.  # noqa: E501
        :type: bool
        """

        self._cdn_ip = cdn_ip

    @property
    def ip(self):
        """Gets the ip of this IPForDescribeCdnIPOutput.  # noqa: E501


        :return: The ip of this IPForDescribeCdnIPOutput.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this IPForDescribeCdnIPOutput.


        :param ip: The ip of this IPForDescribeCdnIPOutput.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def isp(self):
        """Gets the isp of this IPForDescribeCdnIPOutput.  # noqa: E501


        :return: The isp of this IPForDescribeCdnIPOutput.  # noqa: E501
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this IPForDescribeCdnIPOutput.


        :param isp: The isp of this IPForDescribeCdnIPOutput.  # noqa: E501
        :type: str
        """

        self._isp = isp

    @property
    def location(self):
        """Gets the location of this IPForDescribeCdnIPOutput.  # noqa: E501


        :return: The location of this IPForDescribeCdnIPOutput.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this IPForDescribeCdnIPOutput.


        :param location: The location of this IPForDescribeCdnIPOutput.  # noqa: E501
        :type: str
        """

        self._location = location

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
        if issubclass(IPForDescribeCdnIPOutput, dict):
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
        if not isinstance(other, IPForDescribeCdnIPOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IPForDescribeCdnIPOutput):
            return True

        return self.to_dict() != other.to_dict()
