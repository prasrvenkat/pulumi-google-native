// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.AccessContextManager.V1.Inputs
{

    /// <summary>
    /// Sub-segment ranges inside of a VPC Network.
    /// </summary>
    public sealed class VpcSubNetworkArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Network name. If the network is not part of the organization, the `compute.network.get` permission must be granted to the caller. Format: `//compute.googleapis.com/projects/{PROJECT_ID}/global/networks/{NETWORK_NAME}` Example: `//compute.googleapis.com/projects/my-project/global/networks/network-1`
        /// </summary>
        [Input("network", required: true)]
        public Input<string> Network { get; set; } = null!;

        [Input("vpcIpSubnetworks")]
        private InputList<string>? _vpcIpSubnetworks;

        /// <summary>
        /// CIDR block IP subnetwork specification. The IP address must be an IPv4 address and can be a public or private IP address. Note that for a CIDR IP address block, the specified IP address portion must be properly truncated (i.e. all the host bits must be zero) or the input is considered malformed. For example, "192.0.2.0/24" is accepted but "192.0.2.1/24" is not. If empty, all IP addresses are allowed.
        /// </summary>
        public InputList<string> VpcIpSubnetworks
        {
            get => _vpcIpSubnetworks ?? (_vpcIpSubnetworks = new InputList<string>());
            set => _vpcIpSubnetworks = value;
        }

        public VpcSubNetworkArgs()
        {
        }
        public static new VpcSubNetworkArgs Empty => new VpcSubNetworkArgs();
    }
}