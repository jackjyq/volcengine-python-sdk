# coding: utf-8

"""
    vpc

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeHaVipsRequest(object):
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
        'ha_vip_ids': 'list[str]',
        'ha_vip_name': 'str',
        'ip_address': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'status': 'str',
        'subnet_id': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'ha_vip_ids': 'HaVipIds',
        'ha_vip_name': 'HaVipName',
        'ip_address': 'IpAddress',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'status': 'Status',
        'subnet_id': 'SubnetId',
        'vpc_id': 'VpcId'
    }

    def __init__(self, ha_vip_ids=None, ha_vip_name=None, ip_address=None, page_number=None, page_size=None, status=None, subnet_id=None, vpc_id=None, _configuration=None):  # noqa: E501
        """DescribeHaVipsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ha_vip_ids = None
        self._ha_vip_name = None
        self._ip_address = None
        self._page_number = None
        self._page_size = None
        self._status = None
        self._subnet_id = None
        self._vpc_id = None
        self.discriminator = None

        if ha_vip_ids is not None:
            self.ha_vip_ids = ha_vip_ids
        if ha_vip_name is not None:
            self.ha_vip_name = ha_vip_name
        if ip_address is not None:
            self.ip_address = ip_address
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if status is not None:
            self.status = status
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def ha_vip_ids(self):
        """Gets the ha_vip_ids of this DescribeHaVipsRequest.  # noqa: E501


        :return: The ha_vip_ids of this DescribeHaVipsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._ha_vip_ids

    @ha_vip_ids.setter
    def ha_vip_ids(self, ha_vip_ids):
        """Sets the ha_vip_ids of this DescribeHaVipsRequest.


        :param ha_vip_ids: The ha_vip_ids of this DescribeHaVipsRequest.  # noqa: E501
        :type: list[str]
        """

        self._ha_vip_ids = ha_vip_ids

    @property
    def ha_vip_name(self):
        """Gets the ha_vip_name of this DescribeHaVipsRequest.  # noqa: E501


        :return: The ha_vip_name of this DescribeHaVipsRequest.  # noqa: E501
        :rtype: str
        """
        return self._ha_vip_name

    @ha_vip_name.setter
    def ha_vip_name(self, ha_vip_name):
        """Sets the ha_vip_name of this DescribeHaVipsRequest.


        :param ha_vip_name: The ha_vip_name of this DescribeHaVipsRequest.  # noqa: E501
        :type: str
        """

        self._ha_vip_name = ha_vip_name

    @property
    def ip_address(self):
        """Gets the ip_address of this DescribeHaVipsRequest.  # noqa: E501


        :return: The ip_address of this DescribeHaVipsRequest.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this DescribeHaVipsRequest.


        :param ip_address: The ip_address of this DescribeHaVipsRequest.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def page_number(self):
        """Gets the page_number of this DescribeHaVipsRequest.  # noqa: E501


        :return: The page_number of this DescribeHaVipsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeHaVipsRequest.


        :param page_number: The page_number of this DescribeHaVipsRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeHaVipsRequest.  # noqa: E501


        :return: The page_size of this DescribeHaVipsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeHaVipsRequest.


        :param page_size: The page_size of this DescribeHaVipsRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                page_size is not None and page_size > 100):  # noqa: E501
            raise ValueError("Invalid value for `page_size`, must be a value less than or equal to `100`")  # noqa: E501

        self._page_size = page_size

    @property
    def status(self):
        """Gets the status of this DescribeHaVipsRequest.  # noqa: E501


        :return: The status of this DescribeHaVipsRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DescribeHaVipsRequest.


        :param status: The status of this DescribeHaVipsRequest.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def subnet_id(self):
        """Gets the subnet_id of this DescribeHaVipsRequest.  # noqa: E501


        :return: The subnet_id of this DescribeHaVipsRequest.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this DescribeHaVipsRequest.


        :param subnet_id: The subnet_id of this DescribeHaVipsRequest.  # noqa: E501
        :type: str
        """

        self._subnet_id = subnet_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this DescribeHaVipsRequest.  # noqa: E501


        :return: The vpc_id of this DescribeHaVipsRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this DescribeHaVipsRequest.


        :param vpc_id: The vpc_id of this DescribeHaVipsRequest.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

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
        if issubclass(DescribeHaVipsRequest, dict):
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
        if not isinstance(other, DescribeHaVipsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeHaVipsRequest):
            return True

        return self.to_dict() != other.to_dict()