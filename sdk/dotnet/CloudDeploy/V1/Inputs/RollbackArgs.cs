// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.CloudDeploy.V1.Inputs
{

    /// <summary>
    /// Rolls back a `Rollout`.
    /// </summary>
    public sealed class RollbackArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Optional. The starting phase ID for the `Rollout`. If unspecified, the `Rollout` will start in the stable phase.
        /// </summary>
        [Input("destinationPhase")]
        public Input<string>? DestinationPhase { get; set; }

        public RollbackArgs()
        {
        }
        public static new RollbackArgs Empty => new RollbackArgs();
    }
}