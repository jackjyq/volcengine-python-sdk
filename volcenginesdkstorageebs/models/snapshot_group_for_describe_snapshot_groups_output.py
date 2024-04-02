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


class SnapshotGroupForDescribeSnapshotGroupsOutput(object):
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
        'creation_time': 'str',
        'description': 'str',
        'image_id': 'str',
        'instance_id': 'str',
        'name': 'str',
        'project_name': 'str',
        'snapshot_group_id': 'str',
        'snapshots': 'list[SnapshotForDescribeSnapshotGroupsOutput]',
        'status': 'str',
        'tags': 'list[TagForDescribeSnapshotGroupsOutput]'
    }

    attribute_map = {
        'creation_time': 'CreationTime',
        'description': 'Description',
        'image_id': 'ImageId',
        'instance_id': 'InstanceId',
        'name': 'Name',
        'project_name': 'ProjectName',
        'snapshot_group_id': 'SnapshotGroupId',
        'snapshots': 'Snapshots',
        'status': 'Status',
        'tags': 'Tags'
    }

    def __init__(self, creation_time=None, description=None, image_id=None, instance_id=None, name=None, project_name=None, snapshot_group_id=None, snapshots=None, status=None, tags=None, _configuration=None):  # noqa: E501
        """SnapshotGroupForDescribeSnapshotGroupsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._creation_time = None
        self._description = None
        self._image_id = None
        self._instance_id = None
        self._name = None
        self._project_name = None
        self._snapshot_group_id = None
        self._snapshots = None
        self._status = None
        self._tags = None
        self.discriminator = None

        if creation_time is not None:
            self.creation_time = creation_time
        if description is not None:
            self.description = description
        if image_id is not None:
            self.image_id = image_id
        if instance_id is not None:
            self.instance_id = instance_id
        if name is not None:
            self.name = name
        if project_name is not None:
            self.project_name = project_name
        if snapshot_group_id is not None:
            self.snapshot_group_id = snapshot_group_id
        if snapshots is not None:
            self.snapshots = snapshots
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags

    @property
    def creation_time(self):
        """Gets the creation_time of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501


        :return: The creation_time of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this SnapshotGroupForDescribeSnapshotGroupsOutput.


        :param creation_time: The creation_time of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def description(self):
        """Gets the description of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501


        :return: The description of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SnapshotGroupForDescribeSnapshotGroupsOutput.


        :param description: The description of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def image_id(self):
        """Gets the image_id of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501


        :return: The image_id of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this SnapshotGroupForDescribeSnapshotGroupsOutput.


        :param image_id: The image_id of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501
        :type: str
        """

        self._image_id = image_id

    @property
    def instance_id(self):
        """Gets the instance_id of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501


        :return: The instance_id of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this SnapshotGroupForDescribeSnapshotGroupsOutput.


        :param instance_id: The instance_id of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def name(self):
        """Gets the name of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501


        :return: The name of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SnapshotGroupForDescribeSnapshotGroupsOutput.


        :param name: The name of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def project_name(self):
        """Gets the project_name of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501


        :return: The project_name of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this SnapshotGroupForDescribeSnapshotGroupsOutput.


        :param project_name: The project_name of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def snapshot_group_id(self):
        """Gets the snapshot_group_id of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501


        :return: The snapshot_group_id of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._snapshot_group_id

    @snapshot_group_id.setter
    def snapshot_group_id(self, snapshot_group_id):
        """Sets the snapshot_group_id of this SnapshotGroupForDescribeSnapshotGroupsOutput.


        :param snapshot_group_id: The snapshot_group_id of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501
        :type: str
        """

        self._snapshot_group_id = snapshot_group_id

    @property
    def snapshots(self):
        """Gets the snapshots of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501


        :return: The snapshots of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501
        :rtype: list[SnapshotForDescribeSnapshotGroupsOutput]
        """
        return self._snapshots

    @snapshots.setter
    def snapshots(self, snapshots):
        """Sets the snapshots of this SnapshotGroupForDescribeSnapshotGroupsOutput.


        :param snapshots: The snapshots of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501
        :type: list[SnapshotForDescribeSnapshotGroupsOutput]
        """

        self._snapshots = snapshots

    @property
    def status(self):
        """Gets the status of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501


        :return: The status of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SnapshotGroupForDescribeSnapshotGroupsOutput.


        :param status: The status of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501


        :return: The tags of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501
        :rtype: list[TagForDescribeSnapshotGroupsOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SnapshotGroupForDescribeSnapshotGroupsOutput.


        :param tags: The tags of this SnapshotGroupForDescribeSnapshotGroupsOutput.  # noqa: E501
        :type: list[TagForDescribeSnapshotGroupsOutput]
        """

        self._tags = tags

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
        if issubclass(SnapshotGroupForDescribeSnapshotGroupsOutput, dict):
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
        if not isinstance(other, SnapshotGroupForDescribeSnapshotGroupsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SnapshotGroupForDescribeSnapshotGroupsOutput):
            return True

        return self.to_dict() != other.to_dict()
