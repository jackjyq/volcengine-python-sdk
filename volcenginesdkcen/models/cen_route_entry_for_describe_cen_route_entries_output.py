# coding: utf-8

"""
    cen

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CenRouteEntryForDescribeCenRouteEntriesOutput(object):
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
        'as_path': 'list[str]',
        'cen_id': 'str',
        'destination_cidr_block': 'str',
        'instance_id': 'str',
        'instance_region_id': 'str',
        'instance_type': 'str',
        'publish_status': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'as_path': 'AsPath',
        'cen_id': 'CenId',
        'destination_cidr_block': 'DestinationCidrBlock',
        'instance_id': 'InstanceId',
        'instance_region_id': 'InstanceRegionId',
        'instance_type': 'InstanceType',
        'publish_status': 'PublishStatus',
        'status': 'Status',
        'type': 'Type'
    }

    def __init__(self, as_path=None, cen_id=None, destination_cidr_block=None, instance_id=None, instance_region_id=None, instance_type=None, publish_status=None, status=None, type=None, _configuration=None):  # noqa: E501
        """CenRouteEntryForDescribeCenRouteEntriesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._as_path = None
        self._cen_id = None
        self._destination_cidr_block = None
        self._instance_id = None
        self._instance_region_id = None
        self._instance_type = None
        self._publish_status = None
        self._status = None
        self._type = None
        self.discriminator = None

        if as_path is not None:
            self.as_path = as_path
        if cen_id is not None:
            self.cen_id = cen_id
        if destination_cidr_block is not None:
            self.destination_cidr_block = destination_cidr_block
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_region_id is not None:
            self.instance_region_id = instance_region_id
        if instance_type is not None:
            self.instance_type = instance_type
        if publish_status is not None:
            self.publish_status = publish_status
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type

    @property
    def as_path(self):
        """Gets the as_path of this CenRouteEntryForDescribeCenRouteEntriesOutput.  # noqa: E501


        :return: The as_path of this CenRouteEntryForDescribeCenRouteEntriesOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._as_path

    @as_path.setter
    def as_path(self, as_path):
        """Sets the as_path of this CenRouteEntryForDescribeCenRouteEntriesOutput.


        :param as_path: The as_path of this CenRouteEntryForDescribeCenRouteEntriesOutput.  # noqa: E501
        :type: list[str]
        """

        self._as_path = as_path

    @property
    def cen_id(self):
        """Gets the cen_id of this CenRouteEntryForDescribeCenRouteEntriesOutput.  # noqa: E501


        :return: The cen_id of this CenRouteEntryForDescribeCenRouteEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._cen_id

    @cen_id.setter
    def cen_id(self, cen_id):
        """Sets the cen_id of this CenRouteEntryForDescribeCenRouteEntriesOutput.


        :param cen_id: The cen_id of this CenRouteEntryForDescribeCenRouteEntriesOutput.  # noqa: E501
        :type: str
        """

        self._cen_id = cen_id

    @property
    def destination_cidr_block(self):
        """Gets the destination_cidr_block of this CenRouteEntryForDescribeCenRouteEntriesOutput.  # noqa: E501


        :return: The destination_cidr_block of this CenRouteEntryForDescribeCenRouteEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._destination_cidr_block

    @destination_cidr_block.setter
    def destination_cidr_block(self, destination_cidr_block):
        """Sets the destination_cidr_block of this CenRouteEntryForDescribeCenRouteEntriesOutput.


        :param destination_cidr_block: The destination_cidr_block of this CenRouteEntryForDescribeCenRouteEntriesOutput.  # noqa: E501
        :type: str
        """

        self._destination_cidr_block = destination_cidr_block

    @property
    def instance_id(self):
        """Gets the instance_id of this CenRouteEntryForDescribeCenRouteEntriesOutput.  # noqa: E501


        :return: The instance_id of this CenRouteEntryForDescribeCenRouteEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CenRouteEntryForDescribeCenRouteEntriesOutput.


        :param instance_id: The instance_id of this CenRouteEntryForDescribeCenRouteEntriesOutput.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def instance_region_id(self):
        """Gets the instance_region_id of this CenRouteEntryForDescribeCenRouteEntriesOutput.  # noqa: E501


        :return: The instance_region_id of this CenRouteEntryForDescribeCenRouteEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_region_id

    @instance_region_id.setter
    def instance_region_id(self, instance_region_id):
        """Sets the instance_region_id of this CenRouteEntryForDescribeCenRouteEntriesOutput.


        :param instance_region_id: The instance_region_id of this CenRouteEntryForDescribeCenRouteEntriesOutput.  # noqa: E501
        :type: str
        """

        self._instance_region_id = instance_region_id

    @property
    def instance_type(self):
        """Gets the instance_type of this CenRouteEntryForDescribeCenRouteEntriesOutput.  # noqa: E501


        :return: The instance_type of this CenRouteEntryForDescribeCenRouteEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this CenRouteEntryForDescribeCenRouteEntriesOutput.


        :param instance_type: The instance_type of this CenRouteEntryForDescribeCenRouteEntriesOutput.  # noqa: E501
        :type: str
        """

        self._instance_type = instance_type

    @property
    def publish_status(self):
        """Gets the publish_status of this CenRouteEntryForDescribeCenRouteEntriesOutput.  # noqa: E501


        :return: The publish_status of this CenRouteEntryForDescribeCenRouteEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._publish_status

    @publish_status.setter
    def publish_status(self, publish_status):
        """Sets the publish_status of this CenRouteEntryForDescribeCenRouteEntriesOutput.


        :param publish_status: The publish_status of this CenRouteEntryForDescribeCenRouteEntriesOutput.  # noqa: E501
        :type: str
        """

        self._publish_status = publish_status

    @property
    def status(self):
        """Gets the status of this CenRouteEntryForDescribeCenRouteEntriesOutput.  # noqa: E501


        :return: The status of this CenRouteEntryForDescribeCenRouteEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CenRouteEntryForDescribeCenRouteEntriesOutput.


        :param status: The status of this CenRouteEntryForDescribeCenRouteEntriesOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this CenRouteEntryForDescribeCenRouteEntriesOutput.  # noqa: E501


        :return: The type of this CenRouteEntryForDescribeCenRouteEntriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CenRouteEntryForDescribeCenRouteEntriesOutput.


        :param type: The type of this CenRouteEntryForDescribeCenRouteEntriesOutput.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(CenRouteEntryForDescribeCenRouteEntriesOutput, dict):
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
        if not isinstance(other, CenRouteEntryForDescribeCenRouteEntriesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CenRouteEntryForDescribeCenRouteEntriesOutput):
            return True

        return self.to_dict() != other.to_dict()
