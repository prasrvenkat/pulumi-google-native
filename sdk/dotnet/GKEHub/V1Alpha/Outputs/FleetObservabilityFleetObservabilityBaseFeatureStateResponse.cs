// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.GKEHub.V1Alpha.Outputs
{

    /// <summary>
    /// Base state for fleet observability feature.
    /// </summary>
    [OutputType]
    public sealed class FleetObservabilityFleetObservabilityBaseFeatureStateResponse
    {
        /// <summary>
        /// The high-level, machine-readable status of this Feature.
        /// </summary>
        public readonly string Code;
        /// <summary>
        /// Errors after reconciling the monitoring and logging feature if the code is not OK.
        /// </summary>
        public readonly ImmutableArray<Outputs.FleetObservabilityFeatureErrorResponse> Errors;

        [OutputConstructor]
        private FleetObservabilityFleetObservabilityBaseFeatureStateResponse(
            string code,

            ImmutableArray<Outputs.FleetObservabilityFeatureErrorResponse> errors)
        {
            Code = code;
            Errors = errors;
        }
    }
}