# coding: utf-8

"""
    billing

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ListBillDetailRequest(object):
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
        'bill_category': 'list[str]',
        'bill_period': 'str',
        'billing_mode': 'list[str]',
        'group_period': 'int',
        'group_term': 'int',
        'ignore_zero': 'int',
        'instance_no': 'str',
        'limit': 'int',
        'need_record_num': 'int',
        'offset': 'int',
        'product': 'list[str]'
    }

    attribute_map = {
        'bill_category': 'BillCategory',
        'bill_period': 'BillPeriod',
        'billing_mode': 'BillingMode',
        'group_period': 'GroupPeriod',
        'group_term': 'GroupTerm',
        'ignore_zero': 'IgnoreZero',
        'instance_no': 'InstanceNo',
        'limit': 'Limit',
        'need_record_num': 'NeedRecordNum',
        'offset': 'Offset',
        'product': 'Product'
    }

    def __init__(self, bill_category=None, bill_period=None, billing_mode=None, group_period=None, group_term=None, ignore_zero=None, instance_no=None, limit=None, need_record_num=None, offset=None, product=None, _configuration=None):  # noqa: E501
        """ListBillDetailRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bill_category = None
        self._bill_period = None
        self._billing_mode = None
        self._group_period = None
        self._group_term = None
        self._ignore_zero = None
        self._instance_no = None
        self._limit = None
        self._need_record_num = None
        self._offset = None
        self._product = None
        self.discriminator = None

        if bill_category is not None:
            self.bill_category = bill_category
        self.bill_period = bill_period
        if billing_mode is not None:
            self.billing_mode = billing_mode
        if group_period is not None:
            self.group_period = group_period
        if group_term is not None:
            self.group_term = group_term
        if ignore_zero is not None:
            self.ignore_zero = ignore_zero
        if instance_no is not None:
            self.instance_no = instance_no
        self.limit = limit
        if need_record_num is not None:
            self.need_record_num = need_record_num
        if offset is not None:
            self.offset = offset
        if product is not None:
            self.product = product

    @property
    def bill_category(self):
        """Gets the bill_category of this ListBillDetailRequest.  # noqa: E501


        :return: The bill_category of this ListBillDetailRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._bill_category

    @bill_category.setter
    def bill_category(self, bill_category):
        """Sets the bill_category of this ListBillDetailRequest.


        :param bill_category: The bill_category of this ListBillDetailRequest.  # noqa: E501
        :type: list[str]
        """

        self._bill_category = bill_category

    @property
    def bill_period(self):
        """Gets the bill_period of this ListBillDetailRequest.  # noqa: E501


        :return: The bill_period of this ListBillDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._bill_period

    @bill_period.setter
    def bill_period(self, bill_period):
        """Sets the bill_period of this ListBillDetailRequest.


        :param bill_period: The bill_period of this ListBillDetailRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and bill_period is None:
            raise ValueError("Invalid value for `bill_period`, must not be `None`")  # noqa: E501

        self._bill_period = bill_period

    @property
    def billing_mode(self):
        """Gets the billing_mode of this ListBillDetailRequest.  # noqa: E501


        :return: The billing_mode of this ListBillDetailRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, billing_mode):
        """Sets the billing_mode of this ListBillDetailRequest.


        :param billing_mode: The billing_mode of this ListBillDetailRequest.  # noqa: E501
        :type: list[str]
        """

        self._billing_mode = billing_mode

    @property
    def group_period(self):
        """Gets the group_period of this ListBillDetailRequest.  # noqa: E501


        :return: The group_period of this ListBillDetailRequest.  # noqa: E501
        :rtype: int
        """
        return self._group_period

    @group_period.setter
    def group_period(self, group_period):
        """Sets the group_period of this ListBillDetailRequest.


        :param group_period: The group_period of this ListBillDetailRequest.  # noqa: E501
        :type: int
        """

        self._group_period = group_period

    @property
    def group_term(self):
        """Gets the group_term of this ListBillDetailRequest.  # noqa: E501


        :return: The group_term of this ListBillDetailRequest.  # noqa: E501
        :rtype: int
        """
        return self._group_term

    @group_term.setter
    def group_term(self, group_term):
        """Sets the group_term of this ListBillDetailRequest.


        :param group_term: The group_term of this ListBillDetailRequest.  # noqa: E501
        :type: int
        """

        self._group_term = group_term

    @property
    def ignore_zero(self):
        """Gets the ignore_zero of this ListBillDetailRequest.  # noqa: E501


        :return: The ignore_zero of this ListBillDetailRequest.  # noqa: E501
        :rtype: int
        """
        return self._ignore_zero

    @ignore_zero.setter
    def ignore_zero(self, ignore_zero):
        """Sets the ignore_zero of this ListBillDetailRequest.


        :param ignore_zero: The ignore_zero of this ListBillDetailRequest.  # noqa: E501
        :type: int
        """

        self._ignore_zero = ignore_zero

    @property
    def instance_no(self):
        """Gets the instance_no of this ListBillDetailRequest.  # noqa: E501


        :return: The instance_no of this ListBillDetailRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_no

    @instance_no.setter
    def instance_no(self, instance_no):
        """Sets the instance_no of this ListBillDetailRequest.


        :param instance_no: The instance_no of this ListBillDetailRequest.  # noqa: E501
        :type: str
        """

        self._instance_no = instance_no

    @property
    def limit(self):
        """Gets the limit of this ListBillDetailRequest.  # noqa: E501


        :return: The limit of this ListBillDetailRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListBillDetailRequest.


        :param limit: The limit of this ListBillDetailRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def need_record_num(self):
        """Gets the need_record_num of this ListBillDetailRequest.  # noqa: E501


        :return: The need_record_num of this ListBillDetailRequest.  # noqa: E501
        :rtype: int
        """
        return self._need_record_num

    @need_record_num.setter
    def need_record_num(self, need_record_num):
        """Sets the need_record_num of this ListBillDetailRequest.


        :param need_record_num: The need_record_num of this ListBillDetailRequest.  # noqa: E501
        :type: int
        """

        self._need_record_num = need_record_num

    @property
    def offset(self):
        """Gets the offset of this ListBillDetailRequest.  # noqa: E501


        :return: The offset of this ListBillDetailRequest.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListBillDetailRequest.


        :param offset: The offset of this ListBillDetailRequest.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def product(self):
        """Gets the product of this ListBillDetailRequest.  # noqa: E501


        :return: The product of this ListBillDetailRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this ListBillDetailRequest.


        :param product: The product of this ListBillDetailRequest.  # noqa: E501
        :type: list[str]
        """

        self._product = product

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
        if issubclass(ListBillDetailRequest, dict):
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
        if not isinstance(other, ListBillDetailRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListBillDetailRequest):
            return True

        return self.to_dict() != other.to_dict()