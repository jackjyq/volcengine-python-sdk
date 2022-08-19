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


class ChartAttributeForListTagsOutput(object):
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
        'api_version': 'str',
        'name': 'str',
        'version': 'str'
    }

    attribute_map = {
        'api_version': 'ApiVersion',
        'name': 'Name',
        'version': 'Version'
    }

    def __init__(self, api_version=None, name=None, version=None, _configuration=None):  # noqa: E501
        """ChartAttributeForListTagsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._api_version = None
        self._name = None
        self._version = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version

    @property
    def api_version(self):
        """Gets the api_version of this ChartAttributeForListTagsOutput.  # noqa: E501


        :return: The api_version of this ChartAttributeForListTagsOutput.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this ChartAttributeForListTagsOutput.


        :param api_version: The api_version of this ChartAttributeForListTagsOutput.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def name(self):
        """Gets the name of this ChartAttributeForListTagsOutput.  # noqa: E501


        :return: The name of this ChartAttributeForListTagsOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChartAttributeForListTagsOutput.


        :param name: The name of this ChartAttributeForListTagsOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def version(self):
        """Gets the version of this ChartAttributeForListTagsOutput.  # noqa: E501


        :return: The version of this ChartAttributeForListTagsOutput.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ChartAttributeForListTagsOutput.


        :param version: The version of this ChartAttributeForListTagsOutput.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(ChartAttributeForListTagsOutput, dict):
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
        if not isinstance(other, ChartAttributeForListTagsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChartAttributeForListTagsOutput):
            return True

        return self.to_dict() != other.to_dict()
