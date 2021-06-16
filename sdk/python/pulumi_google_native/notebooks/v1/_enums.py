# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AcceleratorConfigType',
    'ExecutionTemplateScaleTier',
    'InstanceBootDiskType',
    'InstanceDataDiskType',
    'InstanceDiskEncryption',
    'InstanceNicType',
    'LocalDiskInitializeParamsDiskType',
    'RuntimeAcceleratorConfigType',
    'RuntimeAccessConfigAccessType',
    'ScheduleState',
    'SchedulerAcceleratorConfigType',
    'UpgradeHistoryEntryAction',
    'UpgradeHistoryEntryState',
    'VirtualMachineConfigNicType',
]


class AcceleratorConfigType(str, Enum):
    """
    Type of this accelerator.
    """
    ACCELERATOR_TYPE_UNSPECIFIED = "ACCELERATOR_TYPE_UNSPECIFIED"
    NVIDIA_TESLA_K80 = "NVIDIA_TESLA_K80"
    NVIDIA_TESLA_P100 = "NVIDIA_TESLA_P100"
    NVIDIA_TESLA_V100 = "NVIDIA_TESLA_V100"
    NVIDIA_TESLA_P4 = "NVIDIA_TESLA_P4"
    NVIDIA_TESLA_T4 = "NVIDIA_TESLA_T4"
    NVIDIA_TESLA_A100 = "NVIDIA_TESLA_A100"
    NVIDIA_TESLA_T4_VWS = "NVIDIA_TESLA_T4_VWS"
    NVIDIA_TESLA_P100_VWS = "NVIDIA_TESLA_P100_VWS"
    NVIDIA_TESLA_P4_VWS = "NVIDIA_TESLA_P4_VWS"
    TPU_V2 = "TPU_V2"
    TPU_V3 = "TPU_V3"


class ExecutionTemplateScaleTier(str, Enum):
    """
    Required. Scale tier of the hardware used for notebook execution.
    """
    SCALE_TIER_UNSPECIFIED = "SCALE_TIER_UNSPECIFIED"
    BASIC = "BASIC"
    STANDARD1 = "STANDARD_1"
    PREMIUM1 = "PREMIUM_1"
    BASIC_GPU = "BASIC_GPU"
    BASIC_TPU = "BASIC_TPU"
    CUSTOM = "CUSTOM"


class InstanceBootDiskType(str, Enum):
    """
    Input only. The type of the boot disk attached to this instance, defaults to standard persistent disk (`PD_STANDARD`).
    """
    DISK_TYPE_UNSPECIFIED = "DISK_TYPE_UNSPECIFIED"
    PD_STANDARD = "PD_STANDARD"
    PD_SSD = "PD_SSD"
    PD_BALANCED = "PD_BALANCED"


class InstanceDataDiskType(str, Enum):
    """
    Input only. The type of the data disk attached to this instance, defaults to standard persistent disk (`PD_STANDARD`).
    """
    DISK_TYPE_UNSPECIFIED = "DISK_TYPE_UNSPECIFIED"
    PD_STANDARD = "PD_STANDARD"
    PD_SSD = "PD_SSD"
    PD_BALANCED = "PD_BALANCED"


class InstanceDiskEncryption(str, Enum):
    """
    Input only. Disk encryption method used on the boot and data disks, defaults to GMEK.
    """
    DISK_ENCRYPTION_UNSPECIFIED = "DISK_ENCRYPTION_UNSPECIFIED"
    GMEK = "GMEK"
    CMEK = "CMEK"


class InstanceNicType(str, Enum):
    """
    Optional. The type of vNIC to be used on this interface. This may be gVNIC or VirtioNet.
    """
    UNSPECIFIED_NIC_TYPE = "UNSPECIFIED_NIC_TYPE"
    VIRTIO_NET = "VIRTIO_NET"
    GVNIC = "GVNIC"


class LocalDiskInitializeParamsDiskType(str, Enum):
    """
    Input only. The type of the boot disk attached to this instance, defaults to standard persistent disk (`PD_STANDARD`).
    """
    DISK_TYPE_UNSPECIFIED = "DISK_TYPE_UNSPECIFIED"
    PD_STANDARD = "PD_STANDARD"
    PD_SSD = "PD_SSD"
    PD_BALANCED = "PD_BALANCED"


class RuntimeAcceleratorConfigType(str, Enum):
    """
    Accelerator model.
    """
    ACCELERATOR_TYPE_UNSPECIFIED = "ACCELERATOR_TYPE_UNSPECIFIED"
    NVIDIA_TESLA_K80 = "NVIDIA_TESLA_K80"
    NVIDIA_TESLA_P100 = "NVIDIA_TESLA_P100"
    NVIDIA_TESLA_V100 = "NVIDIA_TESLA_V100"
    NVIDIA_TESLA_P4 = "NVIDIA_TESLA_P4"
    NVIDIA_TESLA_T4 = "NVIDIA_TESLA_T4"
    NVIDIA_TESLA_A100 = "NVIDIA_TESLA_A100"
    TPU_V2 = "TPU_V2"
    TPU_V3 = "TPU_V3"
    NVIDIA_TESLA_T4_VWS = "NVIDIA_TESLA_T4_VWS"
    NVIDIA_TESLA_P100_VWS = "NVIDIA_TESLA_P100_VWS"
    NVIDIA_TESLA_P4_VWS = "NVIDIA_TESLA_P4_VWS"


class RuntimeAccessConfigAccessType(str, Enum):
    """
    The type of access mode this instance.
    """
    RUNTIME_ACCESS_TYPE_UNSPECIFIED = "RUNTIME_ACCESS_TYPE_UNSPECIFIED"
    SINGLE_USER = "SINGLE_USER"


class ScheduleState(str, Enum):
    STATE_UNSPECIFIED = "STATE_UNSPECIFIED"
    ENABLED = "ENABLED"
    PAUSED = "PAUSED"
    DISABLED = "DISABLED"
    UPDATE_FAILED = "UPDATE_FAILED"


class SchedulerAcceleratorConfigType(str, Enum):
    """
    Type of this accelerator.
    """
    SCHEDULER_ACCELERATOR_TYPE_UNSPECIFIED = "SCHEDULER_ACCELERATOR_TYPE_UNSPECIFIED"
    NVIDIA_TESLA_K80 = "NVIDIA_TESLA_K80"
    NVIDIA_TESLA_P100 = "NVIDIA_TESLA_P100"
    NVIDIA_TESLA_V100 = "NVIDIA_TESLA_V100"
    NVIDIA_TESLA_P4 = "NVIDIA_TESLA_P4"
    NVIDIA_TESLA_T4 = "NVIDIA_TESLA_T4"
    TPU_V2 = "TPU_V2"
    TPU_V3 = "TPU_V3"


class UpgradeHistoryEntryAction(str, Enum):
    """
    Action. Rolloback or Upgrade.
    """
    ACTION_UNSPECIFIED = "ACTION_UNSPECIFIED"
    UPGRADE = "UPGRADE"
    ROLLBACK = "ROLLBACK"


class UpgradeHistoryEntryState(str, Enum):
    """
    The state of this instance upgrade history entry.
    """
    STATE_UNSPECIFIED = "STATE_UNSPECIFIED"
    STARTED = "STARTED"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class VirtualMachineConfigNicType(str, Enum):
    """
    Optional. The type of vNIC to be used on this interface. This may be gVNIC or VirtioNet.
    """
    UNSPECIFIED_NIC_TYPE = "UNSPECIFIED_NIC_TYPE"
    VIRTIO_NET = "VIRTIO_NET"
    GVNIC = "GVNIC"