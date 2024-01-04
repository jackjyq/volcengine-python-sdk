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


class CreateCenServiceRouteEntryRequest(object):
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
        'cen_id': 'str',
        'description': 'str',
        'destination_cidr_block': 'str',
        'publish_mode': 'str',
        'publish_to_instances': 'list[PublishToInstanceForCreateCenServiceRouteEntryInput]',
        'service_region_id': 'str',
        'service_vpc_id': 'str'
    }

    attribute_map = {
        'cen_id': 'CenId',
        'description': 'Description',
        'destination_cidr_block': 'DestinationCidrBlock',
        'publish_mode': 'PublishMode',
        'publish_to_instances': 'PublishToInstances',
        'service_region_id': 'ServiceRegionId',
        'service_vpc_id': 'ServiceVpcId'
    }

    def __init__(self, cen_id=None, description=None, destination_cidr_block=None, publish_mode=None, publish_to_instances=None, service_region_id=None, service_vpc_id=None, _configuration=None):  # noqa: E501
        """CreateCenServiceRouteEntryRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cen_id = None
        self._description = None
        self._destination_cidr_block = None
        self._publish_mode = None
        self._publish_to_instances = None
        self._service_region_id = None
        self._service_vpc_id = None
        self.discriminator = None

        self.cen_id = cen_id
        if description is not None:
            self.description = description
        self.destination_cidr_block = destination_cidr_block
        if publish_mode is not None:
            self.publish_mode = publish_mode
        if publish_to_instances is not None:
            self.publish_to_instances = publish_to_instances
        self.service_region_id = service_region_id
        self.service_vpc_id = service_vpc_id

    @property
    def cen_id(self):
        """Gets the cen_id of this CreateCenServiceRouteEntryRequest.  # noqa: E501


        :return: The cen_id of this CreateCenServiceRouteEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._cen_id

    @cen_id.setter
    def cen_id(self, cen_id):
        """Sets the cen_id of this CreateCenServiceRouteEntryRequest.


        :param cen_id: The cen_id of this CreateCenServiceRouteEntryRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and cen_id is None:
            raise ValueError("Invalid value for `cen_id`, must not be `None`")  # noqa: E501

        self._cen_id = cen_id

    @property
    def description(self):
        """Gets the description of this CreateCenServiceRouteEntryRequest.  # noqa: E501


        :return: The description of this CreateCenServiceRouteEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateCenServiceRouteEntryRequest.


        :param description: The description of this CreateCenServiceRouteEntryRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def destination_cidr_block(self):
        """Gets the destination_cidr_block of this CreateCenServiceRouteEntryRequest.  # noqa: E501


        :return: The destination_cidr_block of this CreateCenServiceRouteEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._destination_cidr_block

    @destination_cidr_block.setter
    def destination_cidr_block(self, destination_cidr_block):
        """Sets the destination_cidr_block of this CreateCenServiceRouteEntryRequest.


        :param destination_cidr_block: The destination_cidr_block of this CreateCenServiceRouteEntryRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and destination_cidr_block is None:
            raise ValueError("Invalid value for `destination_cidr_block`, must not be `None`")  # noqa: E501

        self._destination_cidr_block = destination_cidr_block

    @property
    def publish_mode(self):
        """Gets the publish_mode of this CreateCenServiceRouteEntryRequest.  # noqa: E501


        :return: The publish_mode of this CreateCenServiceRouteEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._publish_mode

    @publish_mode.setter
    def publish_mode(self, publish_mode):
        """Sets the publish_mode of this CreateCenServiceRouteEntryRequest.


        :param publish_mode: The publish_mode of this CreateCenServiceRouteEntryRequest.  # noqa: E501
        :type: str
        """

        self._publish_mode = publish_mode

    @property
    def publish_to_instances(self):
        """Gets the publish_to_instances of this CreateCenServiceRouteEntryRequest.  # noqa: E501


        :return: The publish_to_instances of this CreateCenServiceRouteEntryRequest.  # noqa: E501
        :rtype: list[PublishToInstanceForCreateCenServiceRouteEntryInput]
        """
        return self._publish_to_instances

    @publish_to_instances.setter
    def publish_to_instances(self, publish_to_instances):
        """Sets the publish_to_instances of this CreateCenServiceRouteEntryRequest.


        :param publish_to_instances: The publish_to_instances of this CreateCenServiceRouteEntryRequest.  # noqa: E501
        :type: list[PublishToInstanceForCreateCenServiceRouteEntryInput]
        """

        self._publish_to_instances = publish_to_instances

    @property
    def service_region_id(self):
        """Gets the service_region_id of this CreateCenServiceRouteEntryRequest.  # noqa: E501


        :return: The service_region_id of this CreateCenServiceRouteEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._service_region_id

    @service_region_id.setter
    def service_region_id(self, service_region_id):
        """Sets the service_region_id of this CreateCenServiceRouteEntryRequest.


        :param service_region_id: The service_region_id of this CreateCenServiceRouteEntryRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and service_region_id is None:
            raise ValueError("Invalid value for `service_region_id`, must not be `None`")  # noqa: E501

        self._service_region_id = service_region_id

    @property
    def service_vpc_id(self):
        """Gets the service_vpc_id of this CreateCenServiceRouteEntryRequest.  # noqa: E501


        :return: The service_vpc_id of this CreateCenServiceRouteEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._service_vpc_id

    @service_vpc_id.setter
    def service_vpc_id(self, service_vpc_id):
        """Sets the service_vpc_id of this CreateCenServiceRouteEntryRequest.


        :param service_vpc_id: The service_vpc_id of this CreateCenServiceRouteEntryRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and service_vpc_id is None:
            raise ValueError("Invalid value for `service_vpc_id`, must not be `None`")  # noqa: E501

        self._service_vpc_id = service_vpc_id

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
        if issubclass(CreateCenServiceRouteEntryRequest, dict):
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
        if not isinstance(other, CreateCenServiceRouteEntryRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateCenServiceRouteEntryRequest):
            return True

        return self.to_dict() != other.to_dict()
