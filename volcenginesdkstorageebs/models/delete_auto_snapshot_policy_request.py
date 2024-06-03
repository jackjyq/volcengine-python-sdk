# coding: utf-8

"""
    storage_ebs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DeleteAutoSnapshotPolicyRequest(object):
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
        'auto_snapshot_policy_id': 'str'
    }

    attribute_map = {
        'auto_snapshot_policy_id': 'AutoSnapshotPolicyId'
    }

    def __init__(self, auto_snapshot_policy_id=None, _configuration=None):  # noqa: E501
        """DeleteAutoSnapshotPolicyRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_snapshot_policy_id = None
        self.discriminator = None

        self.auto_snapshot_policy_id = auto_snapshot_policy_id

    @property
    def auto_snapshot_policy_id(self):
        """Gets the auto_snapshot_policy_id of this DeleteAutoSnapshotPolicyRequest.  # noqa: E501


        :return: The auto_snapshot_policy_id of this DeleteAutoSnapshotPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._auto_snapshot_policy_id

    @auto_snapshot_policy_id.setter
    def auto_snapshot_policy_id(self, auto_snapshot_policy_id):
        """Sets the auto_snapshot_policy_id of this DeleteAutoSnapshotPolicyRequest.


        :param auto_snapshot_policy_id: The auto_snapshot_policy_id of this DeleteAutoSnapshotPolicyRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and auto_snapshot_policy_id is None:
            raise ValueError("Invalid value for `auto_snapshot_policy_id`, must not be `None`")  # noqa: E501

        self._auto_snapshot_policy_id = auto_snapshot_policy_id

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
        if issubclass(DeleteAutoSnapshotPolicyRequest, dict):
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
        if not isinstance(other, DeleteAutoSnapshotPolicyRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeleteAutoSnapshotPolicyRequest):
            return True

        return self.to_dict() != other.to_dict()