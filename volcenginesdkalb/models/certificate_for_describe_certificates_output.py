# coding: utf-8

"""
    alb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CertificateForDescribeCertificatesOutput(object):
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
        'certificate_id': 'str',
        'certificate_name': 'str',
        'certificate_type': 'str',
        'create_time': 'str',
        'description': 'str',
        'domain_name': 'str',
        'expired_at': 'str',
        'listeners': 'list[str]',
        'project_name': 'str',
        'status': 'str'
    }

    attribute_map = {
        'certificate_id': 'CertificateId',
        'certificate_name': 'CertificateName',
        'certificate_type': 'CertificateType',
        'create_time': 'CreateTime',
        'description': 'Description',
        'domain_name': 'DomainName',
        'expired_at': 'ExpiredAt',
        'listeners': 'Listeners',
        'project_name': 'ProjectName',
        'status': 'Status'
    }

    def __init__(self, certificate_id=None, certificate_name=None, certificate_type=None, create_time=None, description=None, domain_name=None, expired_at=None, listeners=None, project_name=None, status=None, _configuration=None):  # noqa: E501
        """CertificateForDescribeCertificatesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._certificate_id = None
        self._certificate_name = None
        self._certificate_type = None
        self._create_time = None
        self._description = None
        self._domain_name = None
        self._expired_at = None
        self._listeners = None
        self._project_name = None
        self._status = None
        self.discriminator = None

        if certificate_id is not None:
            self.certificate_id = certificate_id
        if certificate_name is not None:
            self.certificate_name = certificate_name
        if certificate_type is not None:
            self.certificate_type = certificate_type
        if create_time is not None:
            self.create_time = create_time
        if description is not None:
            self.description = description
        if domain_name is not None:
            self.domain_name = domain_name
        if expired_at is not None:
            self.expired_at = expired_at
        if listeners is not None:
            self.listeners = listeners
        if project_name is not None:
            self.project_name = project_name
        if status is not None:
            self.status = status

    @property
    def certificate_id(self):
        """Gets the certificate_id of this CertificateForDescribeCertificatesOutput.  # noqa: E501


        :return: The certificate_id of this CertificateForDescribeCertificatesOutput.  # noqa: E501
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """Sets the certificate_id of this CertificateForDescribeCertificatesOutput.


        :param certificate_id: The certificate_id of this CertificateForDescribeCertificatesOutput.  # noqa: E501
        :type: str
        """

        self._certificate_id = certificate_id

    @property
    def certificate_name(self):
        """Gets the certificate_name of this CertificateForDescribeCertificatesOutput.  # noqa: E501


        :return: The certificate_name of this CertificateForDescribeCertificatesOutput.  # noqa: E501
        :rtype: str
        """
        return self._certificate_name

    @certificate_name.setter
    def certificate_name(self, certificate_name):
        """Sets the certificate_name of this CertificateForDescribeCertificatesOutput.


        :param certificate_name: The certificate_name of this CertificateForDescribeCertificatesOutput.  # noqa: E501
        :type: str
        """

        self._certificate_name = certificate_name

    @property
    def certificate_type(self):
        """Gets the certificate_type of this CertificateForDescribeCertificatesOutput.  # noqa: E501


        :return: The certificate_type of this CertificateForDescribeCertificatesOutput.  # noqa: E501
        :rtype: str
        """
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, certificate_type):
        """Sets the certificate_type of this CertificateForDescribeCertificatesOutput.


        :param certificate_type: The certificate_type of this CertificateForDescribeCertificatesOutput.  # noqa: E501
        :type: str
        """

        self._certificate_type = certificate_type

    @property
    def create_time(self):
        """Gets the create_time of this CertificateForDescribeCertificatesOutput.  # noqa: E501


        :return: The create_time of this CertificateForDescribeCertificatesOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CertificateForDescribeCertificatesOutput.


        :param create_time: The create_time of this CertificateForDescribeCertificatesOutput.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def description(self):
        """Gets the description of this CertificateForDescribeCertificatesOutput.  # noqa: E501


        :return: The description of this CertificateForDescribeCertificatesOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CertificateForDescribeCertificatesOutput.


        :param description: The description of this CertificateForDescribeCertificatesOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def domain_name(self):
        """Gets the domain_name of this CertificateForDescribeCertificatesOutput.  # noqa: E501


        :return: The domain_name of this CertificateForDescribeCertificatesOutput.  # noqa: E501
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this CertificateForDescribeCertificatesOutput.


        :param domain_name: The domain_name of this CertificateForDescribeCertificatesOutput.  # noqa: E501
        :type: str
        """

        self._domain_name = domain_name

    @property
    def expired_at(self):
        """Gets the expired_at of this CertificateForDescribeCertificatesOutput.  # noqa: E501


        :return: The expired_at of this CertificateForDescribeCertificatesOutput.  # noqa: E501
        :rtype: str
        """
        return self._expired_at

    @expired_at.setter
    def expired_at(self, expired_at):
        """Sets the expired_at of this CertificateForDescribeCertificatesOutput.


        :param expired_at: The expired_at of this CertificateForDescribeCertificatesOutput.  # noqa: E501
        :type: str
        """

        self._expired_at = expired_at

    @property
    def listeners(self):
        """Gets the listeners of this CertificateForDescribeCertificatesOutput.  # noqa: E501


        :return: The listeners of this CertificateForDescribeCertificatesOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        """Sets the listeners of this CertificateForDescribeCertificatesOutput.


        :param listeners: The listeners of this CertificateForDescribeCertificatesOutput.  # noqa: E501
        :type: list[str]
        """

        self._listeners = listeners

    @property
    def project_name(self):
        """Gets the project_name of this CertificateForDescribeCertificatesOutput.  # noqa: E501


        :return: The project_name of this CertificateForDescribeCertificatesOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this CertificateForDescribeCertificatesOutput.


        :param project_name: The project_name of this CertificateForDescribeCertificatesOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def status(self):
        """Gets the status of this CertificateForDescribeCertificatesOutput.  # noqa: E501


        :return: The status of this CertificateForDescribeCertificatesOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CertificateForDescribeCertificatesOutput.


        :param status: The status of this CertificateForDescribeCertificatesOutput.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(CertificateForDescribeCertificatesOutput, dict):
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
        if not isinstance(other, CertificateForDescribeCertificatesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CertificateForDescribeCertificatesOutput):
            return True

        return self.to_dict() != other.to_dict()
