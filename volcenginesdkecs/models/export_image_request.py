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


class ExportImageRequest(object):
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
        'image_id': 'str',
        'tos_bucket': 'str',
        'tos_prefix': 'str'
    }

    attribute_map = {
        'image_id': 'ImageId',
        'tos_bucket': 'TOSBucket',
        'tos_prefix': 'TOSPrefix'
    }

    def __init__(self, image_id=None, tos_bucket=None, tos_prefix=None, _configuration=None):  # noqa: E501
        """ExportImageRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._image_id = None
        self._tos_bucket = None
        self._tos_prefix = None
        self.discriminator = None

        if image_id is not None:
            self.image_id = image_id
        if tos_bucket is not None:
            self.tos_bucket = tos_bucket
        if tos_prefix is not None:
            self.tos_prefix = tos_prefix

    @property
    def image_id(self):
        """Gets the image_id of this ExportImageRequest.  # noqa: E501


        :return: The image_id of this ExportImageRequest.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ExportImageRequest.


        :param image_id: The image_id of this ExportImageRequest.  # noqa: E501
        :type: str
        """

        self._image_id = image_id

    @property
    def tos_bucket(self):
        """Gets the tos_bucket of this ExportImageRequest.  # noqa: E501


        :return: The tos_bucket of this ExportImageRequest.  # noqa: E501
        :rtype: str
        """
        return self._tos_bucket

    @tos_bucket.setter
    def tos_bucket(self, tos_bucket):
        """Sets the tos_bucket of this ExportImageRequest.


        :param tos_bucket: The tos_bucket of this ExportImageRequest.  # noqa: E501
        :type: str
        """

        self._tos_bucket = tos_bucket

    @property
    def tos_prefix(self):
        """Gets the tos_prefix of this ExportImageRequest.  # noqa: E501


        :return: The tos_prefix of this ExportImageRequest.  # noqa: E501
        :rtype: str
        """
        return self._tos_prefix

    @tos_prefix.setter
    def tos_prefix(self, tos_prefix):
        """Sets the tos_prefix of this ExportImageRequest.


        :param tos_prefix: The tos_prefix of this ExportImageRequest.  # noqa: E501
        :type: str
        """

        self._tos_prefix = tos_prefix

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
        if issubclass(ExportImageRequest, dict):
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
        if not isinstance(other, ExportImageRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExportImageRequest):
            return True

        return self.to_dict() != other.to_dict()
