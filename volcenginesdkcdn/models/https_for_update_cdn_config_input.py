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


class HTTPSForUpdateCdnConfigInput(object):
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
        'cert_check': 'CertCheckForUpdateCdnConfigInput',
        'cert_info': 'CertInfoForUpdateCdnConfigInput',
        'cert_info_list': 'list[CertInfoListForUpdateCdnConfigInput]',
        'disable_http': 'bool',
        'forced_redirect': 'ForcedRedirectForUpdateCdnConfigInput',
        'http2': 'bool',
        'hsts': 'HstsForUpdateCdnConfigInput',
        'ocsp': 'bool',
        'switch': 'bool',
        'tls_version': 'list[str]'
    }

    attribute_map = {
        'cert_check': 'CertCheck',
        'cert_info': 'CertInfo',
        'cert_info_list': 'CertInfoList',
        'disable_http': 'DisableHttp',
        'forced_redirect': 'ForcedRedirect',
        'http2': 'HTTP2',
        'hsts': 'Hsts',
        'ocsp': 'OCSP',
        'switch': 'Switch',
        'tls_version': 'TlsVersion'
    }

    def __init__(self, cert_check=None, cert_info=None, cert_info_list=None, disable_http=None, forced_redirect=None, http2=None, hsts=None, ocsp=None, switch=None, tls_version=None, _configuration=None):  # noqa: E501
        """HTTPSForUpdateCdnConfigInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cert_check = None
        self._cert_info = None
        self._cert_info_list = None
        self._disable_http = None
        self._forced_redirect = None
        self._http2 = None
        self._hsts = None
        self._ocsp = None
        self._switch = None
        self._tls_version = None
        self.discriminator = None

        if cert_check is not None:
            self.cert_check = cert_check
        if cert_info is not None:
            self.cert_info = cert_info
        if cert_info_list is not None:
            self.cert_info_list = cert_info_list
        if disable_http is not None:
            self.disable_http = disable_http
        if forced_redirect is not None:
            self.forced_redirect = forced_redirect
        if http2 is not None:
            self.http2 = http2
        if hsts is not None:
            self.hsts = hsts
        if ocsp is not None:
            self.ocsp = ocsp
        if switch is not None:
            self.switch = switch
        if tls_version is not None:
            self.tls_version = tls_version

    @property
    def cert_check(self):
        """Gets the cert_check of this HTTPSForUpdateCdnConfigInput.  # noqa: E501


        :return: The cert_check of this HTTPSForUpdateCdnConfigInput.  # noqa: E501
        :rtype: CertCheckForUpdateCdnConfigInput
        """
        return self._cert_check

    @cert_check.setter
    def cert_check(self, cert_check):
        """Sets the cert_check of this HTTPSForUpdateCdnConfigInput.


        :param cert_check: The cert_check of this HTTPSForUpdateCdnConfigInput.  # noqa: E501
        :type: CertCheckForUpdateCdnConfigInput
        """

        self._cert_check = cert_check

    @property
    def cert_info(self):
        """Gets the cert_info of this HTTPSForUpdateCdnConfigInput.  # noqa: E501


        :return: The cert_info of this HTTPSForUpdateCdnConfigInput.  # noqa: E501
        :rtype: CertInfoForUpdateCdnConfigInput
        """
        return self._cert_info

    @cert_info.setter
    def cert_info(self, cert_info):
        """Sets the cert_info of this HTTPSForUpdateCdnConfigInput.


        :param cert_info: The cert_info of this HTTPSForUpdateCdnConfigInput.  # noqa: E501
        :type: CertInfoForUpdateCdnConfigInput
        """

        self._cert_info = cert_info

    @property
    def cert_info_list(self):
        """Gets the cert_info_list of this HTTPSForUpdateCdnConfigInput.  # noqa: E501


        :return: The cert_info_list of this HTTPSForUpdateCdnConfigInput.  # noqa: E501
        :rtype: list[CertInfoListForUpdateCdnConfigInput]
        """
        return self._cert_info_list

    @cert_info_list.setter
    def cert_info_list(self, cert_info_list):
        """Sets the cert_info_list of this HTTPSForUpdateCdnConfigInput.


        :param cert_info_list: The cert_info_list of this HTTPSForUpdateCdnConfigInput.  # noqa: E501
        :type: list[CertInfoListForUpdateCdnConfigInput]
        """

        self._cert_info_list = cert_info_list

    @property
    def disable_http(self):
        """Gets the disable_http of this HTTPSForUpdateCdnConfigInput.  # noqa: E501


        :return: The disable_http of this HTTPSForUpdateCdnConfigInput.  # noqa: E501
        :rtype: bool
        """
        return self._disable_http

    @disable_http.setter
    def disable_http(self, disable_http):
        """Sets the disable_http of this HTTPSForUpdateCdnConfigInput.


        :param disable_http: The disable_http of this HTTPSForUpdateCdnConfigInput.  # noqa: E501
        :type: bool
        """

        self._disable_http = disable_http

    @property
    def forced_redirect(self):
        """Gets the forced_redirect of this HTTPSForUpdateCdnConfigInput.  # noqa: E501


        :return: The forced_redirect of this HTTPSForUpdateCdnConfigInput.  # noqa: E501
        :rtype: ForcedRedirectForUpdateCdnConfigInput
        """
        return self._forced_redirect

    @forced_redirect.setter
    def forced_redirect(self, forced_redirect):
        """Sets the forced_redirect of this HTTPSForUpdateCdnConfigInput.


        :param forced_redirect: The forced_redirect of this HTTPSForUpdateCdnConfigInput.  # noqa: E501
        :type: ForcedRedirectForUpdateCdnConfigInput
        """

        self._forced_redirect = forced_redirect

    @property
    def http2(self):
        """Gets the http2 of this HTTPSForUpdateCdnConfigInput.  # noqa: E501


        :return: The http2 of this HTTPSForUpdateCdnConfigInput.  # noqa: E501
        :rtype: bool
        """
        return self._http2

    @http2.setter
    def http2(self, http2):
        """Sets the http2 of this HTTPSForUpdateCdnConfigInput.


        :param http2: The http2 of this HTTPSForUpdateCdnConfigInput.  # noqa: E501
        :type: bool
        """

        self._http2 = http2

    @property
    def hsts(self):
        """Gets the hsts of this HTTPSForUpdateCdnConfigInput.  # noqa: E501


        :return: The hsts of this HTTPSForUpdateCdnConfigInput.  # noqa: E501
        :rtype: HstsForUpdateCdnConfigInput
        """
        return self._hsts

    @hsts.setter
    def hsts(self, hsts):
        """Sets the hsts of this HTTPSForUpdateCdnConfigInput.


        :param hsts: The hsts of this HTTPSForUpdateCdnConfigInput.  # noqa: E501
        :type: HstsForUpdateCdnConfigInput
        """

        self._hsts = hsts

    @property
    def ocsp(self):
        """Gets the ocsp of this HTTPSForUpdateCdnConfigInput.  # noqa: E501


        :return: The ocsp of this HTTPSForUpdateCdnConfigInput.  # noqa: E501
        :rtype: bool
        """
        return self._ocsp

    @ocsp.setter
    def ocsp(self, ocsp):
        """Sets the ocsp of this HTTPSForUpdateCdnConfigInput.


        :param ocsp: The ocsp of this HTTPSForUpdateCdnConfigInput.  # noqa: E501
        :type: bool
        """

        self._ocsp = ocsp

    @property
    def switch(self):
        """Gets the switch of this HTTPSForUpdateCdnConfigInput.  # noqa: E501


        :return: The switch of this HTTPSForUpdateCdnConfigInput.  # noqa: E501
        :rtype: bool
        """
        return self._switch

    @switch.setter
    def switch(self, switch):
        """Sets the switch of this HTTPSForUpdateCdnConfigInput.


        :param switch: The switch of this HTTPSForUpdateCdnConfigInput.  # noqa: E501
        :type: bool
        """

        self._switch = switch

    @property
    def tls_version(self):
        """Gets the tls_version of this HTTPSForUpdateCdnConfigInput.  # noqa: E501


        :return: The tls_version of this HTTPSForUpdateCdnConfigInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._tls_version

    @tls_version.setter
    def tls_version(self, tls_version):
        """Sets the tls_version of this HTTPSForUpdateCdnConfigInput.


        :param tls_version: The tls_version of this HTTPSForUpdateCdnConfigInput.  # noqa: E501
        :type: list[str]
        """

        self._tls_version = tls_version

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
        if issubclass(HTTPSForUpdateCdnConfigInput, dict):
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
        if not isinstance(other, HTTPSForUpdateCdnConfigInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HTTPSForUpdateCdnConfigInput):
            return True

        return self.to_dict() != other.to_dict()
