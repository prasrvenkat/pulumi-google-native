// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.CloudSearch.V1.Outputs
{

    /// <summary>
    /// Set search results crowding limits. Crowding is a situation in which multiple results from the same source or host "crowd out" other results, diminishing the quality of search for users. To foster better search quality and source diversity in search results, you can set a condition to reduce repetitive results by source.
    /// </summary>
    [OutputType]
    public sealed class SourceCrowdingConfigResponse
    {
        /// <summary>
        /// Maximum number of results allowed from a datasource in a result page as long as results from other sources are not exhausted. Value specified must not be negative. A default value is used if this value is equal to 0. To disable crowding, set the value greater than 100.
        /// </summary>
        public readonly int NumResults;
        /// <summary>
        /// Maximum number of suggestions allowed from a source. No limits will be set on results if this value is less than or equal to 0.
        /// </summary>
        public readonly int NumSuggestions;

        [OutputConstructor]
        private SourceCrowdingConfigResponse(
            int numResults,

            int numSuggestions)
        {
            NumResults = numResults;
            NumSuggestions = numSuggestions;
        }
    }
}
