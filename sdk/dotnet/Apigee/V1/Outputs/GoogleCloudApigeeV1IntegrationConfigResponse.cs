// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Apigee.V1.Outputs
{

    /// <summary>
    /// Configuration for the Integration add-on.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudApigeeV1IntegrationConfigResponse
    {
        /// <summary>
        /// Flag that specifies whether the Integration add-on is enabled.
        /// </summary>
        public readonly bool Enabled;

        [OutputConstructor]
        private GoogleCloudApigeeV1IntegrationConfigResponse(bool enabled)
        {
            Enabled = enabled;
        }
    }
}
