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


class ModifyBandwidthPackageAttributesRequest(object):
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
        'bandwidth_package_id': 'str',
        'bandwidth_package_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'bandwidth_package_id': 'BandwidthPackageId',
        'bandwidth_package_name': 'BandwidthPackageName',
        'description': 'Description'
    }

    def __init__(self, bandwidth_package_id=None, bandwidth_package_name=None, description=None, _configuration=None):  # noqa: E501
        """ModifyBandwidthPackageAttributesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bandwidth_package_id = None
        self._bandwidth_package_name = None
        self._description = None
        self.discriminator = None

        self.bandwidth_package_id = bandwidth_package_id
        if bandwidth_package_name is not None:
            self.bandwidth_package_name = bandwidth_package_name
        if description is not None:
            self.description = description

    @property
    def bandwidth_package_id(self):
        """Gets the bandwidth_package_id of this ModifyBandwidthPackageAttributesRequest.  # noqa: E501


        :return: The bandwidth_package_id of this ModifyBandwidthPackageAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._bandwidth_package_id

    @bandwidth_package_id.setter
    def bandwidth_package_id(self, bandwidth_package_id):
        """Sets the bandwidth_package_id of this ModifyBandwidthPackageAttributesRequest.


        :param bandwidth_package_id: The bandwidth_package_id of this ModifyBandwidthPackageAttributesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and bandwidth_package_id is None:
            raise ValueError("Invalid value for `bandwidth_package_id`, must not be `None`")  # noqa: E501

        self._bandwidth_package_id = bandwidth_package_id

    @property
    def bandwidth_package_name(self):
        """Gets the bandwidth_package_name of this ModifyBandwidthPackageAttributesRequest.  # noqa: E501


        :return: The bandwidth_package_name of this ModifyBandwidthPackageAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._bandwidth_package_name

    @bandwidth_package_name.setter
    def bandwidth_package_name(self, bandwidth_package_name):
        """Sets the bandwidth_package_name of this ModifyBandwidthPackageAttributesRequest.


        :param bandwidth_package_name: The bandwidth_package_name of this ModifyBandwidthPackageAttributesRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                bandwidth_package_name is not None and len(bandwidth_package_name) > 128):
            raise ValueError("Invalid value for `bandwidth_package_name`, length must be less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                bandwidth_package_name is not None and len(bandwidth_package_name) < 1):
            raise ValueError("Invalid value for `bandwidth_package_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._bandwidth_package_name = bandwidth_package_name

    @property
    def description(self):
        """Gets the description of this ModifyBandwidthPackageAttributesRequest.  # noqa: E501


        :return: The description of this ModifyBandwidthPackageAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModifyBandwidthPackageAttributesRequest.


        :param description: The description of this ModifyBandwidthPackageAttributesRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                description is not None and len(description) > 255):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

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
        if issubclass(ModifyBandwidthPackageAttributesRequest, dict):
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
        if not isinstance(other, ModifyBandwidthPackageAttributesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyBandwidthPackageAttributesRequest):
            return True

        return self.to_dict() != other.to_dict()
