// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.AlloyDB.V1.Outputs
{

    /// <summary>
    /// EncryptionInfo describes the encryption information of a cluster or a backup.
    /// </summary>
    [OutputType]
    public sealed class EncryptionInfoResponse
    {
        /// <summary>
        /// Type of encryption.
        /// </summary>
        public readonly string EncryptionType;
        /// <summary>
        /// Cloud KMS key versions that are being used to protect the database or the backup.
        /// </summary>
        public readonly ImmutableArray<string> KmsKeyVersions;

        [OutputConstructor]
        private EncryptionInfoResponse(
            string encryptionType,

            ImmutableArray<string> kmsKeyVersions)
        {
            EncryptionType = encryptionType;
            KmsKeyVersions = kmsKeyVersions;
        }
    }
}