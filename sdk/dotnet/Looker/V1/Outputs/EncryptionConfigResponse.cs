// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Looker.V1.Outputs
{

    /// <summary>
    /// Encryption configuration (i.e. CMEK).
    /// </summary>
    [OutputType]
    public sealed class EncryptionConfigResponse
    {
        /// <summary>
        /// Name of the CMEK key in KMS (input parameter).
        /// </summary>
        public readonly string KmsKeyName;
        /// <summary>
        /// Full name and version of the CMEK key currently in use to encrypt Looker data. Format: `projects/{project}/locations/{location}/keyRings/{ring}/cryptoKeys/{key}/cryptoKeyVersions/{version}`. Empty if CMEK is not configured in this instance.
        /// </summary>
        public readonly string KmsKeyNameVersion;
        /// <summary>
        /// Status of the CMEK key.
        /// </summary>
        public readonly string KmsKeyState;

        [OutputConstructor]
        private EncryptionConfigResponse(
            string kmsKeyName,

            string kmsKeyNameVersion,

            string kmsKeyState)
        {
            KmsKeyName = kmsKeyName;
            KmsKeyNameVersion = kmsKeyNameVersion;
            KmsKeyState = kmsKeyState;
        }
    }
}