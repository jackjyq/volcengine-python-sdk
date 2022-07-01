# coding: utf-8

"""
    auto_scaling

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ModifyLifecycleHookRequest(object):
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
        'lifecycle_hook_id': 'str',
        'lifecycle_hook_policy': 'str',
        'lifecycle_hook_timeout': 'int',
        'lifecycle_hook_type': 'str'
    }

    attribute_map = {
        'lifecycle_hook_id': 'LifecycleHookId',
        'lifecycle_hook_policy': 'LifecycleHookPolicy',
        'lifecycle_hook_timeout': 'LifecycleHookTimeout',
        'lifecycle_hook_type': 'LifecycleHookType'
    }

    def __init__(self, lifecycle_hook_id=None, lifecycle_hook_policy=None, lifecycle_hook_timeout=None, lifecycle_hook_type=None, _configuration=None):  # noqa: E501
        """ModifyLifecycleHookRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._lifecycle_hook_id = None
        self._lifecycle_hook_policy = None
        self._lifecycle_hook_timeout = None
        self._lifecycle_hook_type = None
        self.discriminator = None

        if lifecycle_hook_id is not None:
            self.lifecycle_hook_id = lifecycle_hook_id
        if lifecycle_hook_policy is not None:
            self.lifecycle_hook_policy = lifecycle_hook_policy
        if lifecycle_hook_timeout is not None:
            self.lifecycle_hook_timeout = lifecycle_hook_timeout
        if lifecycle_hook_type is not None:
            self.lifecycle_hook_type = lifecycle_hook_type

    @property
    def lifecycle_hook_id(self):
        """Gets the lifecycle_hook_id of this ModifyLifecycleHookRequest.  # noqa: E501


        :return: The lifecycle_hook_id of this ModifyLifecycleHookRequest.  # noqa: E501
        :rtype: str
        """
        return self._lifecycle_hook_id

    @lifecycle_hook_id.setter
    def lifecycle_hook_id(self, lifecycle_hook_id):
        """Sets the lifecycle_hook_id of this ModifyLifecycleHookRequest.


        :param lifecycle_hook_id: The lifecycle_hook_id of this ModifyLifecycleHookRequest.  # noqa: E501
        :type: str
        """

        self._lifecycle_hook_id = lifecycle_hook_id

    @property
    def lifecycle_hook_policy(self):
        """Gets the lifecycle_hook_policy of this ModifyLifecycleHookRequest.  # noqa: E501


        :return: The lifecycle_hook_policy of this ModifyLifecycleHookRequest.  # noqa: E501
        :rtype: str
        """
        return self._lifecycle_hook_policy

    @lifecycle_hook_policy.setter
    def lifecycle_hook_policy(self, lifecycle_hook_policy):
        """Sets the lifecycle_hook_policy of this ModifyLifecycleHookRequest.


        :param lifecycle_hook_policy: The lifecycle_hook_policy of this ModifyLifecycleHookRequest.  # noqa: E501
        :type: str
        """

        self._lifecycle_hook_policy = lifecycle_hook_policy

    @property
    def lifecycle_hook_timeout(self):
        """Gets the lifecycle_hook_timeout of this ModifyLifecycleHookRequest.  # noqa: E501


        :return: The lifecycle_hook_timeout of this ModifyLifecycleHookRequest.  # noqa: E501
        :rtype: int
        """
        return self._lifecycle_hook_timeout

    @lifecycle_hook_timeout.setter
    def lifecycle_hook_timeout(self, lifecycle_hook_timeout):
        """Sets the lifecycle_hook_timeout of this ModifyLifecycleHookRequest.


        :param lifecycle_hook_timeout: The lifecycle_hook_timeout of this ModifyLifecycleHookRequest.  # noqa: E501
        :type: int
        """

        self._lifecycle_hook_timeout = lifecycle_hook_timeout

    @property
    def lifecycle_hook_type(self):
        """Gets the lifecycle_hook_type of this ModifyLifecycleHookRequest.  # noqa: E501


        :return: The lifecycle_hook_type of this ModifyLifecycleHookRequest.  # noqa: E501
        :rtype: str
        """
        return self._lifecycle_hook_type

    @lifecycle_hook_type.setter
    def lifecycle_hook_type(self, lifecycle_hook_type):
        """Sets the lifecycle_hook_type of this ModifyLifecycleHookRequest.


        :param lifecycle_hook_type: The lifecycle_hook_type of this ModifyLifecycleHookRequest.  # noqa: E501
        :type: str
        """

        self._lifecycle_hook_type = lifecycle_hook_type

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
        if issubclass(ModifyLifecycleHookRequest, dict):
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
        if not isinstance(other, ModifyLifecycleHookRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyLifecycleHookRequest):
            return True

        return self.to_dict() != other.to_dict()