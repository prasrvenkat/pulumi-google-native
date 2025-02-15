// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Gkeonprem.V1.Outputs
{

    /// <summary>
    /// Specifies the bare metal user cluster's observability infrastructure.
    /// </summary>
    [OutputType]
    public sealed class BareMetalClusterOperationsConfigResponse
    {
        /// <summary>
        /// Whether collection of application logs/metrics should be enabled (in addition to system logs/metrics).
        /// </summary>
        public readonly bool EnableApplicationLogs;

        [OutputConstructor]
        private BareMetalClusterOperationsConfigResponse(bool enableApplicationLogs)
        {
            EnableApplicationLogs = enableApplicationLogs;
        }
    }
}
