// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Compute.Beta.Inputs
{

    /// <summary>
    /// [Output Only] A connection connected to this service attachment.
    /// </summary>
    public sealed class ServiceAttachmentConnectedEndpointArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The url of a connected endpoint.
        /// </summary>
        [Input("endpoint")]
        public Input<string>? Endpoint { get; set; }

        /// <summary>
        /// The url of a consumer forwarding rule. [Deprecated] Do not use.
        /// </summary>
        [Input("forwardingRule")]
        public Input<string>? ForwardingRule { get; set; }

        /// <summary>
        /// The PSC connection id of the connected endpoint.
        /// </summary>
        [Input("pscConnectionId")]
        public Input<string>? PscConnectionId { get; set; }

        /// <summary>
        /// The status of a connected endpoint to this service attachment.
        /// </summary>
        [Input("status")]
        public Input<string>? Status { get; set; }

        public ServiceAttachmentConnectedEndpointArgs()
        {
        }
    }
}