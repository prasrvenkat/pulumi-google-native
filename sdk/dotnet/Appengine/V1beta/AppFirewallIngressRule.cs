// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Appengine.V1beta
{
    /// <summary>
    /// Creates a firewall rule for the application.
    /// </summary>
    [GoogleCloudResourceType("google-cloud:appengine/v1beta:AppFirewallIngressRule")]
    public partial class AppFirewallIngressRule : Pulumi.CustomResource
    {
        /// <summary>
        /// The action to take on matched requests.
        /// </summary>
        [Output("action")]
        public Output<string> Action { get; private set; } = null!;

        /// <summary>
        /// An optional string description of this rule. This field has a maximum length of 100 characters.
        /// </summary>
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        /// <summary>
        /// A positive integer between 1, Int32.MaxValue-1 that defines the order of rule evaluation. Rules with the lowest priority are evaluated first.A default rule at priority Int32.MaxValue matches all IPv4 and IPv6 traffic when no previous rule matches. Only the action of this rule can be modified by the user.
        /// </summary>
        [Output("priority")]
        public Output<int> Priority { get; private set; } = null!;

        /// <summary>
        /// IP address or range, defined using CIDR notation, of requests that this rule applies to. You can use the wildcard character "*" to match all IPs equivalent to "0/0" and "::/0" together. Examples: 192.168.1.1 or 192.168.0.0/16 or 2001:db8::/32 or 2001:0db8:0000:0042:0000:8a2e:0370:7334. Truncation will be silently performed on addresses which are not properly truncated. For example, 1.2.3.4/24 is accepted as the same address as 1.2.3.0/24. Similarly, for IPv6, 2001:db8::1/32 is accepted as the same address as 2001:db8::/32.
        /// </summary>
        [Output("sourceRange")]
        public Output<string> SourceRange { get; private set; } = null!;


        /// <summary>
        /// Create a AppFirewallIngressRule resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AppFirewallIngressRule(string name, AppFirewallIngressRuleArgs args, CustomResourceOptions? options = null)
            : base("google-cloud:appengine/v1beta:AppFirewallIngressRule", name, args ?? new AppFirewallIngressRuleArgs(), MakeResourceOptions(options, ""))
        {
        }

        private AppFirewallIngressRule(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("google-cloud:appengine/v1beta:AppFirewallIngressRule", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing AppFirewallIngressRule resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AppFirewallIngressRule Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new AppFirewallIngressRule(name, id, options);
        }
    }

    public sealed class AppFirewallIngressRuleArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The action to take on matched requests.
        /// </summary>
        [Input("action")]
        public Input<string>? Action { get; set; }

        [Input("appsId", required: true)]
        public Input<string> AppsId { get; set; } = null!;

        /// <summary>
        /// An optional string description of this rule. This field has a maximum length of 100 characters.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("ingressRulesId", required: true)]
        public Input<string> IngressRulesId { get; set; } = null!;

        /// <summary>
        /// A positive integer between 1, Int32.MaxValue-1 that defines the order of rule evaluation. Rules with the lowest priority are evaluated first.A default rule at priority Int32.MaxValue matches all IPv4 and IPv6 traffic when no previous rule matches. Only the action of this rule can be modified by the user.
        /// </summary>
        [Input("priority")]
        public Input<int>? Priority { get; set; }

        /// <summary>
        /// IP address or range, defined using CIDR notation, of requests that this rule applies to. You can use the wildcard character "*" to match all IPs equivalent to "0/0" and "::/0" together. Examples: 192.168.1.1 or 192.168.0.0/16 or 2001:db8::/32 or 2001:0db8:0000:0042:0000:8a2e:0370:7334. Truncation will be silently performed on addresses which are not properly truncated. For example, 1.2.3.4/24 is accepted as the same address as 1.2.3.0/24. Similarly, for IPv6, 2001:db8::1/32 is accepted as the same address as 2001:db8::/32.
        /// </summary>
        [Input("sourceRange")]
        public Input<string>? SourceRange { get; set; }

        public AppFirewallIngressRuleArgs()
        {
        }
    }
}