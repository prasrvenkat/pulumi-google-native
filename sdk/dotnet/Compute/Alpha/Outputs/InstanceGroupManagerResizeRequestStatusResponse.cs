// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Compute.Alpha.Outputs
{

    [OutputType]
    public sealed class InstanceGroupManagerResizeRequestStatusResponse
    {
        /// <summary>
        /// Errors encountered during the queueing or provisioning phases of the ResizeRequest.
        /// </summary>
        public readonly Outputs.InstanceGroupManagerResizeRequestStatusErrorResponse Error;
        /// <summary>
        /// Constraints for the time when the instances start provisioning. Always exposed as absolute time.
        /// </summary>
        public readonly Outputs.QueuingPolicyResponse QueuingPolicy;

        [OutputConstructor]
        private InstanceGroupManagerResizeRequestStatusResponse(
            Outputs.InstanceGroupManagerResizeRequestStatusErrorResponse error,

            Outputs.QueuingPolicyResponse queuingPolicy)
        {
            Error = error;
            QueuingPolicy = queuingPolicy;
        }
    }
}
