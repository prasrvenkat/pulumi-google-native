// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleCloud.Dialogflow.V3beta1.Outputs
{

    [OutputType]
    public sealed class GoogleCloudDialogflowCxV3beta1EventHandlerResponse
    {
        /// <summary>
        /// Required. The name of the event to handle.
        /// </summary>
        public readonly string Event;
        /// <summary>
        /// The unique identifier of this event handler.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The target flow to transition to. Format: `projects//locations//agents//flows/`.
        /// </summary>
        public readonly string TargetFlow;
        /// <summary>
        /// The target page to transition to. Format: `projects//locations//agents//flows//pages/`.
        /// </summary>
        public readonly string TargetPage;
        /// <summary>
        /// The fulfillment to call when the event occurs. Handling webhook errors with a fulfillment enabled with webhook could cause infinite loop. It is invalid to specify such fulfillment for a handler handling webhooks.
        /// </summary>
        public readonly Outputs.GoogleCloudDialogflowCxV3beta1FulfillmentResponse TriggerFulfillment;

        [OutputConstructor]
        private GoogleCloudDialogflowCxV3beta1EventHandlerResponse(
            string @event,

            string name,

            string targetFlow,

            string targetPage,

            Outputs.GoogleCloudDialogflowCxV3beta1FulfillmentResponse triggerFulfillment)
        {
            Event = @event;
            Name = name;
            TargetFlow = targetFlow;
            TargetPage = targetPage;
            TriggerFulfillment = triggerFulfillment;
        }
    }
}