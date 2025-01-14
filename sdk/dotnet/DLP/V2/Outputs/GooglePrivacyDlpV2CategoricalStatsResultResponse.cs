// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.DLP.V2.Outputs
{

    /// <summary>
    /// Result of the categorical stats computation.
    /// </summary>
    [OutputType]
    public sealed class GooglePrivacyDlpV2CategoricalStatsResultResponse
    {
        /// <summary>
        /// Histogram of value frequencies in the column.
        /// </summary>
        public readonly ImmutableArray<Outputs.GooglePrivacyDlpV2CategoricalStatsHistogramBucketResponse> ValueFrequencyHistogramBuckets;

        [OutputConstructor]
        private GooglePrivacyDlpV2CategoricalStatsResultResponse(ImmutableArray<Outputs.GooglePrivacyDlpV2CategoricalStatsHistogramBucketResponse> valueFrequencyHistogramBuckets)
        {
            ValueFrequencyHistogramBuckets = valueFrequencyHistogramBuckets;
        }
    }
}
