# coding: utf-8

"""
    filenas

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class PermissionRuleForUpdatePermissionRuleInput(object):
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
        'cidr_ip': 'str',
        'permission_rule_id': 'str',
        'rw_mode': 'str',
        'user_mode': 'str'
    }

    attribute_map = {
        'cidr_ip': 'CidrIp',
        'permission_rule_id': 'PermissionRuleId',
        'rw_mode': 'RwMode',
        'user_mode': 'UserMode'
    }

    def __init__(self, cidr_ip=None, permission_rule_id=None, rw_mode=None, user_mode=None, _configuration=None):  # noqa: E501
        """PermissionRuleForUpdatePermissionRuleInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cidr_ip = None
        self._permission_rule_id = None
        self._rw_mode = None
        self._user_mode = None
        self.discriminator = None

        if cidr_ip is not None:
            self.cidr_ip = cidr_ip
        if permission_rule_id is not None:
            self.permission_rule_id = permission_rule_id
        if rw_mode is not None:
            self.rw_mode = rw_mode
        if user_mode is not None:
            self.user_mode = user_mode

    @property
    def cidr_ip(self):
        """Gets the cidr_ip of this PermissionRuleForUpdatePermissionRuleInput.  # noqa: E501


        :return: The cidr_ip of this PermissionRuleForUpdatePermissionRuleInput.  # noqa: E501
        :rtype: str
        """
        return self._cidr_ip

    @cidr_ip.setter
    def cidr_ip(self, cidr_ip):
        """Sets the cidr_ip of this PermissionRuleForUpdatePermissionRuleInput.


        :param cidr_ip: The cidr_ip of this PermissionRuleForUpdatePermissionRuleInput.  # noqa: E501
        :type: str
        """

        self._cidr_ip = cidr_ip

    @property
    def permission_rule_id(self):
        """Gets the permission_rule_id of this PermissionRuleForUpdatePermissionRuleInput.  # noqa: E501


        :return: The permission_rule_id of this PermissionRuleForUpdatePermissionRuleInput.  # noqa: E501
        :rtype: str
        """
        return self._permission_rule_id

    @permission_rule_id.setter
    def permission_rule_id(self, permission_rule_id):
        """Sets the permission_rule_id of this PermissionRuleForUpdatePermissionRuleInput.


        :param permission_rule_id: The permission_rule_id of this PermissionRuleForUpdatePermissionRuleInput.  # noqa: E501
        :type: str
        """

        self._permission_rule_id = permission_rule_id

    @property
    def rw_mode(self):
        """Gets the rw_mode of this PermissionRuleForUpdatePermissionRuleInput.  # noqa: E501


        :return: The rw_mode of this PermissionRuleForUpdatePermissionRuleInput.  # noqa: E501
        :rtype: str
        """
        return self._rw_mode

    @rw_mode.setter
    def rw_mode(self, rw_mode):
        """Sets the rw_mode of this PermissionRuleForUpdatePermissionRuleInput.


        :param rw_mode: The rw_mode of this PermissionRuleForUpdatePermissionRuleInput.  # noqa: E501
        :type: str
        """

        self._rw_mode = rw_mode

    @property
    def user_mode(self):
        """Gets the user_mode of this PermissionRuleForUpdatePermissionRuleInput.  # noqa: E501


        :return: The user_mode of this PermissionRuleForUpdatePermissionRuleInput.  # noqa: E501
        :rtype: str
        """
        return self._user_mode

    @user_mode.setter
    def user_mode(self, user_mode):
        """Sets the user_mode of this PermissionRuleForUpdatePermissionRuleInput.


        :param user_mode: The user_mode of this PermissionRuleForUpdatePermissionRuleInput.  # noqa: E501
        :type: str
        """

        self._user_mode = user_mode

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
        if issubclass(PermissionRuleForUpdatePermissionRuleInput, dict):
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
        if not isinstance(other, PermissionRuleForUpdatePermissionRuleInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PermissionRuleForUpdatePermissionRuleInput):
            return True

        return self.to_dict() != other.to_dict()
