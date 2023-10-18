# coding: utf-8

"""
    vedbm

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ZoneNodeInfoForModifyDBInstanceSpecInput(object):
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
        'zone_id': 'str',
        'zone_node_number': 'int'
    }

    attribute_map = {
        'zone_id': 'ZoneId',
        'zone_node_number': 'ZoneNodeNumber'
    }

    def __init__(self, zone_id=None, zone_node_number=None, _configuration=None):  # noqa: E501
        """ZoneNodeInfoForModifyDBInstanceSpecInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._zone_id = None
        self._zone_node_number = None
        self.discriminator = None

        if zone_id is not None:
            self.zone_id = zone_id
        if zone_node_number is not None:
            self.zone_node_number = zone_node_number

    @property
    def zone_id(self):
        """Gets the zone_id of this ZoneNodeInfoForModifyDBInstanceSpecInput.  # noqa: E501


        :return: The zone_id of this ZoneNodeInfoForModifyDBInstanceSpecInput.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this ZoneNodeInfoForModifyDBInstanceSpecInput.


        :param zone_id: The zone_id of this ZoneNodeInfoForModifyDBInstanceSpecInput.  # noqa: E501
        :type: str
        """

        self._zone_id = zone_id

    @property
    def zone_node_number(self):
        """Gets the zone_node_number of this ZoneNodeInfoForModifyDBInstanceSpecInput.  # noqa: E501


        :return: The zone_node_number of this ZoneNodeInfoForModifyDBInstanceSpecInput.  # noqa: E501
        :rtype: int
        """
        return self._zone_node_number

    @zone_node_number.setter
    def zone_node_number(self, zone_node_number):
        """Sets the zone_node_number of this ZoneNodeInfoForModifyDBInstanceSpecInput.


        :param zone_node_number: The zone_node_number of this ZoneNodeInfoForModifyDBInstanceSpecInput.  # noqa: E501
        :type: int
        """

        self._zone_node_number = zone_node_number

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
        if issubclass(ZoneNodeInfoForModifyDBInstanceSpecInput, dict):
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
        if not isinstance(other, ZoneNodeInfoForModifyDBInstanceSpecInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ZoneNodeInfoForModifyDBInstanceSpecInput):
            return True

        return self.to_dict() != other.to_dict()
