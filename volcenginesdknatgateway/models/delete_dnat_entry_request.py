# coding: utf-8

"""
    natgateway

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DeleteDnatEntryRequest(object):
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
        'dnat_entry_id': 'str'
    }

    attribute_map = {
        'dnat_entry_id': 'DnatEntryId'
    }

    def __init__(self, dnat_entry_id=None, _configuration=None):  # noqa: E501
        """DeleteDnatEntryRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._dnat_entry_id = None
        self.discriminator = None

        self.dnat_entry_id = dnat_entry_id

    @property
    def dnat_entry_id(self):
        """Gets the dnat_entry_id of this DeleteDnatEntryRequest.  # noqa: E501


        :return: The dnat_entry_id of this DeleteDnatEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._dnat_entry_id

    @dnat_entry_id.setter
    def dnat_entry_id(self, dnat_entry_id):
        """Sets the dnat_entry_id of this DeleteDnatEntryRequest.


        :param dnat_entry_id: The dnat_entry_id of this DeleteDnatEntryRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and dnat_entry_id is None:
            raise ValueError("Invalid value for `dnat_entry_id`, must not be `None`")  # noqa: E501

        self._dnat_entry_id = dnat_entry_id

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
        if issubclass(DeleteDnatEntryRequest, dict):
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
        if not isinstance(other, DeleteDnatEntryRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeleteDnatEntryRequest):
            return True

        return self.to_dict() != other.to_dict()
