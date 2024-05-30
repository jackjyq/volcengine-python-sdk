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


class UrlNormalizeForAddCdnDomainInput(object):
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
        'normalize_object': 'list[str]',
        'switch': 'bool'
    }

    attribute_map = {
        'normalize_object': 'NormalizeObject',
        'switch': 'Switch'
    }

    def __init__(self, normalize_object=None, switch=None, _configuration=None):  # noqa: E501
        """UrlNormalizeForAddCdnDomainInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._normalize_object = None
        self._switch = None
        self.discriminator = None

        if normalize_object is not None:
            self.normalize_object = normalize_object
        if switch is not None:
            self.switch = switch

    @property
    def normalize_object(self):
        """Gets the normalize_object of this UrlNormalizeForAddCdnDomainInput.  # noqa: E501


        :return: The normalize_object of this UrlNormalizeForAddCdnDomainInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._normalize_object

    @normalize_object.setter
    def normalize_object(self, normalize_object):
        """Sets the normalize_object of this UrlNormalizeForAddCdnDomainInput.


        :param normalize_object: The normalize_object of this UrlNormalizeForAddCdnDomainInput.  # noqa: E501
        :type: list[str]
        """

        self._normalize_object = normalize_object

    @property
    def switch(self):
        """Gets the switch of this UrlNormalizeForAddCdnDomainInput.  # noqa: E501


        :return: The switch of this UrlNormalizeForAddCdnDomainInput.  # noqa: E501
        :rtype: bool
        """
        return self._switch

    @switch.setter
    def switch(self, switch):
        """Sets the switch of this UrlNormalizeForAddCdnDomainInput.


        :param switch: The switch of this UrlNormalizeForAddCdnDomainInput.  # noqa: E501
        :type: bool
        """

        self._switch = switch

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
        if issubclass(UrlNormalizeForAddCdnDomainInput, dict):
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
        if not isinstance(other, UrlNormalizeForAddCdnDomainInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UrlNormalizeForAddCdnDomainInput):
            return True

        return self.to_dict() != other.to_dict()
