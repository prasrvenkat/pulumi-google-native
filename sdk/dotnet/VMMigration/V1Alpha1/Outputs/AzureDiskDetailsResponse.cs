// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.VMMigration.V1Alpha1.Outputs
{

    /// <summary>
    /// The details of an Azure VM disk.
    /// </summary>
    [OutputType]
    public sealed class AzureDiskDetailsResponse
    {
        /// <summary>
        /// Azure disk ID.
        /// </summary>
        public readonly string DiskId;
        /// <summary>
        /// The ordinal number of the disk.
        /// </summary>
        public readonly int DiskNumber;
        /// <summary>
        /// Size in GB.
        /// </summary>
        public readonly string SizeGb;

        [OutputConstructor]
        private AzureDiskDetailsResponse(
            string diskId,

            int diskNumber,

            string sizeGb)
        {
            DiskId = diskId;
            DiskNumber = diskNumber;
            SizeGb = sizeGb;
        }
    }
}
