// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.NetworkServices.V1Beta1.Inputs
{

    /// <summary>
    /// A single extension in the chain to execute for the matching request.
    /// </summary>
    public sealed class ExtensionChainExtensionArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The `:authority` header in the gRPC request sent from Envoy to the extension service.
        /// </summary>
        [Input("authority", required: true)]
        public Input<string> Authority { get; set; } = null!;

        /// <summary>
        /// Optional. Determines how the proxy behaves if the call to the extension fails or times out. When set to `TRUE`, request or response processing continues without error. Any subsequent extensions in the extension chain are also executed. When set to `FALSE`: * If response headers have not been delivered to the downstream client, a generic 500 error is returned to the client. The error response can be tailored by configuring a custom error response in the load balancer. * If response headers have been delivered, then the HTTP stream to the downstream client is reset. Default is `FALSE`.
        /// </summary>
        [Input("failOpen")]
        public Input<bool>? FailOpen { get; set; }

        [Input("forwardHeaders")]
        private InputList<string>? _forwardHeaders;

        /// <summary>
        /// Optional. List of the HTTP headers to forward to the extension (from the client or backend). If omitted, all headers are sent. Each element is a string indicating the header name.
        /// </summary>
        public InputList<string> ForwardHeaders
        {
            get => _forwardHeaders ?? (_forwardHeaders = new InputList<string>());
            set => _forwardHeaders = value;
        }

        /// <summary>
        /// The name for this extension. The name is logged as part of the HTTP request logs. The name must conform with RFC-1034, is restricted to lower-cased letters, numbers and hyphens, and can have a maximum length of 63 characters. Additionally, the first character must be a letter and the last a letter or a number.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// The reference to the service that runs the extension. Must be a reference to a [backend service](https://cloud.google.com/compute/docs/reference/rest/v1/backendServices).
        /// </summary>
        [Input("service", required: true)]
        public Input<string> Service { get; set; } = null!;

        [Input("supportedEvents")]
        private InputList<Pulumi.GoogleNative.NetworkServices.V1Beta1.ExtensionChainExtensionSupportedEventsItem>? _supportedEvents;

        /// <summary>
        /// Optional. A set of events during request or response processing for which this extension is called. This field is required for the `LbTrafficExtension` resource. It's not relevant for the `LbRouteExtension` resource.
        /// </summary>
        public InputList<Pulumi.GoogleNative.NetworkServices.V1Beta1.ExtensionChainExtensionSupportedEventsItem> SupportedEvents
        {
            get => _supportedEvents ?? (_supportedEvents = new InputList<Pulumi.GoogleNative.NetworkServices.V1Beta1.ExtensionChainExtensionSupportedEventsItem>());
            set => _supportedEvents = value;
        }

        /// <summary>
        /// Specifies the timeout for each individual message on the stream. The timeout must be between 10-1000 milliseconds.
        /// </summary>
        [Input("timeout", required: true)]
        public Input<string> Timeout { get; set; } = null!;

        public ExtensionChainExtensionArgs()
        {
        }
        public static new ExtensionChainExtensionArgs Empty => new ExtensionChainExtensionArgs();
    }
}
