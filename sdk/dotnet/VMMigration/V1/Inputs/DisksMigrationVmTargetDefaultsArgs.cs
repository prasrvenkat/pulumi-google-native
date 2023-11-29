// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.VMMigration.V1.Inputs
{

    /// <summary>
    /// Details for creation of a VM that migrated data disks will be attached to.
    /// </summary>
    public sealed class DisksMigrationVmTargetDefaultsArgs : global::Pulumi.ResourceArgs
    {
        [Input("additionalLicenses")]
        private InputList<string>? _additionalLicenses;

        /// <summary>
        /// Optional. Additional licenses to assign to the VM.
        /// </summary>
        public InputList<string> AdditionalLicenses
        {
            get => _additionalLicenses ?? (_additionalLicenses = new InputList<string>());
            set => _additionalLicenses = value;
        }

        /// <summary>
        /// Optional. Details of the boot disk of the VM.
        /// </summary>
        [Input("bootDiskDefaults")]
        public Input<Inputs.BootDiskDefaultsArgs>? BootDiskDefaults { get; set; }

        /// <summary>
        /// Optional. Compute instance scheduling information (if empty default is used).
        /// </summary>
        [Input("computeScheduling")]
        public Input<Inputs.ComputeSchedulingArgs>? ComputeScheduling { get; set; }

        /// <summary>
        /// Optional. The encryption to apply to the VM.
        /// </summary>
        [Input("encryption")]
        public Input<Inputs.EncryptionArgs>? Encryption { get; set; }

        /// <summary>
        /// Optional. The hostname to assign to the VM.
        /// </summary>
        [Input("hostname")]
        public Input<string>? Hostname { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// Optional. A map of labels to associate with the VM.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        /// <summary>
        /// The machine type to create the VM with.
        /// </summary>
        [Input("machineType", required: true)]
        public Input<string> MachineType { get; set; } = null!;

        /// <summary>
        /// Optional. The machine type series to create the VM with. For presentation only.
        /// </summary>
        [Input("machineTypeSeries")]
        public Input<string>? MachineTypeSeries { get; set; }

        [Input("metadata")]
        private InputMap<string>? _metadata;

        /// <summary>
        /// Optional. The metadata key/value pairs to assign to the VM.
        /// </summary>
        public InputMap<string> Metadata
        {
            get => _metadata ?? (_metadata = new InputMap<string>());
            set => _metadata = value;
        }

        [Input("networkInterfaces")]
        private InputList<Inputs.NetworkInterfaceArgs>? _networkInterfaces;

        /// <summary>
        /// Optional. NICs to attach to the VM.
        /// </summary>
        public InputList<Inputs.NetworkInterfaceArgs> NetworkInterfaces
        {
            get => _networkInterfaces ?? (_networkInterfaces = new InputList<Inputs.NetworkInterfaceArgs>());
            set => _networkInterfaces = value;
        }

        [Input("networkTags")]
        private InputList<string>? _networkTags;

        /// <summary>
        /// Optional. A list of network tags to associate with the VM.
        /// </summary>
        public InputList<string> NetworkTags
        {
            get => _networkTags ?? (_networkTags = new InputList<string>());
            set => _networkTags = value;
        }

        /// <summary>
        /// Optional. Defines whether the instance has Secure Boot enabled. This can be set to true only if the VM boot option is EFI.
        /// </summary>
        [Input("secureBoot")]
        public Input<bool>? SecureBoot { get; set; }

        /// <summary>
        /// Optional. The service account to associate the VM with.
        /// </summary>
        [Input("serviceAccount")]
        public Input<string>? ServiceAccount { get; set; }

        /// <summary>
        /// The name of the VM to create.
        /// </summary>
        [Input("vmName", required: true)]
        public Input<string> VmName { get; set; } = null!;

        public DisksMigrationVmTargetDefaultsArgs()
        {
        }
        public static new DisksMigrationVmTargetDefaultsArgs Empty => new DisksMigrationVmTargetDefaultsArgs();
    }
}