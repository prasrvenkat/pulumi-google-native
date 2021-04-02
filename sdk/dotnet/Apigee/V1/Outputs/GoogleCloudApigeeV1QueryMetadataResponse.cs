// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Apigee.V1.Outputs
{

    [OutputType]
    public sealed class GoogleCloudApigeeV1QueryMetadataResponse
    {
        /// <summary>
        /// Dimensions of the AsyncQuery.
        /// </summary>
        public readonly ImmutableArray<string> Dimensions;
        /// <summary>
        /// End timestamp of the query range.
        /// </summary>
        public readonly string EndTimestamp;
        /// <summary>
        /// Metrics of the AsyncQuery. Example: ["name:message_count,func:sum,alias:sum_message_count"]
        /// </summary>
        public readonly ImmutableArray<string> Metrics;
        /// <summary>
        /// Output format.
        /// </summary>
        public readonly string OutputFormat;
        /// <summary>
        /// Start timestamp of the query range.
        /// </summary>
        public readonly string StartTimestamp;
        /// <summary>
        /// Query GroupBy time unit.
        /// </summary>
        public readonly string TimeUnit;

        [OutputConstructor]
        private GoogleCloudApigeeV1QueryMetadataResponse(
            ImmutableArray<string> dimensions,

            string endTimestamp,

            ImmutableArray<string> metrics,

            string outputFormat,

            string startTimestamp,

            string timeUnit)
        {
            Dimensions = dimensions;
            EndTimestamp = endTimestamp;
            Metrics = metrics;
            OutputFormat = outputFormat;
            StartTimestamp = startTimestamp;
            TimeUnit = timeUnit;
        }
    }
}