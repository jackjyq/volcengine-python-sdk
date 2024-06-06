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


class ListAmortizedCostBillMonthlyRequest(object):
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
        'amortized_month': 'str',
        'amortized_type': 'list[str]',
        'bill_category': 'list[str]',
        'bill_period': 'str',
        'billing_mode': 'list[str]',
        'ignore_zero': 'int',
        'instance_no': 'str',
        'limit': 'int',
        'need_record_num': 'int',
        'offset': 'int',
        'owner_id': 'list[int]',
        'payer_id': 'list[int]',
        'product': 'list[str]'
    }

    attribute_map = {
        'amortized_month': 'AmortizedMonth',
        'amortized_type': 'AmortizedType',
        'bill_category': 'BillCategory',
        'bill_period': 'BillPeriod',
        'billing_mode': 'BillingMode',
        'ignore_zero': 'IgnoreZero',
        'instance_no': 'InstanceNo',
        'limit': 'Limit',
        'need_record_num': 'NeedRecordNum',
        'offset': 'Offset',
        'owner_id': 'OwnerID',
        'payer_id': 'PayerID',
        'product': 'Product'
    }

    def __init__(self, amortized_month=None, amortized_type=None, bill_category=None, bill_period=None, billing_mode=None, ignore_zero=None, instance_no=None, limit=None, need_record_num=None, offset=None, owner_id=None, payer_id=None, product=None, _configuration=None):  # noqa: E501
        """ListAmortizedCostBillMonthlyRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._amortized_month = None
        self._amortized_type = None
        self._bill_category = None
        self._bill_period = None
        self._billing_mode = None
        self._ignore_zero = None
        self._instance_no = None
        self._limit = None
        self._need_record_num = None
        self._offset = None
        self._owner_id = None
        self._payer_id = None
        self._product = None
        self.discriminator = None

        self.amortized_month = amortized_month
        if amortized_type is not None:
            self.amortized_type = amortized_type
        if bill_category is not None:
            self.bill_category = bill_category
        if bill_period is not None:
            self.bill_period = bill_period
        if billing_mode is not None:
            self.billing_mode = billing_mode
        if ignore_zero is not None:
            self.ignore_zero = ignore_zero
        if instance_no is not None:
            self.instance_no = instance_no
        self.limit = limit
        if need_record_num is not None:
            self.need_record_num = need_record_num
        if offset is not None:
            self.offset = offset
        if owner_id is not None:
            self.owner_id = owner_id
        if payer_id is not None:
            self.payer_id = payer_id
        if product is not None:
            self.product = product

    @property
    def amortized_month(self):
        """Gets the amortized_month of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501


        :return: The amortized_month of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501
        :rtype: str
        """
        return self._amortized_month

    @amortized_month.setter
    def amortized_month(self, amortized_month):
        """Sets the amortized_month of this ListAmortizedCostBillMonthlyRequest.


        :param amortized_month: The amortized_month of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and amortized_month is None:
            raise ValueError("Invalid value for `amortized_month`, must not be `None`")  # noqa: E501

        self._amortized_month = amortized_month

    @property
    def amortized_type(self):
        """Gets the amortized_type of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501


        :return: The amortized_type of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._amortized_type

    @amortized_type.setter
    def amortized_type(self, amortized_type):
        """Sets the amortized_type of this ListAmortizedCostBillMonthlyRequest.


        :param amortized_type: The amortized_type of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501
        :type: list[str]
        """

        self._amortized_type = amortized_type

    @property
    def bill_category(self):
        """Gets the bill_category of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501


        :return: The bill_category of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._bill_category

    @bill_category.setter
    def bill_category(self, bill_category):
        """Sets the bill_category of this ListAmortizedCostBillMonthlyRequest.


        :param bill_category: The bill_category of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501
        :type: list[str]
        """

        self._bill_category = bill_category

    @property
    def bill_period(self):
        """Gets the bill_period of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501


        :return: The bill_period of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501
        :rtype: str
        """
        return self._bill_period

    @bill_period.setter
    def bill_period(self, bill_period):
        """Sets the bill_period of this ListAmortizedCostBillMonthlyRequest.


        :param bill_period: The bill_period of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501
        :type: str
        """

        self._bill_period = bill_period

    @property
    def billing_mode(self):
        """Gets the billing_mode of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501


        :return: The billing_mode of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, billing_mode):
        """Sets the billing_mode of this ListAmortizedCostBillMonthlyRequest.


        :param billing_mode: The billing_mode of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501
        :type: list[str]
        """

        self._billing_mode = billing_mode

    @property
    def ignore_zero(self):
        """Gets the ignore_zero of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501


        :return: The ignore_zero of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501
        :rtype: int
        """
        return self._ignore_zero

    @ignore_zero.setter
    def ignore_zero(self, ignore_zero):
        """Sets the ignore_zero of this ListAmortizedCostBillMonthlyRequest.


        :param ignore_zero: The ignore_zero of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501
        :type: int
        """

        self._ignore_zero = ignore_zero

    @property
    def instance_no(self):
        """Gets the instance_no of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501


        :return: The instance_no of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_no

    @instance_no.setter
    def instance_no(self, instance_no):
        """Sets the instance_no of this ListAmortizedCostBillMonthlyRequest.


        :param instance_no: The instance_no of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501
        :type: str
        """

        self._instance_no = instance_no

    @property
    def limit(self):
        """Gets the limit of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501


        :return: The limit of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAmortizedCostBillMonthlyRequest.


        :param limit: The limit of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def need_record_num(self):
        """Gets the need_record_num of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501


        :return: The need_record_num of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501
        :rtype: int
        """
        return self._need_record_num

    @need_record_num.setter
    def need_record_num(self, need_record_num):
        """Sets the need_record_num of this ListAmortizedCostBillMonthlyRequest.


        :param need_record_num: The need_record_num of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501
        :type: int
        """

        self._need_record_num = need_record_num

    @property
    def offset(self):
        """Gets the offset of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501


        :return: The offset of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAmortizedCostBillMonthlyRequest.


        :param offset: The offset of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def owner_id(self):
        """Gets the owner_id of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501


        :return: The owner_id of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this ListAmortizedCostBillMonthlyRequest.


        :param owner_id: The owner_id of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501
        :type: list[int]
        """

        self._owner_id = owner_id

    @property
    def payer_id(self):
        """Gets the payer_id of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501


        :return: The payer_id of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._payer_id

    @payer_id.setter
    def payer_id(self, payer_id):
        """Sets the payer_id of this ListAmortizedCostBillMonthlyRequest.


        :param payer_id: The payer_id of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501
        :type: list[int]
        """

        self._payer_id = payer_id

    @property
    def product(self):
        """Gets the product of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501


        :return: The product of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this ListAmortizedCostBillMonthlyRequest.


        :param product: The product of this ListAmortizedCostBillMonthlyRequest.  # noqa: E501
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
        if issubclass(ListAmortizedCostBillMonthlyRequest, dict):
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
        if not isinstance(other, ListAmortizedCostBillMonthlyRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListAmortizedCostBillMonthlyRequest):
            return True

        return self.to_dict() != other.to_dict()
