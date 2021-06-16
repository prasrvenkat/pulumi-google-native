// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package v1

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Type of this accelerator.
type AcceleratorConfigType pulumi.String

const (
	// Accelerator type is not specified.
	AcceleratorConfigTypeAcceleratorTypeUnspecified = AcceleratorConfigType("ACCELERATOR_TYPE_UNSPECIFIED")
	// Accelerator type is Nvidia Tesla K80.
	AcceleratorConfigTypeNvidiaTeslaK80 = AcceleratorConfigType("NVIDIA_TESLA_K80")
	// Accelerator type is Nvidia Tesla P100.
	AcceleratorConfigTypeNvidiaTeslaP100 = AcceleratorConfigType("NVIDIA_TESLA_P100")
	// Accelerator type is Nvidia Tesla V100.
	AcceleratorConfigTypeNvidiaTeslaV100 = AcceleratorConfigType("NVIDIA_TESLA_V100")
	// Accelerator type is Nvidia Tesla P4.
	AcceleratorConfigTypeNvidiaTeslaP4 = AcceleratorConfigType("NVIDIA_TESLA_P4")
	// Accelerator type is Nvidia Tesla T4.
	AcceleratorConfigTypeNvidiaTeslaT4 = AcceleratorConfigType("NVIDIA_TESLA_T4")
	// Accelerator type is Nvidia Tesla A100.
	AcceleratorConfigTypeNvidiaTeslaA100 = AcceleratorConfigType("NVIDIA_TESLA_A100")
	// Accelerator type is NVIDIA Tesla T4 Virtual Workstations.
	AcceleratorConfigTypeNvidiaTeslaT4Vws = AcceleratorConfigType("NVIDIA_TESLA_T4_VWS")
	// Accelerator type is NVIDIA Tesla P100 Virtual Workstations.
	AcceleratorConfigTypeNvidiaTeslaP100Vws = AcceleratorConfigType("NVIDIA_TESLA_P100_VWS")
	// Accelerator type is NVIDIA Tesla P4 Virtual Workstations.
	AcceleratorConfigTypeNvidiaTeslaP4Vws = AcceleratorConfigType("NVIDIA_TESLA_P4_VWS")
	// (Coming soon) Accelerator type is TPU V2.
	AcceleratorConfigTypeTpuV2 = AcceleratorConfigType("TPU_V2")
	// (Coming soon) Accelerator type is TPU V3.
	AcceleratorConfigTypeTpuV3 = AcceleratorConfigType("TPU_V3")
)

func (AcceleratorConfigType) ElementType() reflect.Type {
	return reflect.TypeOf((*pulumi.String)(nil)).Elem()
}

func (e AcceleratorConfigType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e AcceleratorConfigType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e AcceleratorConfigType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e AcceleratorConfigType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

// Required. Scale tier of the hardware used for notebook execution.
type ExecutionTemplateScaleTier pulumi.String

const (
	// Unspecified Scale Tier.
	ExecutionTemplateScaleTierScaleTierUnspecified = ExecutionTemplateScaleTier("SCALE_TIER_UNSPECIFIED")
	// A single worker instance. This tier is suitable for learning how to use Cloud ML, and for experimenting with new models using small datasets.
	ExecutionTemplateScaleTierBasic = ExecutionTemplateScaleTier("BASIC")
	// Many workers and a few parameter servers.
	ExecutionTemplateScaleTierStandard1 = ExecutionTemplateScaleTier("STANDARD_1")
	// A large number of workers with many parameter servers.
	ExecutionTemplateScaleTierPremium1 = ExecutionTemplateScaleTier("PREMIUM_1")
	// A single worker instance with a K80 GPU.
	ExecutionTemplateScaleTierBasicGpu = ExecutionTemplateScaleTier("BASIC_GPU")
	// A single worker instance with a Cloud TPU.
	ExecutionTemplateScaleTierBasicTpu = ExecutionTemplateScaleTier("BASIC_TPU")
	// The CUSTOM tier is not a set tier, but rather enables you to use your own cluster specification. When you use this tier, set values to configure your processing cluster according to these guidelines: * You _must_ set `TrainingInput.masterType` to specify the type of machine to use for your master node. This is the only required setting. * You _may_ set `TrainingInput.workerCount` to specify the number of workers to use. If you specify one or more workers, you _must_ also set `TrainingInput.workerType` to specify the type of machine to use for your worker nodes. * You _may_ set `TrainingInput.parameterServerCount` to specify the number of parameter servers to use. If you specify one or more parameter servers, you _must_ also set `TrainingInput.parameterServerType` to specify the type of machine to use for your parameter servers. Note that all of your workers must use the same machine type, which can be different from your parameter server type and master type. Your parameter servers must likewise use the same machine type, which can be different from your worker type and master type.
	ExecutionTemplateScaleTierCustom = ExecutionTemplateScaleTier("CUSTOM")
)

func (ExecutionTemplateScaleTier) ElementType() reflect.Type {
	return reflect.TypeOf((*pulumi.String)(nil)).Elem()
}

func (e ExecutionTemplateScaleTier) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e ExecutionTemplateScaleTier) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e ExecutionTemplateScaleTier) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e ExecutionTemplateScaleTier) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

// Input only. The type of the boot disk attached to this instance, defaults to standard persistent disk (`PD_STANDARD`).
type InstanceBootDiskType pulumi.String

const (
	// Disk type not set.
	InstanceBootDiskTypeDiskTypeUnspecified = InstanceBootDiskType("DISK_TYPE_UNSPECIFIED")
	// Standard persistent disk type.
	InstanceBootDiskTypePdStandard = InstanceBootDiskType("PD_STANDARD")
	// SSD persistent disk type.
	InstanceBootDiskTypePdSsd = InstanceBootDiskType("PD_SSD")
	// Balanced persistent disk type.
	InstanceBootDiskTypePdBalanced = InstanceBootDiskType("PD_BALANCED")
)

func (InstanceBootDiskType) ElementType() reflect.Type {
	return reflect.TypeOf((*pulumi.String)(nil)).Elem()
}

func (e InstanceBootDiskType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e InstanceBootDiskType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e InstanceBootDiskType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e InstanceBootDiskType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

// Input only. The type of the data disk attached to this instance, defaults to standard persistent disk (`PD_STANDARD`).
type InstanceDataDiskType pulumi.String

const (
	// Disk type not set.
	InstanceDataDiskTypeDiskTypeUnspecified = InstanceDataDiskType("DISK_TYPE_UNSPECIFIED")
	// Standard persistent disk type.
	InstanceDataDiskTypePdStandard = InstanceDataDiskType("PD_STANDARD")
	// SSD persistent disk type.
	InstanceDataDiskTypePdSsd = InstanceDataDiskType("PD_SSD")
	// Balanced persistent disk type.
	InstanceDataDiskTypePdBalanced = InstanceDataDiskType("PD_BALANCED")
)

func (InstanceDataDiskType) ElementType() reflect.Type {
	return reflect.TypeOf((*pulumi.String)(nil)).Elem()
}

func (e InstanceDataDiskType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e InstanceDataDiskType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e InstanceDataDiskType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e InstanceDataDiskType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

// Input only. Disk encryption method used on the boot and data disks, defaults to GMEK.
type InstanceDiskEncryption pulumi.String

const (
	// Disk encryption is not specified.
	InstanceDiskEncryptionDiskEncryptionUnspecified = InstanceDiskEncryption("DISK_ENCRYPTION_UNSPECIFIED")
	// Use Google managed encryption keys to encrypt the boot disk.
	InstanceDiskEncryptionGmek = InstanceDiskEncryption("GMEK")
	// Use customer managed encryption keys to encrypt the boot disk.
	InstanceDiskEncryptionCmek = InstanceDiskEncryption("CMEK")
)

func (InstanceDiskEncryption) ElementType() reflect.Type {
	return reflect.TypeOf((*pulumi.String)(nil)).Elem()
}

func (e InstanceDiskEncryption) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e InstanceDiskEncryption) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e InstanceDiskEncryption) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e InstanceDiskEncryption) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

// Optional. The type of vNIC to be used on this interface. This may be gVNIC or VirtioNet.
type InstanceNicType pulumi.String

const (
	// No type specified.
	InstanceNicTypeUnspecifiedNicType = InstanceNicType("UNSPECIFIED_NIC_TYPE")
	// VIRTIO
	InstanceNicTypeVirtioNet = InstanceNicType("VIRTIO_NET")
	// GVNIC
	InstanceNicTypeGvnic = InstanceNicType("GVNIC")
)

func (InstanceNicType) ElementType() reflect.Type {
	return reflect.TypeOf((*pulumi.String)(nil)).Elem()
}

func (e InstanceNicType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e InstanceNicType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e InstanceNicType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e InstanceNicType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

// Input only. The type of the boot disk attached to this instance, defaults to standard persistent disk (`PD_STANDARD`).
type LocalDiskInitializeParamsDiskType pulumi.String

const (
	// Disk type not set.
	LocalDiskInitializeParamsDiskTypeDiskTypeUnspecified = LocalDiskInitializeParamsDiskType("DISK_TYPE_UNSPECIFIED")
	// Standard persistent disk type.
	LocalDiskInitializeParamsDiskTypePdStandard = LocalDiskInitializeParamsDiskType("PD_STANDARD")
	// SSD persistent disk type.
	LocalDiskInitializeParamsDiskTypePdSsd = LocalDiskInitializeParamsDiskType("PD_SSD")
	// Balanced persistent disk type.
	LocalDiskInitializeParamsDiskTypePdBalanced = LocalDiskInitializeParamsDiskType("PD_BALANCED")
)

func (LocalDiskInitializeParamsDiskType) ElementType() reflect.Type {
	return reflect.TypeOf((*pulumi.String)(nil)).Elem()
}

func (e LocalDiskInitializeParamsDiskType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e LocalDiskInitializeParamsDiskType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e LocalDiskInitializeParamsDiskType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e LocalDiskInitializeParamsDiskType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

// Accelerator model.
type RuntimeAcceleratorConfigType pulumi.String

const (
	// Accelerator type is not specified.
	RuntimeAcceleratorConfigTypeAcceleratorTypeUnspecified = RuntimeAcceleratorConfigType("ACCELERATOR_TYPE_UNSPECIFIED")
	// Accelerator type is Nvidia Tesla K80.
	RuntimeAcceleratorConfigTypeNvidiaTeslaK80 = RuntimeAcceleratorConfigType("NVIDIA_TESLA_K80")
	// Accelerator type is Nvidia Tesla P100.
	RuntimeAcceleratorConfigTypeNvidiaTeslaP100 = RuntimeAcceleratorConfigType("NVIDIA_TESLA_P100")
	// Accelerator type is Nvidia Tesla V100.
	RuntimeAcceleratorConfigTypeNvidiaTeslaV100 = RuntimeAcceleratorConfigType("NVIDIA_TESLA_V100")
	// Accelerator type is Nvidia Tesla P4.
	RuntimeAcceleratorConfigTypeNvidiaTeslaP4 = RuntimeAcceleratorConfigType("NVIDIA_TESLA_P4")
	// Accelerator type is Nvidia Tesla T4.
	RuntimeAcceleratorConfigTypeNvidiaTeslaT4 = RuntimeAcceleratorConfigType("NVIDIA_TESLA_T4")
	// Accelerator type is Nvidia Tesla A100.
	RuntimeAcceleratorConfigTypeNvidiaTeslaA100 = RuntimeAcceleratorConfigType("NVIDIA_TESLA_A100")
	// (Coming soon) Accelerator type is TPU V2.
	RuntimeAcceleratorConfigTypeTpuV2 = RuntimeAcceleratorConfigType("TPU_V2")
	// (Coming soon) Accelerator type is TPU V3.
	RuntimeAcceleratorConfigTypeTpuV3 = RuntimeAcceleratorConfigType("TPU_V3")
	// Accelerator type is NVIDIA Tesla T4 Virtual Workstations.
	RuntimeAcceleratorConfigTypeNvidiaTeslaT4Vws = RuntimeAcceleratorConfigType("NVIDIA_TESLA_T4_VWS")
	// Accelerator type is NVIDIA Tesla P100 Virtual Workstations.
	RuntimeAcceleratorConfigTypeNvidiaTeslaP100Vws = RuntimeAcceleratorConfigType("NVIDIA_TESLA_P100_VWS")
	// Accelerator type is NVIDIA Tesla P4 Virtual Workstations.
	RuntimeAcceleratorConfigTypeNvidiaTeslaP4Vws = RuntimeAcceleratorConfigType("NVIDIA_TESLA_P4_VWS")
)

func (RuntimeAcceleratorConfigType) ElementType() reflect.Type {
	return reflect.TypeOf((*pulumi.String)(nil)).Elem()
}

func (e RuntimeAcceleratorConfigType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e RuntimeAcceleratorConfigType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e RuntimeAcceleratorConfigType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e RuntimeAcceleratorConfigType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

// The type of access mode this instance.
type RuntimeAccessConfigAccessType pulumi.String

const (
	// Unspecified access.
	RuntimeAccessConfigAccessTypeRuntimeAccessTypeUnspecified = RuntimeAccessConfigAccessType("RUNTIME_ACCESS_TYPE_UNSPECIFIED")
	// Single user login.
	RuntimeAccessConfigAccessTypeSingleUser = RuntimeAccessConfigAccessType("SINGLE_USER")
)

func (RuntimeAccessConfigAccessType) ElementType() reflect.Type {
	return reflect.TypeOf((*pulumi.String)(nil)).Elem()
}

func (e RuntimeAccessConfigAccessType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e RuntimeAccessConfigAccessType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e RuntimeAccessConfigAccessType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e RuntimeAccessConfigAccessType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type ScheduleStateEnum pulumi.String

const (
	// Unspecified state.
	ScheduleStateEnumStateUnspecified = ScheduleStateEnum("STATE_UNSPECIFIED")
	// The job is executing normally.
	ScheduleStateEnumEnabled = ScheduleStateEnum("ENABLED")
	// The job is paused by the user. It will not execute. A user can intentionally pause the job using PauseJobRequest.
	ScheduleStateEnumPaused = ScheduleStateEnum("PAUSED")
	// The job is disabled by the system due to error. The user cannot directly set a job to be disabled.
	ScheduleStateEnumDisabled = ScheduleStateEnum("DISABLED")
	// The job state resulting from a failed CloudScheduler.UpdateJob operation. To recover a job from this state, retry CloudScheduler.UpdateJob until a successful response is received.
	ScheduleStateEnumUpdateFailed = ScheduleStateEnum("UPDATE_FAILED")
)

func (ScheduleStateEnum) ElementType() reflect.Type {
	return reflect.TypeOf((*pulumi.String)(nil)).Elem()
}

func (e ScheduleStateEnum) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e ScheduleStateEnum) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e ScheduleStateEnum) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e ScheduleStateEnum) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

// Type of this accelerator.
type SchedulerAcceleratorConfigType pulumi.String

const (
	// Unspecified accelerator type. Default to no GPU.
	SchedulerAcceleratorConfigTypeSchedulerAcceleratorTypeUnspecified = SchedulerAcceleratorConfigType("SCHEDULER_ACCELERATOR_TYPE_UNSPECIFIED")
	// Nvidia Tesla K80 GPU.
	SchedulerAcceleratorConfigTypeNvidiaTeslaK80 = SchedulerAcceleratorConfigType("NVIDIA_TESLA_K80")
	// Nvidia Tesla P100 GPU.
	SchedulerAcceleratorConfigTypeNvidiaTeslaP100 = SchedulerAcceleratorConfigType("NVIDIA_TESLA_P100")
	// Nvidia Tesla V100 GPU.
	SchedulerAcceleratorConfigTypeNvidiaTeslaV100 = SchedulerAcceleratorConfigType("NVIDIA_TESLA_V100")
	// Nvidia Tesla P4 GPU.
	SchedulerAcceleratorConfigTypeNvidiaTeslaP4 = SchedulerAcceleratorConfigType("NVIDIA_TESLA_P4")
	// Nvidia Tesla T4 GPU.
	SchedulerAcceleratorConfigTypeNvidiaTeslaT4 = SchedulerAcceleratorConfigType("NVIDIA_TESLA_T4")
	// TPU v2.
	SchedulerAcceleratorConfigTypeTpuV2 = SchedulerAcceleratorConfigType("TPU_V2")
	// TPU v3.
	SchedulerAcceleratorConfigTypeTpuV3 = SchedulerAcceleratorConfigType("TPU_V3")
)

func (SchedulerAcceleratorConfigType) ElementType() reflect.Type {
	return reflect.TypeOf((*pulumi.String)(nil)).Elem()
}

func (e SchedulerAcceleratorConfigType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e SchedulerAcceleratorConfigType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e SchedulerAcceleratorConfigType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e SchedulerAcceleratorConfigType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

// Action. Rolloback or Upgrade.
type UpgradeHistoryEntryAction pulumi.String

const (
	// Operation is not specified.
	UpgradeHistoryEntryActionActionUnspecified = UpgradeHistoryEntryAction("ACTION_UNSPECIFIED")
	// Upgrade.
	UpgradeHistoryEntryActionUpgrade = UpgradeHistoryEntryAction("UPGRADE")
	// Rollback.
	UpgradeHistoryEntryActionRollback = UpgradeHistoryEntryAction("ROLLBACK")
)

func (UpgradeHistoryEntryAction) ElementType() reflect.Type {
	return reflect.TypeOf((*pulumi.String)(nil)).Elem()
}

func (e UpgradeHistoryEntryAction) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e UpgradeHistoryEntryAction) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e UpgradeHistoryEntryAction) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e UpgradeHistoryEntryAction) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

// The state of this instance upgrade history entry.
type UpgradeHistoryEntryState pulumi.String

const (
	// State is not specified.
	UpgradeHistoryEntryStateStateUnspecified = UpgradeHistoryEntryState("STATE_UNSPECIFIED")
	// The instance upgrade is started.
	UpgradeHistoryEntryStateStarted = UpgradeHistoryEntryState("STARTED")
	// The instance upgrade is succeeded.
	UpgradeHistoryEntryStateSucceeded = UpgradeHistoryEntryState("SUCCEEDED")
	// The instance upgrade is failed.
	UpgradeHistoryEntryStateFailed = UpgradeHistoryEntryState("FAILED")
)

func (UpgradeHistoryEntryState) ElementType() reflect.Type {
	return reflect.TypeOf((*pulumi.String)(nil)).Elem()
}

func (e UpgradeHistoryEntryState) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e UpgradeHistoryEntryState) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e UpgradeHistoryEntryState) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e UpgradeHistoryEntryState) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

// Optional. The type of vNIC to be used on this interface. This may be gVNIC or VirtioNet.
type VirtualMachineConfigNicType pulumi.String

const (
	// No type specified.
	VirtualMachineConfigNicTypeUnspecifiedNicType = VirtualMachineConfigNicType("UNSPECIFIED_NIC_TYPE")
	// VIRTIO
	VirtualMachineConfigNicTypeVirtioNet = VirtualMachineConfigNicType("VIRTIO_NET")
	// GVNIC
	VirtualMachineConfigNicTypeGvnic = VirtualMachineConfigNicType("GVNIC")
)

func (VirtualMachineConfigNicType) ElementType() reflect.Type {
	return reflect.TypeOf((*pulumi.String)(nil)).Elem()
}

func (e VirtualMachineConfigNicType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e VirtualMachineConfigNicType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e VirtualMachineConfigNicType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e VirtualMachineConfigNicType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}