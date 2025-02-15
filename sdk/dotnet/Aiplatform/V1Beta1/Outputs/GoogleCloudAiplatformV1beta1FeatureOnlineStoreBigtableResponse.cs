// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Aiplatform.V1Beta1.Outputs
{

    [OutputType]
    public sealed class GoogleCloudAiplatformV1beta1FeatureOnlineStoreBigtableResponse
    {
        /// <summary>
        /// Autoscaling config applied to Bigtable Instance.
        /// </summary>
        public readonly Outputs.GoogleCloudAiplatformV1beta1FeatureOnlineStoreBigtableAutoScalingResponse AutoScaling;

        [OutputConstructor]
        private GoogleCloudAiplatformV1beta1FeatureOnlineStoreBigtableResponse(Outputs.GoogleCloudAiplatformV1beta1FeatureOnlineStoreBigtableAutoScalingResponse autoScaling)
        {
            AutoScaling = autoScaling;
        }
    }
}
