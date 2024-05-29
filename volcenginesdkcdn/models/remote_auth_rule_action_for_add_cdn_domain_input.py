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


class RemoteAuthRuleActionForAddCdnDomainInput(object):
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
        'auth_mode_config': 'AuthModeConfigForAddCdnDomainInput',
        'auth_response_config': 'AuthResponseConfigForAddCdnDomainInput',
        'query_string_rules': 'QueryStringRulesForAddCdnDomainInput',
        'request_body_rules': 'str',
        'request_header_rules': 'RequestHeaderRulesForAddCdnDomainInput'
    }

    attribute_map = {
        'auth_mode_config': 'AuthModeConfig',
        'auth_response_config': 'AuthResponseConfig',
        'query_string_rules': 'QueryStringRules',
        'request_body_rules': 'RequestBodyRules',
        'request_header_rules': 'RequestHeaderRules'
    }

    def __init__(self, auth_mode_config=None, auth_response_config=None, query_string_rules=None, request_body_rules=None, request_header_rules=None, _configuration=None):  # noqa: E501
        """RemoteAuthRuleActionForAddCdnDomainInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auth_mode_config = None
        self._auth_response_config = None
        self._query_string_rules = None
        self._request_body_rules = None
        self._request_header_rules = None
        self.discriminator = None

        if auth_mode_config is not None:
            self.auth_mode_config = auth_mode_config
        if auth_response_config is not None:
            self.auth_response_config = auth_response_config
        if query_string_rules is not None:
            self.query_string_rules = query_string_rules
        if request_body_rules is not None:
            self.request_body_rules = request_body_rules
        if request_header_rules is not None:
            self.request_header_rules = request_header_rules

    @property
    def auth_mode_config(self):
        """Gets the auth_mode_config of this RemoteAuthRuleActionForAddCdnDomainInput.  # noqa: E501


        :return: The auth_mode_config of this RemoteAuthRuleActionForAddCdnDomainInput.  # noqa: E501
        :rtype: AuthModeConfigForAddCdnDomainInput
        """
        return self._auth_mode_config

    @auth_mode_config.setter
    def auth_mode_config(self, auth_mode_config):
        """Sets the auth_mode_config of this RemoteAuthRuleActionForAddCdnDomainInput.


        :param auth_mode_config: The auth_mode_config of this RemoteAuthRuleActionForAddCdnDomainInput.  # noqa: E501
        :type: AuthModeConfigForAddCdnDomainInput
        """

        self._auth_mode_config = auth_mode_config

    @property
    def auth_response_config(self):
        """Gets the auth_response_config of this RemoteAuthRuleActionForAddCdnDomainInput.  # noqa: E501


        :return: The auth_response_config of this RemoteAuthRuleActionForAddCdnDomainInput.  # noqa: E501
        :rtype: AuthResponseConfigForAddCdnDomainInput
        """
        return self._auth_response_config

    @auth_response_config.setter
    def auth_response_config(self, auth_response_config):
        """Sets the auth_response_config of this RemoteAuthRuleActionForAddCdnDomainInput.


        :param auth_response_config: The auth_response_config of this RemoteAuthRuleActionForAddCdnDomainInput.  # noqa: E501
        :type: AuthResponseConfigForAddCdnDomainInput
        """

        self._auth_response_config = auth_response_config

    @property
    def query_string_rules(self):
        """Gets the query_string_rules of this RemoteAuthRuleActionForAddCdnDomainInput.  # noqa: E501


        :return: The query_string_rules of this RemoteAuthRuleActionForAddCdnDomainInput.  # noqa: E501
        :rtype: QueryStringRulesForAddCdnDomainInput
        """
        return self._query_string_rules

    @query_string_rules.setter
    def query_string_rules(self, query_string_rules):
        """Sets the query_string_rules of this RemoteAuthRuleActionForAddCdnDomainInput.


        :param query_string_rules: The query_string_rules of this RemoteAuthRuleActionForAddCdnDomainInput.  # noqa: E501
        :type: QueryStringRulesForAddCdnDomainInput
        """

        self._query_string_rules = query_string_rules

    @property
    def request_body_rules(self):
        """Gets the request_body_rules of this RemoteAuthRuleActionForAddCdnDomainInput.  # noqa: E501


        :return: The request_body_rules of this RemoteAuthRuleActionForAddCdnDomainInput.  # noqa: E501
        :rtype: str
        """
        return self._request_body_rules

    @request_body_rules.setter
    def request_body_rules(self, request_body_rules):
        """Sets the request_body_rules of this RemoteAuthRuleActionForAddCdnDomainInput.


        :param request_body_rules: The request_body_rules of this RemoteAuthRuleActionForAddCdnDomainInput.  # noqa: E501
        :type: str
        """

        self._request_body_rules = request_body_rules

    @property
    def request_header_rules(self):
        """Gets the request_header_rules of this RemoteAuthRuleActionForAddCdnDomainInput.  # noqa: E501


        :return: The request_header_rules of this RemoteAuthRuleActionForAddCdnDomainInput.  # noqa: E501
        :rtype: RequestHeaderRulesForAddCdnDomainInput
        """
        return self._request_header_rules

    @request_header_rules.setter
    def request_header_rules(self, request_header_rules):
        """Sets the request_header_rules of this RemoteAuthRuleActionForAddCdnDomainInput.


        :param request_header_rules: The request_header_rules of this RemoteAuthRuleActionForAddCdnDomainInput.  # noqa: E501
        :type: RequestHeaderRulesForAddCdnDomainInput
        """

        self._request_header_rules = request_header_rules

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
        if issubclass(RemoteAuthRuleActionForAddCdnDomainInput, dict):
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
        if not isinstance(other, RemoteAuthRuleActionForAddCdnDomainInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RemoteAuthRuleActionForAddCdnDomainInput):
            return True

        return self.to_dict() != other.to_dict()
