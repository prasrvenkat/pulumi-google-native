// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.VMMigration.V1.Inputs
{

    /// <summary>
    /// NetworkInterface represents a NIC of a VM.
    /// </summary>
    public sealed class NetworkInterfaceArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The external IP to define in the NIC.
        /// </summary>
        [Input("externalIp")]
        public Input<string>? ExternalIp { get; set; }

        /// <summary>
        /// The internal IP to define in the NIC. The formats accepted are: `ephemeral` \ ipv4 address \ a named address resource full path.
        /// </summary>
        [Input("internalIp")]
        public Input<string>? InternalIp { get; set; }

        /// <summary>
        /// The network to connect the NIC to.
        /// </summary>
        [Input("network")]
        public Input<string>? Network { get; set; }

        /// <summary>
        /// The subnetwork to connect the NIC to.
        /// </summary>
        [Input("subnetwork")]
        public Input<string>? Subnetwork { get; set; }

        public NetworkInterfaceArgs()
        {
        }
        public static new NetworkInterfaceArgs Empty => new NetworkInterfaceArgs();
    }
}
