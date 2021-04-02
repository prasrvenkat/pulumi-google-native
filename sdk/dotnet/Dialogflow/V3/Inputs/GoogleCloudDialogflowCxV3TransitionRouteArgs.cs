// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Dialogflow.V3.Inputs
{

    /// <summary>
    /// A transition route specifies a intent that can be matched and/or a data condition that can be evaluated during a session. When a specified transition is matched, the following actions are taken in order: * If there is a `trigger_fulfillment` associated with the transition, it will be called. * If there is a `target_page` associated with the transition, the session will transition into the specified page. * If there is a `target_flow` associated with the transition, the session will transition into the specified flow.
    /// </summary>
    public sealed class GoogleCloudDialogflowCxV3TransitionRouteArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The condition to evaluate against form parameters or session parameters. See the [conditions reference](https://cloud.google.com/dialogflow/cx/docs/reference/condition). At least one of `intent` or `condition` must be specified. When both `intent` and `condition` are specified, the transition can only happen when both are fulfilled.
        /// </summary>
        [Input("condition")]
        public Input<string>? Condition { get; set; }

        /// <summary>
        /// The unique identifier of an Intent. Format: `projects//locations//agents//intents/`. Indicates that the transition can only happen when the given intent is matched. At least one of `intent` or `condition` must be specified. When both `intent` and `condition` are specified, the transition can only happen when both are fulfilled.
        /// </summary>
        [Input("intent")]
        public Input<string>? Intent { get; set; }

        /// <summary>
        /// The target flow to transition to. Format: `projects//locations//agents//flows/`.
        /// </summary>
        [Input("targetFlow")]
        public Input<string>? TargetFlow { get; set; }

        /// <summary>
        /// The target page to transition to. Format: `projects//locations//agents//flows//pages/`.
        /// </summary>
        [Input("targetPage")]
        public Input<string>? TargetPage { get; set; }

        /// <summary>
        /// The fulfillment to call when the condition is satisfied. At least one of `trigger_fulfillment` and `target` must be specified. When both are defined, `trigger_fulfillment` is executed first.
        /// </summary>
        [Input("triggerFulfillment")]
        public Input<Inputs.GoogleCloudDialogflowCxV3FulfillmentArgs>? TriggerFulfillment { get; set; }

        public GoogleCloudDialogflowCxV3TransitionRouteArgs()
        {
        }
    }
}