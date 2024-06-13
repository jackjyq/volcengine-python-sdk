# coding: utf-8

"""
    auto_scaling

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeScalingInstancesRequest(object):
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
        'creation_type': 'str',
        'instance_ids': 'list[str]',
        'page_number': 'int',
        'page_size': 'int',
        'scaling_configuration_id': 'str',
        'scaling_group_id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'creation_type': 'CreationType',
        'instance_ids': 'InstanceIds',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'scaling_configuration_id': 'ScalingConfigurationId',
        'scaling_group_id': 'ScalingGroupId',
        'status': 'Status'
    }

    def __init__(self, creation_type=None, instance_ids=None, page_number=None, page_size=None, scaling_configuration_id=None, scaling_group_id=None, status=None, _configuration=None):  # noqa: E501
        """DescribeScalingInstancesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._creation_type = None
        self._instance_ids = None
        self._page_number = None
        self._page_size = None
        self._scaling_configuration_id = None
        self._scaling_group_id = None
        self._status = None
        self.discriminator = None

        if creation_type is not None:
            self.creation_type = creation_type
        if instance_ids is not None:
            self.instance_ids = instance_ids
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if scaling_configuration_id is not None:
            self.scaling_configuration_id = scaling_configuration_id
        if scaling_group_id is not None:
            self.scaling_group_id = scaling_group_id
        if status is not None:
            self.status = status

    @property
    def creation_type(self):
        """Gets the creation_type of this DescribeScalingInstancesRequest.  # noqa: E501


        :return: The creation_type of this DescribeScalingInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._creation_type

    @creation_type.setter
    def creation_type(self, creation_type):
        """Sets the creation_type of this DescribeScalingInstancesRequest.


        :param creation_type: The creation_type of this DescribeScalingInstancesRequest.  # noqa: E501
        :type: str
        """

        self._creation_type = creation_type

    @property
    def instance_ids(self):
        """Gets the instance_ids of this DescribeScalingInstancesRequest.  # noqa: E501


        :return: The instance_ids of this DescribeScalingInstancesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        """Sets the instance_ids of this DescribeScalingInstancesRequest.


        :param instance_ids: The instance_ids of this DescribeScalingInstancesRequest.  # noqa: E501
        :type: list[str]
        """

        self._instance_ids = instance_ids

    @property
    def page_number(self):
        """Gets the page_number of this DescribeScalingInstancesRequest.  # noqa: E501


        :return: The page_number of this DescribeScalingInstancesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeScalingInstancesRequest.


        :param page_number: The page_number of this DescribeScalingInstancesRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeScalingInstancesRequest.  # noqa: E501


        :return: The page_size of this DescribeScalingInstancesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeScalingInstancesRequest.


        :param page_size: The page_size of this DescribeScalingInstancesRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                page_size is not None and page_size > 100):  # noqa: E501
            raise ValueError("Invalid value for `page_size`, must be a value less than or equal to `100`")  # noqa: E501
        if (self._configuration.client_side_validation and
                page_size is not None and page_size < 1):  # noqa: E501
            raise ValueError("Invalid value for `page_size`, must be a value greater than or equal to `1`")  # noqa: E501

        self._page_size = page_size

    @property
    def scaling_configuration_id(self):
        """Gets the scaling_configuration_id of this DescribeScalingInstancesRequest.  # noqa: E501


        :return: The scaling_configuration_id of this DescribeScalingInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._scaling_configuration_id

    @scaling_configuration_id.setter
    def scaling_configuration_id(self, scaling_configuration_id):
        """Sets the scaling_configuration_id of this DescribeScalingInstancesRequest.


        :param scaling_configuration_id: The scaling_configuration_id of this DescribeScalingInstancesRequest.  # noqa: E501
        :type: str
        """

        self._scaling_configuration_id = scaling_configuration_id

    @property
    def scaling_group_id(self):
        """Gets the scaling_group_id of this DescribeScalingInstancesRequest.  # noqa: E501


        :return: The scaling_group_id of this DescribeScalingInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._scaling_group_id

    @scaling_group_id.setter
    def scaling_group_id(self, scaling_group_id):
        """Sets the scaling_group_id of this DescribeScalingInstancesRequest.


        :param scaling_group_id: The scaling_group_id of this DescribeScalingInstancesRequest.  # noqa: E501
        :type: str
        """

        self._scaling_group_id = scaling_group_id

    @property
    def status(self):
        """Gets the status of this DescribeScalingInstancesRequest.  # noqa: E501


        :return: The status of this DescribeScalingInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DescribeScalingInstancesRequest.


        :param status: The status of this DescribeScalingInstancesRequest.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(DescribeScalingInstancesRequest, dict):
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
        if not isinstance(other, DescribeScalingInstancesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeScalingInstancesRequest):
            return True

        return self.to_dict() != other.to_dict()
