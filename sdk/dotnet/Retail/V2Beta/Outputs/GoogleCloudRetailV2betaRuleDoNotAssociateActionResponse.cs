// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Retail.V2Beta.Outputs
{

    /// <summary>
    /// Prevents `query_term` from being associated with specified terms during search. Example: Don't associate "gShoe" and "cheap".
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudRetailV2betaRuleDoNotAssociateActionResponse
    {
        /// <summary>
        /// Cannot contain duplicates or the query term. Can specify up to 100 terms.
        /// </summary>
        public readonly ImmutableArray<string> DoNotAssociateTerms;
        /// <summary>
        /// Terms from the search query. Will not consider do_not_associate_terms for search if in search query. Can specify up to 100 terms.
        /// </summary>
        public readonly ImmutableArray<string> QueryTerms;
        /// <summary>
        /// Will be [deprecated = true] post migration;
        /// </summary>
        public readonly ImmutableArray<string> Terms;

        [OutputConstructor]
        private GoogleCloudRetailV2betaRuleDoNotAssociateActionResponse(
            ImmutableArray<string> doNotAssociateTerms,

            ImmutableArray<string> queryTerms,

            ImmutableArray<string> terms)
        {
            DoNotAssociateTerms = doNotAssociateTerms;
            QueryTerms = queryTerms;
            Terms = terms;
        }
    }
}
