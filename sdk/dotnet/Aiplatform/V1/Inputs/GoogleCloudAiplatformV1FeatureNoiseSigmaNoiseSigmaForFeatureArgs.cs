// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Aiplatform.V1.Inputs
{

    /// <summary>
    /// Noise sigma for a single feature.
    /// </summary>
    public sealed class GoogleCloudAiplatformV1FeatureNoiseSigmaNoiseSigmaForFeatureArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the input feature for which noise sigma is provided. The features are defined in explanation metadata inputs.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// This represents the standard deviation of the Gaussian kernel that will be used to add noise to the feature prior to computing gradients. Similar to noise_sigma but represents the noise added to the current feature. Defaults to 0.1.
        /// </summary>
        [Input("sigma")]
        public Input<double>? Sigma { get; set; }

        public GoogleCloudAiplatformV1FeatureNoiseSigmaNoiseSigmaForFeatureArgs()
        {
        }
        public static new GoogleCloudAiplatformV1FeatureNoiseSigmaNoiseSigmaForFeatureArgs Empty => new GoogleCloudAiplatformV1FeatureNoiseSigmaNoiseSigmaForFeatureArgs();
    }
}