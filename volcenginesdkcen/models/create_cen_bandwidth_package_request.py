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


class CreateCenBandwidthPackageRequest(object):
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
        'bandwidth': 'int',
        'billing_type': 'int',
        'cen_bandwidth_package_name': 'str',
        'cen_id': 'str',
        'client_token': 'str',
        'description': 'str',
        'local_geographic_region_set_id': 'str',
        'peer_geographic_region_set_id': 'str',
        'period': 'int',
        'period_unit': 'str',
        'project_name': 'str',
        'tags': 'list[TagForCreateCenBandwidthPackageInput]'
    }

    attribute_map = {
        'bandwidth': 'Bandwidth',
        'billing_type': 'BillingType',
        'cen_bandwidth_package_name': 'CenBandwidthPackageName',
        'cen_id': 'CenId',
        'client_token': 'ClientToken',
        'description': 'Description',
        'local_geographic_region_set_id': 'LocalGeographicRegionSetId',
        'peer_geographic_region_set_id': 'PeerGeographicRegionSetId',
        'period': 'Period',
        'period_unit': 'PeriodUnit',
        'project_name': 'ProjectName',
        'tags': 'Tags'
    }

    def __init__(self, bandwidth=None, billing_type=None, cen_bandwidth_package_name=None, cen_id=None, client_token=None, description=None, local_geographic_region_set_id=None, peer_geographic_region_set_id=None, period=None, period_unit=None, project_name=None, tags=None, _configuration=None):  # noqa: E501
        """CreateCenBandwidthPackageRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bandwidth = None
        self._billing_type = None
        self._cen_bandwidth_package_name = None
        self._cen_id = None
        self._client_token = None
        self._description = None
        self._local_geographic_region_set_id = None
        self._peer_geographic_region_set_id = None
        self._period = None
        self._period_unit = None
        self._project_name = None
        self._tags = None
        self.discriminator = None

        if bandwidth is not None:
            self.bandwidth = bandwidth
        if billing_type is not None:
            self.billing_type = billing_type
        if cen_bandwidth_package_name is not None:
            self.cen_bandwidth_package_name = cen_bandwidth_package_name
        if cen_id is not None:
            self.cen_id = cen_id
        if client_token is not None:
            self.client_token = client_token
        if description is not None:
            self.description = description
        self.local_geographic_region_set_id = local_geographic_region_set_id
        self.peer_geographic_region_set_id = peer_geographic_region_set_id
        if period is not None:
            self.period = period
        if period_unit is not None:
            self.period_unit = period_unit
        if project_name is not None:
            self.project_name = project_name
        if tags is not None:
            self.tags = tags

    @property
    def bandwidth(self):
        """Gets the bandwidth of this CreateCenBandwidthPackageRequest.  # noqa: E501


        :return: The bandwidth of this CreateCenBandwidthPackageRequest.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this CreateCenBandwidthPackageRequest.


        :param bandwidth: The bandwidth of this CreateCenBandwidthPackageRequest.  # noqa: E501
        :type: int
        """

        self._bandwidth = bandwidth

    @property
    def billing_type(self):
        """Gets the billing_type of this CreateCenBandwidthPackageRequest.  # noqa: E501


        :return: The billing_type of this CreateCenBandwidthPackageRequest.  # noqa: E501
        :rtype: int
        """
        return self._billing_type

    @billing_type.setter
    def billing_type(self, billing_type):
        """Sets the billing_type of this CreateCenBandwidthPackageRequest.


        :param billing_type: The billing_type of this CreateCenBandwidthPackageRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                billing_type is not None and billing_type > 4):  # noqa: E501
            raise ValueError("Invalid value for `billing_type`, must be a value less than or equal to `4`")  # noqa: E501
        if (self._configuration.client_side_validation and
                billing_type is not None and billing_type < 1):  # noqa: E501
            raise ValueError("Invalid value for `billing_type`, must be a value greater than or equal to `1`")  # noqa: E501

        self._billing_type = billing_type

    @property
    def cen_bandwidth_package_name(self):
        """Gets the cen_bandwidth_package_name of this CreateCenBandwidthPackageRequest.  # noqa: E501


        :return: The cen_bandwidth_package_name of this CreateCenBandwidthPackageRequest.  # noqa: E501
        :rtype: str
        """
        return self._cen_bandwidth_package_name

    @cen_bandwidth_package_name.setter
    def cen_bandwidth_package_name(self, cen_bandwidth_package_name):
        """Sets the cen_bandwidth_package_name of this CreateCenBandwidthPackageRequest.


        :param cen_bandwidth_package_name: The cen_bandwidth_package_name of this CreateCenBandwidthPackageRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                cen_bandwidth_package_name is not None and len(cen_bandwidth_package_name) > 128):
            raise ValueError("Invalid value for `cen_bandwidth_package_name`, length must be less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                cen_bandwidth_package_name is not None and len(cen_bandwidth_package_name) < 1):
            raise ValueError("Invalid value for `cen_bandwidth_package_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._cen_bandwidth_package_name = cen_bandwidth_package_name

    @property
    def cen_id(self):
        """Gets the cen_id of this CreateCenBandwidthPackageRequest.  # noqa: E501


        :return: The cen_id of this CreateCenBandwidthPackageRequest.  # noqa: E501
        :rtype: str
        """
        return self._cen_id

    @cen_id.setter
    def cen_id(self, cen_id):
        """Sets the cen_id of this CreateCenBandwidthPackageRequest.


        :param cen_id: The cen_id of this CreateCenBandwidthPackageRequest.  # noqa: E501
        :type: str
        """

        self._cen_id = cen_id

    @property
    def client_token(self):
        """Gets the client_token of this CreateCenBandwidthPackageRequest.  # noqa: E501


        :return: The client_token of this CreateCenBandwidthPackageRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this CreateCenBandwidthPackageRequest.


        :param client_token: The client_token of this CreateCenBandwidthPackageRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def description(self):
        """Gets the description of this CreateCenBandwidthPackageRequest.  # noqa: E501


        :return: The description of this CreateCenBandwidthPackageRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateCenBandwidthPackageRequest.


        :param description: The description of this CreateCenBandwidthPackageRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                description is not None and len(description) > 255):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def local_geographic_region_set_id(self):
        """Gets the local_geographic_region_set_id of this CreateCenBandwidthPackageRequest.  # noqa: E501


        :return: The local_geographic_region_set_id of this CreateCenBandwidthPackageRequest.  # noqa: E501
        :rtype: str
        """
        return self._local_geographic_region_set_id

    @local_geographic_region_set_id.setter
    def local_geographic_region_set_id(self, local_geographic_region_set_id):
        """Sets the local_geographic_region_set_id of this CreateCenBandwidthPackageRequest.


        :param local_geographic_region_set_id: The local_geographic_region_set_id of this CreateCenBandwidthPackageRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and local_geographic_region_set_id is None:
            raise ValueError("Invalid value for `local_geographic_region_set_id`, must not be `None`")  # noqa: E501

        self._local_geographic_region_set_id = local_geographic_region_set_id

    @property
    def peer_geographic_region_set_id(self):
        """Gets the peer_geographic_region_set_id of this CreateCenBandwidthPackageRequest.  # noqa: E501


        :return: The peer_geographic_region_set_id of this CreateCenBandwidthPackageRequest.  # noqa: E501
        :rtype: str
        """
        return self._peer_geographic_region_set_id

    @peer_geographic_region_set_id.setter
    def peer_geographic_region_set_id(self, peer_geographic_region_set_id):
        """Sets the peer_geographic_region_set_id of this CreateCenBandwidthPackageRequest.


        :param peer_geographic_region_set_id: The peer_geographic_region_set_id of this CreateCenBandwidthPackageRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and peer_geographic_region_set_id is None:
            raise ValueError("Invalid value for `peer_geographic_region_set_id`, must not be `None`")  # noqa: E501

        self._peer_geographic_region_set_id = peer_geographic_region_set_id

    @property
    def period(self):
        """Gets the period of this CreateCenBandwidthPackageRequest.  # noqa: E501


        :return: The period of this CreateCenBandwidthPackageRequest.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this CreateCenBandwidthPackageRequest.


        :param period: The period of this CreateCenBandwidthPackageRequest.  # noqa: E501
        :type: int
        """

        self._period = period

    @property
    def period_unit(self):
        """Gets the period_unit of this CreateCenBandwidthPackageRequest.  # noqa: E501


        :return: The period_unit of this CreateCenBandwidthPackageRequest.  # noqa: E501
        :rtype: str
        """
        return self._period_unit

    @period_unit.setter
    def period_unit(self, period_unit):
        """Sets the period_unit of this CreateCenBandwidthPackageRequest.


        :param period_unit: The period_unit of this CreateCenBandwidthPackageRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Moth", "Year"]  # noqa: E501
        if (self._configuration.client_side_validation and
                period_unit not in allowed_values):
            raise ValueError(
                "Invalid value for `period_unit` ({0}), must be one of {1}"  # noqa: E501
                .format(period_unit, allowed_values)
            )

        self._period_unit = period_unit

    @property
    def project_name(self):
        """Gets the project_name of this CreateCenBandwidthPackageRequest.  # noqa: E501


        :return: The project_name of this CreateCenBandwidthPackageRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this CreateCenBandwidthPackageRequest.


        :param project_name: The project_name of this CreateCenBandwidthPackageRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def tags(self):
        """Gets the tags of this CreateCenBandwidthPackageRequest.  # noqa: E501


        :return: The tags of this CreateCenBandwidthPackageRequest.  # noqa: E501
        :rtype: list[TagForCreateCenBandwidthPackageInput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateCenBandwidthPackageRequest.


        :param tags: The tags of this CreateCenBandwidthPackageRequest.  # noqa: E501
        :type: list[TagForCreateCenBandwidthPackageInput]
        """

        self._tags = tags

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
        if issubclass(CreateCenBandwidthPackageRequest, dict):
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
        if not isinstance(other, CreateCenBandwidthPackageRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateCenBandwidthPackageRequest):
            return True

        return self.to_dict() != other.to_dict()
