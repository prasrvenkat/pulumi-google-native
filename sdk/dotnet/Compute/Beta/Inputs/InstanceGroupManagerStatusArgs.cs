// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Compute.Beta.Inputs
{

    public sealed class InstanceGroupManagerStatusArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// [Output Only] The URL of the Autoscaler that targets this instance group manager.
        /// </summary>
        [Input("autoscaler")]
        public Input<string>? Autoscaler { get; set; }

        /// <summary>
        /// [Output Only] A bit indicating whether the managed instance group is in a stable state. A stable state means that: none of the instances in the managed instance group is currently undergoing any type of change (for example, creation, restart, or deletion); no future changes are scheduled for instances in the managed instance group; and the managed instance group itself is not being modified.
        /// </summary>
        [Input("isStable")]
        public Input<bool>? IsStable { get; set; }

        /// <summary>
        /// [Output Only] Stateful status of the given Instance Group Manager.
        /// </summary>
        [Input("stateful")]
        public Input<Inputs.InstanceGroupManagerStatusStatefulArgs>? Stateful { get; set; }

        /// <summary>
        /// [Output Only] A status of consistency of Instances' versions with their target version specified by version field on Instance Group Manager.
        /// </summary>
        [Input("versionTarget")]
        public Input<Inputs.InstanceGroupManagerStatusVersionTargetArgs>? VersionTarget { get; set; }

        public InstanceGroupManagerStatusArgs()
        {
        }
    }
}