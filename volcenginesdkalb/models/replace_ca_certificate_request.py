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


class ReplaceCACertificateRequest(object):
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
        'ca_certificate': 'str',
        'ca_certificate_id': 'str',
        'ca_certificate_name': 'str',
        'description': 'str',
        'old_ca_certificate_id': 'str',
        'project_name': 'str',
        'update_mode': 'str'
    }

    attribute_map = {
        'ca_certificate': 'CACertificate',
        'ca_certificate_id': 'CACertificateId',
        'ca_certificate_name': 'CACertificateName',
        'description': 'Description',
        'old_ca_certificate_id': 'OldCACertificateId',
        'project_name': 'ProjectName',
        'update_mode': 'UpdateMode'
    }

    def __init__(self, ca_certificate=None, ca_certificate_id=None, ca_certificate_name=None, description=None, old_ca_certificate_id=None, project_name=None, update_mode=None, _configuration=None):  # noqa: E501
        """ReplaceCACertificateRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ca_certificate = None
        self._ca_certificate_id = None
        self._ca_certificate_name = None
        self._description = None
        self._old_ca_certificate_id = None
        self._project_name = None
        self._update_mode = None
        self.discriminator = None

        self.ca_certificate = ca_certificate
        if ca_certificate_id is not None:
            self.ca_certificate_id = ca_certificate_id
        if ca_certificate_name is not None:
            self.ca_certificate_name = ca_certificate_name
        if description is not None:
            self.description = description
        self.old_ca_certificate_id = old_ca_certificate_id
        if project_name is not None:
            self.project_name = project_name
        self.update_mode = update_mode

    @property
    def ca_certificate(self):
        """Gets the ca_certificate of this ReplaceCACertificateRequest.  # noqa: E501


        :return: The ca_certificate of this ReplaceCACertificateRequest.  # noqa: E501
        :rtype: str
        """
        return self._ca_certificate

    @ca_certificate.setter
    def ca_certificate(self, ca_certificate):
        """Sets the ca_certificate of this ReplaceCACertificateRequest.


        :param ca_certificate: The ca_certificate of this ReplaceCACertificateRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and ca_certificate is None:
            raise ValueError("Invalid value for `ca_certificate`, must not be `None`")  # noqa: E501

        self._ca_certificate = ca_certificate

    @property
    def ca_certificate_id(self):
        """Gets the ca_certificate_id of this ReplaceCACertificateRequest.  # noqa: E501


        :return: The ca_certificate_id of this ReplaceCACertificateRequest.  # noqa: E501
        :rtype: str
        """
        return self._ca_certificate_id

    @ca_certificate_id.setter
    def ca_certificate_id(self, ca_certificate_id):
        """Sets the ca_certificate_id of this ReplaceCACertificateRequest.


        :param ca_certificate_id: The ca_certificate_id of this ReplaceCACertificateRequest.  # noqa: E501
        :type: str
        """

        self._ca_certificate_id = ca_certificate_id

    @property
    def ca_certificate_name(self):
        """Gets the ca_certificate_name of this ReplaceCACertificateRequest.  # noqa: E501


        :return: The ca_certificate_name of this ReplaceCACertificateRequest.  # noqa: E501
        :rtype: str
        """
        return self._ca_certificate_name

    @ca_certificate_name.setter
    def ca_certificate_name(self, ca_certificate_name):
        """Sets the ca_certificate_name of this ReplaceCACertificateRequest.


        :param ca_certificate_name: The ca_certificate_name of this ReplaceCACertificateRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                ca_certificate_name is not None and len(ca_certificate_name) > 128):
            raise ValueError("Invalid value for `ca_certificate_name`, length must be less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                ca_certificate_name is not None and len(ca_certificate_name) < 1):
            raise ValueError("Invalid value for `ca_certificate_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._ca_certificate_name = ca_certificate_name

    @property
    def description(self):
        """Gets the description of this ReplaceCACertificateRequest.  # noqa: E501


        :return: The description of this ReplaceCACertificateRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ReplaceCACertificateRequest.


        :param description: The description of this ReplaceCACertificateRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def old_ca_certificate_id(self):
        """Gets the old_ca_certificate_id of this ReplaceCACertificateRequest.  # noqa: E501


        :return: The old_ca_certificate_id of this ReplaceCACertificateRequest.  # noqa: E501
        :rtype: str
        """
        return self._old_ca_certificate_id

    @old_ca_certificate_id.setter
    def old_ca_certificate_id(self, old_ca_certificate_id):
        """Sets the old_ca_certificate_id of this ReplaceCACertificateRequest.


        :param old_ca_certificate_id: The old_ca_certificate_id of this ReplaceCACertificateRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and old_ca_certificate_id is None:
            raise ValueError("Invalid value for `old_ca_certificate_id`, must not be `None`")  # noqa: E501

        self._old_ca_certificate_id = old_ca_certificate_id

    @property
    def project_name(self):
        """Gets the project_name of this ReplaceCACertificateRequest.  # noqa: E501


        :return: The project_name of this ReplaceCACertificateRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ReplaceCACertificateRequest.


        :param project_name: The project_name of this ReplaceCACertificateRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def update_mode(self):
        """Gets the update_mode of this ReplaceCACertificateRequest.  # noqa: E501


        :return: The update_mode of this ReplaceCACertificateRequest.  # noqa: E501
        :rtype: str
        """
        return self._update_mode

    @update_mode.setter
    def update_mode(self, update_mode):
        """Sets the update_mode of this ReplaceCACertificateRequest.


        :param update_mode: The update_mode of this ReplaceCACertificateRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and update_mode is None:
            raise ValueError("Invalid value for `update_mode`, must not be `None`")  # noqa: E501

        self._update_mode = update_mode

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
        if issubclass(ReplaceCACertificateRequest, dict):
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
        if not isinstance(other, ReplaceCACertificateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReplaceCACertificateRequest):
            return True

        return self.to_dict() != other.to_dict()