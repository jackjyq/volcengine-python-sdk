# coding: utf-8

"""
    spark

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateProjectRequest(object):
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
        'authority_type': 'str',
        'description': 'str',
        'owner_account_id': 'str',
        'owner_id': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'project_type': 'str'
    }

    attribute_map = {
        'authority_type': 'AuthorityType',
        'description': 'Description',
        'owner_account_id': 'OwnerAccountId',
        'owner_id': 'OwnerId',
        'project_id': 'ProjectId',
        'project_name': 'ProjectName',
        'project_type': 'ProjectType'
    }

    def __init__(self, authority_type=None, description=None, owner_account_id=None, owner_id=None, project_id=None, project_name=None, project_type=None, _configuration=None):  # noqa: E501
        """CreateProjectRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._authority_type = None
        self._description = None
        self._owner_account_id = None
        self._owner_id = None
        self._project_id = None
        self._project_name = None
        self._project_type = None
        self.discriminator = None

        if authority_type is not None:
            self.authority_type = authority_type
        if description is not None:
            self.description = description
        if owner_account_id is not None:
            self.owner_account_id = owner_account_id
        if owner_id is not None:
            self.owner_id = owner_id
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if project_type is not None:
            self.project_type = project_type

    @property
    def authority_type(self):
        """Gets the authority_type of this CreateProjectRequest.  # noqa: E501


        :return: The authority_type of this CreateProjectRequest.  # noqa: E501
        :rtype: str
        """
        return self._authority_type

    @authority_type.setter
    def authority_type(self, authority_type):
        """Sets the authority_type of this CreateProjectRequest.


        :param authority_type: The authority_type of this CreateProjectRequest.  # noqa: E501
        :type: str
        """

        self._authority_type = authority_type

    @property
    def description(self):
        """Gets the description of this CreateProjectRequest.  # noqa: E501


        :return: The description of this CreateProjectRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateProjectRequest.


        :param description: The description of this CreateProjectRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def owner_account_id(self):
        """Gets the owner_account_id of this CreateProjectRequest.  # noqa: E501


        :return: The owner_account_id of this CreateProjectRequest.  # noqa: E501
        :rtype: str
        """
        return self._owner_account_id

    @owner_account_id.setter
    def owner_account_id(self, owner_account_id):
        """Sets the owner_account_id of this CreateProjectRequest.


        :param owner_account_id: The owner_account_id of this CreateProjectRequest.  # noqa: E501
        :type: str
        """

        self._owner_account_id = owner_account_id

    @property
    def owner_id(self):
        """Gets the owner_id of this CreateProjectRequest.  # noqa: E501


        :return: The owner_id of this CreateProjectRequest.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this CreateProjectRequest.


        :param owner_id: The owner_id of this CreateProjectRequest.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

    @property
    def project_id(self):
        """Gets the project_id of this CreateProjectRequest.  # noqa: E501


        :return: The project_id of this CreateProjectRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateProjectRequest.


        :param project_id: The project_id of this CreateProjectRequest.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this CreateProjectRequest.  # noqa: E501


        :return: The project_name of this CreateProjectRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this CreateProjectRequest.


        :param project_name: The project_name of this CreateProjectRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def project_type(self):
        """Gets the project_type of this CreateProjectRequest.  # noqa: E501


        :return: The project_type of this CreateProjectRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_type

    @project_type.setter
    def project_type(self, project_type):
        """Sets the project_type of this CreateProjectRequest.


        :param project_type: The project_type of this CreateProjectRequest.  # noqa: E501
        :type: str
        """

        self._project_type = project_type

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
        if issubclass(CreateProjectRequest, dict):
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
        if not isinstance(other, CreateProjectRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateProjectRequest):
            return True

        return self.to_dict() != other.to_dict()
