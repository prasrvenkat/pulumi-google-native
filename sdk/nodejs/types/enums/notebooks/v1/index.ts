// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const AcceleratorConfigType = {
    /**
     * Accelerator type is not specified.
     */
    AcceleratorTypeUnspecified: "ACCELERATOR_TYPE_UNSPECIFIED",
    /**
     * Accelerator type is Nvidia Tesla K80.
     */
    NvidiaTeslaK80: "NVIDIA_TESLA_K80",
    /**
     * Accelerator type is Nvidia Tesla P100.
     */
    NvidiaTeslaP100: "NVIDIA_TESLA_P100",
    /**
     * Accelerator type is Nvidia Tesla V100.
     */
    NvidiaTeslaV100: "NVIDIA_TESLA_V100",
    /**
     * Accelerator type is Nvidia Tesla P4.
     */
    NvidiaTeslaP4: "NVIDIA_TESLA_P4",
    /**
     * Accelerator type is Nvidia Tesla T4.
     */
    NvidiaTeslaT4: "NVIDIA_TESLA_T4",
    /**
     * Accelerator type is Nvidia Tesla A100.
     */
    NvidiaTeslaA100: "NVIDIA_TESLA_A100",
    /**
     * Accelerator type is Nvidia Tesla L4.
     */
    NvidiaL4: "NVIDIA_L4",
    /**
     * Accelerator type is NVIDIA Tesla T4 Virtual Workstations.
     */
    NvidiaTeslaT4Vws: "NVIDIA_TESLA_T4_VWS",
    /**
     * Accelerator type is NVIDIA Tesla P100 Virtual Workstations.
     */
    NvidiaTeslaP100Vws: "NVIDIA_TESLA_P100_VWS",
    /**
     * Accelerator type is NVIDIA Tesla P4 Virtual Workstations.
     */
    NvidiaTeslaP4Vws: "NVIDIA_TESLA_P4_VWS",
    /**
     * (Coming soon) Accelerator type is TPU V2.
     */
    TpuV2: "TPU_V2",
    /**
     * (Coming soon) Accelerator type is TPU V3.
     */
    TpuV3: "TPU_V3",
} as const;

/**
 * Type of this accelerator.
 */
export type AcceleratorConfigType = (typeof AcceleratorConfigType)[keyof typeof AcceleratorConfigType];

export const ExecutionTemplateJobType = {
    /**
     * No type specified.
     */
    JobTypeUnspecified: "JOB_TYPE_UNSPECIFIED",
    /**
     * Custom Job in `aiplatform.googleapis.com`. Default value for an execution.
     */
    VertexAi: "VERTEX_AI",
    /**
     * Run execution on a cluster with Dataproc as a job. https://cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.jobs
     */
    Dataproc: "DATAPROC",
} as const;

/**
 * The type of Job to be used on this execution.
 */
export type ExecutionTemplateJobType = (typeof ExecutionTemplateJobType)[keyof typeof ExecutionTemplateJobType];

export const ExecutionTemplateScaleTier = {
    /**
     * Unspecified Scale Tier.
     */
    ScaleTierUnspecified: "SCALE_TIER_UNSPECIFIED",
    /**
     * A single worker instance. This tier is suitable for learning how to use Cloud ML, and for experimenting with new models using small datasets.
     */
    Basic: "BASIC",
    /**
     * Many workers and a few parameter servers.
     */
    Standard1: "STANDARD_1",
    /**
     * A large number of workers with many parameter servers.
     */
    Premium1: "PREMIUM_1",
    /**
     * A single worker instance with a K80 GPU.
     */
    BasicGpu: "BASIC_GPU",
    /**
     * A single worker instance with a Cloud TPU.
     */
    BasicTpu: "BASIC_TPU",
    /**
     * The CUSTOM tier is not a set tier, but rather enables you to use your own cluster specification. When you use this tier, set values to configure your processing cluster according to these guidelines: * You _must_ set `ExecutionTemplate.masterType` to specify the type of machine to use for your master node. This is the only required setting.
     */
    Custom: "CUSTOM",
} as const;

/**
 * Required. Scale tier of the hardware used for notebook execution. DEPRECATED Will be discontinued. As right now only CUSTOM is supported.
 */
export type ExecutionTemplateScaleTier = (typeof ExecutionTemplateScaleTier)[keyof typeof ExecutionTemplateScaleTier];

export const InstanceBootDiskType = {
    /**
     * Disk type not set.
     */
    DiskTypeUnspecified: "DISK_TYPE_UNSPECIFIED",
    /**
     * Standard persistent disk type.
     */
    PdStandard: "PD_STANDARD",
    /**
     * SSD persistent disk type.
     */
    PdSsd: "PD_SSD",
    /**
     * Balanced persistent disk type.
     */
    PdBalanced: "PD_BALANCED",
    /**
     * Extreme persistent disk type.
     */
    PdExtreme: "PD_EXTREME",
} as const;

/**
 * Input only. The type of the boot disk attached to this instance, defaults to standard persistent disk (`PD_STANDARD`).
 */
export type InstanceBootDiskType = (typeof InstanceBootDiskType)[keyof typeof InstanceBootDiskType];

export const InstanceDataDiskType = {
    /**
     * Disk type not set.
     */
    DiskTypeUnspecified: "DISK_TYPE_UNSPECIFIED",
    /**
     * Standard persistent disk type.
     */
    PdStandard: "PD_STANDARD",
    /**
     * SSD persistent disk type.
     */
    PdSsd: "PD_SSD",
    /**
     * Balanced persistent disk type.
     */
    PdBalanced: "PD_BALANCED",
    /**
     * Extreme persistent disk type.
     */
    PdExtreme: "PD_EXTREME",
} as const;

/**
 * Input only. The type of the data disk attached to this instance, defaults to standard persistent disk (`PD_STANDARD`).
 */
export type InstanceDataDiskType = (typeof InstanceDataDiskType)[keyof typeof InstanceDataDiskType];

export const InstanceDiskEncryption = {
    /**
     * Disk encryption is not specified.
     */
    DiskEncryptionUnspecified: "DISK_ENCRYPTION_UNSPECIFIED",
    /**
     * Use Google managed encryption keys to encrypt the boot disk.
     */
    Gmek: "GMEK",
    /**
     * Use customer managed encryption keys to encrypt the boot disk.
     */
    Cmek: "CMEK",
} as const;

/**
 * Input only. Disk encryption method used on the boot and data disks, defaults to GMEK.
 */
export type InstanceDiskEncryption = (typeof InstanceDiskEncryption)[keyof typeof InstanceDiskEncryption];

export const InstanceNicType = {
    /**
     * No type specified.
     */
    UnspecifiedNicType: "UNSPECIFIED_NIC_TYPE",
    /**
     * VIRTIO
     */
    VirtioNet: "VIRTIO_NET",
    /**
     * GVNIC
     */
    Gvnic: "GVNIC",
} as const;

/**
 * Optional. The type of vNIC to be used on this interface. This may be gVNIC or VirtioNet.
 */
export type InstanceNicType = (typeof InstanceNicType)[keyof typeof InstanceNicType];

export const LocalDiskInitializeParamsDiskType = {
    /**
     * Disk type not set.
     */
    DiskTypeUnspecified: "DISK_TYPE_UNSPECIFIED",
    /**
     * Standard persistent disk type.
     */
    PdStandard: "PD_STANDARD",
    /**
     * SSD persistent disk type.
     */
    PdSsd: "PD_SSD",
    /**
     * Balanced persistent disk type.
     */
    PdBalanced: "PD_BALANCED",
    /**
     * Extreme persistent disk type.
     */
    PdExtreme: "PD_EXTREME",
} as const;

/**
 * Input only. The type of the boot disk attached to this instance, defaults to standard persistent disk (`PD_STANDARD`).
 */
export type LocalDiskInitializeParamsDiskType = (typeof LocalDiskInitializeParamsDiskType)[keyof typeof LocalDiskInitializeParamsDiskType];

export const ReservationAffinityConsumeReservationType = {
    /**
     * Default type.
     */
    TypeUnspecified: "TYPE_UNSPECIFIED",
    /**
     * Do not consume from any allocated capacity.
     */
    NoReservation: "NO_RESERVATION",
    /**
     * Consume any reservation available.
     */
    AnyReservation: "ANY_RESERVATION",
    /**
     * Must consume from a specific reservation. Must specify key value fields for specifying the reservations.
     */
    SpecificReservation: "SPECIFIC_RESERVATION",
} as const;

/**
 * Optional. Type of reservation to consume
 */
export type ReservationAffinityConsumeReservationType = (typeof ReservationAffinityConsumeReservationType)[keyof typeof ReservationAffinityConsumeReservationType];

export const RuntimeAcceleratorConfigType = {
    /**
     * Accelerator type is not specified.
     */
    AcceleratorTypeUnspecified: "ACCELERATOR_TYPE_UNSPECIFIED",
    /**
     * Accelerator type is Nvidia Tesla K80.
     */
    NvidiaTeslaK80: "NVIDIA_TESLA_K80",
    /**
     * Accelerator type is Nvidia Tesla P100.
     */
    NvidiaTeslaP100: "NVIDIA_TESLA_P100",
    /**
     * Accelerator type is Nvidia Tesla V100.
     */
    NvidiaTeslaV100: "NVIDIA_TESLA_V100",
    /**
     * Accelerator type is Nvidia Tesla P4.
     */
    NvidiaTeslaP4: "NVIDIA_TESLA_P4",
    /**
     * Accelerator type is Nvidia Tesla T4.
     */
    NvidiaTeslaT4: "NVIDIA_TESLA_T4",
    /**
     * Accelerator type is Nvidia Tesla A100 - 40GB.
     */
    NvidiaTeslaA100: "NVIDIA_TESLA_A100",
    /**
     * Accelerator type is Nvidia L4.
     */
    NvidiaL4: "NVIDIA_L4",
    /**
     * (Coming soon) Accelerator type is TPU V2.
     */
    TpuV2: "TPU_V2",
    /**
     * (Coming soon) Accelerator type is TPU V3.
     */
    TpuV3: "TPU_V3",
    /**
     * Accelerator type is NVIDIA Tesla T4 Virtual Workstations.
     */
    NvidiaTeslaT4Vws: "NVIDIA_TESLA_T4_VWS",
    /**
     * Accelerator type is NVIDIA Tesla P100 Virtual Workstations.
     */
    NvidiaTeslaP100Vws: "NVIDIA_TESLA_P100_VWS",
    /**
     * Accelerator type is NVIDIA Tesla P4 Virtual Workstations.
     */
    NvidiaTeslaP4Vws: "NVIDIA_TESLA_P4_VWS",
} as const;

/**
 * Accelerator model.
 */
export type RuntimeAcceleratorConfigType = (typeof RuntimeAcceleratorConfigType)[keyof typeof RuntimeAcceleratorConfigType];

export const RuntimeAccessConfigAccessType = {
    /**
     * Unspecified access.
     */
    RuntimeAccessTypeUnspecified: "RUNTIME_ACCESS_TYPE_UNSPECIFIED",
    /**
     * Single user login.
     */
    SingleUser: "SINGLE_USER",
    /**
     * Service Account mode. In Service Account mode, Runtime creator will specify a SA that exists in the consumer project. Using Runtime Service Account field. Users accessing the Runtime need ActAs (Service Account User) permission.
     */
    ServiceAccount: "SERVICE_ACCOUNT",
} as const;

/**
 * The type of access mode this instance.
 */
export type RuntimeAccessConfigAccessType = (typeof RuntimeAccessConfigAccessType)[keyof typeof RuntimeAccessConfigAccessType];

export const RuntimeSoftwareConfigPostStartupScriptBehavior = {
    /**
     * Unspecified post startup script behavior. Will run only once at creation.
     */
    PostStartupScriptBehaviorUnspecified: "POST_STARTUP_SCRIPT_BEHAVIOR_UNSPECIFIED",
    /**
     * Runs the post startup script provided during creation at every start.
     */
    RunEveryStart: "RUN_EVERY_START",
    /**
     * Downloads and runs the provided post startup script at every start.
     */
    DownloadAndRunEveryStart: "DOWNLOAD_AND_RUN_EVERY_START",
} as const;

/**
 * Behavior for the post startup script.
 */
export type RuntimeSoftwareConfigPostStartupScriptBehavior = (typeof RuntimeSoftwareConfigPostStartupScriptBehavior)[keyof typeof RuntimeSoftwareConfigPostStartupScriptBehavior];

export const ScheduleState = {
    /**
     * Unspecified state.
     */
    StateUnspecified: "STATE_UNSPECIFIED",
    /**
     * The job is executing normally.
     */
    Enabled: "ENABLED",
    /**
     * The job is paused by the user. It will not execute. A user can intentionally pause the job using PauseJobRequest.
     */
    Paused: "PAUSED",
    /**
     * The job is disabled by the system due to error. The user cannot directly set a job to be disabled.
     */
    Disabled: "DISABLED",
    /**
     * The job state resulting from a failed CloudScheduler.UpdateJob operation. To recover a job from this state, retry CloudScheduler.UpdateJob until a successful response is received.
     */
    UpdateFailed: "UPDATE_FAILED",
    /**
     * The schedule resource is being created.
     */
    Initializing: "INITIALIZING",
    /**
     * The schedule resource is being deleted.
     */
    Deleting: "DELETING",
} as const;

export type ScheduleState = (typeof ScheduleState)[keyof typeof ScheduleState];

export const SchedulerAcceleratorConfigType = {
    /**
     * Unspecified accelerator type. Default to no GPU.
     */
    SchedulerAcceleratorTypeUnspecified: "SCHEDULER_ACCELERATOR_TYPE_UNSPECIFIED",
    /**
     * Nvidia Tesla K80 GPU.
     */
    NvidiaTeslaK80: "NVIDIA_TESLA_K80",
    /**
     * Nvidia Tesla P100 GPU.
     */
    NvidiaTeslaP100: "NVIDIA_TESLA_P100",
    /**
     * Nvidia Tesla V100 GPU.
     */
    NvidiaTeslaV100: "NVIDIA_TESLA_V100",
    /**
     * Nvidia Tesla P4 GPU.
     */
    NvidiaTeslaP4: "NVIDIA_TESLA_P4",
    /**
     * Nvidia Tesla T4 GPU.
     */
    NvidiaTeslaT4: "NVIDIA_TESLA_T4",
    /**
     * Nvidia Tesla A100 GPU.
     */
    NvidiaTeslaA100: "NVIDIA_TESLA_A100",
    /**
     * TPU v2.
     */
    TpuV2: "TPU_V2",
    /**
     * TPU v3.
     */
    TpuV3: "TPU_V3",
} as const;

/**
 * Type of this accelerator.
 */
export type SchedulerAcceleratorConfigType = (typeof SchedulerAcceleratorConfigType)[keyof typeof SchedulerAcceleratorConfigType];

export const UpgradeHistoryEntryAction = {
    /**
     * Operation is not specified.
     */
    ActionUnspecified: "ACTION_UNSPECIFIED",
    /**
     * Upgrade.
     */
    Upgrade: "UPGRADE",
    /**
     * Rollback.
     */
    Rollback: "ROLLBACK",
} as const;

/**
 * Action. Rolloback or Upgrade.
 */
export type UpgradeHistoryEntryAction = (typeof UpgradeHistoryEntryAction)[keyof typeof UpgradeHistoryEntryAction];

export const UpgradeHistoryEntryState = {
    /**
     * State is not specified.
     */
    StateUnspecified: "STATE_UNSPECIFIED",
    /**
     * The instance upgrade is started.
     */
    Started: "STARTED",
    /**
     * The instance upgrade is succeeded.
     */
    Succeeded: "SUCCEEDED",
    /**
     * The instance upgrade is failed.
     */
    Failed: "FAILED",
} as const;

/**
 * The state of this instance upgrade history entry.
 */
export type UpgradeHistoryEntryState = (typeof UpgradeHistoryEntryState)[keyof typeof UpgradeHistoryEntryState];

export const VirtualMachineConfigNicType = {
    /**
     * No type specified.
     */
    UnspecifiedNicType: "UNSPECIFIED_NIC_TYPE",
    /**
     * VIRTIO
     */
    VirtioNet: "VIRTIO_NET",
    /**
     * GVNIC
     */
    Gvnic: "GVNIC",
} as const;

/**
 * Optional. The type of vNIC to be used on this interface. This may be gVNIC or VirtioNet.
 */
export type VirtualMachineConfigNicType = (typeof VirtualMachineConfigNicType)[keyof typeof VirtualMachineConfigNicType];
