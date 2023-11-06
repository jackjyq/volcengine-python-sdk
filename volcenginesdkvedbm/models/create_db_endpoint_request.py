# coding: utf-8

"""
    vedbm

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateDBEndpointRequest(object):
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
        'auto_add_new_nodes': 'bool',
        'consist_level': 'str',
        'consist_timeout': 'int',
        'consist_timeout_action': 'str',
        'description': 'str',
        'distributed_transaction': 'bool',
        'endpoint_name': 'str',
        'endpoint_type': 'str',
        'instance_id': 'str',
        'master_accept_read_requests': 'bool',
        'nodes': 'str',
        'read_write_mode': 'str'
    }

    attribute_map = {
        'auto_add_new_nodes': 'AutoAddNewNodes',
        'consist_level': 'ConsistLevel',
        'consist_timeout': 'ConsistTimeout',
        'consist_timeout_action': 'ConsistTimeoutAction',
        'description': 'Description',
        'distributed_transaction': 'DistributedTransaction',
        'endpoint_name': 'EndpointName',
        'endpoint_type': 'EndpointType',
        'instance_id': 'InstanceId',
        'master_accept_read_requests': 'MasterAcceptReadRequests',
        'nodes': 'Nodes',
        'read_write_mode': 'ReadWriteMode'
    }

    def __init__(self, auto_add_new_nodes=None, consist_level=None, consist_timeout=None, consist_timeout_action=None, description=None, distributed_transaction=None, endpoint_name=None, endpoint_type=None, instance_id=None, master_accept_read_requests=None, nodes=None, read_write_mode=None, _configuration=None):  # noqa: E501
        """CreateDBEndpointRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_add_new_nodes = None
        self._consist_level = None
        self._consist_timeout = None
        self._consist_timeout_action = None
        self._description = None
        self._distributed_transaction = None
        self._endpoint_name = None
        self._endpoint_type = None
        self._instance_id = None
        self._master_accept_read_requests = None
        self._nodes = None
        self._read_write_mode = None
        self.discriminator = None

        if auto_add_new_nodes is not None:
            self.auto_add_new_nodes = auto_add_new_nodes
        if consist_level is not None:
            self.consist_level = consist_level
        if consist_timeout is not None:
            self.consist_timeout = consist_timeout
        if consist_timeout_action is not None:
            self.consist_timeout_action = consist_timeout_action
        if description is not None:
            self.description = description
        if distributed_transaction is not None:
            self.distributed_transaction = distributed_transaction
        if endpoint_name is not None:
            self.endpoint_name = endpoint_name
        if endpoint_type is not None:
            self.endpoint_type = endpoint_type
        if instance_id is not None:
            self.instance_id = instance_id
        if master_accept_read_requests is not None:
            self.master_accept_read_requests = master_accept_read_requests
        if nodes is not None:
            self.nodes = nodes
        if read_write_mode is not None:
            self.read_write_mode = read_write_mode

    @property
    def auto_add_new_nodes(self):
        """Gets the auto_add_new_nodes of this CreateDBEndpointRequest.  # noqa: E501


        :return: The auto_add_new_nodes of this CreateDBEndpointRequest.  # noqa: E501
        :rtype: bool
        """
        return self._auto_add_new_nodes

    @auto_add_new_nodes.setter
    def auto_add_new_nodes(self, auto_add_new_nodes):
        """Sets the auto_add_new_nodes of this CreateDBEndpointRequest.


        :param auto_add_new_nodes: The auto_add_new_nodes of this CreateDBEndpointRequest.  # noqa: E501
        :type: bool
        """

        self._auto_add_new_nodes = auto_add_new_nodes

    @property
    def consist_level(self):
        """Gets the consist_level of this CreateDBEndpointRequest.  # noqa: E501


        :return: The consist_level of this CreateDBEndpointRequest.  # noqa: E501
        :rtype: str
        """
        return self._consist_level

    @consist_level.setter
    def consist_level(self, consist_level):
        """Sets the consist_level of this CreateDBEndpointRequest.


        :param consist_level: The consist_level of this CreateDBEndpointRequest.  # noqa: E501
        :type: str
        """

        self._consist_level = consist_level

    @property
    def consist_timeout(self):
        """Gets the consist_timeout of this CreateDBEndpointRequest.  # noqa: E501


        :return: The consist_timeout of this CreateDBEndpointRequest.  # noqa: E501
        :rtype: int
        """
        return self._consist_timeout

    @consist_timeout.setter
    def consist_timeout(self, consist_timeout):
        """Sets the consist_timeout of this CreateDBEndpointRequest.


        :param consist_timeout: The consist_timeout of this CreateDBEndpointRequest.  # noqa: E501
        :type: int
        """

        self._consist_timeout = consist_timeout

    @property
    def consist_timeout_action(self):
        """Gets the consist_timeout_action of this CreateDBEndpointRequest.  # noqa: E501


        :return: The consist_timeout_action of this CreateDBEndpointRequest.  # noqa: E501
        :rtype: str
        """
        return self._consist_timeout_action

    @consist_timeout_action.setter
    def consist_timeout_action(self, consist_timeout_action):
        """Sets the consist_timeout_action of this CreateDBEndpointRequest.


        :param consist_timeout_action: The consist_timeout_action of this CreateDBEndpointRequest.  # noqa: E501
        :type: str
        """

        self._consist_timeout_action = consist_timeout_action

    @property
    def description(self):
        """Gets the description of this CreateDBEndpointRequest.  # noqa: E501


        :return: The description of this CreateDBEndpointRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateDBEndpointRequest.


        :param description: The description of this CreateDBEndpointRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def distributed_transaction(self):
        """Gets the distributed_transaction of this CreateDBEndpointRequest.  # noqa: E501


        :return: The distributed_transaction of this CreateDBEndpointRequest.  # noqa: E501
        :rtype: bool
        """
        return self._distributed_transaction

    @distributed_transaction.setter
    def distributed_transaction(self, distributed_transaction):
        """Sets the distributed_transaction of this CreateDBEndpointRequest.


        :param distributed_transaction: The distributed_transaction of this CreateDBEndpointRequest.  # noqa: E501
        :type: bool
        """

        self._distributed_transaction = distributed_transaction

    @property
    def endpoint_name(self):
        """Gets the endpoint_name of this CreateDBEndpointRequest.  # noqa: E501


        :return: The endpoint_name of this CreateDBEndpointRequest.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        """Sets the endpoint_name of this CreateDBEndpointRequest.


        :param endpoint_name: The endpoint_name of this CreateDBEndpointRequest.  # noqa: E501
        :type: str
        """

        self._endpoint_name = endpoint_name

    @property
    def endpoint_type(self):
        """Gets the endpoint_type of this CreateDBEndpointRequest.  # noqa: E501


        :return: The endpoint_type of this CreateDBEndpointRequest.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_type

    @endpoint_type.setter
    def endpoint_type(self, endpoint_type):
        """Sets the endpoint_type of this CreateDBEndpointRequest.


        :param endpoint_type: The endpoint_type of this CreateDBEndpointRequest.  # noqa: E501
        :type: str
        """

        self._endpoint_type = endpoint_type

    @property
    def instance_id(self):
        """Gets the instance_id of this CreateDBEndpointRequest.  # noqa: E501


        :return: The instance_id of this CreateDBEndpointRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CreateDBEndpointRequest.


        :param instance_id: The instance_id of this CreateDBEndpointRequest.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def master_accept_read_requests(self):
        """Gets the master_accept_read_requests of this CreateDBEndpointRequest.  # noqa: E501


        :return: The master_accept_read_requests of this CreateDBEndpointRequest.  # noqa: E501
        :rtype: bool
        """
        return self._master_accept_read_requests

    @master_accept_read_requests.setter
    def master_accept_read_requests(self, master_accept_read_requests):
        """Sets the master_accept_read_requests of this CreateDBEndpointRequest.


        :param master_accept_read_requests: The master_accept_read_requests of this CreateDBEndpointRequest.  # noqa: E501
        :type: bool
        """

        self._master_accept_read_requests = master_accept_read_requests

    @property
    def nodes(self):
        """Gets the nodes of this CreateDBEndpointRequest.  # noqa: E501


        :return: The nodes of this CreateDBEndpointRequest.  # noqa: E501
        :rtype: str
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this CreateDBEndpointRequest.


        :param nodes: The nodes of this CreateDBEndpointRequest.  # noqa: E501
        :type: str
        """

        self._nodes = nodes

    @property
    def read_write_mode(self):
        """Gets the read_write_mode of this CreateDBEndpointRequest.  # noqa: E501


        :return: The read_write_mode of this CreateDBEndpointRequest.  # noqa: E501
        :rtype: str
        """
        return self._read_write_mode

    @read_write_mode.setter
    def read_write_mode(self, read_write_mode):
        """Sets the read_write_mode of this CreateDBEndpointRequest.


        :param read_write_mode: The read_write_mode of this CreateDBEndpointRequest.  # noqa: E501
        :type: str
        """

        self._read_write_mode = read_write_mode

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
        if issubclass(CreateDBEndpointRequest, dict):
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
        if not isinstance(other, CreateDBEndpointRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDBEndpointRequest):
            return True

        return self.to_dict() != other.to_dict()