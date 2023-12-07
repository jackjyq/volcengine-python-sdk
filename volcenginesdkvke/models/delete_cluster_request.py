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


class DeleteClusterRequest(object):
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
        'force': 'bool',
        'id': 'str',
        'retain_resources': 'list[str]'
    }

    attribute_map = {
        'cascading_delete_resources': 'CascadingDeleteResources',
        'force': 'Force',
        'id': 'Id',
        'retain_resources': 'RetainResources'
    }

    def __init__(self, cascading_delete_resources=None, force=None, id=None, retain_resources=None, _configuration=None):  # noqa: E501
        """DeleteClusterRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cascading_delete_resources = None
        self._force = None
        self._id = None
        self._retain_resources = None
        self.discriminator = None

        if cascading_delete_resources is not None:
            self.cascading_delete_resources = cascading_delete_resources
        if force is not None:
            self.force = force
        self.id = id
        if retain_resources is not None:
            self.retain_resources = retain_resources

    @property
    def cascading_delete_resources(self):
        """Gets the cascading_delete_resources of this DeleteClusterRequest.  # noqa: E501


        :return: The cascading_delete_resources of this DeleteClusterRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._cascading_delete_resources

    @cascading_delete_resources.setter
    def cascading_delete_resources(self, cascading_delete_resources):
        """Sets the cascading_delete_resources of this DeleteClusterRequest.


        :param cascading_delete_resources: The cascading_delete_resources of this DeleteClusterRequest.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["DefaultNodePoolResource", "NodePoolResource", "Clb", "Nat", "TryBest"]  # noqa: E501
        if (self._configuration.client_side_validation and
                not set(cascading_delete_resources).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `cascading_delete_resources` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(cascading_delete_resources) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._cascading_delete_resources = cascading_delete_resources

    @property
    def force(self):
        """Gets the force of this DeleteClusterRequest.  # noqa: E501


        :return: The force of this DeleteClusterRequest.  # noqa: E501
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this DeleteClusterRequest.


        :param force: The force of this DeleteClusterRequest.  # noqa: E501
        :type: bool
        """

        self._force = force

    @property
    def id(self):
        """Gets the id of this DeleteClusterRequest.  # noqa: E501


        :return: The id of this DeleteClusterRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeleteClusterRequest.


        :param id: The id of this DeleteClusterRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def retain_resources(self):
        """Gets the retain_resources of this DeleteClusterRequest.  # noqa: E501


        :return: The retain_resources of this DeleteClusterRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._retain_resources

    @retain_resources.setter
    def retain_resources(self, retain_resources):
        """Sets the retain_resources of this DeleteClusterRequest.


        :param retain_resources: The retain_resources of this DeleteClusterRequest.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["DefaultNodePoolResource", "NodePoolResource", "Alb", "Clb", "Nat", "SecurityGroup", "All"]  # noqa: E501
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
        if issubclass(DeleteClusterRequest, dict):
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
        if not isinstance(other, DeleteClusterRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeleteClusterRequest):
            return True

        return self.to_dict() != other.to_dict()
