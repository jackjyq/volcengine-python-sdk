# coding: utf-8

"""
    cdn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeContentTasksRequest(object):
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
        'domain_name': 'str',
        'end_time': 'int',
        'page_num': 'int',
        'page_size': 'int',
        'remark': 'str',
        'start_time': 'int',
        'status': 'str',
        'task_id': 'str',
        'task_type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'domain_name': 'DomainName',
        'end_time': 'EndTime',
        'page_num': 'PageNum',
        'page_size': 'PageSize',
        'remark': 'Remark',
        'start_time': 'StartTime',
        'status': 'Status',
        'task_id': 'TaskID',
        'task_type': 'TaskType',
        'url': 'Url'
    }

    def __init__(self, domain_name=None, end_time=None, page_num=None, page_size=None, remark=None, start_time=None, status=None, task_id=None, task_type=None, url=None, _configuration=None):  # noqa: E501
        """DescribeContentTasksRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._domain_name = None
        self._end_time = None
        self._page_num = None
        self._page_size = None
        self._remark = None
        self._start_time = None
        self._status = None
        self._task_id = None
        self._task_type = None
        self._url = None
        self.discriminator = None

        if domain_name is not None:
            self.domain_name = domain_name
        if end_time is not None:
            self.end_time = end_time
        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size
        if remark is not None:
            self.remark = remark
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status
        if task_id is not None:
            self.task_id = task_id
        self.task_type = task_type
        if url is not None:
            self.url = url

    @property
    def domain_name(self):
        """Gets the domain_name of this DescribeContentTasksRequest.  # noqa: E501


        :return: The domain_name of this DescribeContentTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this DescribeContentTasksRequest.


        :param domain_name: The domain_name of this DescribeContentTasksRequest.  # noqa: E501
        :type: str
        """

        self._domain_name = domain_name

    @property
    def end_time(self):
        """Gets the end_time of this DescribeContentTasksRequest.  # noqa: E501


        :return: The end_time of this DescribeContentTasksRequest.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this DescribeContentTasksRequest.


        :param end_time: The end_time of this DescribeContentTasksRequest.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

    @property
    def page_num(self):
        """Gets the page_num of this DescribeContentTasksRequest.  # noqa: E501


        :return: The page_num of this DescribeContentTasksRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        """Sets the page_num of this DescribeContentTasksRequest.


        :param page_num: The page_num of this DescribeContentTasksRequest.  # noqa: E501
        :type: int
        """

        self._page_num = page_num

    @property
    def page_size(self):
        """Gets the page_size of this DescribeContentTasksRequest.  # noqa: E501


        :return: The page_size of this DescribeContentTasksRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeContentTasksRequest.


        :param page_size: The page_size of this DescribeContentTasksRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def remark(self):
        """Gets the remark of this DescribeContentTasksRequest.  # noqa: E501


        :return: The remark of this DescribeContentTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this DescribeContentTasksRequest.


        :param remark: The remark of this DescribeContentTasksRequest.  # noqa: E501
        :type: str
        """

        self._remark = remark

    @property
    def start_time(self):
        """Gets the start_time of this DescribeContentTasksRequest.  # noqa: E501


        :return: The start_time of this DescribeContentTasksRequest.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DescribeContentTasksRequest.


        :param start_time: The start_time of this DescribeContentTasksRequest.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this DescribeContentTasksRequest.  # noqa: E501


        :return: The status of this DescribeContentTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DescribeContentTasksRequest.


        :param status: The status of this DescribeContentTasksRequest.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def task_id(self):
        """Gets the task_id of this DescribeContentTasksRequest.  # noqa: E501


        :return: The task_id of this DescribeContentTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this DescribeContentTasksRequest.


        :param task_id: The task_id of this DescribeContentTasksRequest.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

    @property
    def task_type(self):
        """Gets the task_type of this DescribeContentTasksRequest.  # noqa: E501


        :return: The task_type of this DescribeContentTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this DescribeContentTasksRequest.


        :param task_type: The task_type of this DescribeContentTasksRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and task_type is None:
            raise ValueError("Invalid value for `task_type`, must not be `None`")  # noqa: E501

        self._task_type = task_type

    @property
    def url(self):
        """Gets the url of this DescribeContentTasksRequest.  # noqa: E501


        :return: The url of this DescribeContentTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DescribeContentTasksRequest.


        :param url: The url of this DescribeContentTasksRequest.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(DescribeContentTasksRequest, dict):
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
        if not isinstance(other, DescribeContentTasksRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeContentTasksRequest):
            return True

        return self.to_dict() != other.to_dict()
