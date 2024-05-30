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


class BatchDeployCertRequest(object):
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
        'cert_id': 'str',
        'cert_id2': 'str',
        'domain': 'str'
    }

    attribute_map = {
        'cert_id': 'CertId',
        'cert_id2': 'CertId2',
        'domain': 'Domain'
    }

    def __init__(self, cert_id=None, cert_id2=None, domain=None, _configuration=None):  # noqa: E501
        """BatchDeployCertRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cert_id = None
        self._cert_id2 = None
        self._domain = None
        self.discriminator = None

        self.cert_id = cert_id
        if cert_id2 is not None:
            self.cert_id2 = cert_id2
        self.domain = domain

    @property
    def cert_id(self):
        """Gets the cert_id of this BatchDeployCertRequest.  # noqa: E501


        :return: The cert_id of this BatchDeployCertRequest.  # noqa: E501
        :rtype: str
        """
        return self._cert_id

    @cert_id.setter
    def cert_id(self, cert_id):
        """Sets the cert_id of this BatchDeployCertRequest.


        :param cert_id: The cert_id of this BatchDeployCertRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and cert_id is None:
            raise ValueError("Invalid value for `cert_id`, must not be `None`")  # noqa: E501

        self._cert_id = cert_id

    @property
    def cert_id2(self):
        """Gets the cert_id2 of this BatchDeployCertRequest.  # noqa: E501


        :return: The cert_id2 of this BatchDeployCertRequest.  # noqa: E501
        :rtype: str
        """
        return self._cert_id2

    @cert_id2.setter
    def cert_id2(self, cert_id2):
        """Sets the cert_id2 of this BatchDeployCertRequest.


        :param cert_id2: The cert_id2 of this BatchDeployCertRequest.  # noqa: E501
        :type: str
        """

        self._cert_id2 = cert_id2

    @property
    def domain(self):
        """Gets the domain of this BatchDeployCertRequest.  # noqa: E501


        :return: The domain of this BatchDeployCertRequest.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this BatchDeployCertRequest.


        :param domain: The domain of this BatchDeployCertRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

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
        if issubclass(BatchDeployCertRequest, dict):
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
        if not isinstance(other, BatchDeployCertRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BatchDeployCertRequest):
            return True

        return self.to_dict() != other.to_dict()
