// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Container.V1Beta1.Inputs
{

    /// <summary>
    /// Configuration options for the HTTP (L7) load balancing controller addon, which makes it easy to set up HTTP load balancers for services in a cluster.
    /// </summary>
    public sealed class HttpLoadBalancingArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Whether the HTTP Load Balancing controller is enabled in the cluster. When enabled, it runs a small pod in the cluster that manages the load balancers.
        /// </summary>
        [Input("disabled")]
        public Input<bool>? Disabled { get; set; }

        public HttpLoadBalancingArgs()
        {
        }
        public static new HttpLoadBalancingArgs Empty => new HttpLoadBalancingArgs();
    }
}
