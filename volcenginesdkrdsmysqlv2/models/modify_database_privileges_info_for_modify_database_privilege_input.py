# coding: utf-8

"""
    rds_mysql_v2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ModifyDatabasePrivilegesInfoForModifyDatabasePrivilegeInput(object):
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
        'account_name': 'str',
        'action_type': 'str',
        'privilege': 'str',
        'privilege_custom': 'str'
    }

    attribute_map = {
        'account_name': 'AccountName',
        'action_type': 'ActionType',
        'privilege': 'Privilege',
        'privilege_custom': 'PrivilegeCustom'
    }

    def __init__(self, account_name=None, action_type=None, privilege=None, privilege_custom=None, _configuration=None):  # noqa: E501
        """ModifyDatabasePrivilegesInfoForModifyDatabasePrivilegeInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_name = None
        self._action_type = None
        self._privilege = None
        self._privilege_custom = None
        self.discriminator = None

        if account_name is not None:
            self.account_name = account_name
        if action_type is not None:
            self.action_type = action_type
        if privilege is not None:
            self.privilege = privilege
        if privilege_custom is not None:
            self.privilege_custom = privilege_custom

    @property
    def account_name(self):
        """Gets the account_name of this ModifyDatabasePrivilegesInfoForModifyDatabasePrivilegeInput.  # noqa: E501


        :return: The account_name of this ModifyDatabasePrivilegesInfoForModifyDatabasePrivilegeInput.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this ModifyDatabasePrivilegesInfoForModifyDatabasePrivilegeInput.


        :param account_name: The account_name of this ModifyDatabasePrivilegesInfoForModifyDatabasePrivilegeInput.  # noqa: E501
        :type: str
        """

        self._account_name = account_name

    @property
    def action_type(self):
        """Gets the action_type of this ModifyDatabasePrivilegesInfoForModifyDatabasePrivilegeInput.  # noqa: E501


        :return: The action_type of this ModifyDatabasePrivilegesInfoForModifyDatabasePrivilegeInput.  # noqa: E501
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this ModifyDatabasePrivilegesInfoForModifyDatabasePrivilegeInput.


        :param action_type: The action_type of this ModifyDatabasePrivilegesInfoForModifyDatabasePrivilegeInput.  # noqa: E501
        :type: str
        """

        self._action_type = action_type

    @property
    def privilege(self):
        """Gets the privilege of this ModifyDatabasePrivilegesInfoForModifyDatabasePrivilegeInput.  # noqa: E501


        :return: The privilege of this ModifyDatabasePrivilegesInfoForModifyDatabasePrivilegeInput.  # noqa: E501
        :rtype: str
        """
        return self._privilege

    @privilege.setter
    def privilege(self, privilege):
        """Sets the privilege of this ModifyDatabasePrivilegesInfoForModifyDatabasePrivilegeInput.


        :param privilege: The privilege of this ModifyDatabasePrivilegesInfoForModifyDatabasePrivilegeInput.  # noqa: E501
        :type: str
        """

        self._privilege = privilege

    @property
    def privilege_custom(self):
        """Gets the privilege_custom of this ModifyDatabasePrivilegesInfoForModifyDatabasePrivilegeInput.  # noqa: E501


        :return: The privilege_custom of this ModifyDatabasePrivilegesInfoForModifyDatabasePrivilegeInput.  # noqa: E501
        :rtype: str
        """
        return self._privilege_custom

    @privilege_custom.setter
    def privilege_custom(self, privilege_custom):
        """Sets the privilege_custom of this ModifyDatabasePrivilegesInfoForModifyDatabasePrivilegeInput.


        :param privilege_custom: The privilege_custom of this ModifyDatabasePrivilegesInfoForModifyDatabasePrivilegeInput.  # noqa: E501
        :type: str
        """

        self._privilege_custom = privilege_custom

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
        if issubclass(ModifyDatabasePrivilegesInfoForModifyDatabasePrivilegeInput, dict):
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
        if not isinstance(other, ModifyDatabasePrivilegesInfoForModifyDatabasePrivilegeInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyDatabasePrivilegesInfoForModifyDatabasePrivilegeInput):
            return True

        return self.to_dict() != other.to_dict()
