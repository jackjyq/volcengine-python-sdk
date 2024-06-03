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


class SnapshotForDescribeSnapshotsOutput(object):
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
        'progress': 'int',
        'project_name': 'str',
        'retention_days': 'int',
        'snapshot_group_id': 'str',
        'snapshot_id': 'str',
        'snapshot_name': 'str',
        'snapshot_type': 'str',
        'status': 'str',
        'tags': 'list[TagForDescribeSnapshotsOutput]',
        'volume_id': 'str',
        'volume_kind': 'str',
        'volume_name': 'str',
        'volume_size': 'int',
        'volume_status': 'str',
        'volume_type': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'creation_time': 'CreationTime',
        'description': 'Description',
        'image_id': 'ImageId',
        'progress': 'Progress',
        'project_name': 'ProjectName',
        'retention_days': 'RetentionDays',
        'snapshot_group_id': 'SnapshotGroupId',
        'snapshot_id': 'SnapshotId',
        'snapshot_name': 'SnapshotName',
        'snapshot_type': 'SnapshotType',
        'status': 'Status',
        'tags': 'Tags',
        'volume_id': 'VolumeId',
        'volume_kind': 'VolumeKind',
        'volume_name': 'VolumeName',
        'volume_size': 'VolumeSize',
        'volume_status': 'VolumeStatus',
        'volume_type': 'VolumeType',
        'zone_id': 'ZoneId'
    }

    def __init__(self, creation_time=None, description=None, image_id=None, progress=None, project_name=None, retention_days=None, snapshot_group_id=None, snapshot_id=None, snapshot_name=None, snapshot_type=None, status=None, tags=None, volume_id=None, volume_kind=None, volume_name=None, volume_size=None, volume_status=None, volume_type=None, zone_id=None, _configuration=None):  # noqa: E501
        """SnapshotForDescribeSnapshotsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._creation_time = None
        self._description = None
        self._image_id = None
        self._progress = None
        self._project_name = None
        self._retention_days = None
        self._snapshot_group_id = None
        self._snapshot_id = None
        self._snapshot_name = None
        self._snapshot_type = None
        self._status = None
        self._tags = None
        self._volume_id = None
        self._volume_kind = None
        self._volume_name = None
        self._volume_size = None
        self._volume_status = None
        self._volume_type = None
        self._zone_id = None
        self.discriminator = None

        if creation_time is not None:
            self.creation_time = creation_time
        if description is not None:
            self.description = description
        if image_id is not None:
            self.image_id = image_id
        if progress is not None:
            self.progress = progress
        if project_name is not None:
            self.project_name = project_name
        if retention_days is not None:
            self.retention_days = retention_days
        if snapshot_group_id is not None:
            self.snapshot_group_id = snapshot_group_id
        if snapshot_id is not None:
            self.snapshot_id = snapshot_id
        if snapshot_name is not None:
            self.snapshot_name = snapshot_name
        if snapshot_type is not None:
            self.snapshot_type = snapshot_type
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if volume_id is not None:
            self.volume_id = volume_id
        if volume_kind is not None:
            self.volume_kind = volume_kind
        if volume_name is not None:
            self.volume_name = volume_name
        if volume_size is not None:
            self.volume_size = volume_size
        if volume_status is not None:
            self.volume_status = volume_status
        if volume_type is not None:
            self.volume_type = volume_type
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def creation_time(self):
        """Gets the creation_time of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501


        :return: The creation_time of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this SnapshotForDescribeSnapshotsOutput.


        :param creation_time: The creation_time of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def description(self):
        """Gets the description of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501


        :return: The description of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SnapshotForDescribeSnapshotsOutput.


        :param description: The description of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def image_id(self):
        """Gets the image_id of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501


        :return: The image_id of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this SnapshotForDescribeSnapshotsOutput.


        :param image_id: The image_id of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :type: str
        """

        self._image_id = image_id

    @property
    def progress(self):
        """Gets the progress of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501


        :return: The progress of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this SnapshotForDescribeSnapshotsOutput.


        :param progress: The progress of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :type: int
        """

        self._progress = progress

    @property
    def project_name(self):
        """Gets the project_name of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501


        :return: The project_name of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this SnapshotForDescribeSnapshotsOutput.


        :param project_name: The project_name of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def retention_days(self):
        """Gets the retention_days of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501


        :return: The retention_days of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :rtype: int
        """
        return self._retention_days

    @retention_days.setter
    def retention_days(self, retention_days):
        """Sets the retention_days of this SnapshotForDescribeSnapshotsOutput.


        :param retention_days: The retention_days of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :type: int
        """

        self._retention_days = retention_days

    @property
    def snapshot_group_id(self):
        """Gets the snapshot_group_id of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501


        :return: The snapshot_group_id of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :rtype: str
        """
        return self._snapshot_group_id

    @snapshot_group_id.setter
    def snapshot_group_id(self, snapshot_group_id):
        """Sets the snapshot_group_id of this SnapshotForDescribeSnapshotsOutput.


        :param snapshot_group_id: The snapshot_group_id of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :type: str
        """

        self._snapshot_group_id = snapshot_group_id

    @property
    def snapshot_id(self):
        """Gets the snapshot_id of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501


        :return: The snapshot_id of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :rtype: str
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        """Sets the snapshot_id of this SnapshotForDescribeSnapshotsOutput.


        :param snapshot_id: The snapshot_id of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :type: str
        """

        self._snapshot_id = snapshot_id

    @property
    def snapshot_name(self):
        """Gets the snapshot_name of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501


        :return: The snapshot_name of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :rtype: str
        """
        return self._snapshot_name

    @snapshot_name.setter
    def snapshot_name(self, snapshot_name):
        """Sets the snapshot_name of this SnapshotForDescribeSnapshotsOutput.


        :param snapshot_name: The snapshot_name of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :type: str
        """

        self._snapshot_name = snapshot_name

    @property
    def snapshot_type(self):
        """Gets the snapshot_type of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501


        :return: The snapshot_type of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :rtype: str
        """
        return self._snapshot_type

    @snapshot_type.setter
    def snapshot_type(self, snapshot_type):
        """Sets the snapshot_type of this SnapshotForDescribeSnapshotsOutput.


        :param snapshot_type: The snapshot_type of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :type: str
        """

        self._snapshot_type = snapshot_type

    @property
    def status(self):
        """Gets the status of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501


        :return: The status of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SnapshotForDescribeSnapshotsOutput.


        :param status: The status of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501


        :return: The tags of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :rtype: list[TagForDescribeSnapshotsOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SnapshotForDescribeSnapshotsOutput.


        :param tags: The tags of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :type: list[TagForDescribeSnapshotsOutput]
        """

        self._tags = tags

    @property
    def volume_id(self):
        """Gets the volume_id of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501


        :return: The volume_id of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this SnapshotForDescribeSnapshotsOutput.


        :param volume_id: The volume_id of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :type: str
        """

        self._volume_id = volume_id

    @property
    def volume_kind(self):
        """Gets the volume_kind of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501


        :return: The volume_kind of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :rtype: str
        """
        return self._volume_kind

    @volume_kind.setter
    def volume_kind(self, volume_kind):
        """Sets the volume_kind of this SnapshotForDescribeSnapshotsOutput.


        :param volume_kind: The volume_kind of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :type: str
        """

        self._volume_kind = volume_kind

    @property
    def volume_name(self):
        """Gets the volume_name of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501


        :return: The volume_name of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :rtype: str
        """
        return self._volume_name

    @volume_name.setter
    def volume_name(self, volume_name):
        """Sets the volume_name of this SnapshotForDescribeSnapshotsOutput.


        :param volume_name: The volume_name of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :type: str
        """

        self._volume_name = volume_name

    @property
    def volume_size(self):
        """Gets the volume_size of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501


        :return: The volume_size of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :rtype: int
        """
        return self._volume_size

    @volume_size.setter
    def volume_size(self, volume_size):
        """Sets the volume_size of this SnapshotForDescribeSnapshotsOutput.


        :param volume_size: The volume_size of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :type: int
        """

        self._volume_size = volume_size

    @property
    def volume_status(self):
        """Gets the volume_status of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501


        :return: The volume_status of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :rtype: str
        """
        return self._volume_status

    @volume_status.setter
    def volume_status(self, volume_status):
        """Sets the volume_status of this SnapshotForDescribeSnapshotsOutput.


        :param volume_status: The volume_status of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :type: str
        """

        self._volume_status = volume_status

    @property
    def volume_type(self):
        """Gets the volume_type of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501


        :return: The volume_type of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this SnapshotForDescribeSnapshotsOutput.


        :param volume_type: The volume_type of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :type: str
        """

        self._volume_type = volume_type

    @property
    def zone_id(self):
        """Gets the zone_id of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501


        :return: The zone_id of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this SnapshotForDescribeSnapshotsOutput.


        :param zone_id: The zone_id of this SnapshotForDescribeSnapshotsOutput.  # noqa: E501
        :type: str
        """

        self._zone_id = zone_id

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
        if issubclass(SnapshotForDescribeSnapshotsOutput, dict):
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
        if not isinstance(other, SnapshotForDescribeSnapshotsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SnapshotForDescribeSnapshotsOutput):
            return True

        return self.to_dict() != other.to_dict()