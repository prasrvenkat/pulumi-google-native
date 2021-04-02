// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Networkmanagement.V1beta1.Outputs
{

    [OutputType]
    public sealed class TraceResponse
    {
        /// <summary>
        /// Derived from the source and destination endpoints definition, and validated by the data plane model. If there are multiple traces starting from different source locations, then the endpoint_info may be different between traces.
        /// </summary>
        public readonly Outputs.EndpointInfoResponse EndpointInfo;
        /// <summary>
        /// A trace of a test contains multiple steps from the initial state to the final state (delivered, dropped, forwarded, or aborted). The steps are ordered by the processing sequence within the simulated network state machine. It is critical to preserve the order of the steps and avoid reordering or sorting them.
        /// </summary>
        public readonly ImmutableArray<Outputs.StepResponse> Steps;

        [OutputConstructor]
        private TraceResponse(
            Outputs.EndpointInfoResponse endpointInfo,

            ImmutableArray<Outputs.StepResponse> steps)
        {
            EndpointInfo = endpointInfo;
            Steps = steps;
        }
    }
}