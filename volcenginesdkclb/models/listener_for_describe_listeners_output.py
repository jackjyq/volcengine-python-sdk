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


class ListenerForDescribeListenersOutput(object):
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
        'acl_ids': 'list[str]',
        'acl_status': 'str',
        'acl_type': 'str',
        'bandwidth': 'int',
        'certificate_id': 'str',
        'client_body_timeout': 'int',
        'client_header_timeout': 'int',
        'connection_drain_enabled': 'str',
        'connection_drain_timeout': 'int',
        'cookie': 'str',
        'create_time': 'str',
        'description': 'str',
        'enabled': 'str',
        'end_port': 'int',
        'health_check': 'HealthCheckForDescribeListenersOutput',
        'http2_enabled': 'str',
        'keepalive_timeout': 'int',
        'listener_id': 'str',
        'listener_name': 'str',
        'persistence_timeout': 'int',
        'persistence_type': 'str',
        'port': 'int',
        'protocol': 'str',
        'proxy_connect_timeout': 'int',
        'proxy_protocol_type': 'str',
        'proxy_read_timeout': 'int',
        'proxy_send_timeout': 'int',
        'scheduler': 'str',
        'security_policy_id': 'str',
        'send_timeout': 'int',
        'server_group_id': 'str',
        'start_port': 'int',
        'status': 'str',
        'tags': 'list[TagForDescribeListenersOutput]',
        'update_time': 'str'
    }

    attribute_map = {
        'acl_ids': 'AclIds',
        'acl_status': 'AclStatus',
        'acl_type': 'AclType',
        'bandwidth': 'Bandwidth',
        'certificate_id': 'CertificateId',
        'client_body_timeout': 'ClientBodyTimeout',
        'client_header_timeout': 'ClientHeaderTimeout',
        'connection_drain_enabled': 'ConnectionDrainEnabled',
        'connection_drain_timeout': 'ConnectionDrainTimeout',
        'cookie': 'Cookie',
        'create_time': 'CreateTime',
        'description': 'Description',
        'enabled': 'Enabled',
        'end_port': 'EndPort',
        'health_check': 'HealthCheck',
        'http2_enabled': 'Http2Enabled',
        'keepalive_timeout': 'KeepaliveTimeout',
        'listener_id': 'ListenerId',
        'listener_name': 'ListenerName',
        'persistence_timeout': 'PersistenceTimeout',
        'persistence_type': 'PersistenceType',
        'port': 'Port',
        'protocol': 'Protocol',
        'proxy_connect_timeout': 'ProxyConnectTimeout',
        'proxy_protocol_type': 'ProxyProtocolType',
        'proxy_read_timeout': 'ProxyReadTimeout',
        'proxy_send_timeout': 'ProxySendTimeout',
        'scheduler': 'Scheduler',
        'security_policy_id': 'SecurityPolicyId',
        'send_timeout': 'SendTimeout',
        'server_group_id': 'ServerGroupId',
        'start_port': 'StartPort',
        'status': 'Status',
        'tags': 'Tags',
        'update_time': 'UpdateTime'
    }

    def __init__(self, acl_ids=None, acl_status=None, acl_type=None, bandwidth=None, certificate_id=None, client_body_timeout=None, client_header_timeout=None, connection_drain_enabled=None, connection_drain_timeout=None, cookie=None, create_time=None, description=None, enabled=None, end_port=None, health_check=None, http2_enabled=None, keepalive_timeout=None, listener_id=None, listener_name=None, persistence_timeout=None, persistence_type=None, port=None, protocol=None, proxy_connect_timeout=None, proxy_protocol_type=None, proxy_read_timeout=None, proxy_send_timeout=None, scheduler=None, security_policy_id=None, send_timeout=None, server_group_id=None, start_port=None, status=None, tags=None, update_time=None, _configuration=None):  # noqa: E501
        """ListenerForDescribeListenersOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._acl_ids = None
        self._acl_status = None
        self._acl_type = None
        self._bandwidth = None
        self._certificate_id = None
        self._client_body_timeout = None
        self._client_header_timeout = None
        self._connection_drain_enabled = None
        self._connection_drain_timeout = None
        self._cookie = None
        self._create_time = None
        self._description = None
        self._enabled = None
        self._end_port = None
        self._health_check = None
        self._http2_enabled = None
        self._keepalive_timeout = None
        self._listener_id = None
        self._listener_name = None
        self._persistence_timeout = None
        self._persistence_type = None
        self._port = None
        self._protocol = None
        self._proxy_connect_timeout = None
        self._proxy_protocol_type = None
        self._proxy_read_timeout = None
        self._proxy_send_timeout = None
        self._scheduler = None
        self._security_policy_id = None
        self._send_timeout = None
        self._server_group_id = None
        self._start_port = None
        self._status = None
        self._tags = None
        self._update_time = None
        self.discriminator = None

        if acl_ids is not None:
            self.acl_ids = acl_ids
        if acl_status is not None:
            self.acl_status = acl_status
        if acl_type is not None:
            self.acl_type = acl_type
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if certificate_id is not None:
            self.certificate_id = certificate_id
        if client_body_timeout is not None:
            self.client_body_timeout = client_body_timeout
        if client_header_timeout is not None:
            self.client_header_timeout = client_header_timeout
        if connection_drain_enabled is not None:
            self.connection_drain_enabled = connection_drain_enabled
        if connection_drain_timeout is not None:
            self.connection_drain_timeout = connection_drain_timeout
        if cookie is not None:
            self.cookie = cookie
        if create_time is not None:
            self.create_time = create_time
        if description is not None:
            self.description = description
        if enabled is not None:
            self.enabled = enabled
        if end_port is not None:
            self.end_port = end_port
        if health_check is not None:
            self.health_check = health_check
        if http2_enabled is not None:
            self.http2_enabled = http2_enabled
        if keepalive_timeout is not None:
            self.keepalive_timeout = keepalive_timeout
        if listener_id is not None:
            self.listener_id = listener_id
        if listener_name is not None:
            self.listener_name = listener_name
        if persistence_timeout is not None:
            self.persistence_timeout = persistence_timeout
        if persistence_type is not None:
            self.persistence_type = persistence_type
        if port is not None:
            self.port = port
        if protocol is not None:
            self.protocol = protocol
        if proxy_connect_timeout is not None:
            self.proxy_connect_timeout = proxy_connect_timeout
        if proxy_protocol_type is not None:
            self.proxy_protocol_type = proxy_protocol_type
        if proxy_read_timeout is not None:
            self.proxy_read_timeout = proxy_read_timeout
        if proxy_send_timeout is not None:
            self.proxy_send_timeout = proxy_send_timeout
        if scheduler is not None:
            self.scheduler = scheduler
        if security_policy_id is not None:
            self.security_policy_id = security_policy_id
        if send_timeout is not None:
            self.send_timeout = send_timeout
        if server_group_id is not None:
            self.server_group_id = server_group_id
        if start_port is not None:
            self.start_port = start_port
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if update_time is not None:
            self.update_time = update_time

    @property
    def acl_ids(self):
        """Gets the acl_ids of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The acl_ids of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._acl_ids

    @acl_ids.setter
    def acl_ids(self, acl_ids):
        """Sets the acl_ids of this ListenerForDescribeListenersOutput.


        :param acl_ids: The acl_ids of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: list[str]
        """

        self._acl_ids = acl_ids

    @property
    def acl_status(self):
        """Gets the acl_status of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The acl_status of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: str
        """
        return self._acl_status

    @acl_status.setter
    def acl_status(self, acl_status):
        """Sets the acl_status of this ListenerForDescribeListenersOutput.


        :param acl_status: The acl_status of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: str
        """

        self._acl_status = acl_status

    @property
    def acl_type(self):
        """Gets the acl_type of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The acl_type of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: str
        """
        return self._acl_type

    @acl_type.setter
    def acl_type(self, acl_type):
        """Sets the acl_type of this ListenerForDescribeListenersOutput.


        :param acl_type: The acl_type of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: str
        """

        self._acl_type = acl_type

    @property
    def bandwidth(self):
        """Gets the bandwidth of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The bandwidth of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this ListenerForDescribeListenersOutput.


        :param bandwidth: The bandwidth of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: int
        """

        self._bandwidth = bandwidth

    @property
    def certificate_id(self):
        """Gets the certificate_id of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The certificate_id of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """Sets the certificate_id of this ListenerForDescribeListenersOutput.


        :param certificate_id: The certificate_id of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: str
        """

        self._certificate_id = certificate_id

    @property
    def client_body_timeout(self):
        """Gets the client_body_timeout of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The client_body_timeout of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: int
        """
        return self._client_body_timeout

    @client_body_timeout.setter
    def client_body_timeout(self, client_body_timeout):
        """Sets the client_body_timeout of this ListenerForDescribeListenersOutput.


        :param client_body_timeout: The client_body_timeout of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: int
        """

        self._client_body_timeout = client_body_timeout

    @property
    def client_header_timeout(self):
        """Gets the client_header_timeout of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The client_header_timeout of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: int
        """
        return self._client_header_timeout

    @client_header_timeout.setter
    def client_header_timeout(self, client_header_timeout):
        """Sets the client_header_timeout of this ListenerForDescribeListenersOutput.


        :param client_header_timeout: The client_header_timeout of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: int
        """

        self._client_header_timeout = client_header_timeout

    @property
    def connection_drain_enabled(self):
        """Gets the connection_drain_enabled of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The connection_drain_enabled of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: str
        """
        return self._connection_drain_enabled

    @connection_drain_enabled.setter
    def connection_drain_enabled(self, connection_drain_enabled):
        """Sets the connection_drain_enabled of this ListenerForDescribeListenersOutput.


        :param connection_drain_enabled: The connection_drain_enabled of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: str
        """

        self._connection_drain_enabled = connection_drain_enabled

    @property
    def connection_drain_timeout(self):
        """Gets the connection_drain_timeout of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The connection_drain_timeout of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: int
        """
        return self._connection_drain_timeout

    @connection_drain_timeout.setter
    def connection_drain_timeout(self, connection_drain_timeout):
        """Sets the connection_drain_timeout of this ListenerForDescribeListenersOutput.


        :param connection_drain_timeout: The connection_drain_timeout of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: int
        """

        self._connection_drain_timeout = connection_drain_timeout

    @property
    def cookie(self):
        """Gets the cookie of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The cookie of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: str
        """
        return self._cookie

    @cookie.setter
    def cookie(self, cookie):
        """Sets the cookie of this ListenerForDescribeListenersOutput.


        :param cookie: The cookie of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: str
        """

        self._cookie = cookie

    @property
    def create_time(self):
        """Gets the create_time of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The create_time of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ListenerForDescribeListenersOutput.


        :param create_time: The create_time of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def description(self):
        """Gets the description of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The description of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListenerForDescribeListenersOutput.


        :param description: The description of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enabled(self):
        """Gets the enabled of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The enabled of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: str
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ListenerForDescribeListenersOutput.


        :param enabled: The enabled of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: str
        """

        self._enabled = enabled

    @property
    def end_port(self):
        """Gets the end_port of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The end_port of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: int
        """
        return self._end_port

    @end_port.setter
    def end_port(self, end_port):
        """Sets the end_port of this ListenerForDescribeListenersOutput.


        :param end_port: The end_port of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: int
        """

        self._end_port = end_port

    @property
    def health_check(self):
        """Gets the health_check of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The health_check of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: HealthCheckForDescribeListenersOutput
        """
        return self._health_check

    @health_check.setter
    def health_check(self, health_check):
        """Sets the health_check of this ListenerForDescribeListenersOutput.


        :param health_check: The health_check of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: HealthCheckForDescribeListenersOutput
        """

        self._health_check = health_check

    @property
    def http2_enabled(self):
        """Gets the http2_enabled of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The http2_enabled of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: str
        """
        return self._http2_enabled

    @http2_enabled.setter
    def http2_enabled(self, http2_enabled):
        """Sets the http2_enabled of this ListenerForDescribeListenersOutput.


        :param http2_enabled: The http2_enabled of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: str
        """

        self._http2_enabled = http2_enabled

    @property
    def keepalive_timeout(self):
        """Gets the keepalive_timeout of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The keepalive_timeout of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: int
        """
        return self._keepalive_timeout

    @keepalive_timeout.setter
    def keepalive_timeout(self, keepalive_timeout):
        """Sets the keepalive_timeout of this ListenerForDescribeListenersOutput.


        :param keepalive_timeout: The keepalive_timeout of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: int
        """

        self._keepalive_timeout = keepalive_timeout

    @property
    def listener_id(self):
        """Gets the listener_id of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The listener_id of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this ListenerForDescribeListenersOutput.


        :param listener_id: The listener_id of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: str
        """

        self._listener_id = listener_id

    @property
    def listener_name(self):
        """Gets the listener_name of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The listener_name of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: str
        """
        return self._listener_name

    @listener_name.setter
    def listener_name(self, listener_name):
        """Sets the listener_name of this ListenerForDescribeListenersOutput.


        :param listener_name: The listener_name of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: str
        """

        self._listener_name = listener_name

    @property
    def persistence_timeout(self):
        """Gets the persistence_timeout of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The persistence_timeout of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: int
        """
        return self._persistence_timeout

    @persistence_timeout.setter
    def persistence_timeout(self, persistence_timeout):
        """Sets the persistence_timeout of this ListenerForDescribeListenersOutput.


        :param persistence_timeout: The persistence_timeout of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: int
        """

        self._persistence_timeout = persistence_timeout

    @property
    def persistence_type(self):
        """Gets the persistence_type of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The persistence_type of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: str
        """
        return self._persistence_type

    @persistence_type.setter
    def persistence_type(self, persistence_type):
        """Sets the persistence_type of this ListenerForDescribeListenersOutput.


        :param persistence_type: The persistence_type of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: str
        """

        self._persistence_type = persistence_type

    @property
    def port(self):
        """Gets the port of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The port of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ListenerForDescribeListenersOutput.


        :param port: The port of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def protocol(self):
        """Gets the protocol of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The protocol of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ListenerForDescribeListenersOutput.


        :param protocol: The protocol of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def proxy_connect_timeout(self):
        """Gets the proxy_connect_timeout of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The proxy_connect_timeout of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: int
        """
        return self._proxy_connect_timeout

    @proxy_connect_timeout.setter
    def proxy_connect_timeout(self, proxy_connect_timeout):
        """Sets the proxy_connect_timeout of this ListenerForDescribeListenersOutput.


        :param proxy_connect_timeout: The proxy_connect_timeout of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: int
        """

        self._proxy_connect_timeout = proxy_connect_timeout

    @property
    def proxy_protocol_type(self):
        """Gets the proxy_protocol_type of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The proxy_protocol_type of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: str
        """
        return self._proxy_protocol_type

    @proxy_protocol_type.setter
    def proxy_protocol_type(self, proxy_protocol_type):
        """Sets the proxy_protocol_type of this ListenerForDescribeListenersOutput.


        :param proxy_protocol_type: The proxy_protocol_type of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: str
        """

        self._proxy_protocol_type = proxy_protocol_type

    @property
    def proxy_read_timeout(self):
        """Gets the proxy_read_timeout of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The proxy_read_timeout of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: int
        """
        return self._proxy_read_timeout

    @proxy_read_timeout.setter
    def proxy_read_timeout(self, proxy_read_timeout):
        """Sets the proxy_read_timeout of this ListenerForDescribeListenersOutput.


        :param proxy_read_timeout: The proxy_read_timeout of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: int
        """

        self._proxy_read_timeout = proxy_read_timeout

    @property
    def proxy_send_timeout(self):
        """Gets the proxy_send_timeout of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The proxy_send_timeout of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: int
        """
        return self._proxy_send_timeout

    @proxy_send_timeout.setter
    def proxy_send_timeout(self, proxy_send_timeout):
        """Sets the proxy_send_timeout of this ListenerForDescribeListenersOutput.


        :param proxy_send_timeout: The proxy_send_timeout of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: int
        """

        self._proxy_send_timeout = proxy_send_timeout

    @property
    def scheduler(self):
        """Gets the scheduler of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The scheduler of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: str
        """
        return self._scheduler

    @scheduler.setter
    def scheduler(self, scheduler):
        """Sets the scheduler of this ListenerForDescribeListenersOutput.


        :param scheduler: The scheduler of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: str
        """

        self._scheduler = scheduler

    @property
    def security_policy_id(self):
        """Gets the security_policy_id of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The security_policy_id of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: str
        """
        return self._security_policy_id

    @security_policy_id.setter
    def security_policy_id(self, security_policy_id):
        """Sets the security_policy_id of this ListenerForDescribeListenersOutput.


        :param security_policy_id: The security_policy_id of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: str
        """

        self._security_policy_id = security_policy_id

    @property
    def send_timeout(self):
        """Gets the send_timeout of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The send_timeout of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: int
        """
        return self._send_timeout

    @send_timeout.setter
    def send_timeout(self, send_timeout):
        """Sets the send_timeout of this ListenerForDescribeListenersOutput.


        :param send_timeout: The send_timeout of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: int
        """

        self._send_timeout = send_timeout

    @property
    def server_group_id(self):
        """Gets the server_group_id of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The server_group_id of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        """Sets the server_group_id of this ListenerForDescribeListenersOutput.


        :param server_group_id: The server_group_id of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: str
        """

        self._server_group_id = server_group_id

    @property
    def start_port(self):
        """Gets the start_port of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The start_port of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: int
        """
        return self._start_port

    @start_port.setter
    def start_port(self, start_port):
        """Sets the start_port of this ListenerForDescribeListenersOutput.


        :param start_port: The start_port of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: int
        """

        self._start_port = start_port

    @property
    def status(self):
        """Gets the status of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The status of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListenerForDescribeListenersOutput.


        :param status: The status of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The tags of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: list[TagForDescribeListenersOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListenerForDescribeListenersOutput.


        :param tags: The tags of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: list[TagForDescribeListenersOutput]
        """

        self._tags = tags

    @property
    def update_time(self):
        """Gets the update_time of this ListenerForDescribeListenersOutput.  # noqa: E501


        :return: The update_time of this ListenerForDescribeListenersOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ListenerForDescribeListenersOutput.


        :param update_time: The update_time of this ListenerForDescribeListenersOutput.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

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
        if issubclass(ListenerForDescribeListenersOutput, dict):
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
        if not isinstance(other, ListenerForDescribeListenersOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListenerForDescribeListenersOutput):
            return True

        return self.to_dict() != other.to_dict()
