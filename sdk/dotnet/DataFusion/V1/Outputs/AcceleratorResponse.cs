// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GcpNative.DataFusion.V1.Outputs
{

    [OutputType]
    public sealed class AcceleratorResponse
    {
        /// <summary>
        /// The type of an accelator for a CDF instance.
        /// </summary>
        public readonly string AcceleratorType;
        /// <summary>
        /// The state of the accelerator
        /// </summary>
        public readonly string State;

        [OutputConstructor]
        private AcceleratorResponse(
            string acceleratorType,

            string state)
        {
            AcceleratorType = acceleratorType;
            State = state;
        }
    }
}