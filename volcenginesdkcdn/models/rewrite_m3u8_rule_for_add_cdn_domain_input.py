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


class RewriteM3u8RuleForAddCdnDomainInput(object):
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
        'delete_param': 'bool',
        'keep_m3u8_param': 'bool',
        'transfer_encoding': 'bool'
    }

    attribute_map = {
        'delete_param': 'DeleteParam',
        'keep_m3u8_param': 'KeepM3u8Param',
        'transfer_encoding': 'TransferEncoding'
    }

    def __init__(self, delete_param=None, keep_m3u8_param=None, transfer_encoding=None, _configuration=None):  # noqa: E501
        """RewriteM3u8RuleForAddCdnDomainInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._delete_param = None
        self._keep_m3u8_param = None
        self._transfer_encoding = None
        self.discriminator = None

        if delete_param is not None:
            self.delete_param = delete_param
        if keep_m3u8_param is not None:
            self.keep_m3u8_param = keep_m3u8_param
        if transfer_encoding is not None:
            self.transfer_encoding = transfer_encoding

    @property
    def delete_param(self):
        """Gets the delete_param of this RewriteM3u8RuleForAddCdnDomainInput.  # noqa: E501


        :return: The delete_param of this RewriteM3u8RuleForAddCdnDomainInput.  # noqa: E501
        :rtype: bool
        """
        return self._delete_param

    @delete_param.setter
    def delete_param(self, delete_param):
        """Sets the delete_param of this RewriteM3u8RuleForAddCdnDomainInput.


        :param delete_param: The delete_param of this RewriteM3u8RuleForAddCdnDomainInput.  # noqa: E501
        :type: bool
        """

        self._delete_param = delete_param

    @property
    def keep_m3u8_param(self):
        """Gets the keep_m3u8_param of this RewriteM3u8RuleForAddCdnDomainInput.  # noqa: E501


        :return: The keep_m3u8_param of this RewriteM3u8RuleForAddCdnDomainInput.  # noqa: E501
        :rtype: bool
        """
        return self._keep_m3u8_param

    @keep_m3u8_param.setter
    def keep_m3u8_param(self, keep_m3u8_param):
        """Sets the keep_m3u8_param of this RewriteM3u8RuleForAddCdnDomainInput.


        :param keep_m3u8_param: The keep_m3u8_param of this RewriteM3u8RuleForAddCdnDomainInput.  # noqa: E501
        :type: bool
        """

        self._keep_m3u8_param = keep_m3u8_param

    @property
    def transfer_encoding(self):
        """Gets the transfer_encoding of this RewriteM3u8RuleForAddCdnDomainInput.  # noqa: E501


        :return: The transfer_encoding of this RewriteM3u8RuleForAddCdnDomainInput.  # noqa: E501
        :rtype: bool
        """
        return self._transfer_encoding

    @transfer_encoding.setter
    def transfer_encoding(self, transfer_encoding):
        """Sets the transfer_encoding of this RewriteM3u8RuleForAddCdnDomainInput.


        :param transfer_encoding: The transfer_encoding of this RewriteM3u8RuleForAddCdnDomainInput.  # noqa: E501
        :type: bool
        """

        self._transfer_encoding = transfer_encoding

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
        if issubclass(RewriteM3u8RuleForAddCdnDomainInput, dict):
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
        if not isinstance(other, RewriteM3u8RuleForAddCdnDomainInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RewriteM3u8RuleForAddCdnDomainInput):
            return True

        return self.to_dict() != other.to_dict()
