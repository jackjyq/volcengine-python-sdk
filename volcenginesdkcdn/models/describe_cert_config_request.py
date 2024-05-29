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


class DescribeCertConfigRequest(object):
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
        'cert_type': 'str',
        'encry_type': 'str',
        'status': 'str'
    }

    attribute_map = {
        'cert_id': 'CertId',
        'cert_id2': 'CertId2',
        'cert_type': 'CertType',
        'encry_type': 'EncryType',
        'status': 'Status'
    }

    def __init__(self, cert_id=None, cert_id2=None, cert_type=None, encry_type=None, status=None, _configuration=None):  # noqa: E501
        """DescribeCertConfigRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cert_id = None
        self._cert_id2 = None
        self._cert_type = None
        self._encry_type = None
        self._status = None
        self.discriminator = None

        self.cert_id = cert_id
        if cert_id2 is not None:
            self.cert_id2 = cert_id2
        if cert_type is not None:
            self.cert_type = cert_type
        if encry_type is not None:
            self.encry_type = encry_type
        if status is not None:
            self.status = status

    @property
    def cert_id(self):
        """Gets the cert_id of this DescribeCertConfigRequest.  # noqa: E501


        :return: The cert_id of this DescribeCertConfigRequest.  # noqa: E501
        :rtype: str
        """
        return self._cert_id

    @cert_id.setter
    def cert_id(self, cert_id):
        """Sets the cert_id of this DescribeCertConfigRequest.


        :param cert_id: The cert_id of this DescribeCertConfigRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and cert_id is None:
            raise ValueError("Invalid value for `cert_id`, must not be `None`")  # noqa: E501

        self._cert_id = cert_id

    @property
    def cert_id2(self):
        """Gets the cert_id2 of this DescribeCertConfigRequest.  # noqa: E501


        :return: The cert_id2 of this DescribeCertConfigRequest.  # noqa: E501
        :rtype: str
        """
        return self._cert_id2

    @cert_id2.setter
    def cert_id2(self, cert_id2):
        """Sets the cert_id2 of this DescribeCertConfigRequest.


        :param cert_id2: The cert_id2 of this DescribeCertConfigRequest.  # noqa: E501
        :type: str
        """

        self._cert_id2 = cert_id2

    @property
    def cert_type(self):
        """Gets the cert_type of this DescribeCertConfigRequest.  # noqa: E501


        :return: The cert_type of this DescribeCertConfigRequest.  # noqa: E501
        :rtype: str
        """
        return self._cert_type

    @cert_type.setter
    def cert_type(self, cert_type):
        """Sets the cert_type of this DescribeCertConfigRequest.


        :param cert_type: The cert_type of this DescribeCertConfigRequest.  # noqa: E501
        :type: str
        """

        self._cert_type = cert_type

    @property
    def encry_type(self):
        """Gets the encry_type of this DescribeCertConfigRequest.  # noqa: E501


        :return: The encry_type of this DescribeCertConfigRequest.  # noqa: E501
        :rtype: str
        """
        return self._encry_type

    @encry_type.setter
    def encry_type(self, encry_type):
        """Sets the encry_type of this DescribeCertConfigRequest.


        :param encry_type: The encry_type of this DescribeCertConfigRequest.  # noqa: E501
        :type: str
        """

        self._encry_type = encry_type

    @property
    def status(self):
        """Gets the status of this DescribeCertConfigRequest.  # noqa: E501


        :return: The status of this DescribeCertConfigRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DescribeCertConfigRequest.


        :param status: The status of this DescribeCertConfigRequest.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(DescribeCertConfigRequest, dict):
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
        if not isinstance(other, DescribeCertConfigRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeCertConfigRequest):
            return True

        return self.to_dict() != other.to_dict()
