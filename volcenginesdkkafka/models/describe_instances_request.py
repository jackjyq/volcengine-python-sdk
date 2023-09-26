# coding: utf-8

"""
    kafka

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeInstancesRequest(object):
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
        'instance_id': 'str',
        'instance_name': 'str',
        'instance_status': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'tags': 'dict(str, list[str])',
        'zone_id': 'str'
    }

    attribute_map = {
        'instance_id': 'InstanceId',
        'instance_name': 'InstanceName',
        'instance_status': 'InstanceStatus',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'tags': 'Tags',
        'zone_id': 'ZoneId'
    }

    def __init__(self, instance_id=None, instance_name=None, instance_status=None, page_number=None, page_size=None, tags=None, zone_id=None, _configuration=None):  # noqa: E501
        """DescribeInstancesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._instance_id = None
        self._instance_name = None
        self._instance_status = None
        self._page_number = None
        self._page_size = None
        self._tags = None
        self._zone_id = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_status is not None:
            self.instance_status = instance_status
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if tags is not None:
            self.tags = tags
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def instance_id(self):
        """Gets the instance_id of this DescribeInstancesRequest.  # noqa: E501


        :return: The instance_id of this DescribeInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DescribeInstancesRequest.


        :param instance_id: The instance_id of this DescribeInstancesRequest.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this DescribeInstancesRequest.  # noqa: E501


        :return: The instance_name of this DescribeInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this DescribeInstancesRequest.


        :param instance_name: The instance_name of this DescribeInstancesRequest.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def instance_status(self):
        """Gets the instance_status of this DescribeInstancesRequest.  # noqa: E501


        :return: The instance_status of this DescribeInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        """Sets the instance_status of this DescribeInstancesRequest.


        :param instance_status: The instance_status of this DescribeInstancesRequest.  # noqa: E501
        :type: str
        """

        self._instance_status = instance_status

    @property
    def page_number(self):
        """Gets the page_number of this DescribeInstancesRequest.  # noqa: E501


        :return: The page_number of this DescribeInstancesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeInstancesRequest.


        :param page_number: The page_number of this DescribeInstancesRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeInstancesRequest.  # noqa: E501


        :return: The page_size of this DescribeInstancesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeInstancesRequest.


        :param page_size: The page_size of this DescribeInstancesRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def tags(self):
        """Gets the tags of this DescribeInstancesRequest.  # noqa: E501


        :return: The tags of this DescribeInstancesRequest.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DescribeInstancesRequest.


        :param tags: The tags of this DescribeInstancesRequest.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._tags = tags

    @property
    def zone_id(self):
        """Gets the zone_id of this DescribeInstancesRequest.  # noqa: E501


        :return: The zone_id of this DescribeInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this DescribeInstancesRequest.


        :param zone_id: The zone_id of this DescribeInstancesRequest.  # noqa: E501
        :type: str
        """

        self._zone_id = zone_id

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
        if issubclass(DescribeInstancesRequest, dict):
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
        if not isinstance(other, DescribeInstancesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeInstancesRequest):
            return True

        return self.to_dict() != other.to_dict()