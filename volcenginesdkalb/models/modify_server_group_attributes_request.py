# coding: utf-8

"""
    alb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ModifyServerGroupAttributesRequest(object):
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
        'description': 'str',
        'health_check': 'HealthCheckForModifyServerGroupAttributesInput',
        'scheduler': 'str',
        'server_group_id': 'str',
        'server_group_name': 'str',
        'sticky_session_config': 'StickySessionConfigForModifyServerGroupAttributesInput'
    }

    attribute_map = {
        'description': 'Description',
        'health_check': 'HealthCheck',
        'scheduler': 'Scheduler',
        'server_group_id': 'ServerGroupId',
        'server_group_name': 'ServerGroupName',
        'sticky_session_config': 'StickySessionConfig'
    }

    def __init__(self, description=None, health_check=None, scheduler=None, server_group_id=None, server_group_name=None, sticky_session_config=None, _configuration=None):  # noqa: E501
        """ModifyServerGroupAttributesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._health_check = None
        self._scheduler = None
        self._server_group_id = None
        self._server_group_name = None
        self._sticky_session_config = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if health_check is not None:
            self.health_check = health_check
        if scheduler is not None:
            self.scheduler = scheduler
        self.server_group_id = server_group_id
        if server_group_name is not None:
            self.server_group_name = server_group_name
        if sticky_session_config is not None:
            self.sticky_session_config = sticky_session_config

    @property
    def description(self):
        """Gets the description of this ModifyServerGroupAttributesRequest.  # noqa: E501


        :return: The description of this ModifyServerGroupAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModifyServerGroupAttributesRequest.


        :param description: The description of this ModifyServerGroupAttributesRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def health_check(self):
        """Gets the health_check of this ModifyServerGroupAttributesRequest.  # noqa: E501


        :return: The health_check of this ModifyServerGroupAttributesRequest.  # noqa: E501
        :rtype: HealthCheckForModifyServerGroupAttributesInput
        """
        return self._health_check

    @health_check.setter
    def health_check(self, health_check):
        """Sets the health_check of this ModifyServerGroupAttributesRequest.


        :param health_check: The health_check of this ModifyServerGroupAttributesRequest.  # noqa: E501
        :type: HealthCheckForModifyServerGroupAttributesInput
        """

        self._health_check = health_check

    @property
    def scheduler(self):
        """Gets the scheduler of this ModifyServerGroupAttributesRequest.  # noqa: E501


        :return: The scheduler of this ModifyServerGroupAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._scheduler

    @scheduler.setter
    def scheduler(self, scheduler):
        """Sets the scheduler of this ModifyServerGroupAttributesRequest.


        :param scheduler: The scheduler of this ModifyServerGroupAttributesRequest.  # noqa: E501
        :type: str
        """

        self._scheduler = scheduler

    @property
    def server_group_id(self):
        """Gets the server_group_id of this ModifyServerGroupAttributesRequest.  # noqa: E501


        :return: The server_group_id of this ModifyServerGroupAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        """Sets the server_group_id of this ModifyServerGroupAttributesRequest.


        :param server_group_id: The server_group_id of this ModifyServerGroupAttributesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and server_group_id is None:
            raise ValueError("Invalid value for `server_group_id`, must not be `None`")  # noqa: E501

        self._server_group_id = server_group_id

    @property
    def server_group_name(self):
        """Gets the server_group_name of this ModifyServerGroupAttributesRequest.  # noqa: E501


        :return: The server_group_name of this ModifyServerGroupAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._server_group_name

    @server_group_name.setter
    def server_group_name(self, server_group_name):
        """Sets the server_group_name of this ModifyServerGroupAttributesRequest.


        :param server_group_name: The server_group_name of this ModifyServerGroupAttributesRequest.  # noqa: E501
        :type: str
        """

        self._server_group_name = server_group_name

    @property
    def sticky_session_config(self):
        """Gets the sticky_session_config of this ModifyServerGroupAttributesRequest.  # noqa: E501


        :return: The sticky_session_config of this ModifyServerGroupAttributesRequest.  # noqa: E501
        :rtype: StickySessionConfigForModifyServerGroupAttributesInput
        """
        return self._sticky_session_config

    @sticky_session_config.setter
    def sticky_session_config(self, sticky_session_config):
        """Sets the sticky_session_config of this ModifyServerGroupAttributesRequest.


        :param sticky_session_config: The sticky_session_config of this ModifyServerGroupAttributesRequest.  # noqa: E501
        :type: StickySessionConfigForModifyServerGroupAttributesInput
        """

        self._sticky_session_config = sticky_session_config

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
        if issubclass(ModifyServerGroupAttributesRequest, dict):
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
        if not isinstance(other, ModifyServerGroupAttributesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyServerGroupAttributesRequest):
            return True

        return self.to_dict() != other.to_dict()
