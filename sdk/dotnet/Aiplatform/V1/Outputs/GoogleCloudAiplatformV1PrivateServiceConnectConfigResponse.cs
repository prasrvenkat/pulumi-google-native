// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Aiplatform.V1.Outputs
{

    /// <summary>
    /// Represents configuration for private service connect.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudAiplatformV1PrivateServiceConnectConfigResponse
    {
        /// <summary>
        /// If true, expose the IndexEndpoint via private service connect.
        /// </summary>
        public readonly bool EnablePrivateServiceConnect;
        /// <summary>
        /// A list of Projects from which the forwarding rule will target the service attachment.
        /// </summary>
        public readonly ImmutableArray<string> ProjectAllowlist;

        [OutputConstructor]
        private GoogleCloudAiplatformV1PrivateServiceConnectConfigResponse(
            bool enablePrivateServiceConnect,

            ImmutableArray<string> projectAllowlist)
        {
            EnablePrivateServiceConnect = enablePrivateServiceConnect;
            ProjectAllowlist = projectAllowlist;
        }
    }
}