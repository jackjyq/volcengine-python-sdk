# coding: utf-8

"""
    directconnect

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class AssociateCenForDescribeDirectConnectGatewayAttributesOutput(object):
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
        'cen_owner_id': 'str',
        'cen_status': 'str'
    }

    attribute_map = {
        'cen_id': 'CenId',
        'cen_owner_id': 'CenOwnerId',
        'cen_status': 'CenStatus'
    }

    def __init__(self, cen_id=None, cen_owner_id=None, cen_status=None, _configuration=None):  # noqa: E501
        """AssociateCenForDescribeDirectConnectGatewayAttributesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cen_id = None
        self._cen_owner_id = None
        self._cen_status = None
        self.discriminator = None

        if cen_id is not None:
            self.cen_id = cen_id
        if cen_owner_id is not None:
            self.cen_owner_id = cen_owner_id
        if cen_status is not None:
            self.cen_status = cen_status

    @property
    def cen_id(self):
        """Gets the cen_id of this AssociateCenForDescribeDirectConnectGatewayAttributesOutput.  # noqa: E501


        :return: The cen_id of this AssociateCenForDescribeDirectConnectGatewayAttributesOutput.  # noqa: E501
        :rtype: str
        """
        return self._cen_id

    @cen_id.setter
    def cen_id(self, cen_id):
        """Sets the cen_id of this AssociateCenForDescribeDirectConnectGatewayAttributesOutput.


        :param cen_id: The cen_id of this AssociateCenForDescribeDirectConnectGatewayAttributesOutput.  # noqa: E501
        :type: str
        """

        self._cen_id = cen_id

    @property
    def cen_owner_id(self):
        """Gets the cen_owner_id of this AssociateCenForDescribeDirectConnectGatewayAttributesOutput.  # noqa: E501


        :return: The cen_owner_id of this AssociateCenForDescribeDirectConnectGatewayAttributesOutput.  # noqa: E501
        :rtype: str
        """
        return self._cen_owner_id

    @cen_owner_id.setter
    def cen_owner_id(self, cen_owner_id):
        """Sets the cen_owner_id of this AssociateCenForDescribeDirectConnectGatewayAttributesOutput.


        :param cen_owner_id: The cen_owner_id of this AssociateCenForDescribeDirectConnectGatewayAttributesOutput.  # noqa: E501
        :type: str
        """

        self._cen_owner_id = cen_owner_id

    @property
    def cen_status(self):
        """Gets the cen_status of this AssociateCenForDescribeDirectConnectGatewayAttributesOutput.  # noqa: E501


        :return: The cen_status of this AssociateCenForDescribeDirectConnectGatewayAttributesOutput.  # noqa: E501
        :rtype: str
        """
        return self._cen_status

    @cen_status.setter
    def cen_status(self, cen_status):
        """Sets the cen_status of this AssociateCenForDescribeDirectConnectGatewayAttributesOutput.


        :param cen_status: The cen_status of this AssociateCenForDescribeDirectConnectGatewayAttributesOutput.  # noqa: E501
        :type: str
        """

        self._cen_status = cen_status

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
        if issubclass(AssociateCenForDescribeDirectConnectGatewayAttributesOutput, dict):
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
        if not isinstance(other, AssociateCenForDescribeDirectConnectGatewayAttributesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssociateCenForDescribeDirectConnectGatewayAttributesOutput):
            return True

        return self.to_dict() != other.to_dict()
