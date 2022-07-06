# coding: utf-8

"""
    vke

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateNodePoolRequest(object):
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
        'auto_scaling': 'AutoScalingForCreateNodePoolInput',
        'client_token': 'str',
        'cluster_id': 'str',
        'kubernetes_config': 'KubernetesConfigForCreateNodePoolInput',
        'name': 'str',
        'node_config': 'NodeConfigForCreateNodePoolInput'
    }

    attribute_map = {
        'auto_scaling': 'AutoScaling',
        'client_token': 'ClientToken',
        'cluster_id': 'ClusterId',
        'kubernetes_config': 'KubernetesConfig',
        'name': 'Name',
        'node_config': 'NodeConfig'
    }

    def __init__(self, auto_scaling=None, client_token=None, cluster_id=None, kubernetes_config=None, name=None, node_config=None, _configuration=None):  # noqa: E501
        """CreateNodePoolRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_scaling = None
        self._client_token = None
        self._cluster_id = None
        self._kubernetes_config = None
        self._name = None
        self._node_config = None
        self.discriminator = None

        if auto_scaling is not None:
            self.auto_scaling = auto_scaling
        if client_token is not None:
            self.client_token = client_token
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if kubernetes_config is not None:
            self.kubernetes_config = kubernetes_config
        if name is not None:
            self.name = name
        if node_config is not None:
            self.node_config = node_config

    @property
    def auto_scaling(self):
        """Gets the auto_scaling of this CreateNodePoolRequest.  # noqa: E501


        :return: The auto_scaling of this CreateNodePoolRequest.  # noqa: E501
        :rtype: AutoScalingForCreateNodePoolInput
        """
        return self._auto_scaling

    @auto_scaling.setter
    def auto_scaling(self, auto_scaling):
        """Sets the auto_scaling of this CreateNodePoolRequest.


        :param auto_scaling: The auto_scaling of this CreateNodePoolRequest.  # noqa: E501
        :type: AutoScalingForCreateNodePoolInput
        """

        self._auto_scaling = auto_scaling

    @property
    def client_token(self):
        """Gets the client_token of this CreateNodePoolRequest.  # noqa: E501


        :return: The client_token of this CreateNodePoolRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this CreateNodePoolRequest.


        :param client_token: The client_token of this CreateNodePoolRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def cluster_id(self):
        """Gets the cluster_id of this CreateNodePoolRequest.  # noqa: E501


        :return: The cluster_id of this CreateNodePoolRequest.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this CreateNodePoolRequest.


        :param cluster_id: The cluster_id of this CreateNodePoolRequest.  # noqa: E501
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def kubernetes_config(self):
        """Gets the kubernetes_config of this CreateNodePoolRequest.  # noqa: E501


        :return: The kubernetes_config of this CreateNodePoolRequest.  # noqa: E501
        :rtype: KubernetesConfigForCreateNodePoolInput
        """
        return self._kubernetes_config

    @kubernetes_config.setter
    def kubernetes_config(self, kubernetes_config):
        """Sets the kubernetes_config of this CreateNodePoolRequest.


        :param kubernetes_config: The kubernetes_config of this CreateNodePoolRequest.  # noqa: E501
        :type: KubernetesConfigForCreateNodePoolInput
        """

        self._kubernetes_config = kubernetes_config

    @property
    def name(self):
        """Gets the name of this CreateNodePoolRequest.  # noqa: E501


        :return: The name of this CreateNodePoolRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateNodePoolRequest.


        :param name: The name of this CreateNodePoolRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def node_config(self):
        """Gets the node_config of this CreateNodePoolRequest.  # noqa: E501


        :return: The node_config of this CreateNodePoolRequest.  # noqa: E501
        :rtype: NodeConfigForCreateNodePoolInput
        """
        return self._node_config

    @node_config.setter
    def node_config(self, node_config):
        """Sets the node_config of this CreateNodePoolRequest.


        :param node_config: The node_config of this CreateNodePoolRequest.  # noqa: E501
        :type: NodeConfigForCreateNodePoolInput
        """

        self._node_config = node_config

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
        if issubclass(CreateNodePoolRequest, dict):
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
        if not isinstance(other, CreateNodePoolRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateNodePoolRequest):
            return True

        return self.to_dict() != other.to_dict()
