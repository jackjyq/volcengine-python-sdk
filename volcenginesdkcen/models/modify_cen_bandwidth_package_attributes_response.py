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


class ModifyCenBandwidthPackageAttributesResponse(object):
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
        'pre_order_number': 'str'
    }

    attribute_map = {
        'pre_order_number': 'PreOrderNumber'
    }

    def __init__(self, pre_order_number=None, _configuration=None):  # noqa: E501
        """ModifyCenBandwidthPackageAttributesResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._pre_order_number = None
        self.discriminator = None

        if pre_order_number is not None:
            self.pre_order_number = pre_order_number

    @property
    def pre_order_number(self):
        """Gets the pre_order_number of this ModifyCenBandwidthPackageAttributesResponse.  # noqa: E501


        :return: The pre_order_number of this ModifyCenBandwidthPackageAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._pre_order_number

    @pre_order_number.setter
    def pre_order_number(self, pre_order_number):
        """Sets the pre_order_number of this ModifyCenBandwidthPackageAttributesResponse.


        :param pre_order_number: The pre_order_number of this ModifyCenBandwidthPackageAttributesResponse.  # noqa: E501
        :type: str
        """

        self._pre_order_number = pre_order_number

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
        if issubclass(ModifyCenBandwidthPackageAttributesResponse, dict):
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
        if not isinstance(other, ModifyCenBandwidthPackageAttributesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyCenBandwidthPackageAttributesResponse):
            return True

        return self.to_dict() != other.to_dict()
