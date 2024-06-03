# coding: utf-8

"""
    rds_postgresql

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class SchemaForDescribeSchemasOutput(object):
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
        'db_name': 'str',
        'owner': 'str',
        'schema_name': 'str'
    }

    attribute_map = {
        'db_name': 'DBName',
        'owner': 'Owner',
        'schema_name': 'SchemaName'
    }

    def __init__(self, db_name=None, owner=None, schema_name=None, _configuration=None):  # noqa: E501
        """SchemaForDescribeSchemasOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._db_name = None
        self._owner = None
        self._schema_name = None
        self.discriminator = None

        if db_name is not None:
            self.db_name = db_name
        if owner is not None:
            self.owner = owner
        if schema_name is not None:
            self.schema_name = schema_name

    @property
    def db_name(self):
        """Gets the db_name of this SchemaForDescribeSchemasOutput.  # noqa: E501


        :return: The db_name of this SchemaForDescribeSchemasOutput.  # noqa: E501
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this SchemaForDescribeSchemasOutput.


        :param db_name: The db_name of this SchemaForDescribeSchemasOutput.  # noqa: E501
        :type: str
        """

        self._db_name = db_name

    @property
    def owner(self):
        """Gets the owner of this SchemaForDescribeSchemasOutput.  # noqa: E501


        :return: The owner of this SchemaForDescribeSchemasOutput.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this SchemaForDescribeSchemasOutput.


        :param owner: The owner of this SchemaForDescribeSchemasOutput.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def schema_name(self):
        """Gets the schema_name of this SchemaForDescribeSchemasOutput.  # noqa: E501


        :return: The schema_name of this SchemaForDescribeSchemasOutput.  # noqa: E501
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """Sets the schema_name of this SchemaForDescribeSchemasOutput.


        :param schema_name: The schema_name of this SchemaForDescribeSchemasOutput.  # noqa: E501
        :type: str
        """

        self._schema_name = schema_name

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
        if issubclass(SchemaForDescribeSchemasOutput, dict):
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
        if not isinstance(other, SchemaForDescribeSchemasOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SchemaForDescribeSchemasOutput):
            return True

        return self.to_dict() != other.to_dict()