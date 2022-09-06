# coding: utf-8

"""
    vpc

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class SecurityGroupForDescribeSecurityGroupsOutput(object):
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
        'creation_time': 'str',
        'description': 'str',
        'project_name': 'str',
        'security_group_id': 'str',
        'security_group_name': 'str',
        'status': 'str',
        'tags': 'list[TagForDescribeSecurityGroupsOutput]',
        'type': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'creation_time': 'CreationTime',
        'description': 'Description',
        'project_name': 'ProjectName',
        'security_group_id': 'SecurityGroupId',
        'security_group_name': 'SecurityGroupName',
        'status': 'Status',
        'tags': 'Tags',
        'type': 'Type',
        'vpc_id': 'VpcId'
    }

    def __init__(self, creation_time=None, description=None, project_name=None, security_group_id=None, security_group_name=None, status=None, tags=None, type=None, vpc_id=None, _configuration=None):  # noqa: E501
        """SecurityGroupForDescribeSecurityGroupsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._creation_time = None
        self._description = None
        self._project_name = None
        self._security_group_id = None
        self._security_group_name = None
        self._status = None
        self._tags = None
        self._type = None
        self._vpc_id = None
        self.discriminator = None

        if creation_time is not None:
            self.creation_time = creation_time
        if description is not None:
            self.description = description
        if project_name is not None:
            self.project_name = project_name
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if security_group_name is not None:
            self.security_group_name = security_group_name
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if type is not None:
            self.type = type
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def creation_time(self):
        """Gets the creation_time of this SecurityGroupForDescribeSecurityGroupsOutput.  # noqa: E501


        :return: The creation_time of this SecurityGroupForDescribeSecurityGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this SecurityGroupForDescribeSecurityGroupsOutput.


        :param creation_time: The creation_time of this SecurityGroupForDescribeSecurityGroupsOutput.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def description(self):
        """Gets the description of this SecurityGroupForDescribeSecurityGroupsOutput.  # noqa: E501


        :return: The description of this SecurityGroupForDescribeSecurityGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SecurityGroupForDescribeSecurityGroupsOutput.


        :param description: The description of this SecurityGroupForDescribeSecurityGroupsOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def project_name(self):
        """Gets the project_name of this SecurityGroupForDescribeSecurityGroupsOutput.  # noqa: E501


        :return: The project_name of this SecurityGroupForDescribeSecurityGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this SecurityGroupForDescribeSecurityGroupsOutput.


        :param project_name: The project_name of this SecurityGroupForDescribeSecurityGroupsOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def security_group_id(self):
        """Gets the security_group_id of this SecurityGroupForDescribeSecurityGroupsOutput.  # noqa: E501


        :return: The security_group_id of this SecurityGroupForDescribeSecurityGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this SecurityGroupForDescribeSecurityGroupsOutput.


        :param security_group_id: The security_group_id of this SecurityGroupForDescribeSecurityGroupsOutput.  # noqa: E501
        :type: str
        """

        self._security_group_id = security_group_id

    @property
    def security_group_name(self):
        """Gets the security_group_name of this SecurityGroupForDescribeSecurityGroupsOutput.  # noqa: E501


        :return: The security_group_name of this SecurityGroupForDescribeSecurityGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._security_group_name

    @security_group_name.setter
    def security_group_name(self, security_group_name):
        """Sets the security_group_name of this SecurityGroupForDescribeSecurityGroupsOutput.


        :param security_group_name: The security_group_name of this SecurityGroupForDescribeSecurityGroupsOutput.  # noqa: E501
        :type: str
        """

        self._security_group_name = security_group_name

    @property
    def status(self):
        """Gets the status of this SecurityGroupForDescribeSecurityGroupsOutput.  # noqa: E501


        :return: The status of this SecurityGroupForDescribeSecurityGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SecurityGroupForDescribeSecurityGroupsOutput.


        :param status: The status of this SecurityGroupForDescribeSecurityGroupsOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this SecurityGroupForDescribeSecurityGroupsOutput.  # noqa: E501


        :return: The tags of this SecurityGroupForDescribeSecurityGroupsOutput.  # noqa: E501
        :rtype: list[TagForDescribeSecurityGroupsOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SecurityGroupForDescribeSecurityGroupsOutput.


        :param tags: The tags of this SecurityGroupForDescribeSecurityGroupsOutput.  # noqa: E501
        :type: list[TagForDescribeSecurityGroupsOutput]
        """

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this SecurityGroupForDescribeSecurityGroupsOutput.  # noqa: E501


        :return: The type of this SecurityGroupForDescribeSecurityGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SecurityGroupForDescribeSecurityGroupsOutput.


        :param type: The type of this SecurityGroupForDescribeSecurityGroupsOutput.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def vpc_id(self):
        """Gets the vpc_id of this SecurityGroupForDescribeSecurityGroupsOutput.  # noqa: E501


        :return: The vpc_id of this SecurityGroupForDescribeSecurityGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this SecurityGroupForDescribeSecurityGroupsOutput.


        :param vpc_id: The vpc_id of this SecurityGroupForDescribeSecurityGroupsOutput.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

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
        if issubclass(SecurityGroupForDescribeSecurityGroupsOutput, dict):
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
        if not isinstance(other, SecurityGroupForDescribeSecurityGroupsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SecurityGroupForDescribeSecurityGroupsOutput):
            return True

        return self.to_dict() != other.to_dict()
