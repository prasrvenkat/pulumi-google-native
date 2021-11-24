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
    public sealed class FutureReservationSpecificSKUPropertiesResponse
    {
        /// <summary>
        /// Properties of the SKU instances being reserved.
        /// </summary>
        public readonly Outputs.AllocationSpecificSKUAllocationReservedInstancePropertiesResponse InstanceProperties;
        /// <summary>
        /// Total number of instances for which capacity assurance is requested at a future time period.
        /// </summary>
        public readonly string TotalCount;

        [OutputConstructor]
        private FutureReservationSpecificSKUPropertiesResponse(
            Outputs.AllocationSpecificSKUAllocationReservedInstancePropertiesResponse instanceProperties,

            string totalCount)
        {
            InstanceProperties = instanceProperties;
            TotalCount = totalCount;
        }
    }
}