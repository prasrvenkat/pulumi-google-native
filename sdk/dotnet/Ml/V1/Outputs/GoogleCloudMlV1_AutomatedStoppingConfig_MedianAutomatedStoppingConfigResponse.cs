// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Ml.V1.Outputs
{

    [OutputType]
    public sealed class GoogleCloudMlV1_AutomatedStoppingConfig_MedianAutomatedStoppingConfigResponse
    {
        /// <summary>
        /// If true, the median automated stopping rule applies to measurement.use_elapsed_time, which means the elapsed_time field of the current trial's latest measurement is used to compute the median objective value for each completed trial.
        /// </summary>
        public readonly bool UseElapsedTime;

        [OutputConstructor]
        private GoogleCloudMlV1_AutomatedStoppingConfig_MedianAutomatedStoppingConfigResponse(bool useElapsedTime)
        {
            UseElapsedTime = useElapsedTime;
        }
    }
}