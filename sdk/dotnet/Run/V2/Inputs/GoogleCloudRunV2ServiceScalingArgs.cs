// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Run.V2.Inputs
{

    /// <summary>
    /// Scaling settings applied at the service level rather than at the revision level.
    /// </summary>
    public sealed class GoogleCloudRunV2ServiceScalingArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// total min instances for the service. This number of instances is divided among all revisions with specified traffic based on the percent of traffic they are receiving. (ALPHA)
        /// </summary>
        [Input("minInstanceCount")]
        public Input<int>? MinInstanceCount { get; set; }

        public GoogleCloudRunV2ServiceScalingArgs()
        {
        }
        public static new GoogleCloudRunV2ServiceScalingArgs Empty => new GoogleCloudRunV2ServiceScalingArgs();
    }
}