# coding: utf-8

"""
    rds_mysql

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ListParameterTemplatesRequest(object):
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
        'template_category': 'str',
        'template_source': 'str',
        'template_type': 'str',
        'template_type_version': 'str'
    }

    attribute_map = {
        'template_category': 'TemplateCategory',
        'template_source': 'TemplateSource',
        'template_type': 'TemplateType',
        'template_type_version': 'TemplateTypeVersion'
    }

    def __init__(self, template_category=None, template_source=None, template_type=None, template_type_version=None, _configuration=None):  # noqa: E501
        """ListParameterTemplatesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._template_category = None
        self._template_source = None
        self._template_type = None
        self._template_type_version = None
        self.discriminator = None

        if template_category is not None:
            self.template_category = template_category
        if template_source is not None:
            self.template_source = template_source
        if template_type is not None:
            self.template_type = template_type
        if template_type_version is not None:
            self.template_type_version = template_type_version

    @property
    def template_category(self):
        """Gets the template_category of this ListParameterTemplatesRequest.  # noqa: E501


        :return: The template_category of this ListParameterTemplatesRequest.  # noqa: E501
        :rtype: str
        """
        return self._template_category

    @template_category.setter
    def template_category(self, template_category):
        """Sets the template_category of this ListParameterTemplatesRequest.


        :param template_category: The template_category of this ListParameterTemplatesRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["DBEngine", "Proxy"]  # noqa: E501
        if (self._configuration.client_side_validation and
                template_category not in allowed_values):
            raise ValueError(
                "Invalid value for `template_category` ({0}), must be one of {1}"  # noqa: E501
                .format(template_category, allowed_values)
            )

        self._template_category = template_category

    @property
    def template_source(self):
        """Gets the template_source of this ListParameterTemplatesRequest.  # noqa: E501


        :return: The template_source of this ListParameterTemplatesRequest.  # noqa: E501
        :rtype: str
        """
        return self._template_source

    @template_source.setter
    def template_source(self, template_source):
        """Sets the template_source of this ListParameterTemplatesRequest.


        :param template_source: The template_source of this ListParameterTemplatesRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["System", "User"]  # noqa: E501
        if (self._configuration.client_side_validation and
                template_source not in allowed_values):
            raise ValueError(
                "Invalid value for `template_source` ({0}), must be one of {1}"  # noqa: E501
                .format(template_source, allowed_values)
            )

        self._template_source = template_source

    @property
    def template_type(self):
        """Gets the template_type of this ListParameterTemplatesRequest.  # noqa: E501


        :return: The template_type of this ListParameterTemplatesRequest.  # noqa: E501
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        """Sets the template_type of this ListParameterTemplatesRequest.


        :param template_type: The template_type of this ListParameterTemplatesRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["MySQL"]  # noqa: E501
        if (self._configuration.client_side_validation and
                template_type not in allowed_values):
            raise ValueError(
                "Invalid value for `template_type` ({0}), must be one of {1}"  # noqa: E501
                .format(template_type, allowed_values)
            )

        self._template_type = template_type

    @property
    def template_type_version(self):
        """Gets the template_type_version of this ListParameterTemplatesRequest.  # noqa: E501


        :return: The template_type_version of this ListParameterTemplatesRequest.  # noqa: E501
        :rtype: str
        """
        return self._template_type_version

    @template_type_version.setter
    def template_type_version(self, template_type_version):
        """Sets the template_type_version of this ListParameterTemplatesRequest.


        :param template_type_version: The template_type_version of this ListParameterTemplatesRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["MySQL_8_0", "MySQL_Community_5_7"]  # noqa: E501
        if (self._configuration.client_side_validation and
                template_type_version not in allowed_values):
            raise ValueError(
                "Invalid value for `template_type_version` ({0}), must be one of {1}"  # noqa: E501
                .format(template_type_version, allowed_values)
            )

        self._template_type_version = template_type_version

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
        if issubclass(ListParameterTemplatesRequest, dict):
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
        if not isinstance(other, ListParameterTemplatesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListParameterTemplatesRequest):
            return True

        return self.to_dict() != other.to_dict()
