# coding: utf-8

"""
    cr

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DeleteEndpointAclPoliciesRequest(object):
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
        'entries': 'list[str]',
        'registry': 'str',
        'type': 'str'
    }

    attribute_map = {
        'entries': 'Entries',
        'registry': 'Registry',
        'type': 'Type'
    }

    def __init__(self, entries=None, registry=None, type=None, _configuration=None):  # noqa: E501
        """DeleteEndpointAclPoliciesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._entries = None
        self._registry = None
        self._type = None
        self.discriminator = None

        if entries is not None:
            self.entries = entries
        self.registry = registry
        self.type = type

    @property
    def entries(self):
        """Gets the entries of this DeleteEndpointAclPoliciesRequest.  # noqa: E501


        :return: The entries of this DeleteEndpointAclPoliciesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """Sets the entries of this DeleteEndpointAclPoliciesRequest.


        :param entries: The entries of this DeleteEndpointAclPoliciesRequest.  # noqa: E501
        :type: list[str]
        """

        self._entries = entries

    @property
    def registry(self):
        """Gets the registry of this DeleteEndpointAclPoliciesRequest.  # noqa: E501


        :return: The registry of this DeleteEndpointAclPoliciesRequest.  # noqa: E501
        :rtype: str
        """
        return self._registry

    @registry.setter
    def registry(self, registry):
        """Sets the registry of this DeleteEndpointAclPoliciesRequest.


        :param registry: The registry of this DeleteEndpointAclPoliciesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and registry is None:
            raise ValueError("Invalid value for `registry`, must not be `None`")  # noqa: E501

        self._registry = registry

    @property
    def type(self):
        """Gets the type of this DeleteEndpointAclPoliciesRequest.  # noqa: E501


        :return: The type of this DeleteEndpointAclPoliciesRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeleteEndpointAclPoliciesRequest.


        :param type: The type of this DeleteEndpointAclPoliciesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if issubclass(DeleteEndpointAclPoliciesRequest, dict):
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
        if not isinstance(other, DeleteEndpointAclPoliciesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeleteEndpointAclPoliciesRequest):
            return True

        return self.to_dict() != other.to_dict()
