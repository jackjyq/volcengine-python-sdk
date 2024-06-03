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


class ModifyPlannedEventExecuteTimeRequest(object):
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
        'event_id': 'str',
        'modify_begin_time': 'str',
        'modify_end_time': 'str'
    }

    attribute_map = {
        'event_id': 'EventId',
        'modify_begin_time': 'ModifyBeginTime',
        'modify_end_time': 'ModifyEndTime'
    }

    def __init__(self, event_id=None, modify_begin_time=None, modify_end_time=None, _configuration=None):  # noqa: E501
        """ModifyPlannedEventExecuteTimeRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._event_id = None
        self._modify_begin_time = None
        self._modify_end_time = None
        self.discriminator = None

        self.event_id = event_id
        self.modify_begin_time = modify_begin_time
        self.modify_end_time = modify_end_time

    @property
    def event_id(self):
        """Gets the event_id of this ModifyPlannedEventExecuteTimeRequest.  # noqa: E501


        :return: The event_id of this ModifyPlannedEventExecuteTimeRequest.  # noqa: E501
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this ModifyPlannedEventExecuteTimeRequest.


        :param event_id: The event_id of this ModifyPlannedEventExecuteTimeRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and event_id is None:
            raise ValueError("Invalid value for `event_id`, must not be `None`")  # noqa: E501

        self._event_id = event_id

    @property
    def modify_begin_time(self):
        """Gets the modify_begin_time of this ModifyPlannedEventExecuteTimeRequest.  # noqa: E501


        :return: The modify_begin_time of this ModifyPlannedEventExecuteTimeRequest.  # noqa: E501
        :rtype: str
        """
        return self._modify_begin_time

    @modify_begin_time.setter
    def modify_begin_time(self, modify_begin_time):
        """Sets the modify_begin_time of this ModifyPlannedEventExecuteTimeRequest.


        :param modify_begin_time: The modify_begin_time of this ModifyPlannedEventExecuteTimeRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and modify_begin_time is None:
            raise ValueError("Invalid value for `modify_begin_time`, must not be `None`")  # noqa: E501

        self._modify_begin_time = modify_begin_time

    @property
    def modify_end_time(self):
        """Gets the modify_end_time of this ModifyPlannedEventExecuteTimeRequest.  # noqa: E501


        :return: The modify_end_time of this ModifyPlannedEventExecuteTimeRequest.  # noqa: E501
        :rtype: str
        """
        return self._modify_end_time

    @modify_end_time.setter
    def modify_end_time(self, modify_end_time):
        """Sets the modify_end_time of this ModifyPlannedEventExecuteTimeRequest.


        :param modify_end_time: The modify_end_time of this ModifyPlannedEventExecuteTimeRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and modify_end_time is None:
            raise ValueError("Invalid value for `modify_end_time`, must not be `None`")  # noqa: E501

        self._modify_end_time = modify_end_time

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
        if issubclass(ModifyPlannedEventExecuteTimeRequest, dict):
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
        if not isinstance(other, ModifyPlannedEventExecuteTimeRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyPlannedEventExecuteTimeRequest):
            return True

        return self.to_dict() != other.to_dict()