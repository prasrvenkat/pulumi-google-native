// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Compute.Beta
{
    /// <summary>
    /// Creates a HttpHealthCheck resource in the specified project using the data included in the request.
    /// </summary>
    [GoogleCloudResourceType("google-cloud:compute/beta:HttpHealthCheck")]
    public partial class HttpHealthCheck : Pulumi.CustomResource
    {
        /// <summary>
        /// How often (in seconds) to send a health check. The default value is 5 seconds.
        /// </summary>
        [Output("checkIntervalSec")]
        public Output<int> CheckIntervalSec { get; private set; } = null!;

        /// <summary>
        /// [Output Only] Creation timestamp in RFC3339 text format.
        /// </summary>
        [Output("creationTimestamp")]
        public Output<string> CreationTimestamp { get; private set; } = null!;

        /// <summary>
        /// An optional description of this resource. Provide this property when you create the resource.
        /// </summary>
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        /// <summary>
        /// A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is 2.
        /// </summary>
        [Output("healthyThreshold")]
        public Output<int> HealthyThreshold { get; private set; } = null!;

        /// <summary>
        /// The value of the host header in the HTTP health check request. If left empty (default value), the public IP on behalf of which this health check is performed will be used.
        /// </summary>
        [Output("host")]
        public Output<string> Host { get; private set; } = null!;

        /// <summary>
        /// [Output Only] Type of the resource. Always compute#httpHealthCheck for HTTP health checks.
        /// </summary>
        [Output("kind")]
        public Output<string> Kind { get; private set; } = null!;

        /// <summary>
        /// Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The TCP port number for the HTTP health check request. The default value is 80.
        /// </summary>
        [Output("port")]
        public Output<int> Port { get; private set; } = null!;

        /// <summary>
        /// The request path of the HTTP health check request. The default value is /. This field does not support query parameters.
        /// </summary>
        [Output("requestPath")]
        public Output<string> RequestPath { get; private set; } = null!;

        /// <summary>
        /// [Output Only] Server-defined URL for the resource.
        /// </summary>
        [Output("selfLink")]
        public Output<string> SelfLink { get; private set; } = null!;

        /// <summary>
        /// How long (in seconds) to wait before claiming failure. The default value is 5 seconds. It is invalid for timeoutSec to have greater value than checkIntervalSec.
        /// </summary>
        [Output("timeoutSec")]
        public Output<int> TimeoutSec { get; private set; } = null!;

        /// <summary>
        /// A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2.
        /// </summary>
        [Output("unhealthyThreshold")]
        public Output<int> UnhealthyThreshold { get; private set; } = null!;


        /// <summary>
        /// Create a HttpHealthCheck resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public HttpHealthCheck(string name, HttpHealthCheckArgs args, CustomResourceOptions? options = null)
            : base("google-cloud:compute/beta:HttpHealthCheck", name, args ?? new HttpHealthCheckArgs(), MakeResourceOptions(options, ""))
        {
        }

        private HttpHealthCheck(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("google-cloud:compute/beta:HttpHealthCheck", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing HttpHealthCheck resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static HttpHealthCheck Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new HttpHealthCheck(name, id, options);
        }
    }

    public sealed class HttpHealthCheckArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// How often (in seconds) to send a health check. The default value is 5 seconds.
        /// </summary>
        [Input("checkIntervalSec")]
        public Input<int>? CheckIntervalSec { get; set; }

        /// <summary>
        /// [Output Only] Creation timestamp in RFC3339 text format.
        /// </summary>
        [Input("creationTimestamp")]
        public Input<string>? CreationTimestamp { get; set; }

        /// <summary>
        /// An optional description of this resource. Provide this property when you create the resource.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is 2.
        /// </summary>
        [Input("healthyThreshold")]
        public Input<int>? HealthyThreshold { get; set; }

        /// <summary>
        /// The value of the host header in the HTTP health check request. If left empty (default value), the public IP on behalf of which this health check is performed will be used.
        /// </summary>
        [Input("host")]
        public Input<string>? Host { get; set; }

        [Input("httpHealthCheck", required: true)]
        public Input<string> HttpHealthCheck { get; set; } = null!;

        /// <summary>
        /// [Output Only] The unique identifier for the resource. This identifier is defined by the server.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// [Output Only] Type of the resource. Always compute#httpHealthCheck for HTTP health checks.
        /// </summary>
        [Input("kind")]
        public Input<string>? Kind { get; set; }

        /// <summary>
        /// Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The TCP port number for the HTTP health check request. The default value is 80.
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        [Input("project", required: true)]
        public Input<string> Project { get; set; } = null!;

        /// <summary>
        /// The request path of the HTTP health check request. The default value is /. This field does not support query parameters.
        /// </summary>
        [Input("requestPath")]
        public Input<string>? RequestPath { get; set; }

        /// <summary>
        /// [Output Only] Server-defined URL for the resource.
        /// </summary>
        [Input("selfLink")]
        public Input<string>? SelfLink { get; set; }

        /// <summary>
        /// How long (in seconds) to wait before claiming failure. The default value is 5 seconds. It is invalid for timeoutSec to have greater value than checkIntervalSec.
        /// </summary>
        [Input("timeoutSec")]
        public Input<int>? TimeoutSec { get; set; }

        /// <summary>
        /// A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2.
        /// </summary>
        [Input("unhealthyThreshold")]
        public Input<int>? UnhealthyThreshold { get; set; }

        public HttpHealthCheckArgs()
        {
        }
    }
}