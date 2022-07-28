# coding: utf-8

"""
    cen

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class GrantInstanceToCenRequest(object):
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
        'cen_id': 'str',
        'cen_owner_id': 'str',
        'instance_id': 'str',
        'instance_region_id': 'str',
        'instance_type': 'str'
    }

    attribute_map = {
        'cen_id': 'CenId',
        'cen_owner_id': 'CenOwnerId',
        'instance_id': 'InstanceId',
        'instance_region_id': 'InstanceRegionId',
        'instance_type': 'InstanceType'
    }

    def __init__(self, cen_id=None, cen_owner_id=None, instance_id=None, instance_region_id=None, instance_type=None, _configuration=None):  # noqa: E501
        """GrantInstanceToCenRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cen_id = None
        self._cen_owner_id = None
        self._instance_id = None
        self._instance_region_id = None
        self._instance_type = None
        self.discriminator = None

        self.cen_id = cen_id
        self.cen_owner_id = cen_owner_id
        self.instance_id = instance_id
        self.instance_region_id = instance_region_id
        if instance_type is not None:
            self.instance_type = instance_type

    @property
    def cen_id(self):
        """Gets the cen_id of this GrantInstanceToCenRequest.  # noqa: E501


        :return: The cen_id of this GrantInstanceToCenRequest.  # noqa: E501
        :rtype: str
        """
        return self._cen_id

    @cen_id.setter
    def cen_id(self, cen_id):
        """Sets the cen_id of this GrantInstanceToCenRequest.


        :param cen_id: The cen_id of this GrantInstanceToCenRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and cen_id is None:
            raise ValueError("Invalid value for `cen_id`, must not be `None`")  # noqa: E501

        self._cen_id = cen_id

    @property
    def cen_owner_id(self):
        """Gets the cen_owner_id of this GrantInstanceToCenRequest.  # noqa: E501


        :return: The cen_owner_id of this GrantInstanceToCenRequest.  # noqa: E501
        :rtype: str
        """
        return self._cen_owner_id

    @cen_owner_id.setter
    def cen_owner_id(self, cen_owner_id):
        """Sets the cen_owner_id of this GrantInstanceToCenRequest.


        :param cen_owner_id: The cen_owner_id of this GrantInstanceToCenRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and cen_owner_id is None:
            raise ValueError("Invalid value for `cen_owner_id`, must not be `None`")  # noqa: E501

        self._cen_owner_id = cen_owner_id

    @property
    def instance_id(self):
        """Gets the instance_id of this GrantInstanceToCenRequest.  # noqa: E501


        :return: The instance_id of this GrantInstanceToCenRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this GrantInstanceToCenRequest.


        :param instance_id: The instance_id of this GrantInstanceToCenRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def instance_region_id(self):
        """Gets the instance_region_id of this GrantInstanceToCenRequest.  # noqa: E501


        :return: The instance_region_id of this GrantInstanceToCenRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_region_id

    @instance_region_id.setter
    def instance_region_id(self, instance_region_id):
        """Sets the instance_region_id of this GrantInstanceToCenRequest.


        :param instance_region_id: The instance_region_id of this GrantInstanceToCenRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_region_id is None:
            raise ValueError("Invalid value for `instance_region_id`, must not be `None`")  # noqa: E501

        self._instance_region_id = instance_region_id

    @property
    def instance_type(self):
        """Gets the instance_type of this GrantInstanceToCenRequest.  # noqa: E501


        :return: The instance_type of this GrantInstanceToCenRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this GrantInstanceToCenRequest.


        :param instance_type: The instance_type of this GrantInstanceToCenRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["VPC", "DCGW"]  # noqa: E501
        if (self._configuration.client_side_validation and
                instance_type not in allowed_values):
            raise ValueError(
                "Invalid value for `instance_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instance_type, allowed_values)
            )

        self._instance_type = instance_type

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
        if issubclass(GrantInstanceToCenRequest, dict):
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
        if not isinstance(other, GrantInstanceToCenRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GrantInstanceToCenRequest):
            return True

        return self.to_dict() != other.to_dict()