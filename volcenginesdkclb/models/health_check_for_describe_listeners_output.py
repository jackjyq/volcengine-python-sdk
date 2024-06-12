# coding: utf-8

"""
    clb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class HealthCheckForDescribeListenersOutput(object):
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
        'domain': 'str',
        'enabled': 'str',
        'healthy_threshold': 'int',
        'http_code': 'str',
        'interval': 'int',
        'method': 'str',
        'port': 'int',
        'timeout': 'int',
        'udp_expect': 'str',
        'udp_request': 'str',
        'un_healthy_threshold': 'int',
        'uri': 'str'
    }

    attribute_map = {
        'domain': 'Domain',
        'enabled': 'Enabled',
        'healthy_threshold': 'HealthyThreshold',
        'http_code': 'HttpCode',
        'interval': 'Interval',
        'method': 'Method',
        'port': 'Port',
        'timeout': 'Timeout',
        'udp_expect': 'UdpExpect',
        'udp_request': 'UdpRequest',
        'un_healthy_threshold': 'UnHealthyThreshold',
        'uri': 'Uri'
    }

    def __init__(self, domain=None, enabled=None, healthy_threshold=None, http_code=None, interval=None, method=None, port=None, timeout=None, udp_expect=None, udp_request=None, un_healthy_threshold=None, uri=None, _configuration=None):  # noqa: E501
        """HealthCheckForDescribeListenersOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._domain = None
        self._enabled = None
        self._healthy_threshold = None
        self._http_code = None
        self._interval = None
        self._method = None
        self._port = None
        self._timeout = None
        self._udp_expect = None
        self._udp_request = None
        self._un_healthy_threshold = None
        self._uri = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if enabled is not None:
            self.enabled = enabled
        if healthy_threshold is not None:
            self.healthy_threshold = healthy_threshold
        if http_code is not None:
            self.http_code = http_code
        if interval is not None:
            self.interval = interval
        if method is not None:
            self.method = method
        if port is not None:
            self.port = port
        if timeout is not None:
            self.timeout = timeout
        if udp_expect is not None:
            self.udp_expect = udp_expect
        if udp_request is not None:
            self.udp_request = udp_request
        if un_healthy_threshold is not None:
            self.un_healthy_threshold = un_healthy_threshold
        if uri is not None:
            self.uri = uri

    @property
    def domain(self):
        """Gets the domain of this HealthCheckForDescribeListenersOutput.  # noqa: E501


        :return: The domain of this HealthCheckForDescribeListenersOutput.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this HealthCheckForDescribeListenersOutput.


        :param domain: The domain of this HealthCheckForDescribeListenersOutput.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def enabled(self):
        """Gets the enabled of this HealthCheckForDescribeListenersOutput.  # noqa: E501


        :return: The enabled of this HealthCheckForDescribeListenersOutput.  # noqa: E501
        :rtype: str
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this HealthCheckForDescribeListenersOutput.


        :param enabled: The enabled of this HealthCheckForDescribeListenersOutput.  # noqa: E501
        :type: str
        """

        self._enabled = enabled

    @property
    def healthy_threshold(self):
        """Gets the healthy_threshold of this HealthCheckForDescribeListenersOutput.  # noqa: E501


        :return: The healthy_threshold of this HealthCheckForDescribeListenersOutput.  # noqa: E501
        :rtype: int
        """
        return self._healthy_threshold

    @healthy_threshold.setter
    def healthy_threshold(self, healthy_threshold):
        """Sets the healthy_threshold of this HealthCheckForDescribeListenersOutput.


        :param healthy_threshold: The healthy_threshold of this HealthCheckForDescribeListenersOutput.  # noqa: E501
        :type: int
        """

        self._healthy_threshold = healthy_threshold

    @property
    def http_code(self):
        """Gets the http_code of this HealthCheckForDescribeListenersOutput.  # noqa: E501


        :return: The http_code of this HealthCheckForDescribeListenersOutput.  # noqa: E501
        :rtype: str
        """
        return self._http_code

    @http_code.setter
    def http_code(self, http_code):
        """Sets the http_code of this HealthCheckForDescribeListenersOutput.


        :param http_code: The http_code of this HealthCheckForDescribeListenersOutput.  # noqa: E501
        :type: str
        """

        self._http_code = http_code

    @property
    def interval(self):
        """Gets the interval of this HealthCheckForDescribeListenersOutput.  # noqa: E501


        :return: The interval of this HealthCheckForDescribeListenersOutput.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this HealthCheckForDescribeListenersOutput.


        :param interval: The interval of this HealthCheckForDescribeListenersOutput.  # noqa: E501
        :type: int
        """

        self._interval = interval

    @property
    def method(self):
        """Gets the method of this HealthCheckForDescribeListenersOutput.  # noqa: E501


        :return: The method of this HealthCheckForDescribeListenersOutput.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this HealthCheckForDescribeListenersOutput.


        :param method: The method of this HealthCheckForDescribeListenersOutput.  # noqa: E501
        :type: str
        """

        self._method = method

    @property
    def port(self):
        """Gets the port of this HealthCheckForDescribeListenersOutput.  # noqa: E501


        :return: The port of this HealthCheckForDescribeListenersOutput.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this HealthCheckForDescribeListenersOutput.


        :param port: The port of this HealthCheckForDescribeListenersOutput.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def timeout(self):
        """Gets the timeout of this HealthCheckForDescribeListenersOutput.  # noqa: E501


        :return: The timeout of this HealthCheckForDescribeListenersOutput.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this HealthCheckForDescribeListenersOutput.


        :param timeout: The timeout of this HealthCheckForDescribeListenersOutput.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

    @property
    def udp_expect(self):
        """Gets the udp_expect of this HealthCheckForDescribeListenersOutput.  # noqa: E501


        :return: The udp_expect of this HealthCheckForDescribeListenersOutput.  # noqa: E501
        :rtype: str
        """
        return self._udp_expect

    @udp_expect.setter
    def udp_expect(self, udp_expect):
        """Sets the udp_expect of this HealthCheckForDescribeListenersOutput.


        :param udp_expect: The udp_expect of this HealthCheckForDescribeListenersOutput.  # noqa: E501
        :type: str
        """

        self._udp_expect = udp_expect

    @property
    def udp_request(self):
        """Gets the udp_request of this HealthCheckForDescribeListenersOutput.  # noqa: E501


        :return: The udp_request of this HealthCheckForDescribeListenersOutput.  # noqa: E501
        :rtype: str
        """
        return self._udp_request

    @udp_request.setter
    def udp_request(self, udp_request):
        """Sets the udp_request of this HealthCheckForDescribeListenersOutput.


        :param udp_request: The udp_request of this HealthCheckForDescribeListenersOutput.  # noqa: E501
        :type: str
        """

        self._udp_request = udp_request

    @property
    def un_healthy_threshold(self):
        """Gets the un_healthy_threshold of this HealthCheckForDescribeListenersOutput.  # noqa: E501


        :return: The un_healthy_threshold of this HealthCheckForDescribeListenersOutput.  # noqa: E501
        :rtype: int
        """
        return self._un_healthy_threshold

    @un_healthy_threshold.setter
    def un_healthy_threshold(self, un_healthy_threshold):
        """Sets the un_healthy_threshold of this HealthCheckForDescribeListenersOutput.


        :param un_healthy_threshold: The un_healthy_threshold of this HealthCheckForDescribeListenersOutput.  # noqa: E501
        :type: int
        """

        self._un_healthy_threshold = un_healthy_threshold

    @property
    def uri(self):
        """Gets the uri of this HealthCheckForDescribeListenersOutput.  # noqa: E501


        :return: The uri of this HealthCheckForDescribeListenersOutput.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this HealthCheckForDescribeListenersOutput.


        :param uri: The uri of this HealthCheckForDescribeListenersOutput.  # noqa: E501
        :type: str
        """

        self._uri = uri

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
        if issubclass(HealthCheckForDescribeListenersOutput, dict):
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
        if not isinstance(other, HealthCheckForDescribeListenersOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HealthCheckForDescribeListenersOutput):
            return True

        return self.to_dict() != other.to_dict()
