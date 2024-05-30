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


class SignParamForUpdateCdnConfigInput(object):
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
        'param_type': 'str',
        'request_header': 'str',
        'sup_content': 'str',
        'uri_param_sup': 'UriParamSupForUpdateCdnConfigInput',
        'url_param': 'SignCapRuleForUpdateCdnConfigInput'
    }

    attribute_map = {
        'param_type': 'ParamType',
        'request_header': 'RequestHeader',
        'sup_content': 'SupContent',
        'uri_param_sup': 'UriParamSup',
        'url_param': 'UrlParam'
    }

    def __init__(self, param_type=None, request_header=None, sup_content=None, uri_param_sup=None, url_param=None, _configuration=None):  # noqa: E501
        """SignParamForUpdateCdnConfigInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._param_type = None
        self._request_header = None
        self._sup_content = None
        self._uri_param_sup = None
        self._url_param = None
        self.discriminator = None

        if param_type is not None:
            self.param_type = param_type
        if request_header is not None:
            self.request_header = request_header
        if sup_content is not None:
            self.sup_content = sup_content
        if uri_param_sup is not None:
            self.uri_param_sup = uri_param_sup
        if url_param is not None:
            self.url_param = url_param

    @property
    def param_type(self):
        """Gets the param_type of this SignParamForUpdateCdnConfigInput.  # noqa: E501


        :return: The param_type of this SignParamForUpdateCdnConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._param_type

    @param_type.setter
    def param_type(self, param_type):
        """Sets the param_type of this SignParamForUpdateCdnConfigInput.


        :param param_type: The param_type of this SignParamForUpdateCdnConfigInput.  # noqa: E501
        :type: str
        """

        self._param_type = param_type

    @property
    def request_header(self):
        """Gets the request_header of this SignParamForUpdateCdnConfigInput.  # noqa: E501


        :return: The request_header of this SignParamForUpdateCdnConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._request_header

    @request_header.setter
    def request_header(self, request_header):
        """Sets the request_header of this SignParamForUpdateCdnConfigInput.


        :param request_header: The request_header of this SignParamForUpdateCdnConfigInput.  # noqa: E501
        :type: str
        """

        self._request_header = request_header

    @property
    def sup_content(self):
        """Gets the sup_content of this SignParamForUpdateCdnConfigInput.  # noqa: E501


        :return: The sup_content of this SignParamForUpdateCdnConfigInput.  # noqa: E501
        :rtype: str
        """
        return self._sup_content

    @sup_content.setter
    def sup_content(self, sup_content):
        """Sets the sup_content of this SignParamForUpdateCdnConfigInput.


        :param sup_content: The sup_content of this SignParamForUpdateCdnConfigInput.  # noqa: E501
        :type: str
        """

        self._sup_content = sup_content

    @property
    def uri_param_sup(self):
        """Gets the uri_param_sup of this SignParamForUpdateCdnConfigInput.  # noqa: E501


        :return: The uri_param_sup of this SignParamForUpdateCdnConfigInput.  # noqa: E501
        :rtype: UriParamSupForUpdateCdnConfigInput
        """
        return self._uri_param_sup

    @uri_param_sup.setter
    def uri_param_sup(self, uri_param_sup):
        """Sets the uri_param_sup of this SignParamForUpdateCdnConfigInput.


        :param uri_param_sup: The uri_param_sup of this SignParamForUpdateCdnConfigInput.  # noqa: E501
        :type: UriParamSupForUpdateCdnConfigInput
        """

        self._uri_param_sup = uri_param_sup

    @property
    def url_param(self):
        """Gets the url_param of this SignParamForUpdateCdnConfigInput.  # noqa: E501


        :return: The url_param of this SignParamForUpdateCdnConfigInput.  # noqa: E501
        :rtype: SignCapRuleForUpdateCdnConfigInput
        """
        return self._url_param

    @url_param.setter
    def url_param(self, url_param):
        """Sets the url_param of this SignParamForUpdateCdnConfigInput.


        :param url_param: The url_param of this SignParamForUpdateCdnConfigInput.  # noqa: E501
        :type: SignCapRuleForUpdateCdnConfigInput
        """

        self._url_param = url_param

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
        if issubclass(SignParamForUpdateCdnConfigInput, dict):
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
        if not isinstance(other, SignParamForUpdateCdnConfigInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SignParamForUpdateCdnConfigInput):
            return True

        return self.to_dict() != other.to_dict()
