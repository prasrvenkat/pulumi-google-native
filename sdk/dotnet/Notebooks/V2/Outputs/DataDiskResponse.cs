// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Notebooks.V2.Outputs
{

    /// <summary>
    /// An instance-attached disk resource.
    /// </summary>
    [OutputType]
    public sealed class DataDiskResponse
    {
        /// <summary>
        /// Optional. Input only. Disk encryption method used on the boot and data disks, defaults to GMEK.
        /// </summary>
        public readonly string DiskEncryption;
        /// <summary>
        /// Optional. The size of the disk in GB attached to this VM instance, up to a maximum of 64000 GB (64 TB). If not specified, this defaults to 100.
        /// </summary>
        public readonly string DiskSizeGb;
        /// <summary>
        /// Optional. Input only. Indicates the type of the disk.
        /// </summary>
        public readonly string DiskType;
        /// <summary>
        /// Optional. Input only. The KMS key used to encrypt the disks, only applicable if disk_encryption is CMEK. Format: `projects/{project_id}/locations/{location}/keyRings/{key_ring_id}/cryptoKeys/{key_id}` Learn more about using your own encryption keys.
        /// </summary>
        public readonly string KmsKey;

        [OutputConstructor]
        private DataDiskResponse(
            string diskEncryption,

            string diskSizeGb,

            string diskType,

            string kmsKey)
        {
            DiskEncryption = diskEncryption;
            DiskSizeGb = diskSizeGb;
            DiskType = diskType;
            KmsKey = kmsKey;
        }
    }
}
