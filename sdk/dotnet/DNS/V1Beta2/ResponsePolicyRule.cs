// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GcpNative.DNS.V1Beta2
{
    /// <summary>
    /// Creates a new Response Policy Rule.
    /// </summary>
    [GcpNativeResourceType("gcp-native:dns/v1beta2:ResponsePolicyRule")]
    public partial class ResponsePolicyRule : Pulumi.CustomResource
    {
        /// <summary>
        /// Answer this query with a behavior rather than DNS data.
        /// </summary>
        [Output("behavior")]
        public Output<string> Behavior { get; private set; } = null!;

        /// <summary>
        /// The DNS name (wildcard or exact) to apply this rule to. Must be unique within the Response Policy Rule.
        /// </summary>
        [Output("dnsName")]
        public Output<string> DnsName { get; private set; } = null!;

        [Output("kind")]
        public Output<string> Kind { get; private set; } = null!;

        /// <summary>
        /// Answer this query directly with DNS data. These ResourceRecordSets override any other DNS behavior for the matched name; in particular they override private zones, the public internet, and GCP internal DNS. No SOA nor NS types are allowed.
        /// </summary>
        [Output("localData")]
        public Output<Outputs.ResponsePolicyRuleLocalDataResponse> LocalData { get; private set; } = null!;

        /// <summary>
        /// An identifier for this rule. Must be unique with the ResponsePolicy.
        /// </summary>
        [Output("ruleName")]
        public Output<string> RuleName { get; private set; } = null!;


        /// <summary>
        /// Create a ResponsePolicyRule resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ResponsePolicyRule(string name, ResponsePolicyRuleArgs args, CustomResourceOptions? options = null)
            : base("gcp-native:dns/v1beta2:ResponsePolicyRule", name, args ?? new ResponsePolicyRuleArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ResponsePolicyRule(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("gcp-native:dns/v1beta2:ResponsePolicyRule", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing ResponsePolicyRule resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ResponsePolicyRule Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ResponsePolicyRule(name, id, options);
        }
    }

    public sealed class ResponsePolicyRuleArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Answer this query with a behavior rather than DNS data.
        /// </summary>
        [Input("behavior")]
        public Input<string>? Behavior { get; set; }

        /// <summary>
        /// The DNS name (wildcard or exact) to apply this rule to. Must be unique within the Response Policy Rule.
        /// </summary>
        [Input("dnsName")]
        public Input<string>? DnsName { get; set; }

        [Input("kind")]
        public Input<string>? Kind { get; set; }

        /// <summary>
        /// Answer this query directly with DNS data. These ResourceRecordSets override any other DNS behavior for the matched name; in particular they override private zones, the public internet, and GCP internal DNS. No SOA nor NS types are allowed.
        /// </summary>
        [Input("localData")]
        public Input<Inputs.ResponsePolicyRuleLocalDataArgs>? LocalData { get; set; }

        [Input("project", required: true)]
        public Input<string> Project { get; set; } = null!;

        [Input("responsePolicy", required: true)]
        public Input<string> ResponsePolicy { get; set; } = null!;

        [Input("responsePolicyRule", required: true)]
        public Input<string> ResponsePolicyRule { get; set; } = null!;

        /// <summary>
        /// An identifier for this rule. Must be unique with the ResponsePolicy.
        /// </summary>
        [Input("ruleName")]
        public Input<string>? RuleName { get; set; }

        public ResponsePolicyRuleArgs()
        {
        }
    }
}