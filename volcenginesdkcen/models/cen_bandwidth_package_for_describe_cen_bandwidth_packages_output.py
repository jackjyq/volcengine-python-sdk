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


class CenBandwidthPackageForDescribeCenBandwidthPackagesOutput(object):
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
        'account_id': 'str',
        'bandwidth': 'int',
        'billing_type': 'int',
        'business_status': 'str',
        'cen_bandwidth_package_id': 'str',
        'cen_bandwidth_package_name': 'str',
        'cen_ids': 'list[str]',
        'creation_time': 'str',
        'deleted_time': 'str',
        'description': 'str',
        'expired_time': 'str',
        'local_geographic_region_set_id': 'str',
        'peer_geographic_region_set_id': 'str',
        'remaining_bandwidth': 'int',
        'status': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'bandwidth': 'Bandwidth',
        'billing_type': 'BillingType',
        'business_status': 'BusinessStatus',
        'cen_bandwidth_package_id': 'CenBandwidthPackageId',
        'cen_bandwidth_package_name': 'CenBandwidthPackageName',
        'cen_ids': 'CenIds',
        'creation_time': 'CreationTime',
        'deleted_time': 'DeletedTime',
        'description': 'Description',
        'expired_time': 'ExpiredTime',
        'local_geographic_region_set_id': 'LocalGeographicRegionSetId',
        'peer_geographic_region_set_id': 'PeerGeographicRegionSetId',
        'remaining_bandwidth': 'RemainingBandwidth',
        'status': 'Status',
        'update_time': 'UpdateTime'
    }

    def __init__(self, account_id=None, bandwidth=None, billing_type=None, business_status=None, cen_bandwidth_package_id=None, cen_bandwidth_package_name=None, cen_ids=None, creation_time=None, deleted_time=None, description=None, expired_time=None, local_geographic_region_set_id=None, peer_geographic_region_set_id=None, remaining_bandwidth=None, status=None, update_time=None, _configuration=None):  # noqa: E501
        """CenBandwidthPackageForDescribeCenBandwidthPackagesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._bandwidth = None
        self._billing_type = None
        self._business_status = None
        self._cen_bandwidth_package_id = None
        self._cen_bandwidth_package_name = None
        self._cen_ids = None
        self._creation_time = None
        self._deleted_time = None
        self._description = None
        self._expired_time = None
        self._local_geographic_region_set_id = None
        self._peer_geographic_region_set_id = None
        self._remaining_bandwidth = None
        self._status = None
        self._update_time = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if billing_type is not None:
            self.billing_type = billing_type
        if business_status is not None:
            self.business_status = business_status
        if cen_bandwidth_package_id is not None:
            self.cen_bandwidth_package_id = cen_bandwidth_package_id
        if cen_bandwidth_package_name is not None:
            self.cen_bandwidth_package_name = cen_bandwidth_package_name
        if cen_ids is not None:
            self.cen_ids = cen_ids
        if creation_time is not None:
            self.creation_time = creation_time
        if deleted_time is not None:
            self.deleted_time = deleted_time
        if description is not None:
            self.description = description
        if expired_time is not None:
            self.expired_time = expired_time
        if local_geographic_region_set_id is not None:
            self.local_geographic_region_set_id = local_geographic_region_set_id
        if peer_geographic_region_set_id is not None:
            self.peer_geographic_region_set_id = peer_geographic_region_set_id
        if remaining_bandwidth is not None:
            self.remaining_bandwidth = remaining_bandwidth
        if status is not None:
            self.status = status
        if update_time is not None:
            self.update_time = update_time

    @property
    def account_id(self):
        """Gets the account_id of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501


        :return: The account_id of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.


        :param account_id: The account_id of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def bandwidth(self):
        """Gets the bandwidth of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501


        :return: The bandwidth of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.


        :param bandwidth: The bandwidth of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :type: int
        """

        self._bandwidth = bandwidth

    @property
    def billing_type(self):
        """Gets the billing_type of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501


        :return: The billing_type of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :rtype: int
        """
        return self._billing_type

    @billing_type.setter
    def billing_type(self, billing_type):
        """Sets the billing_type of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.


        :param billing_type: The billing_type of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :type: int
        """

        self._billing_type = billing_type

    @property
    def business_status(self):
        """Gets the business_status of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501


        :return: The business_status of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._business_status

    @business_status.setter
    def business_status(self, business_status):
        """Sets the business_status of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.


        :param business_status: The business_status of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :type: str
        """

        self._business_status = business_status

    @property
    def cen_bandwidth_package_id(self):
        """Gets the cen_bandwidth_package_id of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501


        :return: The cen_bandwidth_package_id of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._cen_bandwidth_package_id

    @cen_bandwidth_package_id.setter
    def cen_bandwidth_package_id(self, cen_bandwidth_package_id):
        """Sets the cen_bandwidth_package_id of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.


        :param cen_bandwidth_package_id: The cen_bandwidth_package_id of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :type: str
        """

        self._cen_bandwidth_package_id = cen_bandwidth_package_id

    @property
    def cen_bandwidth_package_name(self):
        """Gets the cen_bandwidth_package_name of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501


        :return: The cen_bandwidth_package_name of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._cen_bandwidth_package_name

    @cen_bandwidth_package_name.setter
    def cen_bandwidth_package_name(self, cen_bandwidth_package_name):
        """Sets the cen_bandwidth_package_name of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.


        :param cen_bandwidth_package_name: The cen_bandwidth_package_name of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :type: str
        """

        self._cen_bandwidth_package_name = cen_bandwidth_package_name

    @property
    def cen_ids(self):
        """Gets the cen_ids of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501


        :return: The cen_ids of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._cen_ids

    @cen_ids.setter
    def cen_ids(self, cen_ids):
        """Sets the cen_ids of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.


        :param cen_ids: The cen_ids of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :type: list[str]
        """

        self._cen_ids = cen_ids

    @property
    def creation_time(self):
        """Gets the creation_time of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501


        :return: The creation_time of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.


        :param creation_time: The creation_time of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def deleted_time(self):
        """Gets the deleted_time of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501


        :return: The deleted_time of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._deleted_time

    @deleted_time.setter
    def deleted_time(self, deleted_time):
        """Sets the deleted_time of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.


        :param deleted_time: The deleted_time of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :type: str
        """

        self._deleted_time = deleted_time

    @property
    def description(self):
        """Gets the description of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501


        :return: The description of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.


        :param description: The description of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def expired_time(self):
        """Gets the expired_time of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501


        :return: The expired_time of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._expired_time

    @expired_time.setter
    def expired_time(self, expired_time):
        """Sets the expired_time of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.


        :param expired_time: The expired_time of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :type: str
        """

        self._expired_time = expired_time

    @property
    def local_geographic_region_set_id(self):
        """Gets the local_geographic_region_set_id of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501


        :return: The local_geographic_region_set_id of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._local_geographic_region_set_id

    @local_geographic_region_set_id.setter
    def local_geographic_region_set_id(self, local_geographic_region_set_id):
        """Sets the local_geographic_region_set_id of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.


        :param local_geographic_region_set_id: The local_geographic_region_set_id of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :type: str
        """

        self._local_geographic_region_set_id = local_geographic_region_set_id

    @property
    def peer_geographic_region_set_id(self):
        """Gets the peer_geographic_region_set_id of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501


        :return: The peer_geographic_region_set_id of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._peer_geographic_region_set_id

    @peer_geographic_region_set_id.setter
    def peer_geographic_region_set_id(self, peer_geographic_region_set_id):
        """Sets the peer_geographic_region_set_id of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.


        :param peer_geographic_region_set_id: The peer_geographic_region_set_id of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :type: str
        """

        self._peer_geographic_region_set_id = peer_geographic_region_set_id

    @property
    def remaining_bandwidth(self):
        """Gets the remaining_bandwidth of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501


        :return: The remaining_bandwidth of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :rtype: int
        """
        return self._remaining_bandwidth

    @remaining_bandwidth.setter
    def remaining_bandwidth(self, remaining_bandwidth):
        """Sets the remaining_bandwidth of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.


        :param remaining_bandwidth: The remaining_bandwidth of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :type: int
        """

        self._remaining_bandwidth = remaining_bandwidth

    @property
    def status(self):
        """Gets the status of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501


        :return: The status of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.


        :param status: The status of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def update_time(self):
        """Gets the update_time of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501


        :return: The update_time of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.


        :param update_time: The update_time of this CenBandwidthPackageForDescribeCenBandwidthPackagesOutput.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

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
        if issubclass(CenBandwidthPackageForDescribeCenBandwidthPackagesOutput, dict):
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
        if not isinstance(other, CenBandwidthPackageForDescribeCenBandwidthPackagesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CenBandwidthPackageForDescribeCenBandwidthPackagesOutput):
            return True

        return self.to_dict() != other.to_dict()
