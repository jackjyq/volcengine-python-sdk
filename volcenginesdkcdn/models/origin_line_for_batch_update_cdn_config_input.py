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


class OriginLineForBatchUpdateCdnConfigInput(object):
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
        'address': 'str',
        'http_port': 'str',
        'https_port': 'str',
        'instance_type': 'str',
        'origin_host': 'str'
    }

    attribute_map = {
        'address': 'Address',
        'http_port': 'HttpPort',
        'https_port': 'HttpsPort',
        'instance_type': 'InstanceType',
        'origin_host': 'OriginHost'
    }

    def __init__(self, address=None, http_port=None, https_port=None, instance_type=None, origin_host=None, _configuration=None):  # noqa: E501
        """OriginLineForBatchUpdateCdnConfigInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._address = None
        self._http_port = None
        self._https_port = None
        self._instance_type = None
        self._origin_host = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if http_port is not None:
            self.http_port = http_port
        if https_port is not None:
            self.https_port = https_port
        if instance_type is not None:
            self.instance_type = instance_type
        if origin_host is not None:
            self.origin_host = origin_host

    @property
    def address(self):
        """Gets the address of this OriginLineForBatchUpdateCdnConfigInput.  # noqa: E501


        :return: The address of this OriginLineForBatchUpdateCdnConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this OriginLineForBatchUpdateCdnConfigInput.


        :param address: The address of this OriginLineForBatchUpdateCdnConfigInput.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def http_port(self):
        """Gets the http_port of this OriginLineForBatchUpdateCdnConfigInput.  # noqa: E501


        :return: The http_port of this OriginLineForBatchUpdateCdnConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._http_port

    @http_port.setter
    def http_port(self, http_port):
        """Sets the http_port of this OriginLineForBatchUpdateCdnConfigInput.


        :param http_port: The http_port of this OriginLineForBatchUpdateCdnConfigInput.  # noqa: E501
        :type: str
        """

        self._http_port = http_port

    @property
    def https_port(self):
        """Gets the https_port of this OriginLineForBatchUpdateCdnConfigInput.  # noqa: E501


        :return: The https_port of this OriginLineForBatchUpdateCdnConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._https_port

    @https_port.setter
    def https_port(self, https_port):
        """Sets the https_port of this OriginLineForBatchUpdateCdnConfigInput.


        :param https_port: The https_port of this OriginLineForBatchUpdateCdnConfigInput.  # noqa: E501
        :type: str
        """

        self._https_port = https_port

    @property
    def instance_type(self):
        """Gets the instance_type of this OriginLineForBatchUpdateCdnConfigInput.  # noqa: E501


        :return: The instance_type of this OriginLineForBatchUpdateCdnConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this OriginLineForBatchUpdateCdnConfigInput.


        :param instance_type: The instance_type of this OriginLineForBatchUpdateCdnConfigInput.  # noqa: E501
        :type: str
        """

        self._instance_type = instance_type

    @property
    def origin_host(self):
        """Gets the origin_host of this OriginLineForBatchUpdateCdnConfigInput.  # noqa: E501


        :return: The origin_host of this OriginLineForBatchUpdateCdnConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._origin_host

    @origin_host.setter
    def origin_host(self, origin_host):
        """Sets the origin_host of this OriginLineForBatchUpdateCdnConfigInput.


        :param origin_host: The origin_host of this OriginLineForBatchUpdateCdnConfigInput.  # noqa: E501
        :type: str
        """

        self._origin_host = origin_host

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
        if issubclass(OriginLineForBatchUpdateCdnConfigInput, dict):
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
        if not isinstance(other, OriginLineForBatchUpdateCdnConfigInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OriginLineForBatchUpdateCdnConfigInput):
            return True

        return self.to_dict() != other.to_dict()
