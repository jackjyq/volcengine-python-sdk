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


class DeleteResourceTagsRequest(object):
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
        'resource_tags': 'list[ResourceTagForDeleteResourceTagsInput]',
        'resources': 'list[str]'
    }

    attribute_map = {
        'resource_tags': 'ResourceTags',
        'resources': 'Resources'
    }

    def __init__(self, resource_tags=None, resources=None, _configuration=None):  # noqa: E501
        """DeleteResourceTagsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._resource_tags = None
        self._resources = None
        self.discriminator = None

        if resource_tags is not None:
            self.resource_tags = resource_tags
        if resources is not None:
            self.resources = resources

    @property
    def resource_tags(self):
        """Gets the resource_tags of this DeleteResourceTagsRequest.  # noqa: E501


        :return: The resource_tags of this DeleteResourceTagsRequest.  # noqa: E501
        :rtype: list[ResourceTagForDeleteResourceTagsInput]
        """
        return self._resource_tags

    @resource_tags.setter
    def resource_tags(self, resource_tags):
        """Sets the resource_tags of this DeleteResourceTagsRequest.


        :param resource_tags: The resource_tags of this DeleteResourceTagsRequest.  # noqa: E501
        :type: list[ResourceTagForDeleteResourceTagsInput]
        """

        self._resource_tags = resource_tags

    @property
    def resources(self):
        """Gets the resources of this DeleteResourceTagsRequest.  # noqa: E501


        :return: The resources of this DeleteResourceTagsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this DeleteResourceTagsRequest.


        :param resources: The resources of this DeleteResourceTagsRequest.  # noqa: E501
        :type: list[str]
        """

        self._resources = resources

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
        if issubclass(DeleteResourceTagsRequest, dict):
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
        if not isinstance(other, DeleteResourceTagsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeleteResourceTagsRequest):
            return True

        return self.to_dict() != other.to_dict()
