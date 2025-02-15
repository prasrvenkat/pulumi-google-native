// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Dataform.V1Beta1.Outputs
{

    /// <summary>
    /// Configures fields for performing SSH authentication.
    /// </summary>
    [OutputType]
    public sealed class SshAuthenticationConfigResponse
    {
        /// <summary>
        /// Content of a public SSH key to verify an identity of a remote Git host.
        /// </summary>
        public readonly string HostPublicKey;
        /// <summary>
        /// The name of the Secret Manager secret version to use as a ssh private key for Git operations. Must be in the format `projects/*/secrets/*/versions/*`.
        /// </summary>
        public readonly string UserPrivateKeySecretVersion;

        [OutputConstructor]
        private SshAuthenticationConfigResponse(
            string hostPublicKey,

            string userPrivateKeySecretVersion)
        {
            HostPublicKey = hostPublicKey;
            UserPrivateKeySecretVersion = userPrivateKeySecretVersion;
        }
    }
}
