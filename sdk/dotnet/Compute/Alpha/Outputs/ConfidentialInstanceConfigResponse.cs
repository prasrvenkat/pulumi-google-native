// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Compute.Alpha.Outputs
{

    [OutputType]
    public sealed class ConfidentialInstanceConfigResponse
    {
        /// <summary>
        /// Defines whether the instance should have confidential compute enabled.
        /// </summary>
        public readonly bool EnableConfidentialCompute;

        [OutputConstructor]
        private ConfidentialInstanceConfigResponse(bool enableConfidentialCompute)
        {
            EnableConfidentialCompute = enableConfidentialCompute;
        }
    }
}