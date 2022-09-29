# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *

__all__ = [
    'GoogleCloudAssuredworkloadsV1beta1WorkloadCJISSettingsResponse',
    'GoogleCloudAssuredworkloadsV1beta1WorkloadComplianceStatusResponse',
    'GoogleCloudAssuredworkloadsV1beta1WorkloadFedrampHighSettingsResponse',
    'GoogleCloudAssuredworkloadsV1beta1WorkloadFedrampModerateSettingsResponse',
    'GoogleCloudAssuredworkloadsV1beta1WorkloadIL4SettingsResponse',
    'GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettingsResponse',
    'GoogleCloudAssuredworkloadsV1beta1WorkloadResourceInfoResponse',
    'GoogleCloudAssuredworkloadsV1beta1WorkloadResourceSettingsResponse',
    'GoogleCloudAssuredworkloadsV1beta1WorkloadSaaEnrollmentResponseResponse',
]

@pulumi.output_type
class GoogleCloudAssuredworkloadsV1beta1WorkloadCJISSettingsResponse(dict):
    """
    Settings specific to resources needed for CJIS.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "kmsSettings":
            suggest = "kms_settings"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GoogleCloudAssuredworkloadsV1beta1WorkloadCJISSettingsResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GoogleCloudAssuredworkloadsV1beta1WorkloadCJISSettingsResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GoogleCloudAssuredworkloadsV1beta1WorkloadCJISSettingsResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 kms_settings: 'outputs.GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettingsResponse'):
        """
        Settings specific to resources needed for CJIS.
        :param 'GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettingsResponse' kms_settings: Input only. Immutable. Settings used to create a CMEK crypto key.
        """
        pulumi.set(__self__, "kms_settings", kms_settings)

    @property
    @pulumi.getter(name="kmsSettings")
    def kms_settings(self) -> 'outputs.GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettingsResponse':
        """
        Input only. Immutable. Settings used to create a CMEK crypto key.
        """
        return pulumi.get(self, "kms_settings")


@pulumi.output_type
class GoogleCloudAssuredworkloadsV1beta1WorkloadComplianceStatusResponse(dict):
    """
    Represents the Compliance Status of this workload
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "acknowledgedViolationCount":
            suggest = "acknowledged_violation_count"
        elif key == "activeViolationCount":
            suggest = "active_violation_count"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GoogleCloudAssuredworkloadsV1beta1WorkloadComplianceStatusResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GoogleCloudAssuredworkloadsV1beta1WorkloadComplianceStatusResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GoogleCloudAssuredworkloadsV1beta1WorkloadComplianceStatusResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 acknowledged_violation_count: int,
                 active_violation_count: int):
        """
        Represents the Compliance Status of this workload
        :param int acknowledged_violation_count: Count of active Violations which are acknowledged in the Workload.
        :param int active_violation_count: Count of active Violations which haven't been acknowledged.
        """
        pulumi.set(__self__, "acknowledged_violation_count", acknowledged_violation_count)
        pulumi.set(__self__, "active_violation_count", active_violation_count)

    @property
    @pulumi.getter(name="acknowledgedViolationCount")
    def acknowledged_violation_count(self) -> int:
        """
        Count of active Violations which are acknowledged in the Workload.
        """
        return pulumi.get(self, "acknowledged_violation_count")

    @property
    @pulumi.getter(name="activeViolationCount")
    def active_violation_count(self) -> int:
        """
        Count of active Violations which haven't been acknowledged.
        """
        return pulumi.get(self, "active_violation_count")


@pulumi.output_type
class GoogleCloudAssuredworkloadsV1beta1WorkloadFedrampHighSettingsResponse(dict):
    """
    Settings specific to resources needed for FedRAMP High.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "kmsSettings":
            suggest = "kms_settings"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GoogleCloudAssuredworkloadsV1beta1WorkloadFedrampHighSettingsResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GoogleCloudAssuredworkloadsV1beta1WorkloadFedrampHighSettingsResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GoogleCloudAssuredworkloadsV1beta1WorkloadFedrampHighSettingsResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 kms_settings: 'outputs.GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettingsResponse'):
        """
        Settings specific to resources needed for FedRAMP High.
        :param 'GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettingsResponse' kms_settings: Input only. Immutable. Settings used to create a CMEK crypto key.
        """
        pulumi.set(__self__, "kms_settings", kms_settings)

    @property
    @pulumi.getter(name="kmsSettings")
    def kms_settings(self) -> 'outputs.GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettingsResponse':
        """
        Input only. Immutable. Settings used to create a CMEK crypto key.
        """
        return pulumi.get(self, "kms_settings")


@pulumi.output_type
class GoogleCloudAssuredworkloadsV1beta1WorkloadFedrampModerateSettingsResponse(dict):
    """
    Settings specific to resources needed for FedRAMP Moderate.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "kmsSettings":
            suggest = "kms_settings"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GoogleCloudAssuredworkloadsV1beta1WorkloadFedrampModerateSettingsResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GoogleCloudAssuredworkloadsV1beta1WorkloadFedrampModerateSettingsResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GoogleCloudAssuredworkloadsV1beta1WorkloadFedrampModerateSettingsResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 kms_settings: 'outputs.GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettingsResponse'):
        """
        Settings specific to resources needed for FedRAMP Moderate.
        :param 'GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettingsResponse' kms_settings: Input only. Immutable. Settings used to create a CMEK crypto key.
        """
        pulumi.set(__self__, "kms_settings", kms_settings)

    @property
    @pulumi.getter(name="kmsSettings")
    def kms_settings(self) -> 'outputs.GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettingsResponse':
        """
        Input only. Immutable. Settings used to create a CMEK crypto key.
        """
        return pulumi.get(self, "kms_settings")


@pulumi.output_type
class GoogleCloudAssuredworkloadsV1beta1WorkloadIL4SettingsResponse(dict):
    """
    Settings specific to resources needed for IL4.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "kmsSettings":
            suggest = "kms_settings"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GoogleCloudAssuredworkloadsV1beta1WorkloadIL4SettingsResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GoogleCloudAssuredworkloadsV1beta1WorkloadIL4SettingsResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GoogleCloudAssuredworkloadsV1beta1WorkloadIL4SettingsResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 kms_settings: 'outputs.GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettingsResponse'):
        """
        Settings specific to resources needed for IL4.
        :param 'GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettingsResponse' kms_settings: Input only. Immutable. Settings used to create a CMEK crypto key.
        """
        pulumi.set(__self__, "kms_settings", kms_settings)

    @property
    @pulumi.getter(name="kmsSettings")
    def kms_settings(self) -> 'outputs.GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettingsResponse':
        """
        Input only. Immutable. Settings used to create a CMEK crypto key.
        """
        return pulumi.get(self, "kms_settings")


@pulumi.output_type
class GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettingsResponse(dict):
    """
    Settings specific to the Key Management Service.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "nextRotationTime":
            suggest = "next_rotation_time"
        elif key == "rotationPeriod":
            suggest = "rotation_period"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettingsResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettingsResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettingsResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 next_rotation_time: str,
                 rotation_period: str):
        """
        Settings specific to the Key Management Service.
        :param str next_rotation_time: Input only. Immutable. The time at which the Key Management Service will automatically create a new version of the crypto key and mark it as the primary.
        :param str rotation_period: Input only. Immutable. [next_rotation_time] will be advanced by this period when the Key Management Service automatically rotates a key. Must be at least 24 hours and at most 876,000 hours.
        """
        pulumi.set(__self__, "next_rotation_time", next_rotation_time)
        pulumi.set(__self__, "rotation_period", rotation_period)

    @property
    @pulumi.getter(name="nextRotationTime")
    def next_rotation_time(self) -> str:
        """
        Input only. Immutable. The time at which the Key Management Service will automatically create a new version of the crypto key and mark it as the primary.
        """
        return pulumi.get(self, "next_rotation_time")

    @property
    @pulumi.getter(name="rotationPeriod")
    def rotation_period(self) -> str:
        """
        Input only. Immutable. [next_rotation_time] will be advanced by this period when the Key Management Service automatically rotates a key. Must be at least 24 hours and at most 876,000 hours.
        """
        return pulumi.get(self, "rotation_period")


@pulumi.output_type
class GoogleCloudAssuredworkloadsV1beta1WorkloadResourceInfoResponse(dict):
    """
    Represent the resources that are children of this Workload.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "resourceId":
            suggest = "resource_id"
        elif key == "resourceType":
            suggest = "resource_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GoogleCloudAssuredworkloadsV1beta1WorkloadResourceInfoResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GoogleCloudAssuredworkloadsV1beta1WorkloadResourceInfoResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GoogleCloudAssuredworkloadsV1beta1WorkloadResourceInfoResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 resource_id: str,
                 resource_type: str):
        """
        Represent the resources that are children of this Workload.
        :param str resource_id: Resource identifier. For a project this represents project_number.
        :param str resource_type: Indicates the type of resource.
        """
        pulumi.set(__self__, "resource_id", resource_id)
        pulumi.set(__self__, "resource_type", resource_type)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> str:
        """
        Resource identifier. For a project this represents project_number.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> str:
        """
        Indicates the type of resource.
        """
        return pulumi.get(self, "resource_type")


@pulumi.output_type
class GoogleCloudAssuredworkloadsV1beta1WorkloadResourceSettingsResponse(dict):
    """
    Represent the custom settings for the resources to be created.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "displayName":
            suggest = "display_name"
        elif key == "resourceId":
            suggest = "resource_id"
        elif key == "resourceType":
            suggest = "resource_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GoogleCloudAssuredworkloadsV1beta1WorkloadResourceSettingsResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GoogleCloudAssuredworkloadsV1beta1WorkloadResourceSettingsResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GoogleCloudAssuredworkloadsV1beta1WorkloadResourceSettingsResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 display_name: str,
                 resource_id: str,
                 resource_type: str):
        """
        Represent the custom settings for the resources to be created.
        :param str display_name: User-assigned resource display name. If not empty it will be used to create a resource with the specified name.
        :param str resource_id: Resource identifier. For a project this represents project_id. If the project is already taken, the workload creation will fail. For KeyRing, this represents the keyring_id. For a folder, don't set this value as folder_id is assigned by Google.
        :param str resource_type: Indicates the type of resource. This field should be specified to correspond the id to the right project type (CONSUMER_PROJECT or ENCRYPTION_KEYS_PROJECT)
        """
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "resource_id", resource_id)
        pulumi.set(__self__, "resource_type", resource_type)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        User-assigned resource display name. If not empty it will be used to create a resource with the specified name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> str:
        """
        Resource identifier. For a project this represents project_id. If the project is already taken, the workload creation will fail. For KeyRing, this represents the keyring_id. For a folder, don't set this value as folder_id is assigned by Google.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> str:
        """
        Indicates the type of resource. This field should be specified to correspond the id to the right project type (CONSUMER_PROJECT or ENCRYPTION_KEYS_PROJECT)
        """
        return pulumi.get(self, "resource_type")


@pulumi.output_type
class GoogleCloudAssuredworkloadsV1beta1WorkloadSaaEnrollmentResponseResponse(dict):
    """
    Signed Access Approvals (SAA) enrollment response.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "setupErrors":
            suggest = "setup_errors"
        elif key == "setupStatus":
            suggest = "setup_status"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GoogleCloudAssuredworkloadsV1beta1WorkloadSaaEnrollmentResponseResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GoogleCloudAssuredworkloadsV1beta1WorkloadSaaEnrollmentResponseResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GoogleCloudAssuredworkloadsV1beta1WorkloadSaaEnrollmentResponseResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 setup_errors: Sequence[str],
                 setup_status: str):
        """
        Signed Access Approvals (SAA) enrollment response.
        :param Sequence[str] setup_errors: Indicates SAA enrollment setup error if any.
        :param str setup_status: Indicates SAA enrollment status of a given workload.
        """
        pulumi.set(__self__, "setup_errors", setup_errors)
        pulumi.set(__self__, "setup_status", setup_status)

    @property
    @pulumi.getter(name="setupErrors")
    def setup_errors(self) -> Sequence[str]:
        """
        Indicates SAA enrollment setup error if any.
        """
        return pulumi.get(self, "setup_errors")

    @property
    @pulumi.getter(name="setupStatus")
    def setup_status(self) -> str:
        """
        Indicates SAA enrollment status of a given workload.
        """
        return pulumi.get(self, "setup_status")

