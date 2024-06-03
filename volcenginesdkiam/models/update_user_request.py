# coding: utf-8

"""
    iam

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class UpdateUserRequest(object):
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
        'new_description': 'str',
        'new_display_name': 'str',
        'new_email': 'str',
        'new_mobile_phone': 'str',
        'new_user_name': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'new_description': 'NewDescription',
        'new_display_name': 'NewDisplayName',
        'new_email': 'NewEmail',
        'new_mobile_phone': 'NewMobilePhone',
        'new_user_name': 'NewUserName',
        'user_name': 'UserName'
    }

    def __init__(self, new_description=None, new_display_name=None, new_email=None, new_mobile_phone=None, new_user_name=None, user_name=None, _configuration=None):  # noqa: E501
        """UpdateUserRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._new_description = None
        self._new_display_name = None
        self._new_email = None
        self._new_mobile_phone = None
        self._new_user_name = None
        self._user_name = None
        self.discriminator = None

        if new_description is not None:
            self.new_description = new_description
        if new_display_name is not None:
            self.new_display_name = new_display_name
        if new_email is not None:
            self.new_email = new_email
        if new_mobile_phone is not None:
            self.new_mobile_phone = new_mobile_phone
        if new_user_name is not None:
            self.new_user_name = new_user_name
        self.user_name = user_name

    @property
    def new_description(self):
        """Gets the new_description of this UpdateUserRequest.  # noqa: E501


        :return: The new_description of this UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_description

    @new_description.setter
    def new_description(self, new_description):
        """Sets the new_description of this UpdateUserRequest.


        :param new_description: The new_description of this UpdateUserRequest.  # noqa: E501
        :type: str
        """

        self._new_description = new_description

    @property
    def new_display_name(self):
        """Gets the new_display_name of this UpdateUserRequest.  # noqa: E501


        :return: The new_display_name of this UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_display_name

    @new_display_name.setter
    def new_display_name(self, new_display_name):
        """Sets the new_display_name of this UpdateUserRequest.


        :param new_display_name: The new_display_name of this UpdateUserRequest.  # noqa: E501
        :type: str
        """

        self._new_display_name = new_display_name

    @property
    def new_email(self):
        """Gets the new_email of this UpdateUserRequest.  # noqa: E501


        :return: The new_email of this UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_email

    @new_email.setter
    def new_email(self, new_email):
        """Sets the new_email of this UpdateUserRequest.


        :param new_email: The new_email of this UpdateUserRequest.  # noqa: E501
        :type: str
        """

        self._new_email = new_email

    @property
    def new_mobile_phone(self):
        """Gets the new_mobile_phone of this UpdateUserRequest.  # noqa: E501


        :return: The new_mobile_phone of this UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_mobile_phone

    @new_mobile_phone.setter
    def new_mobile_phone(self, new_mobile_phone):
        """Sets the new_mobile_phone of this UpdateUserRequest.


        :param new_mobile_phone: The new_mobile_phone of this UpdateUserRequest.  # noqa: E501
        :type: str
        """

        self._new_mobile_phone = new_mobile_phone

    @property
    def new_user_name(self):
        """Gets the new_user_name of this UpdateUserRequest.  # noqa: E501


        :return: The new_user_name of this UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_user_name

    @new_user_name.setter
    def new_user_name(self, new_user_name):
        """Sets the new_user_name of this UpdateUserRequest.


        :param new_user_name: The new_user_name of this UpdateUserRequest.  # noqa: E501
        :type: str
        """

        self._new_user_name = new_user_name

    @property
    def user_name(self):
        """Gets the user_name of this UpdateUserRequest.  # noqa: E501


        :return: The user_name of this UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this UpdateUserRequest.


        :param user_name: The user_name of this UpdateUserRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and user_name is None:
            raise ValueError("Invalid value for `user_name`, must not be `None`")  # noqa: E501

        self._user_name = user_name

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
        if issubclass(UpdateUserRequest, dict):
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
        if not isinstance(other, UpdateUserRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateUserRequest):
            return True

        return self.to_dict() != other.to_dict()