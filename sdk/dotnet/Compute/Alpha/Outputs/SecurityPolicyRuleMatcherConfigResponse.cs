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
    public sealed class SecurityPolicyRuleMatcherConfigResponse
    {
        /// <summary>
        /// CIDR IP address range. This field may only be specified when versioned_expr is set to FIREWALL.
        /// </summary>
        public readonly ImmutableArray<string> DestIpRanges;
        /// <summary>
        /// Pairs of IP protocols and ports that the rule should match. This field may only be specified when versioned_expr is set to FIREWALL.
        /// </summary>
        public readonly ImmutableArray<Outputs.SecurityPolicyRuleMatcherConfigDestinationPortResponse> DestPorts;
        /// <summary>
        /// Pairs of IP protocols and ports that the rule should match. This field may only be specified when versioned_expr is set to FIREWALL.
        /// </summary>
        public readonly ImmutableArray<Outputs.SecurityPolicyRuleMatcherConfigLayer4ConfigResponse> Layer4Configs;
        /// <summary>
        /// CIDR IP address range. Maximum number of src_ip_ranges allowed is 10.
        /// </summary>
        public readonly ImmutableArray<string> SrcIpRanges;

        [OutputConstructor]
        private SecurityPolicyRuleMatcherConfigResponse(
            ImmutableArray<string> destIpRanges,

            ImmutableArray<Outputs.SecurityPolicyRuleMatcherConfigDestinationPortResponse> destPorts,

            ImmutableArray<Outputs.SecurityPolicyRuleMatcherConfigLayer4ConfigResponse> layer4Configs,

            ImmutableArray<string> srcIpRanges)
        {
            DestIpRanges = destIpRanges;
            DestPorts = destPorts;
            Layer4Configs = layer4Configs;
            SrcIpRanges = srcIpRanges;
        }
    }
}
