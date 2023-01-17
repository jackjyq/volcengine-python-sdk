# coding: utf-8

"""
    clb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class EipBillingConfigForCreateLoadBalancerInput(object):
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
        'bandwidth': 'int',
        'bandwidth_package_id': 'str',
        'eip_billing_type': 'int',
        'isp': 'str',
        'security_protection_types': 'list[str]'
    }

    attribute_map = {
        'bandwidth': 'Bandwidth',
        'bandwidth_package_id': 'BandwidthPackageId',
        'eip_billing_type': 'EipBillingType',
        'isp': 'ISP',
        'security_protection_types': 'SecurityProtectionTypes'
    }

    def __init__(self, bandwidth=None, bandwidth_package_id=None, eip_billing_type=None, isp=None, security_protection_types=None, _configuration=None):  # noqa: E501
        """EipBillingConfigForCreateLoadBalancerInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bandwidth = None
        self._bandwidth_package_id = None
        self._eip_billing_type = None
        self._isp = None
        self._security_protection_types = None
        self.discriminator = None

        if bandwidth is not None:
            self.bandwidth = bandwidth
        if bandwidth_package_id is not None:
            self.bandwidth_package_id = bandwidth_package_id
        if eip_billing_type is not None:
            self.eip_billing_type = eip_billing_type
        if isp is not None:
            self.isp = isp
        if security_protection_types is not None:
            self.security_protection_types = security_protection_types

    @property
    def bandwidth(self):
        """Gets the bandwidth of this EipBillingConfigForCreateLoadBalancerInput.  # noqa: E501


        :return: The bandwidth of this EipBillingConfigForCreateLoadBalancerInput.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this EipBillingConfigForCreateLoadBalancerInput.


        :param bandwidth: The bandwidth of this EipBillingConfigForCreateLoadBalancerInput.  # noqa: E501
        :type: int
        """

        self._bandwidth = bandwidth

    @property
    def bandwidth_package_id(self):
        """Gets the bandwidth_package_id of this EipBillingConfigForCreateLoadBalancerInput.  # noqa: E501


        :return: The bandwidth_package_id of this EipBillingConfigForCreateLoadBalancerInput.  # noqa: E501
        :rtype: str
        """
        return self._bandwidth_package_id

    @bandwidth_package_id.setter
    def bandwidth_package_id(self, bandwidth_package_id):
        """Sets the bandwidth_package_id of this EipBillingConfigForCreateLoadBalancerInput.


        :param bandwidth_package_id: The bandwidth_package_id of this EipBillingConfigForCreateLoadBalancerInput.  # noqa: E501
        :type: str
        """

        self._bandwidth_package_id = bandwidth_package_id

    @property
    def eip_billing_type(self):
        """Gets the eip_billing_type of this EipBillingConfigForCreateLoadBalancerInput.  # noqa: E501


        :return: The eip_billing_type of this EipBillingConfigForCreateLoadBalancerInput.  # noqa: E501
        :rtype: int
        """
        return self._eip_billing_type

    @eip_billing_type.setter
    def eip_billing_type(self, eip_billing_type):
        """Sets the eip_billing_type of this EipBillingConfigForCreateLoadBalancerInput.


        :param eip_billing_type: The eip_billing_type of this EipBillingConfigForCreateLoadBalancerInput.  # noqa: E501
        :type: int
        """

        self._eip_billing_type = eip_billing_type

    @property
    def isp(self):
        """Gets the isp of this EipBillingConfigForCreateLoadBalancerInput.  # noqa: E501


        :return: The isp of this EipBillingConfigForCreateLoadBalancerInput.  # noqa: E501
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this EipBillingConfigForCreateLoadBalancerInput.


        :param isp: The isp of this EipBillingConfigForCreateLoadBalancerInput.  # noqa: E501
        :type: str
        """

        self._isp = isp

    @property
    def security_protection_types(self):
        """Gets the security_protection_types of this EipBillingConfigForCreateLoadBalancerInput.  # noqa: E501


        :return: The security_protection_types of this EipBillingConfigForCreateLoadBalancerInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._security_protection_types

    @security_protection_types.setter
    def security_protection_types(self, security_protection_types):
        """Sets the security_protection_types of this EipBillingConfigForCreateLoadBalancerInput.


        :param security_protection_types: The security_protection_types of this EipBillingConfigForCreateLoadBalancerInput.  # noqa: E501
        :type: list[str]
        """

        self._security_protection_types = security_protection_types

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
        if issubclass(EipBillingConfigForCreateLoadBalancerInput, dict):
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
        if not isinstance(other, EipBillingConfigForCreateLoadBalancerInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EipBillingConfigForCreateLoadBalancerInput):
            return True

        return self.to_dict() != other.to_dict()
