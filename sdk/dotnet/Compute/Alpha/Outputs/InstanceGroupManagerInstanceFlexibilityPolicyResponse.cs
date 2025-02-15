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
    public sealed class InstanceGroupManagerInstanceFlexibilityPolicyResponse
    {
        /// <summary>
        /// Named instance selections configuring properties that the group will use when creating new VMs.
        /// </summary>
        public readonly ImmutableDictionary<string, string> InstanceSelectionLists;
        /// <summary>
        /// Named instance selections configuring properties that the group will use when creating new VMs.
        /// </summary>
        public readonly ImmutableDictionary<string, string> InstanceSelections;

        [OutputConstructor]
        private InstanceGroupManagerInstanceFlexibilityPolicyResponse(
            ImmutableDictionary<string, string> instanceSelectionLists,

            ImmutableDictionary<string, string> instanceSelections)
        {
            InstanceSelectionLists = instanceSelectionLists;
            InstanceSelections = instanceSelections;
        }
    }
}
