// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.CloudDeploy.V1.Outputs
{

    /// <summary>
    /// DeployParameters contains deploy parameters information.
    /// </summary>
    [OutputType]
    public sealed class DeployParametersResponse
    {
        /// <summary>
        /// Optional. Deploy parameters are applied to targets with match labels. If unspecified, deploy parameters are applied to all targets (including child targets of a multi-target).
        /// </summary>
        public readonly ImmutableDictionary<string, string> MatchTargetLabels;
        /// <summary>
        /// Values are deploy parameters in key-value pairs.
        /// </summary>
        public readonly ImmutableDictionary<string, string> Values;

        [OutputConstructor]
        private DeployParametersResponse(
            ImmutableDictionary<string, string> matchTargetLabels,

            ImmutableDictionary<string, string> values)
        {
            MatchTargetLabels = matchTargetLabels;
            Values = values;
        }
    }
}