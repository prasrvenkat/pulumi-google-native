// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Dialogflow.V3Beta1.Inputs
{

    /// <summary>
    /// A single rollout step with specified traffic allocation.
    /// </summary>
    public sealed class GoogleCloudDialogflowCxV3beta1RolloutConfigRolloutStepArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the rollout step;
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// The minimum time that this step should last. Should be longer than 1 hour. If not set, the default minimum duration for each step will be 1 hour.
        /// </summary>
        [Input("minDuration")]
        public Input<string>? MinDuration { get; set; }

        /// <summary>
        /// The percentage of traffic allocated to the flow version of this rollout step. (0%, 100%].
        /// </summary>
        [Input("trafficPercent")]
        public Input<int>? TrafficPercent { get; set; }

        public GoogleCloudDialogflowCxV3beta1RolloutConfigRolloutStepArgs()
        {
        }
        public static new GoogleCloudDialogflowCxV3beta1RolloutConfigRolloutStepArgs Empty => new GoogleCloudDialogflowCxV3beta1RolloutConfigRolloutStepArgs();
    }
}
