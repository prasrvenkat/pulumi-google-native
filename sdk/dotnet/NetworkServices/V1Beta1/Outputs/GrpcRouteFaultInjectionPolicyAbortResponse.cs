// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.NetworkServices.V1Beta1.Outputs
{

    /// <summary>
    /// Specification of how client requests are aborted as part of fault injection before being sent to a destination.
    /// </summary>
    [OutputType]
    public sealed class GrpcRouteFaultInjectionPolicyAbortResponse
    {
        /// <summary>
        /// The HTTP status code used to abort the request. The value must be between 200 and 599 inclusive.
        /// </summary>
        public readonly int HttpStatus;
        /// <summary>
        /// The percentage of traffic which will be aborted. The value must be between [0, 100]
        /// </summary>
        public readonly int Percentage;

        [OutputConstructor]
        private GrpcRouteFaultInjectionPolicyAbortResponse(
            int httpStatus,

            int percentage)
        {
            HttpStatus = httpStatus;
            Percentage = percentage;
        }
    }
}
