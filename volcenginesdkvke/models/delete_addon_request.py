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


class DeleteAddonRequest(object):
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
        'cascading_delete_resources': 'list[str]',
        'cluster_id': 'str',
        'name': 'str',
        'retain_resources': 'list[str]'
    }

    attribute_map = {
        'cascading_delete_resources': 'CascadingDeleteResources',
        'cluster_id': 'ClusterId',
        'name': 'Name',
        'retain_resources': 'RetainResources'
    }

    def __init__(self, cascading_delete_resources=None, cluster_id=None, name=None, retain_resources=None, _configuration=None):  # noqa: E501
        """DeleteAddonRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cascading_delete_resources = None
        self._cluster_id = None
        self._name = None
        self._retain_resources = None
        self.discriminator = None

        if cascading_delete_resources is not None:
            self.cascading_delete_resources = cascading_delete_resources
        self.cluster_id = cluster_id
        self.name = name
        if retain_resources is not None:
            self.retain_resources = retain_resources

    @property
    def cascading_delete_resources(self):
        """Gets the cascading_delete_resources of this DeleteAddonRequest.  # noqa: E501


        :return: The cascading_delete_resources of this DeleteAddonRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._cascading_delete_resources

    @cascading_delete_resources.setter
    def cascading_delete_resources(self, cascading_delete_resources):
        """Sets the cascading_delete_resources of this DeleteAddonRequest.


        :param cascading_delete_resources: The cascading_delete_resources of this DeleteAddonRequest.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Crd"]  # noqa: E501
        if (self._configuration.client_side_validation and
                not set(cascading_delete_resources).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `cascading_delete_resources` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(cascading_delete_resources) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._cascading_delete_resources = cascading_delete_resources

    @property
    def cluster_id(self):
        """Gets the cluster_id of this DeleteAddonRequest.  # noqa: E501


        :return: The cluster_id of this DeleteAddonRequest.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this DeleteAddonRequest.


        :param cluster_id: The cluster_id of this DeleteAddonRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and cluster_id is None:
            raise ValueError("Invalid value for `cluster_id`, must not be `None`")  # noqa: E501

        self._cluster_id = cluster_id

    @property
    def name(self):
        """Gets the name of this DeleteAddonRequest.  # noqa: E501


        :return: The name of this DeleteAddonRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeleteAddonRequest.


        :param name: The name of this DeleteAddonRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def retain_resources(self):
        """Gets the retain_resources of this DeleteAddonRequest.  # noqa: E501


        :return: The retain_resources of this DeleteAddonRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._retain_resources

    @retain_resources.setter
    def retain_resources(self, retain_resources):
        """Sets the retain_resources of this DeleteAddonRequest.


        :param retain_resources: The retain_resources of this DeleteAddonRequest.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Crd"]  # noqa: E501
        if (self._configuration.client_side_validation and
                not set(retain_resources).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `retain_resources` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(retain_resources) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._retain_resources = retain_resources

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
        if issubclass(DeleteAddonRequest, dict):
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
        if not isinstance(other, DeleteAddonRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeleteAddonRequest):
            return True

        return self.to_dict() != other.to_dict()
