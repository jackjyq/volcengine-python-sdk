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


class DescribeCensRequest(object):
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
        'cen_ids': 'str',
        'cen_name': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'project_name': 'str',
        'tag_filters': 'list[TagFilterForDescribeCensInput]'
    }

    attribute_map = {
        'cen_ids': 'CenIds',
        'cen_name': 'CenName',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'project_name': 'ProjectName',
        'tag_filters': 'TagFilters'
    }

    def __init__(self, cen_ids=None, cen_name=None, page_number=None, page_size=None, project_name=None, tag_filters=None, _configuration=None):  # noqa: E501
        """DescribeCensRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cen_ids = None
        self._cen_name = None
        self._page_number = None
        self._page_size = None
        self._project_name = None
        self._tag_filters = None
        self.discriminator = None

        if cen_ids is not None:
            self.cen_ids = cen_ids
        if cen_name is not None:
            self.cen_name = cen_name
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if project_name is not None:
            self.project_name = project_name
        if tag_filters is not None:
            self.tag_filters = tag_filters

    @property
    def cen_ids(self):
        """Gets the cen_ids of this DescribeCensRequest.  # noqa: E501


        :return: The cen_ids of this DescribeCensRequest.  # noqa: E501
        :rtype: str
        """
        return self._cen_ids

    @cen_ids.setter
    def cen_ids(self, cen_ids):
        """Sets the cen_ids of this DescribeCensRequest.


        :param cen_ids: The cen_ids of this DescribeCensRequest.  # noqa: E501
        :type: str
        """

        self._cen_ids = cen_ids

    @property
    def cen_name(self):
        """Gets the cen_name of this DescribeCensRequest.  # noqa: E501


        :return: The cen_name of this DescribeCensRequest.  # noqa: E501
        :rtype: str
        """
        return self._cen_name

    @cen_name.setter
    def cen_name(self, cen_name):
        """Sets the cen_name of this DescribeCensRequest.


        :param cen_name: The cen_name of this DescribeCensRequest.  # noqa: E501
        :type: str
        """

        self._cen_name = cen_name

    @property
    def page_number(self):
        """Gets the page_number of this DescribeCensRequest.  # noqa: E501


        :return: The page_number of this DescribeCensRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeCensRequest.


        :param page_number: The page_number of this DescribeCensRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeCensRequest.  # noqa: E501


        :return: The page_size of this DescribeCensRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeCensRequest.


        :param page_size: The page_size of this DescribeCensRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def project_name(self):
        """Gets the project_name of this DescribeCensRequest.  # noqa: E501


        :return: The project_name of this DescribeCensRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DescribeCensRequest.


        :param project_name: The project_name of this DescribeCensRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def tag_filters(self):
        """Gets the tag_filters of this DescribeCensRequest.  # noqa: E501


        :return: The tag_filters of this DescribeCensRequest.  # noqa: E501
        :rtype: list[TagFilterForDescribeCensInput]
        """
        return self._tag_filters

    @tag_filters.setter
    def tag_filters(self, tag_filters):
        """Sets the tag_filters of this DescribeCensRequest.


        :param tag_filters: The tag_filters of this DescribeCensRequest.  # noqa: E501
        :type: list[TagFilterForDescribeCensInput]
        """

        self._tag_filters = tag_filters

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
        if issubclass(DescribeCensRequest, dict):
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
        if not isinstance(other, DescribeCensRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeCensRequest):
            return True

        return self.to_dict() != other.to_dict()
