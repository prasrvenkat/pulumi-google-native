// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Contactcenterinsights.V1.Outputs
{

    /// <summary>
    /// The analysis resource.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudContactcenterinsightsV1AnalysisResponse
    {
        /// <summary>
        /// The result of the analysis, which is populated when the analysis finishes.
        /// </summary>
        public readonly Outputs.GoogleCloudContactcenterinsightsV1AnalysisResultResponse AnalysisResult;
        /// <summary>
        /// The time at which the analysis was created, which occurs when the long-running operation completes.
        /// </summary>
        public readonly string CreateTime;
        /// <summary>
        /// Immutable. The resource name of the analysis. Format: projects/{project}/locations/{location}/conversations/{conversation}/analyses/{analysis}
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The time at which the analysis was requested.
        /// </summary>
        public readonly string RequestTime;

        [OutputConstructor]
        private GoogleCloudContactcenterinsightsV1AnalysisResponse(
            Outputs.GoogleCloudContactcenterinsightsV1AnalysisResultResponse analysisResult,

            string createTime,

            string name,

            string requestTime)
        {
            AnalysisResult = analysisResult;
            CreateTime = createTime;
            Name = name;
            RequestTime = requestTime;
        }
    }
}