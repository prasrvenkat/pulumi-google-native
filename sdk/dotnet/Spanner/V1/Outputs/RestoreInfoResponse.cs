// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Spanner.V1.Outputs
{

    /// <summary>
    /// Information about the database restore.
    /// </summary>
    [OutputType]
    public sealed class RestoreInfoResponse
    {
        /// <summary>
        /// Information about the backup used to restore the database. The backup may no longer exist.
        /// </summary>
        public readonly Outputs.BackupInfoResponse BackupInfo;
        /// <summary>
        /// The type of the restore source.
        /// </summary>
        public readonly string SourceType;

        [OutputConstructor]
        private RestoreInfoResponse(
            Outputs.BackupInfoResponse backupInfo,

            string sourceType)
        {
            BackupInfo = backupInfo;
            SourceType = sourceType;
        }
    }
}
