# coding: utf-8

"""
    ecs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeAvailableResourceRequest(object):
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
        'destination_resource': 'str',
        'instance_charge_type': 'str',
        'instance_type': 'str',
        'instance_type_id': 'str',
        'spot_strategy': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'destination_resource': 'DestinationResource',
        'instance_charge_type': 'InstanceChargeType',
        'instance_type': 'InstanceType',
        'instance_type_id': 'InstanceTypeId',
        'spot_strategy': 'SpotStrategy',
        'zone_id': 'ZoneId'
    }

    def __init__(self, destination_resource=None, instance_charge_type=None, instance_type=None, instance_type_id=None, spot_strategy=None, zone_id=None, _configuration=None):  # noqa: E501
        """DescribeAvailableResourceRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._destination_resource = None
        self._instance_charge_type = None
        self._instance_type = None
        self._instance_type_id = None
        self._spot_strategy = None
        self._zone_id = None
        self.discriminator = None

        if destination_resource is not None:
            self.destination_resource = destination_resource
        if instance_charge_type is not None:
            self.instance_charge_type = instance_charge_type
        if instance_type is not None:
            self.instance_type = instance_type
        if instance_type_id is not None:
            self.instance_type_id = instance_type_id
        if spot_strategy is not None:
            self.spot_strategy = spot_strategy
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def destination_resource(self):
        """Gets the destination_resource of this DescribeAvailableResourceRequest.  # noqa: E501


        :return: The destination_resource of this DescribeAvailableResourceRequest.  # noqa: E501
        :rtype: str
        """
        return self._destination_resource

    @destination_resource.setter
    def destination_resource(self, destination_resource):
        """Sets the destination_resource of this DescribeAvailableResourceRequest.


        :param destination_resource: The destination_resource of this DescribeAvailableResourceRequest.  # noqa: E501
        :type: str
        """

        self._destination_resource = destination_resource

    @property
    def instance_charge_type(self):
        """Gets the instance_charge_type of this DescribeAvailableResourceRequest.  # noqa: E501


        :return: The instance_charge_type of this DescribeAvailableResourceRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_charge_type

    @instance_charge_type.setter
    def instance_charge_type(self, instance_charge_type):
        """Sets the instance_charge_type of this DescribeAvailableResourceRequest.


        :param instance_charge_type: The instance_charge_type of this DescribeAvailableResourceRequest.  # noqa: E501
        :type: str
        """

        self._instance_charge_type = instance_charge_type

    @property
    def instance_type(self):
        """Gets the instance_type of this DescribeAvailableResourceRequest.  # noqa: E501


        :return: The instance_type of this DescribeAvailableResourceRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this DescribeAvailableResourceRequest.


        :param instance_type: The instance_type of this DescribeAvailableResourceRequest.  # noqa: E501
        :type: str
        """

        self._instance_type = instance_type

    @property
    def instance_type_id(self):
        """Gets the instance_type_id of this DescribeAvailableResourceRequest.  # noqa: E501


        :return: The instance_type_id of this DescribeAvailableResourceRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_type_id

    @instance_type_id.setter
    def instance_type_id(self, instance_type_id):
        """Sets the instance_type_id of this DescribeAvailableResourceRequest.


        :param instance_type_id: The instance_type_id of this DescribeAvailableResourceRequest.  # noqa: E501
        :type: str
        """

        self._instance_type_id = instance_type_id

    @property
    def spot_strategy(self):
        """Gets the spot_strategy of this DescribeAvailableResourceRequest.  # noqa: E501


        :return: The spot_strategy of this DescribeAvailableResourceRequest.  # noqa: E501
        :rtype: str
        """
        return self._spot_strategy

    @spot_strategy.setter
    def spot_strategy(self, spot_strategy):
        """Sets the spot_strategy of this DescribeAvailableResourceRequest.


        :param spot_strategy: The spot_strategy of this DescribeAvailableResourceRequest.  # noqa: E501
        :type: str
        """

        self._spot_strategy = spot_strategy

    @property
    def zone_id(self):
        """Gets the zone_id of this DescribeAvailableResourceRequest.  # noqa: E501


        :return: The zone_id of this DescribeAvailableResourceRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this DescribeAvailableResourceRequest.


        :param zone_id: The zone_id of this DescribeAvailableResourceRequest.  # noqa: E501
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
        if issubclass(DescribeAvailableResourceRequest, dict):
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
        if not isinstance(other, DescribeAvailableResourceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeAvailableResourceRequest):
            return True

        return self.to_dict() != other.to_dict()
