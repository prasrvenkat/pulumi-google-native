// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Compute.Alpha.Inputs
{

    /// <summary>
    /// Contains output only fields. Use this sub-message for actual values set on Instance attributes as compared to the value requested by the user (intent) in their instance CRUD calls.
    /// </summary>
    public sealed class ResourceStatusArgs : Pulumi.ResourceArgs
    {
        [Input("scheduling")]
        public Input<Inputs.ResourceStatusSchedulingArgs>? Scheduling { get; set; }

        public ResourceStatusArgs()
        {
        }
    }
}