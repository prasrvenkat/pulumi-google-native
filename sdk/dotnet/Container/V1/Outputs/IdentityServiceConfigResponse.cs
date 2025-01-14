// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Container.V1.Outputs
{

    /// <summary>
    /// IdentityServiceConfig is configuration for Identity Service which allows customers to use external identity providers with the K8S API
    /// </summary>
    [OutputType]
    public sealed class IdentityServiceConfigResponse
    {
        /// <summary>
        /// Whether to enable the Identity Service component
        /// </summary>
        public readonly bool Enabled;

        [OutputConstructor]
        private IdentityServiceConfigResponse(bool enabled)
        {
            Enabled = enabled;
        }
    }
}
