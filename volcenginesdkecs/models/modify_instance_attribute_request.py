# coding: utf-8

"""
    ecs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ModifyInstanceAttributeRequest(object):
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
        'client_token': 'str',
        'description': 'str',
        'hostname': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'password': 'str',
        'user_data': 'str'
    }

    attribute_map = {
        'client_token': 'ClientToken',
        'description': 'Description',
        'hostname': 'Hostname',
        'instance_id': 'InstanceId',
        'instance_name': 'InstanceName',
        'password': 'Password',
        'user_data': 'UserData'
    }

    def __init__(self, client_token=None, description=None, hostname=None, instance_id=None, instance_name=None, password=None, user_data=None, _configuration=None):  # noqa: E501
        """ModifyInstanceAttributeRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_token = None
        self._description = None
        self._hostname = None
        self._instance_id = None
        self._instance_name = None
        self._password = None
        self._user_data = None
        self.discriminator = None

        if client_token is not None:
            self.client_token = client_token
        if description is not None:
            self.description = description
        if hostname is not None:
            self.hostname = hostname
        self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if password is not None:
            self.password = password
        if user_data is not None:
            self.user_data = user_data

    @property
    def client_token(self):
        """Gets the client_token of this ModifyInstanceAttributeRequest.  # noqa: E501


        :return: The client_token of this ModifyInstanceAttributeRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this ModifyInstanceAttributeRequest.


        :param client_token: The client_token of this ModifyInstanceAttributeRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def description(self):
        """Gets the description of this ModifyInstanceAttributeRequest.  # noqa: E501


        :return: The description of this ModifyInstanceAttributeRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModifyInstanceAttributeRequest.


        :param description: The description of this ModifyInstanceAttributeRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def hostname(self):
        """Gets the hostname of this ModifyInstanceAttributeRequest.  # noqa: E501


        :return: The hostname of this ModifyInstanceAttributeRequest.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this ModifyInstanceAttributeRequest.


        :param hostname: The hostname of this ModifyInstanceAttributeRequest.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def instance_id(self):
        """Gets the instance_id of this ModifyInstanceAttributeRequest.  # noqa: E501


        :return: The instance_id of this ModifyInstanceAttributeRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ModifyInstanceAttributeRequest.


        :param instance_id: The instance_id of this ModifyInstanceAttributeRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this ModifyInstanceAttributeRequest.  # noqa: E501


        :return: The instance_name of this ModifyInstanceAttributeRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this ModifyInstanceAttributeRequest.


        :param instance_name: The instance_name of this ModifyInstanceAttributeRequest.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def password(self):
        """Gets the password of this ModifyInstanceAttributeRequest.  # noqa: E501


        :return: The password of this ModifyInstanceAttributeRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ModifyInstanceAttributeRequest.


        :param password: The password of this ModifyInstanceAttributeRequest.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def user_data(self):
        """Gets the user_data of this ModifyInstanceAttributeRequest.  # noqa: E501


        :return: The user_data of this ModifyInstanceAttributeRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this ModifyInstanceAttributeRequest.


        :param user_data: The user_data of this ModifyInstanceAttributeRequest.  # noqa: E501
        :type: str
        """

        self._user_data = user_data

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
        if issubclass(ModifyInstanceAttributeRequest, dict):
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
        if not isinstance(other, ModifyInstanceAttributeRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyInstanceAttributeRequest):
            return True

        return self.to_dict() != other.to_dict()
