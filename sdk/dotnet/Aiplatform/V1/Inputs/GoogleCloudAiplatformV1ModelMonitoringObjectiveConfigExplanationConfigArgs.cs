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
    /// The config for integrating with Vertex Explainable AI. Only applicable if the Model has explanation_spec populated.
    /// </summary>
    public sealed class GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigExplanationConfigArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// If want to analyze the Vertex Explainable AI feature attribute scores or not. If set to true, Vertex AI will log the feature attributions from explain response and do the skew/drift detection for them.
        /// </summary>
        [Input("enableFeatureAttributes")]
        public Input<bool>? EnableFeatureAttributes { get; set; }

        /// <summary>
        /// Predictions generated by the BatchPredictionJob using baseline dataset.
        /// </summary>
        [Input("explanationBaseline")]
        public Input<Inputs.GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigExplanationConfigExplanationBaselineArgs>? ExplanationBaseline { get; set; }

        public GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigExplanationConfigArgs()
        {
        }
        public static new GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigExplanationConfigArgs Empty => new GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigExplanationConfigArgs();
    }
}
