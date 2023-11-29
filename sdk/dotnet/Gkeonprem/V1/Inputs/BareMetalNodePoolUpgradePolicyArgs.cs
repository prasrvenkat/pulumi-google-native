// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Gkeonprem.V1.Inputs
{

    /// <summary>
    /// BareMetalNodePoolUpgradePolicy defines the node pool upgrade policy.
    /// </summary>
    public sealed class BareMetalNodePoolUpgradePolicyArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The parallel upgrade settings for worker node pools.
        /// </summary>
        [Input("parallelUpgradeConfig")]
        public Input<Inputs.BareMetalParallelUpgradeConfigArgs>? ParallelUpgradeConfig { get; set; }

        public BareMetalNodePoolUpgradePolicyArgs()
        {
        }
        public static new BareMetalNodePoolUpgradePolicyArgs Empty => new BareMetalNodePoolUpgradePolicyArgs();
    }
}