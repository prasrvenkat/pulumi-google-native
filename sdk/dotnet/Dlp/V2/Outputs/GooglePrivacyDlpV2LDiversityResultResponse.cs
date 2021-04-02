// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Dlp.V2.Outputs
{

    [OutputType]
    public sealed class GooglePrivacyDlpV2LDiversityResultResponse
    {
        /// <summary>
        /// Histogram of l-diversity equivalence class sensitive value frequencies.
        /// </summary>
        public readonly ImmutableArray<Outputs.GooglePrivacyDlpV2LDiversityHistogramBucketResponse> SensitiveValueFrequencyHistogramBuckets;

        [OutputConstructor]
        private GooglePrivacyDlpV2LDiversityResultResponse(ImmutableArray<Outputs.GooglePrivacyDlpV2LDiversityHistogramBucketResponse> sensitiveValueFrequencyHistogramBuckets)
        {
            SensitiveValueFrequencyHistogramBuckets = sensitiveValueFrequencyHistogramBuckets;
        }
    }
}