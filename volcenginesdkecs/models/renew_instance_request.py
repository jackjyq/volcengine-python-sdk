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


class RenewInstanceRequest(object):
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
        'instance_id': 'str',
        'period': 'int',
        'period_unit': 'str'
    }

    attribute_map = {
        'client_token': 'ClientToken',
        'instance_id': 'InstanceId',
        'period': 'Period',
        'period_unit': 'PeriodUnit'
    }

    def __init__(self, client_token=None, instance_id=None, period=None, period_unit=None, _configuration=None):  # noqa: E501
        """RenewInstanceRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_token = None
        self._instance_id = None
        self._period = None
        self._period_unit = None
        self.discriminator = None

        if client_token is not None:
            self.client_token = client_token
        if instance_id is not None:
            self.instance_id = instance_id
        if period is not None:
            self.period = period
        if period_unit is not None:
            self.period_unit = period_unit

    @property
    def client_token(self):
        """Gets the client_token of this RenewInstanceRequest.  # noqa: E501


        :return: The client_token of this RenewInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this RenewInstanceRequest.


        :param client_token: The client_token of this RenewInstanceRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def instance_id(self):
        """Gets the instance_id of this RenewInstanceRequest.  # noqa: E501


        :return: The instance_id of this RenewInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this RenewInstanceRequest.


        :param instance_id: The instance_id of this RenewInstanceRequest.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def period(self):
        """Gets the period of this RenewInstanceRequest.  # noqa: E501


        :return: The period of this RenewInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this RenewInstanceRequest.


        :param period: The period of this RenewInstanceRequest.  # noqa: E501
        :type: int
        """

        self._period = period

    @property
    def period_unit(self):
        """Gets the period_unit of this RenewInstanceRequest.  # noqa: E501


        :return: The period_unit of this RenewInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._period_unit

    @period_unit.setter
    def period_unit(self, period_unit):
        """Sets the period_unit of this RenewInstanceRequest.


        :param period_unit: The period_unit of this RenewInstanceRequest.  # noqa: E501
        :type: str
        """

        self._period_unit = period_unit

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
        if issubclass(RenewInstanceRequest, dict):
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
        if not isinstance(other, RenewInstanceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RenewInstanceRequest):
            return True

        return self.to_dict() != other.to_dict()
