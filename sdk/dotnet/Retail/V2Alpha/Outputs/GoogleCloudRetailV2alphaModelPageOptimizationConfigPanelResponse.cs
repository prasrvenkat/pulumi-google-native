// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Retail.V2Alpha.Outputs
{

    /// <summary>
    /// An individual panel with a list of ServingConfigs to consider for it.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudRetailV2alphaModelPageOptimizationConfigPanelResponse
    {
        /// <summary>
        /// The candidates to consider on the panel.
        /// </summary>
        public readonly ImmutableArray<Outputs.GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidateResponse> Candidates;
        /// <summary>
        /// The default candidate. If the model fails at serving time, we fall back to the default.
        /// </summary>
        public readonly Outputs.GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidateResponse DefaultCandidate;
        /// <summary>
        /// Optional. The name to display for the panel.
        /// </summary>
        public readonly string DisplayName;

        [OutputConstructor]
        private GoogleCloudRetailV2alphaModelPageOptimizationConfigPanelResponse(
            ImmutableArray<Outputs.GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidateResponse> candidates,

            Outputs.GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidateResponse defaultCandidate,

            string displayName)
        {
            Candidates = candidates;
            DefaultCandidate = defaultCandidate;
            DisplayName = displayName;
        }
    }
}
